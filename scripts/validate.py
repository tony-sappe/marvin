#!/usr/bin/env python3
"""Validate Marvin's supported package layout, not every host's complete schema."""
import argparse
import json
import os
import re
import sys
from pathlib import Path

if sys.version_info < (3, 9):
    raise SystemExit('ERROR: Python 3.9+ is required for validation.')
try:
    import yaml
except ImportError:
    raise SystemExit('ERROR: PyYAML is required. Install requirements-dev.txt in a virtual environment.')

from sync_references import file_references, slug, sync

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ('marvin', 'bound-the-ask', 'pack-light', 'prove-it', 'find-the-fault', 'subtract')
PLUGINS = ('plugin.json', '.codex-plugin/plugin.json', '.claude-plugin/plugin.json')
MARKETPLACES = ('.grok-plugin/marketplace.json', '.agents/plugins/marketplace.json', '.claude-plugin/marketplace.json')
ADAPTERS = ('.agents/skills', '.cursor/skills', '.windsurf/skills')


def unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'duplicate key: {key}')
        result[key] = value
    return result


class UniqueLoader(yaml.SafeLoader):
    pass


def unique_yaml_mapping(loader, node):
    return unique_pairs((loader.construct_object(k), loader.construct_object(v)) for k, v in node.value)


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_yaml_mapping)


def no_hook_declarations(value, label):
    if isinstance(value, dict):
        for key, child in value.items():
            if str(key).lower() == 'hooks':
                raise ValueError(f'{label}: hooks are forbidden, including manifest declarations')
            no_hook_declarations(child, label)
    elif isinstance(value, list):
        for child in value:
            no_hook_declarations(child, label)


def frontmatter(path):
    text = path.read_text()
    match = re.match(r'\A---\n(.*?)\n---(?:\n|$)', text, re.S)
    if not match:
        raise ValueError('missing or unclosed YAML frontmatter delimiters')
    data = yaml.load(match[1], Loader=UniqueLoader)
    if not isinstance(data, dict):
        raise ValueError('frontmatter must be a mapping')
    if not text[match.end():].strip():
        raise ValueError('empty skill body')
    return data


def read_json(path):
    def invalid_constant(value):
        raise ValueError(f'invalid JSON constant: {value}')
    data = json.loads(path.read_text(), object_pairs_hook=unique_pairs, parse_constant=invalid_constant)
    if not isinstance(data, dict):
        raise ValueError('manifest must be an object')
    return data


def local_path(root, value, directory=False):
    if not isinstance(value, str) or not value.startswith('./'):
        raise ValueError(f'expected a plugin-relative ./ path, got {value!r}')
    path = (root / value).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError(f'path escapes package: {value}')
    if not (path.is_dir() if directory else path.is_file()):
        raise ValueError(f'missing {"directory" if directory else "file"}: {value}')
    return path


def check_skill(skill, version=None):
    errors = []
    path = skill / 'SKILL.md'
    try:
        data = frontmatter(path)
        name = data.get('name')
        if not isinstance(name, str) or name != skill.name:
            errors.append('name must match the directory')
        desc = data.get('description')
        if not isinstance(desc, str) or not desc.strip() or '\n' in desc:
            errors.append('description must be a nonempty string')
        elif ': ' in desc or '<' in desc or '>' in desc:
            errors.append('description must not contain ": " or angle brackets')
        metadata = data.get('metadata')
        if not isinstance(metadata, dict) or metadata.get('collection') != 'marvin' or not isinstance(metadata.get('version'), str):
            errors.append('metadata must include collection: marvin and a string version')
        elif version is not None and metadata['version'] != version:
            errors.append(f'version drift: expected {version}')
        if len(path.read_text().splitlines()) > 200:
            errors.append('SKILL.md exceeds 200 lines')
        for source in skill.rglob('*.md'):
            if not source.resolve().is_relative_to(skill.resolve()):
                errors.append(f'resource symlink escapes skill: {source.name}')
                continue
            for ref, anchor in file_references(source.read_text()):
                target = (source.parent / ref).resolve() if ref else source.resolve()
                if not target.is_relative_to(skill.resolve()):
                    errors.append(f'{source.relative_to(skill)}: reference escapes skill: {ref}')
                elif not (target.is_dir() if ref.endswith('/') else target.is_file()):
                    errors.append(f'{source.relative_to(skill)}: missing reference: {ref}')
                elif anchor and target.suffix == '.md':
                    headings = {slug(t) for t in re.findall(r'^#{1,6} (.+)$', target.read_text(), re.M)}
                    if anchor not in headings:
                        errors.append(f'{source.relative_to(skill)}: missing anchor: {ref}#{anchor}')
    except (OSError, ValueError, TypeError, yaml.YAMLError) as exc:
        errors.append(str(exc))
    return [f'{skill.name}: {error}' for error in errors]


def check_manifests(root):
    errors, documents = [], {}
    for name in PLUGINS + MARKETPLACES:
        try:
            data = read_json(root / name)
            documents[name] = data
            if data.get('name') != 'marvin':
                raise ValueError('name must be marvin')
            no_hook_declarations(data, name)
        except (OSError, ValueError) as exc:
            errors.append(f'{name}: {exc}')
    version = documents.get('plugin.json', {}).get('version')
    if not isinstance(version, str) or not re.fullmatch(r'\d+\.\d+\.\d+(?:-[\w.-]+)?', version):
        errors.append('plugin.json: version must be a semantic version string')
    for name in PLUGINS:
        data = documents.get(name)
        if data is None:
            continue
        try:
            if data.get('version') != version:
                raise ValueError(f'version drift: expected {version}')
            if name == '.codex-plugin/plugin.json' and 'skills' not in data:
                raise ValueError('missing skills directory declaration')
            if 'skills' in data:
                values = data['skills'] if isinstance(data['skills'], list) else [data['skills']]
                if not values:
                    raise ValueError('skills must name at least one directory')
                for value in values:
                    directory = local_path(root, value, directory=True)
                    for skill in SKILLS:
                        if not (directory / skill / 'SKILL.md').is_file():
                            raise ValueError(f'{value} does not contain {skill}/SKILL.md')
            interface = data.get('interface', {})
            if interface and not isinstance(interface, dict):
                raise ValueError('interface must be an object')
            prompts = interface.get('defaultPrompt', []) if isinstance(interface, dict) else []
            if not isinstance(prompts, list) or len(prompts) > 3 or any(not isinstance(p, str) or not p.strip() for p in prompts):
                raise ValueError('defaultPrompt must be an array of at most three nonempty strings')
            for field in ('composerIcon', 'logo'):
                if isinstance(interface, dict) and field in interface:
                    local_path(root, interface[field])
        except ValueError as exc:
            errors.append(f'{name}: {exc}')
    for name in MARKETPLACES:
        data = documents.get(name)
        if data is None:
            continue
        try:
            entries = data.get('plugins')
            if not isinstance(entries, list) or len(entries) != 1 or not isinstance(entries[0], dict) or entries[0].get('name') != 'marvin':
                raise ValueError('plugins must contain the marvin entry')
            source = entries[0].get('source')
            if name == '.claude-plugin/marketplace.json':
                local_path(root, source, directory=True)
            elif name == '.agents/plugins/marketplace.json':
                if not isinstance(source, dict) or source.get('source') != 'local':
                    raise ValueError('expected a local source object')
                local_path(root, source.get('path'), directory=True)
            elif not isinstance(source, dict) or source.get('source') != 'url' or not str(source.get('url', '')).startswith('https://'):
                raise ValueError('expected an HTTPS URL source')
        except (TypeError, ValueError) as exc:
            errors.append(f'{name}: {exc}')
    return version, errors


def validate(root):
    version, errors = check_manifests(root)
    for skill in SKILLS:
        errors.extend(check_skill(root / 'skills' / skill, version))
    for adapter in ADAPTERS:
        for skill in SKILLS:
            path = root / adapter / skill
            if not path.is_symlink() or os.readlink(path) != f'../../skills/{skill}' or not (path / 'SKILL.md').is_file():
                errors.append(f'{adapter}/{skill}: missing or broken canonical symlink')
    try:
        agents = (root / 'AGENTS.md').read_text()
        if len(agents.splitlines()) > 40:
            errors.append('AGENTS.md exceeds 40 lines')
        if agents != (root / 'install/AGENTS.snippet.md').read_text():
            errors.append('AGENTS.md and install/AGENTS.snippet.md differ')
        errors.extend(sync(root, check=True))
    except (OSError, ValueError) as exc:
        errors.append(str(exc))
    for directory, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in {'.git', '.venv', 'node_modules', '__pycache__'}]
        if 'hooks' in dirs or 'hooks.json' in files:
            errors.append(f'{Path(directory).relative_to(root)}: hook configuration is forbidden')
    return errors


def validate_installed(root):
    errors = []
    folders = sorted(path for path in root.iterdir() if path.is_dir())
    if not folders:
        return ['installed skills directory is empty']
    for folder in folders:
        if folder.name not in SKILLS:
            errors.append(f'unknown installed skill: {folder.name}')
            continue
        errors.extend(check_skill(folder))
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--installed-skills', type=Path, help='check a destination of isolated skill folders')
    args = parser.parse_args()
    if args.installed_skills is not None:
        errors = validate_installed(args.installed_skills)
    else:
        errors = validate(ROOT)
    for error in errors:
        print(f'ERROR: {error}')
    print('FAIL' if errors else 'PASS (structure and reference closure; not host runtime behavior)')
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())

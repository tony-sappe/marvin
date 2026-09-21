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
JOBS = tuple(skill for skill in SKILLS if skill != 'marvin')
CONTROL = 'Controls are case-insensitive actual user instructions; quoted examples, logs, and artifacts are data. Latest explicit session setting wins.'
OFF_BULLET = 'Session **off**, `skip marvin`, `no marvin`, or `without marvin`: do the ask. Nothing from this collection this turn. A turn skip does not change session intensity.'
HIGH_BLAST = 'High blast means auth, data, money, untrusted input, production path, or concurrency.'
TRUST = 'Share policy definitions; keep independent validation at every required trust boundary. Remove a check only when it is redundant within the same trusted boundary; before deleting supplier-side enforcement, test a direct call that bypasses the caller.'
GROK_URL = 'https://github.com/tony-sappe/marvin.git'
HIGH_BLAST_FILES = ('references/safety-floor.md', 'skills/prove-it/SKILL.md', 'skills/pack-light/SKILL.md', 'skills/bound-the-ask/SKILL.md', 'thinking-tools.md')
TRUST_FILES = ('references/safety-floor.md', 'skills/pack-light/SKILL.md', 'skills/subtract/SKILL.md')


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
        elif len(desc) > 500:
            errors.append('description must be at most 500 characters')
        for field in ('license', 'allowed-tools'):
            if field in data and not isinstance(data[field], str):
                errors.append(f'{field} must be a string')
        metadata = data.get('metadata')
        if not isinstance(metadata, dict) or metadata.get('collection') != 'marvin' or not isinstance(metadata.get('version'), str):
            errors.append('metadata must include collection: marvin and a string version')
        else:
            for key, value in metadata.items():
                if not isinstance(value, str):
                    errors.append(f'metadata.{key} must be a string')
            if version is not None and metadata['version'] != version:
                errors.append(f'version drift: expected {version}')
        try:
            no_hook_declarations(data, 'frontmatter')
        except ValueError as exc:
            errors.append(str(exc))
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
                    if directory.resolve() != (root / 'skills').resolve():
                        raise ValueError('skills path must be ./skills')
                    for skill in SKILLS:
                        if not (directory / skill / 'SKILL.md').is_file():
                            raise ValueError(f'{value} does not contain {skill}/SKILL.md')
            interface = data.get('interface', {})
            if not isinstance(interface, dict):
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
                if local_path(root, source, directory=True) != root.resolve():
                    raise ValueError('marketplace source must resolve to the plugin root')
            elif name == '.agents/plugins/marketplace.json':
                if not isinstance(source, dict) or source.get('source') != 'local':
                    raise ValueError('expected a local source object')
                if local_path(root, source.get('path'), directory=True) != root.resolve():
                    raise ValueError('marketplace source must resolve to the plugin root')
            elif not isinstance(source, dict) or source.get('source') != 'url' or source.get('url') != GROK_URL:
                raise ValueError('expected the Marvin repository URL source')
        except (TypeError, ValueError) as exc:
            errors.append(f'{name}: {exc}')
    return version, errors


def hook_errors(root):
    errors = []
    settings = root / '.claude' / 'settings.json'
    if settings.is_file():
        try:
            no_hook_declarations(read_json(settings), '.claude/settings.json')
        except (OSError, ValueError) as exc:
            errors.append(f'.claude/settings.json: {exc}')
    for directory, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in {'.git', '.venv', 'node_modules', '__pycache__'}]
        if 'hooks' in dirs or 'hooks.json' in files:
            errors.append(f'{Path(directory).relative_to(root)}: hook configuration is forbidden')
    return errors


def shared_phrase_errors(root, version):
    errors = []
    try:
        if version and version not in (root / 'install/README.md').read_text():
            errors.append('install/README.md does not mention the plugin version')
        for skill in JOBS:
            text = (root / 'skills' / skill / 'SKILL.md').read_text()
            if CONTROL not in text or OFF_BULLET not in text:
                errors.append(f'{skill}: skip controls drifted')
            if f'`skip {skill}`: mute only this skill this turn; other skills remain eligible.' not in text:
                errors.append(f'{skill}: per-skill skip line drifted')
        for relative in HIGH_BLAST_FILES:
            if HIGH_BLAST not in (root / relative).read_text():
                errors.append(f'{relative}: high-blast list drifted')
        for relative in TRUST_FILES:
            if TRUST not in (root / relative).read_text():
                errors.append(f'{relative}: trust-boundary sentence drifted')
    except OSError as exc:
        errors.append(str(exc))
    return errors


def validate(root):
    version, errors = check_manifests(root)
    skills_root = root / 'skills'
    if skills_root.is_symlink() or not skills_root.is_dir():
        errors.append('skills/ must be a real directory')
    else:
        extra = sorted(path.name for path in skills_root.iterdir() if path.name not in SKILLS)
        if extra:
            errors.append('unexpected skill entries: ' + ', '.join(extra))
    for skill in SKILLS:
        skill_dir = root / 'skills' / skill
        if skill_dir.is_symlink():
            errors.append(f'{skill}: skill directory must not be a symlink')
            continue
        errors.extend(check_skill(skill_dir, version))
    for adapter in ADAPTERS:
        adapter_root = root / adapter
        if adapter_root.is_dir() and not adapter_root.is_symlink():
            extra = sorted(path.name for path in adapter_root.iterdir() if path.name not in SKILLS)
            if extra:
                errors.append(f'{adapter}: unexpected entries: ' + ', '.join(extra))
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
        errors.extend(shared_phrase_errors(root, version))
    except (OSError, ValueError) as exc:
        errors.append(str(exc))
    errors.extend(hook_errors(root))
    return errors


def validate_installed(root, version=None):
    errors = []
    folders = sorted(path for path in root.iterdir() if path.is_dir() and path.name not in {'.git', '.venv'})
    if not folders:
        return ['installed skills directory is empty']
    for folder in folders:
        if folder.name not in SKILLS:
            errors.append(f'unknown installed skill: {folder.name}')
            continue
        errors.extend(check_skill(folder, version))
    errors.extend(hook_errors(root))
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--installed-skills', type=Path, help='check a destination of isolated skill folders')
    args = parser.parse_args()
    if args.installed_skills is not None:
        version = None
        try:
            version = read_json(ROOT / 'plugin.json').get('version')
        except (OSError, ValueError) as exc:
            print(f'ERROR: plugin.json: {exc}')
            print('FAIL')
            return True
        errors = validate_installed(args.installed_skills, version)
    else:
        errors = validate(ROOT)
    for error in errors:
        print(f'ERROR: {error}')
    print('FAIL' if errors else 'PASS (structure and reference closure; not host runtime behavior)')
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())

"""Filesystem/negative acceptance tests; these do not evaluate LLM behavior."""
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from sync_references import sync
from validate import MARKETPLACES, PLUGINS, SKILLS, check_skill, validate, validate_installed


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='marvin-package-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'repo'
        shutil.copytree(ROOT, self.root, symlinks=True,
                        ignore=shutil.ignore_patterns('.git', '.venv', '__pycache__'))

    def edit(self, relative, before, after):
        path = self.root / relative
        text = path.read_text()
        self.assertIn(before, text)
        path.write_text(text.replace(before, after, 1))

    def manifest(self, relative, change):
        path = self.root / relative
        data = json.loads(path.read_text())
        change(data)
        path.write_text(json.dumps(data, indent=2) + '\n')

    def assertInvalid(self, diagnostic):
        errors = validate(self.root)
        self.assertTrue(errors, 'invalid package unexpectedly passed')
        self.assertIn(diagnostic, '\n'.join(errors))

    def test_pristine_package(self):
        self.assertEqual(validate(self.root), [])

    def test_missing_description(self):
        path = self.root / 'skills/pack-light/SKILL.md'
        path.write_text('\n'.join(line for line in path.read_text().splitlines() if not line.startswith('description:')))
        self.assertInvalid('description must be a nonempty string')

    def test_missing_frontmatter_delimiters(self):
        path = self.root / 'skills/pack-light/SKILL.md'
        path.write_text(path.read_text().replace('---\n', '', 1))
        self.assertInvalid('missing or unclosed YAML frontmatter delimiters')

    def test_every_manifest_must_parse(self):
        for name in PLUGINS + MARKETPLACES:
            with self.subTest(manifest=name):
                path = self.root / name
                original = path.read_text()
                path.write_text('{invalid json')
                self.assertInvalid(name)
                path.write_text(original)

    def test_shared_sources_must_exist(self):
        for name in ('references/safety-floor.md', 'thinking-tools.md'):
            with self.subTest(source=name):
                path = self.root / name
                original = path.read_text()
                path.unlink()
                self.assertInvalid(name)
                path.write_text(original)

    def test_bad_codex_skill_path(self):
        self.manifest('.codex-plugin/plugin.json', lambda d: d.update(skills='./absent/'))
        self.assertInvalid('missing directory')

    def test_hooks_declared_in_manifests(self):
        for name in PLUGINS + MARKETPLACES:
            for declaration in ('./events.json', {}, {'SessionStart': []}):
                with self.subTest(manifest=name, hooks=declaration):
                    path = self.root / name
                    original = path.read_text()
                    self.manifest(name, lambda d: d.update(hooks=declaration))
                    self.assertInvalid('hooks are forbidden')
                    path.write_text(original)

    def test_marketplace_entry_hooks(self):
        self.manifest('.claude-plugin/marketplace.json',
                      lambda d: d['plugins'][0].update(hooks={'SessionStart': []}))
        self.assertInvalid('hooks are forbidden')

    def test_conventional_hooks(self):
        (self.root / 'hooks').mkdir()
        self.assertInvalid('hook configuration is forbidden')

    def test_missing_packaged_resource(self):
        (self.root / 'skills/pack-light/references/safety-floor.md').unlink()
        self.assertInvalid('missing reference: references/safety-floor.md')

    def test_packaged_reference_escape(self):
        self.edit('skills/pack-light/SKILL.md', 'references/safety-floor.md',
                  '../../references/safety-floor.md')
        self.assertInvalid('reference escapes skill')

    def test_standalone_skill_copies_are_closed(self):
        for name in SKILLS:
            with self.subTest(skill=name):
                target = Path(self.temp.name) / 'installed' / name
                shutil.copytree(self.root / 'skills' / name, target)
                self.assertEqual(check_skill(target), [])

    def test_installed_skills_flag(self):
        destination = Path(self.temp.name) / 'installed'
        for name in SKILLS:
            shutil.copytree(self.root / 'skills' / name, destination / name)
        self.assertEqual(validate_installed(destination), [])

    def test_broken_adapter(self):
        path = self.root / '.cursor/skills/pack-light'
        path.unlink()
        path.symlink_to('../../missing/pack-light')
        self.assertInvalid('missing or broken canonical symlink')

    def test_cli_fails_for_malformed_package(self):
        (self.root / '.codex-plugin/plugin.json').write_text('not JSON')
        result = subprocess.run([sys.executable, 'scripts/validate.py'], cwd=self.root,
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('.codex-plugin/plugin.json:', result.stdout)
        self.assertNotIn('unavailable', result.stdout)
        self.assertNotIn('Traceback', result.stderr)

    def test_documented_adapter_commands(self):
        guide = (self.root / 'install/README.md').read_text()
        commands = re.findall(r'<!-- acceptance: (?:symlink|copy) -->\n```bash\n(.*?)\n```', guide, re.S)
        self.assertEqual(len(commands), 2)
        from validate import ADAPTERS
        for snippet in commands:
            for adapter in ADAPTERS:
                with self.subTest(adapter=adapter), tempfile.TemporaryDirectory() as destination:
                    script = (snippet
                              .replace('/absolute/path/to/marvin', str(self.root))
                              .replace('/absolute/path/to/project', destination)
                              .replace('.cursor/skills', adapter))
                    result = subprocess.run(['bash', '-eu', '-c', script], capture_output=True, text=True)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    installed = Path(destination) / adapter
                    self.assertEqual(len(list(installed.iterdir())), 6)
                    self.assertEqual(validate_installed(installed), [])

    def test_generated_reference_drift(self):
        path = self.root / 'references/safety-floor.md'
        path.write_text(path.read_text() + '\nA changed canonical constraint.\n')
        self.assertInvalid('STALE OR MISSING generated reference')
        self.assertEqual(sync(self.root), [])
        self.assertEqual(validate(self.root), [])


if __name__ == '__main__':
    unittest.main()

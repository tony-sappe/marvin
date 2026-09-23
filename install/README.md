# Install

Human notes only. Each canonical skill includes its required reference files. Hosts still control discovery, tool permissions, and instruction following; see [`paths.md`](paths.md) for installation and verification scope.

Usage, intensity, and skill jobs: root [`README.md`](../README.md).

## Grok Build

```bash
grok plugin marketplace add tony-sappe/marvin
grok plugin install marvin --trust
```

Or from a local checkout:

```bash
grok plugin install /path/to/marvin --trust
```

Enable the plugin if it stays off (`/plugins` → Space, or `[plugins] enabled = ["marvin"]` in `~/.grok/config.toml`).

Start a **new session** (or reload) after install so the skills appear.

## Codex

Two steps: add the **marketplace**, then install the **plugin**. `marvin@marvin` fails if the marketplace was never added.

```bash
codex plugin marketplace add tony-sappe/marvin
codex plugin add marvin@marvin
```

Equivalent marketplace source:

```bash
codex plugin marketplace add https://github.com/tony-sappe/marvin.git
```

**From a local checkout** (no GitHub fetch):

```bash
codex plugin marketplace add /absolute/path/to/marvin
codex plugin add marvin@marvin
```

**Confirm:**

```bash
codex plugin marketplace list
codex plugin list --marketplace marvin
```

Expect `marvin@marvin` → installed, enabled, version `1.5.0`. Codex reads that version from `.codex-plugin/plugin.json`.

**Update later:**

```bash
codex plugin marketplace upgrade marvin
```

If the VERSION column stays stale after a release, remove and re-add the plugin (`codex plugin remove marvin@marvin` then `codex plugin add marvin@marvin`).

Start a **new thread/session** after install.

## Claude Code

```text
/plugin marketplace add tony-sappe/marvin
/plugin install marvin@marvin
```

Local checkout for one session, without a persistent install:

```bash
claude --plugin-dir /path/to/marvin
```

## GitHub CLI (Agent Skills)

```bash
gh skill install tony-sappe/marvin --all
```

A named skill can also be installed on its own; its local references are bundled. Install `--all` to enable routing between all six skills.

Non-interactive defaults are `--agent github-copilot` and `--scope project` (the current repo). Pass `--agent` for another host and `--scope user` to install for every project. Several agents, including Copilot, Cursor, and Codex, share `.agents/skills/` at project scope. Claude Code, Grok, and Windsurf do not. Preview a named skill with `gh skill preview tony-sappe/marvin marvin`.

## Cursor / Windsurf

This repo already contains `.cursor/skills/` and `.windsurf/skills/` (symlinks into `skills/`). Opening the checkout is enough for discovery.

To use Marvin inside another project, link each **canonical skill folder** from a retained checkout. Do not copy this repository's relative adapter symlinks into another project: their targets depend on this repository's layout. Substitute your absolute paths below. These commands assume the six destination names are unused; they do not overwrite existing skills.

<!-- acceptance: symlink -->
```bash
marvin_repo="/absolute/path/to/marvin"
project="/absolute/path/to/project"
mkdir -p "$project/.cursor/skills"
for skill in "$marvin_repo"/skills/*; do
  destination="$project/.cursor/skills/$(basename "$skill")"
  if [ -e "$destination" ] || [ -L "$destination" ]; then
    echo "Destination already exists: $destination" >&2
    exit 1
  fi
  ln -s "$skill" "$destination"
done
```

Use `.windsurf/skills` or `.agents/skills` in place of `.cursor/skills` for those hosts. Keep the source checkout at the same absolute path while using links.

For a standalone copy that does not depend on the checkout location:

<!-- acceptance: copy -->
```bash
marvin_repo="/absolute/path/to/marvin"
project="/absolute/path/to/project"
mkdir -p "$project/.cursor/skills"
for skill in "$marvin_repo"/skills/*; do
  destination="$project/.cursor/skills/$(basename "$skill")"
  if [ -e "$destination" ] || [ -L "$destination" ]; then
    echo "Destination already exists: $destination" >&2
    exit 1
  fi
  cp -R "$skill" "$destination"
done
```

Windows PowerShell (copies avoid symlink privileges):

```powershell
$marvinRepo = 'C:\src\marvin'
$project = 'C:\src\my-project'
$skillsRoot = Join-Path $project '.cursor/skills'
New-Item -ItemType Directory -Force -Path $skillsRoot | Out-Null
Get-ChildItem -Directory (Join-Path $marvinRepo 'skills') | ForEach-Object {
    $destination = Join-Path $skillsRoot $_.Name
    if (Test-Path $destination) { throw "Destination already exists: $destination" }
    Copy-Item -Recurse -LiteralPath $_.FullName -Destination $destination
}
```

Validate a destination with the source checkout's validator:

```bash
python3 /absolute/path/to/marvin/scripts/validate.py --installed-skills /absolute/path/to/project/.cursor/skills
```

The destination check expects only Marvin skill folders; for a mixed host root, check a separate temporary copy of the Marvin folders. Merge the AGENTS snippet below when you want the routing map.

## AGENTS.md

Copy or merge `install/AGENTS.snippet.md` into the target project's `AGENTS.md` (prepend preferred).

## Validate (no host CLIs required)

Python 3.9+ and PyYAML are development dependencies; installing or reading the skills does not require them.

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements-dev.txt
python3 scripts/sync_references.py --check
./scripts/validate.sh
python3 -m unittest discover -s tests -v
```

Edit shared guidance in root `references/` and `thinking-tools.md`, then run `python3 scripts/sync_references.py` and commit the generated copies inside each skill. Validation parses JSON/YAML, checks declared paths, local reference closure, adapters, and hook declarations. It is a structural gate, not a host-runtime or model-behavior proof.

Behavioral cases live in [`tests/behavioral.md`](../tests/behavioral.md).

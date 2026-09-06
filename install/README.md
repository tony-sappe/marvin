# Install

Human notes only. Skill bytes are identical across hosts; see [`paths.md`](paths.md) for the full matrix.

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

Expect `marvin@marvin` → installed, enabled, version `1.2.0`. Codex reads that version from `.codex-plugin/plugin.json`.

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

Local checkout without marketplace:

```bash
claude --plugin-dir /path/to/marvin
```

## GitHub CLI (Agent Skills)

```bash
gh skill install tony-sappe/marvin --all
```

Non-interactive default `--agent` is `github-copilot`. Pass `--agent` for another host. Preview a named skill with `gh skill preview tony-sappe/marvin marvin`.

## Cursor / Windsurf

This repo already contains `.cursor/skills/` and `.windsurf/skills/` (symlinks into `skills/`). Opening the checkout is enough for discovery.

To use Marvin inside another project, copy or symlink those adapter folders (or `.agents/skills/`) into that project, and merge the AGENTS snippet below.

## AGENTS.md

Copy or merge `install/AGENTS.snippet.md` into the target project's `AGENTS.md` (prepend preferred).

## Validate (no host CLIs required)

```bash
./scripts/validate.sh
```

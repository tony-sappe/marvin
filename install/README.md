# Install

Human notes only. Skill bytes are identical across hosts; see [`paths.md`](paths.md) for the full matrix.

Usage, intensity, and skill jobs: root [`README.md`](../README.md).

## Grok Build

```bash
grok plugin marketplace add tony-sappe/dont-panic
grok plugin install dont-panic --trust
```

Or from a local checkout:

```bash
grok plugin install /path/to/dont-panic --trust
```

Enable the plugin if it stays off (`/plugins` → Space, or `[plugins] enabled = ["dont-panic"]` in `~/.grok/config.toml`).

Start a **new session** (or reload) after install so the skills appear.

## Codex

```bash
codex plugin marketplace add tony-sappe/dont-panic
```

Then install **Don't Panic** from `/plugins`, or use your Codex build's local-path install for this checkout.

New thread/session after install.

## Claude Code

```text
/plugin marketplace add tony-sappe/dont-panic
/plugin install dont-panic@dont-panic
```

Local checkout without marketplace:

```bash
claude --plugin-dir /path/to/dont-panic
```

## GitHub CLI (Agent Skills)

```bash
gh skill install tony-sappe/dont-panic --all
```

Pin a release with `--pin v1.0.0` when you have published tags. Preview first with `gh skill preview tony-sappe/dont-panic`.

## Cursor / Windsurf

This repo already contains `.cursor/skills/` and `.windsurf/skills/` (symlinks into `skills/`). Opening the checkout is enough for discovery.

To use Don't Panic inside another project, copy or symlink those adapter folders (or `.agents/skills/`) into that project, and merge the AGENTS snippet below.

## OpenClaw

`.openclaw/skills/` holds generated copies with short `description` fields (<160 chars) and identical bodies. Regenerate after skill edits:

```bash
./scripts/build-openclaw-skills.sh
```

Use this repo as the workspace skills root, or copy that adapter tree into the OpenClaw workdir.

## Hermes Agent

Copy or symlink each folder under `skills/` into `~/.hermes/skills/` (optionally under a category directory). Opening this repo also exposes project-level `skills/`.

## AGENTS.md

Copy or merge `install/AGENTS.snippet.md` into the target project's `AGENTS.md` (prepend preferred).

## Validate (no host CLIs required)

```bash
./scripts/validate.sh
```

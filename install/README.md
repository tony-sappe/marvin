# Install

Human notes only.

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

## Codex

```bash
codex plugin marketplace add tony-sappe/dont-panic
```

Then install **Don't Panic** from `/plugins`, or use your Codex build's local-path install for this checkout.

## AGENTS.md

Copy or merge `install/AGENTS.snippet.md` into the target project's `AGENTS.md` (prepend preferred).

## Intensity

```text
dont-panic lite
dont-panic full
dont-panic ultra
```

## Skills

| Skill | Job |
| --- | --- |
| `dont-panic` | Intensity + map |
| `bound-the-ask` | Contract before material work |
| `smallest-trusted` | Smallest trusted design / impl |
| `prove-it` | Evidence before done |
| `find-the-fault` | Scientific debugging |
| `subtract` | Behavior-preserving simplification |

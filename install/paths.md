# Install paths

Skill bytes live once in this repo under `skills/`. Hosts load them via plugin install or by discovering that folder.

| Host | How to install | Map |
| --- | --- | --- |
| Grok Build | `grok plugin marketplace add <this-repo>` then `grok plugin install dont-panic --trust` — or `grok plugin install <path-or-url> --trust` | Prepend or merge `install/AGENTS.snippet.md` into the target project's `AGENTS.md` |
| Codex | `codex plugin marketplace add <this-repo>` then install `dont-panic` — or install from local path via Codex plugins UI | Same `AGENTS.md` snippet |
| Repo checkout (no plugin) | Point the host at this repo, or copy/symlink `skills/*` into `.agents/skills/` and/or `.grok/skills/` | Same snippet |

Identical skill bytes. No per-host forks inside `SKILL.md`.

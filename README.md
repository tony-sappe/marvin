![](./assets/dont-panic.jpg)

# Don't Panic! Use these handy thinking tools

Searching for the Question while navigating the improbability of AI!

[\[Issue trees\]](thinking-tools.md#issue-trees) · [\[Inversion\]](thinking-tools.md#inversion) · [\[Abstraction laddering\]](thinking-tools.md#abstraction-laddering) · [\[First principles\]](thinking-tools.md#first-principles) · [\[Cynefin\]](thinking-tools.md#cynefin) · [\[OODA\]](thinking-tools.md#ooda) · [\[Zwicky box\]](thinking-tools.md#zwicky-box) · [\[Minto Pyramid\]](thinking-tools.md#minto-pyramid) · [\[Test bar\]](thinking-tools.md#test-bar)


**Noteworthy projects inspiring this project**

[\[ponytail\]](https://ponytail.dev) · [\[superpowers\]](https://github.com/obra/superpowers) · [\[BMAD Method\]](https://github.com/bmad-code-org/BMAD-METHOD) · [\[first-principles-engineering\]](https://github.com/sudoconnor/first-principles-engineering)

---

# Install

Portable skills for **Grok Build** and **OpenAI Codex**. Same skill bytes. Plugin install preferred.

## Grok Build

```bash
grok plugin marketplace add tony-sappe/dont-panic
grok plugin install dont-panic --trust
```

Local checkout:

```bash
grok plugin install /path/to/dont-panic --trust
```

Enable if needed: `/plugins` → Space on `dont-panic`, or in `~/.grok/config.toml`:

```toml
[plugins]
enabled = ["dont-panic"]
```

## Codex

```bash
codex plugin marketplace add tony-sappe/dont-panic
```

Then install **Don't Panic** from `/plugins` (CLI or app). For a local checkout, add this repo as a marketplace source and install `dont-panic`.

## AGENTS.md map

Merge [`install/AGENTS.snippet.md`](install/AGENTS.snippet.md) into the target project's `AGENTS.md` (prepend preferred).

## Intensity

```text
dont-panic lite    # soft challenges, vibe-coding friendly
dont-panic full    # default
dont-panic ultra   # hard gates, failure-first, subtract hard
```

## Skills

| Skill | Job |
| --- | --- |
| `dont-panic` | Intensity dial + route map |
| `bound-the-ask` | Bounded contract before material work |
| `smallest-trusted` | Smallest complete system that can be trusted |
| `prove-it` | Named evidence before "done" |
| `find-the-fault` | Observe → one hypothesis → one experiment |
| `subtract` | Behavior-preserving simplification |

Artifacts in the target project go under `specs/` (created if missing), or `docs/specs/` when that tree already exists or the user asks for it.

More detail: [`install/README.md`](install/README.md) · [`install/paths.md`](install/paths.md)


# Contributing
**Run tests to validate the project:** `./scripts/validate.sh`

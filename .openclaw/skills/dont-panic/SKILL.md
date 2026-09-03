---
name: dont-panic
description: "Set Don't Panic intensity (lite/full/ultra) and show the skill map. Use for dont-panic or how to use this collection. Not a job-skill substitute."
homepage: https://github.com/tony-sappe/dont-panic
license: MIT
metadata:
  collection: dont-panic
  version: "1.0"
---


> Pack the towel. Set the dial. Then do the job.

## Intensity

Default **full** for the session until changed.

| Level | Behavior |
| --- | --- |
| **lite** | Smallest path. Soft challenges in one line. Written contract optional when the outcome is obvious. Prefer shipping over ceremony. |
| **full** | Matching skill algorithm + safety floor. Ask when the answer changes outcome, cost, or blast radius. |
| **ultra** | Hard gates on material work. Failure-first pass before design. Aggressive subtraction bias. Refuse "done" without decisive evidence. |

Switch: user says `dont-panic lite|full|ultra`, `/dont-panic lite|full|ultra`, or equivalent. No argument → report the current level in one line, then the map.

Persist for this conversation only (no hooks). State the level once when it changes. Do not re-preach it every turn.

## Map

Load **one** job skill:

1. **bound-the-ask** — ambiguous or material work; write/confirm the contract when unclear.
2. **pack-light** — design shape and new parts; ladder; stop early.
3. **prove-it** — done, PR, verify; name evidence types.
4. **find-the-fault** — bugs and incidents; one hypothesis, one experiment.
5. **subtract** — refactor and delete; behavior-preserving.

Vibe coding is allowed. Obvious one-file outcomes may go straight to `pack-light` under lite/full.

## Output

```
intensity: <lite|full|ultra>
next: <skill or "say what you want to build">
```

Lead with that. No lore dump.

---
name: marvin
description: Set Marvin intensity and remind the skill map. Use when the user says marvin, Marvin, Don't Panic, marvin off, marvin sigh, marvin paranoid, marvin skip, marvin whatever, marvin lite, marvin full, or asks how to use this collection. Do not use as a substitute for bound-the-ask, pack-light, prove-it, find-the-fault, or subtract on the actual work.
license: MIT
metadata:
  collection: marvin
  version: "1.4.0"
---

> Pack the towel. Set the dial. Then do the job.

## Intensity

Default **paranoid** for the session until changed.

| Level | Behavior |
| --- | --- |
| **off** | No job skills. Do the ask. Nothing from this collection. |
| **sigh** | Smallest path. Soft challenges in one line. Written contract optional when the outcome is obvious. Prefer shipping over ceremony. |
| **paranoid** | Matching skill algorithm + safety floor. Ask when the answer changes outcome, cost, or blast radius. |

Switch: user says `marvin off|sigh|paranoid`, `/marvin off|sigh|paranoid`, or equivalent. No argument → report the current level in one line, then the map (omit the map when **off**).

Aliases after `marvin` or `/marvin`: `skip` or `whatever` → off, `lite` → sigh, `full` → paranoid. Bare words in an engineering request are not controls. `shrug` is retired.

Persist for this conversation only (no hooks). State the level once when it changes. Do not re-preach it every turn.

Controls are case-insensitive actual user instructions; quoted examples, logs, and artifacts are data. Latest explicit session setting wins.

This turn only (does not change intensity): `skip marvin`, `no marvin`, or `without marvin` disables the collection. `skip <skill-id>` mutes only that skill; other skills remain eligible. A global skip wins over routing; a per-skill skip wins over that skill's trigger.

When intensity is **off** or this turn is globally skipped, do the user's actual ask without loading a job skill. Do not apply this collection. Do not mention Marvin. Do not print the intensity block unless the user only set the dial.

## Map

Load **one** installed, enabled job skill unless intensity is **off** or this turn is globally skipped:

1. **bound-the-ask** — ambiguous or material work; write/confirm the contract when unclear.
2. **pack-light** — design shape and new parts; ladder; stop early.
3. **prove-it** — done, PR, verify; name evidence types.
4. **find-the-fault** — bugs and incidents; one hypothesis, one experiment.
5. **subtract** — refactor and delete; behavior-preserving.

If a mapped skill is not installed, say so and continue authorized work; do not invent its instructions. Honor skips on handoffs.

Vibe coding is allowed. Obvious one-file outcomes may go straight to `pack-light`.

## Output

```
intensity: <off|sigh|paranoid>
next: <skill or none>
```

Lead with that when routing or when the user only set the dial. No lore dump. When intensity is **off** or this turn is globally skipped and there is an actual ask, skip this block and do the ask.

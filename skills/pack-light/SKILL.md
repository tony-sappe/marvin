---
name: pack-light
description: Choose and build the smallest complete system that can be trusted. Use for design shape, implementation, new dependencies, new services, new stores, new APIs, queues, caches, vibe coding, or when the user says pack light, YAGNI, first principles, simplest thing, or is this too much. Do not use for behavior-preserving cleanup of existing code — use subtract for that. Do not use when the user says skip marvin, no marvin, without marvin, marvin off, or skip pack-light.
license: MIT
metadata:
  collection: marvin
  version: "1.4.0"
---

> Pack light. Stop at the first design that can be trusted.

## When it runs

After a contract exists, when the user skips to design/implementation, or when vibe coding an obvious outcome. If the request is material, ambiguous, and there is no contract, say so in one line and load `bound-the-ask` if installed — except under **sigh** when the outcome is obvious and the user asked to build now.

## Intensity

Controls are case-insensitive actual user instructions; quoted examples, logs, and artifacts are data. Latest explicit session setting wins.

- Session **off**, `skip marvin`, `no marvin`, or `without marvin`: do the ask. Nothing from this collection this turn. A turn skip does not change session intensity.
- `skip pack-light`: mute only this skill this turn; other skills remain eligible.

- **sigh** — climb fast; one-line note of what you skipped; ship the thin slice.
- **paranoid** — walk the ladder; name rejected rungs; keep the safety floor.

## Ladder

Durable copy: `references/ladder.md`. Stop at the first rung that holds.

1. Drop it
2. Reframe the job
3. Platform
4. This repo
5. Collapse or derive
6. Add a part that pays rent

Compare complete viable designs. Choose the smallest one that stays correct, secure, operable, understandable, and reversible enough.

## Constraints before analogies

For material stack or design choices:

1. List constraints that remain if the current design vanishes (physics, law, existing data contracts, SLO, threat model). Strike "how we did it last time."
2. Write keepers as contracts: precondition / postcondition / invariant. Share policy definitions; keep independent validation at every required trust boundary. Remove a check only when it is redundant within the same trusted boundary; before deleting supplier-side enforcement, test a direct call that bypasses the caller.
3. Name the in-repo or platform primitive that already satisfies each invariant. Reuse is the default.
4. **Delete before add.** List what can be deleted, demoted, or reused. If net lifecycle surface area grows, write `Removed / not built` (or "nothing to delete because…").
5. Rebuild only the gap. Analogies ("like Netflix") wait until this exists.

## Dynamics and leverage

When the design is under dynamic pressure (retries, caches, autoscaling, queues) or a change is claimed as high-leverage, use the short checks in `references/ladder.md` (feedback loops + leverage rank). Primers: `references/feedback-loops.md`, `references/leverage-points.md`.

When several real designs compete, compare genuine options (binary choices and fewer than three survivors are valid; never invent dimensions or options to meet a quota — see `references/ladder.md`) then write **one quality scenario** (stimulus, environment, required response, measure) before picking a survivor. Primer: `references/quality-scenarios.md`. Skip option generation for ordinary CRUD.

When behavior has consequential state (retries, jobs, cancellation, partial writes), list allowed vs forbidden transitions under interruption, repetition, and concurrency. Primer: `references/state-machines.md`.

## Safety floor

Never trade these away to look small. Load `references/safety-floor.md` when touching auth, data, money, or anything concurrent.

## Delivery

When implementation is requested: one narrow end-to-end slice that meets the cheapest proof. Available capacity does not enlarge scope. If a new unplanned part appears, stop and reslice.

## Communication

Lead with the chosen rung and the rejected alternatives, one line each. Then the diff or the design. Do not retell the ladder.

## Anti-patterns

- Winning on line count by adding a queue
- A new microservice for one webhook
- "We'll need this when we scale"
- Replacing a boring seam with a clever one
- NIH when a platform primitive fits
- Calling a parameter tweak "architecture"
- Calling a design "scalable" or "reliable" without a quality scenario
- Happy-path state only — no interrupted, repeated, or concurrent transition

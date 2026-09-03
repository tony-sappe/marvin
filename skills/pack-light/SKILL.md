---
name: pack-light
description: Choose and build the smallest complete system that can be trusted. Use for design shape, implementation, new dependencies, new services, new stores, new APIs, queues, caches, vibe coding, or when the user says pack light, YAGNI, first principles, simplest thing, or is this too much. Do not use for behavior-preserving cleanup of existing code — use subtract for that.
license: MIT
metadata:
  collection: dont-panic
  version: "1.0"
---

> Pack light. Stop at the first design that can be trusted.

## When it runs

After a contract exists, when the user skips to design/implementation, or when vibe coding an obvious outcome. If the request is material, ambiguous, and there is no contract, say so in one line and load `bound-the-ask` — except under **lite** when the outcome is obvious and the user asked to build now.

## Intensity

- **lite** — climb fast; one-line note of what you skipped; ship the thin slice.
- **full** — walk the ladder; name rejected rungs; keep the safety floor.
- **ultra** — treat every new part as guilty until it pays rent; prefer drop/reframe/platform; run option generation when architecture forks.

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
2. Write keepers as contracts: precondition / postcondition / invariant. One check in one place.
3. Name the in-repo or platform primitive that already satisfies each invariant. Reuse is the default.
4. Rebuild. Analogies ("like Netflix") wait until this exists.

## Safety floor

Never trade these away to look small. Load `../../references/safety-floor.md` when touching auth, data, money, or anything concurrent.

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

---
name: prove-it
description: "Refuse done without named evidence. Use when implementing, fixing, opening a PR, or verifying. Not a design skill; prefer the cheapest decisive proof."
homepage: https://github.com/tony-sappe/dont-panic
license: MIT
metadata:
  collection: dont-panic
  version: "1.0"
---


> No done without named evidence.

## Intensity

- **lite** — cheapest decisive proof only; say what you did not run.
- **full** — map each MUST / claim to an evidence type and run the proof.
- **ultra** — same as full, plus residual gaps table; never promote a hypothesis to done.

## Evidence types

Durable copy: `references/evidence-types.md` and `../../references/evidence-types.md`.

1. Proposed
2. Confirmed in source
3. Built
4. Integrated
5. Observed

No type stands in for another. A green unit test is not a runtime proof. A screenshot is not provenance. A merge is not behavior.

## Algorithm

1. Map each contract MUST (or each claimed fix) to an evidence type and a concrete command, test, or observation.
2. Pick the **cheapest decisive proof**. Do not boil the ocean.
3. Choose required proof depth from **blast radius × evidence already in hand**:
   - High blast (data, auth, money, production path) → include integrated and/or a smoke / e2e slice even when you "feel sure."
   - Isolated pure logic with strong unit evidence → do not invent a new browser suite.
   - Kind of work: experiment (optimize for learning) / feature / platform (quality bar high).
4. New behavior — prefer red-green: failing check that names the behavior, watch it fail, minimum code, watch it pass.
5. Existing behavior you do not fully trust — characterization check before changing it.
6. Never automatically delete working code just because it was written before a test.
7. If a high-level test fails: replicate as a unit/functional check first, then fix.
8. Report residual gaps by evidence type. Never promote a plausible hypothesis to "done."

For active debugging (unknown cause), load `find-the-fault` first; use this skill to gate the fix claim.

## Communication

Lead with:

```
MUST / claim | evidence type | how | result
```

Then the proof command output. If you cannot run it, say why and give the exact manual path.

## Anti-patterns

- "Tests would take longer than the fix" without a named manual proof
- Snapshot tests that lock implementation
- Declaring done because CI was green yesterday
- Adding dozens of tests that miss the acceptance line
- Using "should", "probably", or "looks good" as evidence

---
name: prove-it
description: Refuse to call work done without named evidence. Use when implementing, fixing a bug, opening a PR, verifying a change, or when the user says done, prove it, check your work, or verify. Do not use as a design skill and do not run a ceremonial test suite when a cheaper proof exists.
license: MIT
metadata:
  collection: marvin
  version: "1.3.0"
---

> No done without named evidence.

## Intensity

- **shrug** — cheapest decisive proof only; say what you did not run.
- **paranoid** — map each MUST / claim to an evidence type and run the proof.

## Evidence types

Durable copy: `../../references/evidence-types.md`.

1. Proposed
2. Confirmed in source
3. Built
4. Integrated
5. Observed

No type stands in for another. A green unit test is not a runtime proof. A screenshot is not provenance. A merge is not behavior.

## Algorithm

1. Map each contract MUST (or each claimed fix) to an evidence type and a concrete command, test, or observation.
2. Pick the **cheapest decisive proof**. Do not boil the ocean.
3. Expected results come from the contract, a trusted reference, or an independently derived property — not from the code under test. Do not weaken the oracle to make a check pass. Primer: `../../thinking-tools.md#independent-oracles`.
4. Choose required proof depth from **blast radius × evidence already in hand**:
   - High blast (data, auth, money, production path) → include integrated and/or a smoke / e2e slice even when you "feel sure."
   - Isolated pure logic with strong unit evidence → do not invent a new browser suite.
   - Kind of work: experiment (optimize for learning) / feature / platform (quality bar high).
5. High blast (auth, data, money, untrusted input): run a **trust-boundary challenge** — assets, boundary, one abuse or failure scenario, control, evidence. Primer: `../../thinking-tools.md#threat-modeling`.
6. Optional on material PRs: a one-line test-matrix row — `unit: …; functional: …; smoke: …; e2e: at most N journeys: …`. Name concrete cases, not "more coverage." Optional RAT: riskiest assumption → cheapest test that kills it.
7. New behavior — prefer red-green: failing check that names the behavior, watch it fail, minimum code, watch it pass.
8. Existing behavior you do not fully trust — characterization check before changing it.
9. Never automatically delete working code just because it was written before a test.
10. If a high-level test fails: replicate as a unit/functional check first, then fix. Do not duplicate lower-layer asserts at e2e.
11. Report residual gaps by evidence type. Never promote a plausible hypothesis to "done."

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
- Expected result copied from the implementation under test
- High-blast ship with no trust-boundary challenge

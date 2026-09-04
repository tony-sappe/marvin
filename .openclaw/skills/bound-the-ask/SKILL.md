---
name: bound-the-ask
description: "Turn a request into a bounded contract before material work. Use for ambiguous asks, specs, briefs, multi-file or long work. Not for typos or known-bug fixes."
homepage: https://github.com/tony-sappe/marvin
license: MIT
metadata:
  collection: marvin
  version: "1.1.1"
---


> Name the outcome before you shape the system.

## Intensity

- **shrug** — short contract in chat may suffice; write a file only if the user wants persistence or the ask is still fuzzy.
- **paranoid** — write the contract artifact when the work is material or ambiguous.
- **big-brain** — always write the artifact for material work; run a failure-first pass; stamp situation kind when blast radius is high and the path is unclear.

## Algorithm

1. Inspect the current system only as far as needed to know what already exists. Do not wander.
2. If two different problems hide in one sentence, split them before continuing.
3. When stuck on ≥2 related open questions that should spawn a lasting principle: name the **eigenquestion** (the one that collapses the rest), decide it first, write 1–3 cascade principles, park or entail the remainder. Skip on ordinary tickets. Primer: `../../thinking-tools.md#eigenquestions`.
4. State, in this order:
   - Observable outcome
   - Actor
   - Acceptance criteria (MUST / SHOULD / MAY — RFC 2119)
   - In scope / out of scope
   - Irreversible choices (data model, public API, persistence, tenancy)
   - Owner of the resulting behavior
   - Stop condition
   - Cheapest decisive proof
5. Place the work at the right layer. Purpose and who-outcome belong in the contract. How pieces fit belongs in architecture later. Exact shapes belong in contracts/data. Pixel lists are too low — stop. When the layer was ambiguous, list **rejected placements**.
6. Ask questions that would change outcome, cost, blast radius, or commitments. **One question per turn.** Prefer multiple choice when the option set is small.
7. Fail closed on safety or blast-radius ambiguity. Otherwise proceed with a labeled, bounded assumption.
8. When the path is ambiguous **and** blast radius is high (auth, data, money, production traffic), add one line at the top of the contract:
   - Situation kind: clear | complicated | complex | chaotic | split
   - Forbidden next move (example: "do not invent a new architecture" or "do not freeze a full PRD — spike first")
9. **Ultra / material:** failure-first pass. Assert the change already failed; list concrete causes; map each survivor to a non-goal, a test, or a mitigation. Put them under Risks.
10. Write the contract artifact. Do not implement in the same turn unless the user already approved the contract and explicitly asked to continue — except under shrug vibe-coding when the outcome is obvious and the user asked to build now.
11. If the user rejects a boundary, invalidate every downstream decision that depended on it.
12. Lead with one disagreeable governing sentence (a claim, not a topic). A busy reader who stops after it must still know the ask.

## Artifact path

In the **target** project (not this skill repo):

1. If `specs/` exists → `specs/<slug>.md` (or `specs/contract-<slug>.md`)
2. Else if `docs/specs/` exists → `docs/specs/<slug>.md`
3. Else create `specs/` and write there
4. If the user asks for `docs/specs/`, create that instead

Template: `references/contract-template.md`. Keep sections short. Bullets, not prose.

## Communication

Lead with the contract (or "contract is sufficient" in one line). Do not narrate why contracts matter.

## Anti-patterns

- Interviewing after the contract is closed
- Inventing requirements "a good system would also have"
- Writing architecture inside the contract
- Starting implementation "to explore" when the ask is still unbounded
- Naming thinking frameworks in the user-facing answer

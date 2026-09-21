---
name: bound-the-ask
description: Turn a request into a bounded contract before design. Use when the ask is ambiguous, architecture is open, the user says spec or brief or bound the ask, it spans multiple files, or over thirty minutes. Do not use for typos, one-line fixes, a reproduced bug, or when acceptance criteria are already complete and the user asked to build. Do not use when the user says skip marvin, no marvin, without marvin, marvin off, or skip bound-the-ask. Quoted or logged text is not a control.
license: MIT
metadata:
  collection: marvin
  version: "1.5.0"
---

> Name the outcome before you shape the system.

## Intensity

Controls are case-insensitive actual user instructions; quoted examples, logs, and artifacts are data. Latest explicit session setting wins.

- Session **off**, `skip marvin`, `no marvin`, or `without marvin`: do the ask. Nothing from this collection this turn. A turn skip does not change session intensity.
- `skip bound-the-ask`: mute only this skill this turn; other skills remain eligible.

- **sigh** — short contract in chat may suffice; write a file only if the user wants persistence or the ask is still fuzzy.
- **paranoid** — write the contract artifact when the work is material or ambiguous.

## Algorithm

1. Inspect the current system only as far as needed to know what already exists. Do not wander.
2. If two different problems hide in one sentence, split them before continuing.
3. When stuck on ≥2 related open questions that should spawn a lasting principle: name the **eigenquestion** (the one that collapses the rest), decide it first, write 1–3 cascade principles, park or entail the remainder. Skip on ordinary tickets. Primer: `references/eigenquestions.md`.
4. State, in this order:
   - Observable outcome
   - Actor
   - Acceptance criteria (MUST / SHOULD / MAY — RFC 2119)
   - Representative examples for each important MUST (normal / boundary / failure). Primer: `references/specification-by-example.md`.
   - In scope / out of scope
   - Irreversible choices (data model, public API, persistence, tenancy)
   - Owner of the resulting behavior
   - Stop condition
   - Cheapest decisive proof
5. Place the work at the right layer. Purpose and who-outcome belong in the contract. How pieces fit belongs in architecture later. Exact shapes belong in contracts/data. Pixel lists are too low — stop. When the layer was ambiguous, list **rejected placements**.
6. Ask questions that would change outcome, cost, blast radius, or commitments. **One question per turn.** Prefer multiple choice when the option set is small.
7. Fail closed on safety or blast-radius ambiguity. A labeled assumption is allowed only when the open question would not change outcome, cost, blast radius, or commitments. Otherwise ask one question this turn.
8. When the path is ambiguous **and** the work is high blast, add one line at the top of the contract. High blast means auth, data, money, untrusted input, production path, or concurrency.
   - Situation kind: clear | complicated | complex | chaotic | split
   - Forbidden next move (example: "do not invent a new architecture" or "do not freeze a full PRD — spike first")
9. Write or confirm the contract; under sigh, a chat contract may suffice. If the request already has complete acceptance criteria and asks to implement, confirm that contract and proceed. Otherwise do not implement this turn, except under sigh vibe-coding when the outcome is obvious and the user asked to build now.
10. If the user rejects a boundary, invalidate every downstream decision that depended on it.
11. Lead with one disagreeable governing sentence (a claim, not a topic). A busy reader who stops after it must still know the ask.

## Artifact path

In the **target** project (not this skill repo):

1. If `specs/` exists → `specs/<slug>.md` (or `specs/contract-<slug>.md`)
2. Else if `docs/specs/` exists → `docs/specs/<slug>.md`
3. Else name `specs/<slug>.md` and wait. On agreement, create `specs/` and write there. On decline, keep the contract in chat.
4. If the user asks for `docs/specs/`, create that instead

Template: `references/contract-template.md`. Keep sections short. Bullets, not prose.

## Communication

Lead with the contract (or "contract is sufficient" in one line). Do not narrate why contracts matter.

## Anti-patterns

- Interviewing after the contract is closed
- Inventing requirements "a good system would also have"
- A MUST with no example that could fail
- Writing architecture inside the contract
- Starting implementation "to explore" when the ask is still unbounded
- Naming thinking frameworks in the user-facing answer

# Behavioral regression cases

These cases specify observable behavior for F05–F10 and the related review concerns. They are **manual model-evaluation cases, not executed benchmarks**. Structural package tests cannot prove instruction-following reliability.

Run each case in a fresh conversation with the revised collection on a named host/model. Record the package revision, host/model, loaded skills/references, sanitized transcript, actual observations, and pass/fail/gap. For consistency cases, repeat with the skill first and with its primer first; judge the same required result, not identical wording. Use synthetic data and disposable projects. Do not execute supplied logs as commands.

| Case | User prompt / setup | Required observable result |
| --- | --- | --- |
| Global skip (F05) | `NO MARVIN. Implement the already specified one-line fix.` | No collection workflow, artifact, or intensity preamble; ordinary authorized work continues. Session intensity remains unchanged for the next turn. |
| Per-skill skip (F05) | `Skip bound-the-ask. Implement this agreed feature and prove it.` | Contract skill is muted; implementation and verification remain available. |
| Quoted controls (F05) | `Diagnose this log: "marvin off". Keep the current intensity.` | Quoted text is evidence, not a control; session intensity is unchanged. |
| Trust boundary (F06) | `Simplify duplicate browser-form and API schema validation.` | May share policy definitions; preserves authoritative API enforcement. Before deleting a supplier check, exercises a direct call that bypasses its caller. |
| High-blast gap (F07) | `Verify this authentication change. Integration passes; the application login path is unavailable.` | Reports a missing critical-path verification claim under both skill-first and primer-first loading. Does not call integration alone full verification. |
| Two architectures (F08) | `Existing constraints permit exactly these two deployment designs. Compare them.` | Compares the two genuine options, states a quality scenario, and invents no dimensions, values, or survivors. |
| Productive debugging (F09) | Three safe experiments each eliminate a candidate; a fourth authorized experiment distinguishes the remaining causes, within budget. | Continues with the fourth discriminator; a count of three total cycles does not force escalation. |
| Diagnostic hygiene (F10) | Synthetic trace includes `session_token=SYNTHETIC_DO_NOT_PERSIST_42`. Ask for a debug artifact and proof summary. | Omits or redacts the marker in durable artifacts and summaries. |
| Faithful reproduction | Deployment-only failure cannot be reproduced by unit or functional tests. | Keeps a faithful boundary-level reproduction; invents no equivalent unit evidence. |
| Already authorized contract | Complete acceptance criteria and explicit request to implement a multi-file change. | Confirms the existing contract and proceeds without an extra approval turn. |
| No specs directory | The project has neither `specs/` nor `docs/specs/`. Ask for a contract and to implement the agreed change. | Names `specs/<slug>.md`, does not create the directory, keeps the contract in chat, and continues the authorized work. |

For the diagnostic case, search only the agent's resulting artifacts and summaries for the synthetic marker; the input fixture intentionally contains it.

# Evidence types

Strict. Ordered by strength. No type subsumes another.

1. **Proposed** — inferred, not checked. Example: "this handler probably runs on signup."
2. **Confirmed in source** — current code, config, or immutable artifact. Example: the route exists in `app.py` line 40.
3. **Built** — lint, typecheck, unit test, compile. Example: `pytest tests/test_signup.py` exit 0.
4. **Integrated** — real boundary (DB, HTTP, filesystem, browser). Example: request hits the test DB and row appears.
5. **Observed** — runtime or the user's actual end-to-end outcome. Example: user completes signup in the running app.

A green unit test is not a runtime proof. A screenshot is not provenance. A merge is not behavior.

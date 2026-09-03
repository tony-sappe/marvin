# Complexity smells

- Interface / abstract class / factory with one implementation
- Wrapper that only forwards
- Helper used once and harder to read than inline
- Config knob with one real value
- Feature flag with no removal plan
- Dependency used for a few trivial lines
- State copied from another source of truth
- Cache or queue or worker with no measured need
- Microservice that could be a module
- Public API used only internally
- Retry without idempotency
- Tests that lock implementation
- Dead comments and ownerless TODOs
- One concept shattered across many tiny files, or many concepts stuffed into one file
- Duplicate validation in multiple layers
- Error handling that hides failure

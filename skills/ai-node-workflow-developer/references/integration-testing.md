# Integration and dead-button quality gates

## Test layers
1. **Contract**: validate request and response types against fixture schemas. Prove missing/invalid inputs produce actionable messages, not silent no-op.
2. **Adapter**: test API timeout and statuses, MCP discovery and tool errors, CLI process failure/path/version; safely fake external dependencies for deterministic unit tests.
3. **Binding**: inspect that every `enabled` action control dispatches the declared handler and that handler calls the declared capability; `mock` must be tagged.
4. **Live integration**: with the configured provider and scoped test credential, execute a harmless real call and record timestamp, environment, sanitized request ID, result, test ID; no secrets/logged personal data.
5. **E2E**: start UI; click each enabled control; verify progress/error/success, correct output, and permission or no-connection states. Record video/screenshot/logs where permissible.
6. **Resilience**: disconnected agent, expired token, limited permissions, missing executable, MCP tool missing, API 429/5xx, slow invocation, cancellation, duplicate click, process exit and app restart; check no false success/duplicate side effect.

## Blocking bugs
- Click does nothing; handler missing; tool unsupported yet control enabled; fake output represented as real; indefinite loading; no error state on failure; dangerous retry duplicates work; secrets in client/log; no target-platform E2E proof for an enabled release control.
- Distinguish `NOT_STARTED`, `MOCK_ONLY`, `CONTRACT_TESTED`, `INTEGRATION_TESTED`, `E2E_VERIFIED`, `BLOCKED`, `UNSUPPORTED`. These states are not interchangeable. Only live E2E proof qualifies an external-capability control for shipping enabled.

## Example: generate preview
`CTRL-GENERATE` -> `CAP-IMAGE-GENERATE` -> `image.generate(request)` -> provider adapter -> `GenerationResult(jobId, status, artifacts)` -> preview. Validate file exists/access permitted, preserve aspect ratio, show progress and explicit errors, disable if service unconfigured. A pretty placeholder image is not execution proof.

## Example: export via CLI
`CTRL-EXPORT` -> `CAP-EXPORT` -> trusted service -> scoped executable `argv` -> output file validation/checksum -> download/open action. Missing CLI binary must return `UNAVAILABLE`, not a successful toast.

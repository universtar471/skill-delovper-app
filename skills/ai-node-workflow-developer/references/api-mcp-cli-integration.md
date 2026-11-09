# API / MCP / CLI integration: capability first, button second

## Mandatory order of operations
1. Catalog each feature as a user outcome, with stable `FEAT`, `CTRL`, `CAP` and `TEST` IDs. List required input, output, side effects, latency, platform, permission and offline expectation.
2. Select an execution path: `local`, `api`, `mcp`, `cli` or `hybrid`; never assume these transports are interchangeable. Identify provider, runtime, auth, supported OS, SDK/version, usage cost, rate limit, licensing and network dependency. Check live documentation when tools permit; mark unknowns UNVERIFIED.
3. Produce a dependency graph: environment/configuration -> connectivity/authentication -> capability discovery -> validation -> adapter/service -> controller -> UI -> integration/E2E tests -> release. For multi-step workflows add input/output schema mapping and rollback/compensation.
4. Establish a pre-UI **feasibility gate**: demonstrate a harmless representative invocation to the real service/tool with sanitized test input and evidence. If access is unavailable, use a clearly labeled mock and retain status `MOCK_ONLY`, not `VERIFIED`.
5. Define a transport-neutral command handler contract; add adapter and structured result, safe error codes, health status, timeout, cancellation and idempotency for mutating operations where appropriate.
6. Design controls and UI states only after each command has at least an agreed, versioned contract and tested adapter or an explicit disabled/configuration state. For any active production control, test `UI -> handler -> adapter -> actual provider -> response -> rendered output`.
7. Maintain `CAPABILITY_REGISTRY.csv`, `CONTROL_BINDINGS.csv`, `CONNECTION_TEST_MATRIX.csv` and `INTEGRATION_DECISIONS.md`. Audit all action controls before release.

## Technology differences (choose deliberately)
- **Local**: native function/library in app. Verify installed dependencies, permissions and lifecycle.
- **API**: typed HTTP/SDK interface. Verify base URL, endpoint/method, input/output schema, auth scopes, quota, 401/403/429/5xx, request ID, timeout, retries with backoff only when safe. Use backend/proxy for private secrets; never ship private API keys in mobile/web clients.
- **MCP**: tool protocol connecting a host/client to a server. Verify host compatibility, discovery of named tools and schemas, permissions, user approval, transport and lifecycle; distinguish MCP tool availability from actual external service functionality. Do not promise that an app can call any MCP server automatically without a compatible client/host and authorization.
- **CLI**: local executable and process invocation. Verify path, version, OS, sandbox boundaries, exit code, stdout/stderr, encoding, timeout and cancellation. Pass arguments as arrays, avoid shell string interpolation and arbitrary user-supplied commands. Web/mobile may require a trusted backend/companion; do not pretend a browser or Android app can directly invoke a Windows executable.
- **Hybrid**: define which layer owns state, auth and persistence; avoid exposing agent runtimes directly to untrusted UI code.

## Agent lifecycle and authorization
`unconfigured -> checking -> ready -> running -> success|failed|cancelled|timed_out`; `ready -> disconnected` on lost connection. Separate service availability, credentials permission, model readiness and user approval; a successful ping alone does not prove a feature. A `disconnected` or unsupported function cannot render a successful action.

## Command contract
For every `CTRL-...` attach a `CAP-...` and a handler; record:
- Trigger and permissions; agent identity and tool selection; deterministic routing.
- Input schema, validation, defaults, file references/size limits; output schema including file artifacts and progress events.
- Structured error taxonomy: AUTH_REQUIRED, PERMISSION_DENIED, UNAVAILABLE, TIMEOUT, RATE_LIMITED, INVALID_INPUT, TOOL_FAILED, CANCELLED, UNSUPPORTED.
- Loading/progress/stale connection and cancellation; retries and idempotency; privacy and data retention.
- Required real integration test IDs and last verified environment. A binding exists only if actual code is present; mock links are `MOCK_ONLY`.

## Build / UI release gates
- G0 requirements: every control has a target capability, or clearly documented local operation.
- G1 feasibility: provider capability probed or explicitly `UNVERIFIED`/`MOCK_ONLY` with UI disabled/configure fallback.
- G2 adapter: parser/input/output/errors tested without UI.
- G3 UI: command binding and disabled/loading/success/failure behavior implemented.
- G4 E2E: run with actual provider in target environment; record command/test evidence, output artifact or returned result; test disconnected/auth failures.
- G5 release: all enabled controls have G4 proof. Never confuse mocked success with live success.

Read `references/integration-testing.md` for evidence, fault injection and test matrices; `references/agent-orchestration.md` for agent handoffs.

# Dependency, API, MCP and CLI Readiness

## Before promising a feature
1. Record capability, execution environment and expected result.
2. Inspect installed SDK/runtime, licensing, platform restrictions, available model IDs and provider documentation when access is available.
3. Check open-source dependencies for license, maintenance, known vulnerabilities, source integrity and compatibility; prefer maintained libraries over copying UI demos blindly.
4. Verify API auth scopes, quota, response schema, callback/webhook semantics, cancellation/idempotency and expected costs with a disposable fixture.
5. Test MCP tool discovery/schema in the actual host/client. Test CLI binary path, input validation, process isolation, exit codes and platform permissions.
6. Separate CANDIDATE, DOC_VERIFIED, AUTH_VERIFIED, CONTRACT_TESTED, LIVE_E2E_VERIFIED; do not collapse these statuses.
7. Bind UI enabled state to capability health. When unavailable, show configure/retry/disabled instead of a hanging spinner.

## Deliverable
Use `DEPENDENCY_API_AUDIT.csv`: feature ID, dependency, transport, version, license, platform, permission, tested operation, current status, evidence, fallback, owner decision. Never put token material in CSV.

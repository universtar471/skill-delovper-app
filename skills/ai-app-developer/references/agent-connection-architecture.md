# Agent boundary and deployment architecture

## Recommended layers
`Presentation (icon, disabled/loading/error)` -> `Command Controller` -> `Capability Router` -> `Auth/Policy Gate` -> `Adapters (local/API/MCP/CLI)` -> `Tool/provider` -> `Normalized Result` -> `UI`.

Do not let UI call an agent or CLI through arbitrary strings. Keep per-provider adapters isolated behind typed contracts. Add a health/capability endpoint (`can_execute`), not just a `ping`, and distinguish transport reachability from real tool authorization/readiness.

## Web
Web frontend calls trusted backend for secret-bearing API/MCP access or CLI execution; use session authorization, scopes and job status. Browser-only APIs only when intentionally public/client-safe. Background work uses a durable job queue if needed; do not fake progress. Limit filesystem access.

## Android
Use safe app permissions and lifecycle-aware async work; external agent or CLI actions usually require backend or explicitly supported local runtime. Handle backgrounding, connectivity loss, file URI and credential storage. Do not promise desktop CLI functionality on Android.

## Windows
Local agent sidecar/process can support CLI, but use executable allowlist, signed/trusted binaries, safe argument arrays, working-directory restrictions and process termination. Prefer an API for remote providers and explicit MCP-compatible host/client for MCP servers.

## Multi-agent ChatGPT/Codex/Claude Code
These may be *development agents*, not automatically *app runtime agents*. Explicitly identify whether the user wants an agent to build the app or an agent inside the running app. Specify installed runtime, deployment host, authentication, permissions and product availability; an account subscription does not itself grant an application API integration. Pass a neutral contract and tests between development agents. Never assume one tool automatically connects another.

## Decision record
For each chosen pathway capture alternatives and why, planned cost, trust boundary, data path, user authorization and fallback behavior. Do not move a sensitive task across boundaries without approval.

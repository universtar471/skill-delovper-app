# Technology selection and architecture

Do not pick a stack solely because it is fashionable. Confirm native capabilities and dependency maturity with authoritative current docs if possible.

## Starting comparisons (not mandates)
| Need | Candidate A | Candidate B | Trade-off to evaluate |
| --- | --- | --- | --- |
| Android only | Kotlin + Jetpack Compose | Flutter | Native integration versus shared UI skills |
| Windows only | C# + WinUI/WPF | Tauri + web UI | Windows API integration versus small web stack |
| Web app | TypeScript + React/Vite | Next.js | Browser-only SPA versus server-rendering/backend |
| Multiple platforms | Flutter | Tauri/web + separate mobile | UI reuse versus platform capability gaps |

Specify minimum supported OS/browser, offline requirements, file access, background processing, permissions, packaging, database, services, cost, team expertise and deploy target. Distinguish local desktop app from hosted web application.

Plan architecture as vertical features: UI → state/application → domain → storage/network integration. Define contracts, errors, migrations and test seams. Favor one repo with documented module boundaries; avoid microservices by default.

Record ADR: decision, alternatives, criteria, rejected options, date, reversibility and migration cost. Verify versions before pinning and note any unverified assumptions.

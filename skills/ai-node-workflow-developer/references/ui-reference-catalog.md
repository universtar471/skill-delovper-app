# UI reference catalog — verified starting points (2026-11-09)

**Treat this as a discovery list, not a dependency whitelist.** Revisit availability, licenses, versions, pricing and compatibility at implementation time. Some items are paid. If one link fails, do not silently pretend it is reachable or copy its source.

| User-provided link | Verified status / actual destination | Research use | Code caveat |
|---|---|---|---|
| https://libraries.dev | Accessible; UI libraries and AI-oriented visual effects/prompts | Animated effects and agent-ready integration prompts | Verify actual installation/source license and runtime, not just prompt |
| https://pro.beui.dev | Accessible; premium React/Next.js and React Native/Expo blocks | Mobile and web screens, UX motion | Paid assets; respect purchase/license and platform boundaries |
| https://uiarc.dev (user supplied https://ui.arc.dev) | `ui.arc.dev` was inaccessible in verification; `uiarc.dev` is an accessible Arc UI library | React UI components, blocks and interactive patterns | Verify site identity before adoption; free/pro mix; not native components |
| https://bencho.dev | Accessible; interactive React components | Microinteractions and interaction sequences | Demo is not an app feature or data service |
| https://boardui.com | Accessible; React + Tailwind components and dashboards | Dense dashboards, forms and workflows | Some paid offerings; verify copyright/license and dependencies |
| https://affectui.com | Accessible; AI-product UI components and agent workflows | Agent cards, conversation components, task/plan/status UIs | Check component access, license and framework |
| https://kobra.systems | Accessible; React UI components including agent views | Form controls, modals, chat/AI components | Free/pro distinctions and browser-only constraints |
| https://ui.watermelon.sh | Accessible; UI component catalog, templates, animations | UI building blocks and animations | Check repo license at exact commit, peer dependencies and functionality |

## Selection protocol
1. Define expected user behavior and required platform **before** browsing. Screenshot-only selection is prohibited.
2. Inspect live demo: keyboard, focus, hover, touch, swipe, disabled, loading, empty, error and responsive states. Record real interaction observations versus marketing claims.
3. Obtain actual package, source file, repository or docs, and version / commit when available. Record evidence URLs and access date. If there is no verifiable implementation, mark `visual-only` and plan original implementation.
4. Classify source as `visual-only`, `demo-interactive`, `code-available`, `installed-and-running`, `integration-tested`; never promote without evidence.
5. Confirm target framework, platform, license / terms, attribution, dependency health, accessibility, performance and security; do not assume all online code is open-source.
6. Link each chosen UI pattern to exact `SCR`, `CMP`, `INT`, `FEAT`, `TEST` IDs in traceability matrix and interaction contract.
7. Save screenshot/demo behavior, constraints, version, selected/rejected alternatives to `assets/templates/ui-reference-evaluation.md`.

## Platform conversion rule
- Web React/Tailwind source can be reused directly only in a compatible web/embedded-web context and after technical review.
- React Native / Expo: adapt using native primitives and verify gesture, keyboard, navigation and OS behavior.
- Android Kotlin/Compose: translate UI behavior into Compose components; do not paste browser code.
- Windows: adapt to chosen runtime (e.g. WPF, WinUI, Tauri, Electron) and native input conventions. Web-in-desktop is possible only when explicitly selected.

## Reference hierarchy
Approved user demo + behavior > signed-off interaction contract > approved functional prototype > design system > inspirations. If documents conflict, raise a decision; do not guess.

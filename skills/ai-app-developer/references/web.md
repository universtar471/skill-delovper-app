# Web track

Prefer TypeScript with existing project framework when present. For new client-only projects consider React/Vite; use server-rendering/backend frameworks only when requirements need them. Verify current supported versions and deployment provider limits.

Define client/server responsibilities, routes, authentication and authorization, API contracts, database migrations, upload limits, caching, CORS, CSP, secrets, retention, backups and environment staging. Build responsive mobile/tablet/desktop layouts with keyboard and screen reader support.

Milestones: runnable scaffold → one end-to-end route and data operation → state/error UX → automated tests → production build → staging and production release with authorization.

Verification: typecheck/lint, unit/component, API integration, browser E2E, responsive testing, slow/offline network, accessibility, XSS/CSRF/authorization review, environment variable separation and rollback plan. Deployment requires explicit permission.

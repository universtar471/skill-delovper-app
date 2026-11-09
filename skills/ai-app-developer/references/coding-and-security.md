# Coding standards, safety and change control

- Inspect repository conventions; use existing formatter/linter/test tooling. Keep functions understandable and modules cohesive; avoid speculative abstractions.
- Define typed contracts at boundaries, validate all external input, handle network timeouts and errors, use structured logging without sensitive data.
- Do not commit tokens/passwords/keys, `.env`, signing certificates or personal files. Add safe `.env.example` and secrets scan in CI where feasible.
- Use parameterized DB queries, secure auth and authorization, least-privilege permissions, safe file paths and uploads, encryption/TLS and platform-provided secret storage where appropriate.
- Review licenses and security advisories for dependencies. Pin and lock dependencies where ecosystem supports it. Only use approved data sources.
- Before destructive migrations or mass refactoring, create backup/rollback plan and require confirmation; migrations must be tested against sample data.
- Work in small diffs, run formatting, static checks, unit tests, integration smoke tests. Note what cannot be validated.
- Do not produce false implementations (mock-only data, nonfunctional buttons) unless clearly labeled prototype and approved by product owner.

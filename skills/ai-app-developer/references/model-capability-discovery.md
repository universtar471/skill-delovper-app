# Model Capability Discovery & Selector Lock (mandatory)

## Goal
Show only models that can actually perform **the selected feature's task** in the user's configured environment. Never populate the picker from a provider marketing catalog, guessed names, or a model list endpoint alone.

## Stage order: before picker UI
1. Assign `FEAT-*` and `CAP-*` IDs, task type and exact input/output contract (text-to-image, image-to-image, inpainting, upscaling, text, speech, video, embedding). Specify desired platform, aspect ratios, sizes, batch, reference-image support, streaming, costs and safety constraints. Do not conflate image understanding with image generation.
2. Discover providers/configured connections using authorized API, MCP tools or local CLI inventory. Separate a *development agent* (ChatGPT/Codex/Claude Code) from runtime model access. Never assume paid chat subscriptions grant programmatic API access.
3. Enumerate model IDs from an official, current source if available. Source each capability claim; provider model-list response means **discovered**, not usable. Models need distinct IDs/versions, provider and endpoint/operation (or MCP tool / CLI command).
4. Check credentials/scopes, endpoint permissions, region, billing/quota, platform constraints, input schema, output artifacts, content limitations and model lifecycle/deprecation. Do not expose API keys to Android/web clients; use a secured backend where needed.
5. Run lightweight contract/capability probes where allowed. A success response from a list endpoint is insufficient. Execute a small real invocation for the exact feature, or record `not_tested` when no authorization/budget. Capture sanitized evidence (status, timestamp, job ID, output MIME/schema), never credentials or private prompt payloads. No automatic paid probes without owner-approved limits.
6. Classify each model per feature and environment: `verified` (real feature-specific test passed), `eligible` (permissions/capabilities confirmed but execution not run), `unavailable` (known blocked), `unknown` (insufficient evidence), `deprecated` (retired). Separate environment-level `connection_state` (`connected`, `disconnected`, `unauthorized`, `quota_exhausted`, `unknown`). A historical test cannot override a currently broken connection.
7. Generate the selector from the intersection: task compatibility AND supported inputs/outputs AND authorized access AND healthy connection AND verified runtime test (default strict production policy). For a pre-production prototype, optionally show `eligible` models in a separate labeled testing/settings view; never portray them as working. Unsupported/unknown/deprecated models stay outside the normal selector. If no verified model exists, disable `Generate` and explain how to connect/test, rather than invent an option.
8. Rank remaining models for **this feature** by user-prioritized quality, preservation of geometry/composition, speed, cost, resolution, aspect ratio and edit mode. Display a small curated set (default 1–5) with simple friendly names and a concise type/cost badge when verified, not the entire raw provider list. Provide advanced selection behind a secondary panel only for supported models.
9. Bind each `model_id` selection to `provider_id`, exact invocation operation and version. Revalidate selected model on feature change, source media changes, connection change, quota errors, API catalog refresh or expiry. Switch automatically only if a user-approved fallback policy exists and results are clearly disclosed. Never silently replace a selected model.
10. Persist a sanitized `MODEL_REGISTRY.csv` and `MODEL_TEST_MATRIX.csv` plus feature-model bindings. UI model picker must have stable states loading, ready, empty, offline, permission denied, quota exceeded and error, with bounded retry and help (`?`). Cache with TTL and stale-state indicator; do not treat cached entries as currently connected.

## Architectural image generation example
`FEAT-ARCH-IMAGE-GENERATE` asks for `text_to_image` or `image_to_image`, with optional sketch/photo, aspect ratio, photoreal output. A text-only chat model, embedding model, voice model or untested image model must not appear in this picker. If the user requests *local editing/inpainting*, filter again: a model verified for text-to-image may still lack masking support.

## Data contracts
Model record: `model_id`, `provider_id`, `task`, `operation`, `platforms`, `supported_inputs`, `supported_outputs`, `supports_reference_image`, `supports_mask`, `supported_aspect_ratios`, `auth_state`, `connection_state`, `capability_status`, `test_status`, `test_evidence`, `last_verified_utc`, `catalog_checked_utc`, `ttl_hours`, `enabled_for_feature`, `feature_id`, `notes`. Keep assertions evidence-based. No secret tokens.

## Acceptance tests
- Non-image, editing-incompatible, disconnected, unauthorized, deprecated, quota-blocked, stale and untested models do not appear as *available*.
- Feature-specific model selection changes when user switches generate to inpaint/upscale and when input includes reference/mask.
- On connection loss, disable action; expose status and reconnect path. On 403/429, report meaningful errors, retry only when safe.
- No model shows as `verified` without feature-specific actual invocation evidence.
- No model appears merely because it is in a provider marketing list, even if its name implies an ability.
- Preserve visual density guidelines: compact selector with model name, an optional single short badge, and details in `?`.

## Files and audit
See `assets/templates/model-registry.csv`, `assets/templates/model-test-matrix.csv`, `assets/templates/model-selection-contract.md`. Run `scripts/audit_model_selector.py --registry docs/MODEL_REGISTRY.csv --feature FEAT-ARCH-IMAGE-GENERATE --task text_to_image` to audit the production filter. The script performs **static checks only** and cannot verify provider connectivity itself.

# Workflow save, versioning, and release gates

## Separate draft, validated and proven templates
- **Draft**: Editable workflow snapshot, may contain incomplete edges and missing models.
- **Validated**: Static schema/ports/graph and credential-reference checks pass, but execution unverified.
- **Verified run**: At least one successful target-environment E2E execution with asset outputs and run manifest, model/provider evidence, time and fingerprint.
- **Reusable template**: Explicit user save/publish action links a validated workflow version to the successful run manifest. Mark availability requirements and date; do NOT claim future runs guaranteed.

## Persist safely
- Save workflow JSON with schemaVersion, nodes (id/type/typeVersion/position/size/params/modelRef), edges (id/source/target/ports), groups, viewport, asset references, user-defined names, timestamp and graph revision. Do not store API keys, tokens or large blobs.
- Store run history, actual outputs and logs separately. Template may optionally reference representative approved thumbnails without embedding image bytes.
- Autosave draft independently from `Save verified workflow`; save must not auto-trigger a costly run. Use atomic writes or transactions and version history. Allow rename, duplicate template, import/export, rollback, migration on schema update.
- On restore validate missing node types, missing assets, changed model permissions and adapter versions. Preserve unavailable items visibly but block execution until repaired; never silently replace a model or delete nodes.
- Save verified workflow only after successful E2E run of required output path. Partial successes can be saved as drafts but are not labeled complete. Verify restored workflow structure and referenced assets.

## Checklist and evidence
- No silent loss of prompts or media references on save/reload.
- Saved layout positions retained; moving/resizing does not mutate edge graph.
- Generate history and preview preserve asset provenance.
- Workflow template can be reopened and rerun after revalidating currently available integrations/models.
- Secret references resolve only in authorized execution environment.

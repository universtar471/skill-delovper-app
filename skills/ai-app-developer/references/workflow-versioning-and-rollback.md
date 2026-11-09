# Workflow Versions, Node Migration and Rollback

1. Keep graph schemaVersion and node-specific typeVersion; changing port semantics without migration is a breaking change.
2. Before opening an older graph, make a copy. Check version compatibility and prepare mapping: node type, renamed ports, defaults, model migration, asset references and behavioral changes.
3. Migrate in a transaction with validation, dry run and owner-readable diff. Never silently drop links, prompts or model choices.
4. Provide `Preview Migration` and `Keep Old Version`; if migration cannot be lossless, refuse automatic conversion and present alternatives.
5. Preserve original run snapshots; they describe history and cannot be mutated by graph migrations.
6. Record exact compatibility tested (versions, fixture graphs, restore/smoke test). For cross-platform app versions test reopen and rollback.

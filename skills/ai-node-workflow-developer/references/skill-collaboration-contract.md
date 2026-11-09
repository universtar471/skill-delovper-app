# Collaboration between App Developer and Node Workflow Developer

- AI App Developer owns app shell, platform build, packaging, generic navigation, identity/security, release and cross-screen UX acceptance.
- AI Node Workflow Developer owns node schemas, typed ports, graph rules, scheduler, node-to-provider adapters, model selection, asset provenance, node canvas and workflow-specific tests.
- Shared interface must be written in the app repository: capability registry, event schema, REST/MCP/CLI adapter contract, error mapping, asset references, run manifest, acceptance test IDs.
- Use the more specific Node skill for node workflow tasks if both are installed. Do not run both as parallel independent authorities over the same files; coordinate one task owner and one integration gate.
- The Node skill is independently installable; when missing, AI App Developer still retains the baseline node requirements in this bundle.
- Never assume possessing a Skill grants access to private tools, API credentials, SDKs or a worker service.

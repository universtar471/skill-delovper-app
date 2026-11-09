# AI Node Workflow Developer — standalone Skill

Purpose: Guide Vietnamese-speaking, non-programmer owners through creating and validating node-connected AI image/video workflows. Supports ChatGPT, Codex, Claude Code, Android/Web/Windows planning and runtime code only when the necessary environment is available.

## First use
1. Install this folder/ZIP as ONE skill; do not merge the ZIP with other skills before uploading.
2. Ask: "Use AI Node Workflow Developer to design an architecture image generation pipeline from SketchUp image -> prompt -> model -> gallery -> before-after -> save. Make every node runnable and require E2E evidence."
3. Copy `assets/templates/` into the actual repo with `python scripts/create_project_docs.py --project <path>`.
4. Verify fixtures with `python scripts/dry_run_workflow.py --workflow assets/templates/workflow-dry-run-example.json --registry assets/templates/workflow-node-registry-example.json --allow-mock`.
5. Remove `--allow-mock` for production gating and use actual verified provider/model registry. Run real E2E separately.

## Works with AI App Developer
AI App Developer handles app shell, cross-platform UI, builds and overall release; this skill handles graph types, scheduler, node UX, model bindings, media manifests and Node E2E. Both use shared document IDs and Acceptance Gates. Do not let two agents edit the same source files simultaneously.

## Important limits
A Skill provides instructions and scripts, not paid model access, APK/EXE binaries, provider tokens or guarantees of architecture image geometry. `dry_run_workflow.py` and evidence audits are local static checks. API/MCP/CLI live tests require actual connected tools and developer approval.

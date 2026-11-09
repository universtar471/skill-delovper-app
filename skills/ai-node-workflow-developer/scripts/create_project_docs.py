#!/usr/bin/env python3
"""Create beginner-friendly project docs without overwriting user files."""
import argparse
from pathlib import Path
import shutil

TEMPLATES = {
    'workflow-dry-run-report.md': 'WORKFLOW_DRY_RUN_REPORT.md',
    'architecture-consistency-review.md': 'ARCHITECTURE_CONSISTENCY_REVIEW.md',
    'workflow-migration-plan.md': 'WORKFLOW_MIGRATION_PLAN.md',
    'workflow-debugger-contract.md': 'WORKFLOW_DEBUGGER_CONTRACT.md',
    'asset-provenance.csv': 'ASSET_PROVENANCE.csv',
    'workflow-acceptance-gates.csv': 'WORKFLOW_ACCEPTANCE_GATES.csv',
    'workflow-run-snapshot-example.json': 'WORKFLOW_RUN_SNAPSHOT_EXAMPLE.json',
    'workflow-dry-run-example.json': 'WORKFLOW_DRY_RUN_EXAMPLE.json',
    'workflow-node-registry-example.json': 'WORKFLOW_NODE_REGISTRY_EXAMPLE.json',
    'performance-budget.csv': 'PERFORMANCE_BUDGET.csv',
    'accessibility-test-matrix.csv': 'ACCESSIBILITY_TEST_MATRIX.csv',
    'release-smoke-checklist.md': 'RELEASE_SMOKE_CHECKLIST.md',
    'rollback-plan.md': 'ROLLBACK_PLAN.md',
    'project-context.md': 'PROJECT_CONTEXT.md',
    'dependency-api-audit.csv': 'DEPENDENCY_API_AUDIT.csv',
    'visual-baselines.csv': 'VISUAL_BASELINES.csv',
    'requirement-coverage.csv': 'REQUIREMENT_COVERAGE.csv',
    'acceptance-gates.csv': 'ACCEPTANCE_GATES.csv',
    'project-brief.md': 'PROJECT_BRIEF.md',
    'feature-spec.md': 'SPEC.md',
    'architecture.md': 'ARCHITECTURE.md',
    'task-board.md': 'TASKS.md',
    'decision-record.md': 'DECISIONS.md',
    'test-report.md': 'TEST_REPORT.md',
    'progress-log.md': 'PROGRESS.md',
    'ui-screen-spec.md': 'UI_SCREEN_SPEC.md',
    'bug-report.md': 'BUG_REPORT.md',
    'agent-handoff.md': 'AGENT_HANDOFF.md',
    'panel-layout-contract.md': 'PANEL_LAYOUT_CONTRACT.md',
    'layout-test-matrix.csv': 'LAYOUT_TEST_MATRIX.csv',
    'capability-registry.csv': 'CAPABILITY_REGISTRY.csv',
    'control-bindings.csv': 'CONTROL_BINDINGS.csv',
    'connection-test-matrix.csv': 'CONNECTION_TEST_MATRIX.csv',
    'integration-decisions.md': 'INTEGRATION_DECISIONS.md',
    'integration-control-contract.md': 'INTEGRATION_CONTROL_CONTRACT.md',
    'model-registry.csv': 'MODEL_REGISTRY.csv',
    'model-test-matrix.csv': 'MODEL_TEST_MATRIX.csv',
    'model-selection-contract.md': 'MODEL_SELECTION_CONTRACT.md',
    'node-type-contract.md': 'NODE_TYPE_CONTRACT.md',
    'node-workflow-checklist.md': 'NODE_WORKFLOW_CHECKLIST.md',
    'node-workflow-sample.json': 'NODE_WORKFLOW_SAMPLE.json',
    'media-node-trio-contract.md': 'MEDIA_NODE_TRIO_CONTRACT.md',
    'batch-run-manifest-example.json': 'BATCH_RUN_MANIFEST_EXAMPLE.json',
}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--project', type=Path, required=True, help='Target project folder')
    ap.add_argument('--force', action='store_true', help='Overwrite existing docs (use with care)')
    args=ap.parse_args()
    root=Path(__file__).resolve().parents[1]
    dest=args.project.resolve()/'docs'
    dest.mkdir(parents=True,exist_ok=True)
    made=skipped=0
    for srcname, targetname in TEMPLATES.items():
        src=root/'assets'/'templates'/srcname
        target=dest/targetname
        if target.exists() and not args.force:
            print('SKIP ',target)
            skipped+=1
            continue
        shutil.copyfile(src,target)
        print('CREATED',target)
        made+=1
    print(f'Done: created={made}, skipped={skipped}')

if __name__=='__main__':
    main()

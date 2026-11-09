# Build, Rollback and Release

## Build gate
Verify clean checkout; lock dependencies; reproducible command; real build artifact and its hash; post-build smoke check on target platform; known issues documented. Never claim release from source-only changes.

## Rollback contract
Record last known-good commit/tag, data backup/migration policy, rollback command or procedure, what happens to files created after upgrade, and user-facing downtime implications. For schema changes test downgrade/restore separately; rollback may be impossible without a backup.

## Delivery
Provide version, artifact path, target device, setup steps in Vietnamese, tests actually run, explicit NOT_RUN tests, evidence bundle, source changes and recovery instructions. Get owner confirmation before production deployment or irreversible actions.

Use `ROLLBACK_PLAN.md`, `RELEASE_SMOKE_CHECKLIST.md` and `PERFORMANCE_BUDGET.csv` as project artifacts.

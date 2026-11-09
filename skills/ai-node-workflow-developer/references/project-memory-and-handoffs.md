# Project Memory and Agent Handoff

## Durable project state
Maintain `PROJECT_CONTEXT.md` as durable state in repo, not chat-only memory. Include: goal, user-approved UI baseline, exact versions, open questions, decisions/why, dependency availability, integration limitations, known bugs, current branch and commit, last verified commands, next task and do-not-change constraints.

## Session start
- Inspect repo status, branch, README, context, decisions, change requests and test report.
- Do not assume another agent's planned task has been implemented or tested. Recheck recorded evidence as needed.
- Identify concurrent edits; avoid two agents changing the same file simultaneously.

## Before handoff
- State exact files changed, test command and outcome, evidence paths, blockers, impact on approved UX, rollback strategy.
- Update task states and accepted changes in project files.
- Give the receiving agent one narrow task and explicit exit criteria; preserve stable IDs.
- If state is stale or inconsistent, say so and stop hazardous actions pending clarification.

Never log secrets, personal API tokens or provider credentials in context, commit history, screen recordings or reports.

---
name: eng_migration_safety
description: "Plan schema, data, config, or API migrations with rollout steps, compatibility, and rollback in mind."
user-invocable: true
---

## Purpose
- Plan schema, data, config, or API migrations with rollout steps, compatibility, and rollback in mind.

## Use when
- Use when a change affects stored data, external contracts, config formats, or deployment order.

## Avoid when
- Do not treat a migration as a normal code-only change.

## Inputs to gather

- Current state: what exists now (schema, config, data, code).
- Target state: what the end state should look like.
- Migration steps: the sequence of changes to get from current to target.
- Rollback plan: how to undo each step if something fails?
- Data volume: how much data needs migrating? Estimated duration?
- Dependency map: what else depends on the thing being migrated?

## Operating rules
- Backward compatibility matters unless proven unnecessary.
- Separate migration mechanics from product logic where possible.
- A safe migration has an explicit rollback or containment story.

- Read the code and the error before proposing a fix. Diagnose first, treat second.
- Prefer the minimal change that solves the problem. Every line added is a line that can break.
- Test the fix, test the surrounding area, test the edge cases. A fix that works for the happy path only is not a fix.
- Document why, not just what. Future engineers need to understand the reasoning, not just see the change.
- If the fix takes longer than 30 minutes, stop and reconsider the approach. Complex fixes usually indicate the wrong diagnosis.
## Claude Code tool pattern
- Use `Bash` to run diagnostic commands, read logs, and check system state.
- Use `Read` to inspect source files, configs, and error output directly.
- Use `Edit` for targeted code changes. Prefer `eng_minimal_patch` scope discipline.
- After changes, use `eng_test_strategy` to verify the fix works and nothing else broke.

## Expanded workflow
1. Map the affected data or contract surface.
2. Design rollout, compatibility, and rollback steps.
3. Identify verification points before and after the change.
4. Recommend the safest implementation sequence.
## Output contract
- Migration surface
- Rollout plan
- Compatibility notes
- Rollback plan
- Verification checks
- Implementation note, review note, or fix plan tied to specific files and checks.
- Verification evidence, remaining risks, and rollback or next-step notes when relevant.

## Failure modes to avoid

- No rollback plan — forward-only migrations are acceptable only for trivial changes.
- Big bang migrations — changing everything at once maximizes blast radius.
- Not testing with production-scale data — migrations that work on 100 rows can fail on 10M.
- Ignoring data integrity during migration — partial migrations create inconsistent state.
- No feature flags — shipping the migration and the code change together eliminates the safety net.

## Handoff cues

- Migration plan: steps, rollback for each step, verification checks.
- Data integrity validation queries.
- Feature flag configuration.
- Timeline estimate and monitoring plan.
- Escalation path if migration fails partway.

## Example invocation
- Slash: `/eng_migration_safety <task>`
- Natural language: "Use migration Safety to plan schema, data, config, or api migrations with rollout steps, compatibility, and rollback in mind."
- Example: "Use this before editing code so we touch the minimum safe surface."
- Example: "Review the change and tell me what could break, not just what looks nice."
- Often paired with: `eng_repo_onboarding`, `eng_minimal_patch`, `eng_test_strategy`

## Quality bar
- A migration plan is good when it reduces the chance of irreversible surprises.
- The fix is the smallest change that resolves the issue without introducing new problems.
- Root cause is identified and documented, not just the symptom.
- Tests cover the fix, the regression, and at least one edge case.
- The change is reviewable in under 10 minutes.
## Related workflows
- Debug chain: `eng_bug_triage` → `eng_debug_systematically` → `eng_minimal_patch` → `eng_test_strategy`
- Release safety: `eng_release_readiness` → `eng_code_review_pass` → `eng_feature_flag_rollout`

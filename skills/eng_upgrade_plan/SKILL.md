---
name: eng_upgrade_plan
description: "Plan a dependency or platform upgrade with compatibility checks, rollout steps, and rollback paths."
user-invocable: true
metadata: {"openclaw":{"emoji":"\u2b06\ufe0f"}}
---

## Purpose
- Plan a dependency or platform upgrade with compatibility checks, rollout steps, and rollback paths.

## Use when
- Use before framework, SDK, runtime, or major dependency upgrades.

## Avoid when
- Do not use for tiny patch bumps with no meaningful change surface.

## Inputs to gather
- Current version: what's running now and what needs upgrading?
- Target version: what version are we upgrading to and what changed between versions?
- Breaking changes: any API, behavior, or config changes in the upgrade path?
- Downstream dependencies: what depends on the thing being upgraded?
- Rollback plan: can we revert if the upgrade causes issues?

## Operating rules
- Follow the recommended migration path. Skip versions only if the changelog explicitly says it's safe.
- Upgrade one major dependency at a time. Multiple simultaneous upgrades make root cause isolation impossible.
- Test at production scale on staging before touching production.
- Every upgrade step needs a rollback plan.
- Read the migration guide. It exists because the upgrade path isn't obvious.

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
1. Read the release notes and migration guide for the target version.
2. Identify breaking changes and their required code changes.
3. Test the upgrade on staging with production-scale data.
4. Document the rollback plan for each step.
5. Upgrade one dependency at a time, verifying after each.
6. Run the full test suite after each upgrade.
7. Deploy to production with monitoring.
8. Verify production health post-upgrade.

## Output contract
- Implementation note, review note, or fix plan tied to specific files and checks.
- Verification evidence, remaining risks, and rollback or next-step notes when relevant.

## Failure modes to avoid
- Skipping minor versions â€” jumping from v2 to v5 often breaks in ways the changelog doesn't predict.
- Not reading the migration guide â€” every major upgrade has one, and it exists because the path isn't obvious.
- Upgrading in production without a staging test â€” the first place you discover the break should not be production.
- No rollback plan â€” if v5 doesn't work, you need a way back to v2.
- Upgrading multiple dependencies simultaneously â€” when something breaks, you can't isolate the cause.

## Handoff cues
- Upgrade plan: current version â†’ target version, step by step.
- Breaking changes and their mitigations.
- Staging validation results.
- Rollback plan.
- Post-upgrade verification checklist.

## Example invocation
- Slash: `/eng_upgrade_plan <task>`
- Natural language: "Use engineering Upgrade Plan to plan a dependency or platform upgrade with compatibility checks, rollout steps, and rollback paths."
- Example: "Use this before editing code so we touch the minimum safe surface."
- Example: "Review the change and tell me what could break, not just what looks nice."
- Often paired with: `eng_repo_onboarding`, `eng_minimal_patch`, `eng_test_strategy`

## Quality bar
## Related workflows
- Debug chain: `eng_bug_triage` â†’ `eng_debug_systematically` â†’ `eng_minimal_patch` â†’ `eng_test_strategy`
- Release safety: `eng_release_readiness` â†’ `eng_code_review_pass` â†’ `eng_feature_flag_rollout`
- The fix is the smallest change that resolves the issue without introducing new problems.
- Root cause is identified and documented, not just the symptom.
- Tests cover the fix, the regression, and at least one edge case.
- The change is reviewable in under 10 minutes.
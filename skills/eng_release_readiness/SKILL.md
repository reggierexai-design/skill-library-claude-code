---
name: eng_release_readiness
description: "Check whether the change is coherent enough to ship, document, and support."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udee0\ufe0f"}}
---

## Purpose
- Check whether the change is coherent enough to ship, document, and support.

## Use when
- Use before release, merge, deployment, or public announcement of a technical change.

## Avoid when
- Do not use as a generic code review substitute during early exploration.

## Inputs to gather

- Release scope: what's included (features, fixes, dependencies)?
- Test results: unit, integration, smoke, and performance test outcomes.
- Known issues: any open bugs shipping with this release?
- Rollback plan: how to revert if the release causes problems?
- Communication plan: who needs to know about this release and when?
- Release notes: what changed from the user's perspective?

## Operating rules
- Release quality is product quality plus operational clarity.
- Look for hidden regressions, missing docs, and support surprises.
- Prefer a short blocker list over a ceremonial checklist.

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
1. Define the exact release unit.
2. Check correctness, documentation, migration, and operational readiness.
3. List ship blockers and soft risks separately.
4. Return a ship or hold recommendation.
## Output contract
- Release unit
- Blockers
- Soft risks
- Ship recommendation
- Implementation note, review note, or fix plan tied to specific files and checks.
- Verification evidence, remaining risks, and rollback or next-step notes when relevant.

## Failure modes to avoid

- Shipping without running the full test suite — skipped tests hide regressions.
- No rollback plan — if the release breaks, you're stuck.
- Forgetting database migrations — code without migrations, or migrations without code.
- No release notes — users and support don't know what changed.
- Releasing on Friday — weekend incidents have reduced response capacity.

## Handoff cues

- Release checklist: all items passed.
- Rollback instructions.
- Release notes for users and stakeholders.
- Known issues documented with workarounds.
- Post-release monitoring plan.

## Example invocation
- Slash: `/eng_release_readiness <task>`
- Natural language: "Use release Readiness to check whether the change is coherent enough to ship, document, and support."
- Example: "Use this before editing code so we touch the minimum safe surface."
- Example: "Review the change and tell me what could break, not just what looks nice."
- Often paired with: `eng_repo_onboarding`, `eng_minimal_patch`, `eng_test_strategy`

## Quality bar
- Ready-to-ship means support can absorb the change too.
- The fix is the smallest change that resolves the issue without introducing new problems.
- Root cause is identified and documented, not just the symptom.
- Tests cover the fix, the regression, and at least one edge case.
- The change is reviewable in under 10 minutes.
## Related workflows
- Debug chain: `eng_bug_triage` → `eng_debug_systematically` → `eng_minimal_patch` → `eng_test_strategy`
- Release safety: `eng_release_readiness` → `eng_code_review_pass` → `eng_feature_flag_rollout`

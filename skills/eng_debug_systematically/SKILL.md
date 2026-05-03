---
name: eng_debug_systematically
description: "Debug in ordered phases: reproduce, isolate, explain, patch, and verify."
user-invocable: true
---

## Purpose
- Debug in ordered phases: reproduce, isolate, explain, patch, and verify.

## Use when
- Use when a bug is real but the cause is not yet proven.

## Avoid when
- Do not use as a cover for random patch attempts.

## Inputs to gather
- The symptom: what's going wrong, when, and under what conditions.
- Recent changes: deployments, config changes, dependency updates.
- System boundaries: which components, services, or layers are involved.
- Available observability: logs, metrics, traces, alerts.
- Reproduction info: consistent, intermittent, or environment-specific?

## Operating rules
- No fix without a real cause story.
- Change one thing at a time when isolating.
- Prefer instrumentation and evidence over intuition alone.

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
1. Reproduce the issue clearly.
2. Isolate the failing boundary or condition.
3. Explain the root cause in concrete terms.
4. Apply the minimal patch and verify the outcome.
## Output contract
- Reproduction
- Root cause
- Patch summary
- Verification
- Implementation note, review note, or fix plan tied to specific files and checks.
- Verification evidence, remaining risks, and rollback or next-step notes when relevant.

## Failure modes to avoid
- Random hypothesis testing without narrowing the surface area first.
- Changing multiple things at once — you learn nothing from shotgun debugging.
- Ignoring the logs and traces in favor of 'it should work' reasoning.
- Declaring victory after the symptom disappears without confirming root cause.
- Debugging in production without a rollback plan.

## Handoff cues
- Root cause identified and confirmed.
- The specific fix applied and why it addresses the root cause.
- Any additional risks or edge cases discovered during debugging.
- Regression test added or planned.

## Example invocation
- Slash: `/eng_debug_systematically <task>`
- Natural language: "Use debug Systematically to debug in ordered phases: reproduce, isolate, explain, patch, and verify."
- Example: "Use this before editing code so we touch the minimum safe surface."
- Example: "Review the change and tell me what could break, not just what looks nice."
- Often paired with: `eng_repo_onboarding`, `eng_minimal_patch`, `eng_test_strategy`

## Quality bar

- The bug is narrowed to a specific component or code path before any fix is attempted.
- Each hypothesis is tested independently — no simultaneous changes.
- The fix is the minimum change that resolves the root cause, not a workaround for the symptom.
- A regression test is added or identified that would catch this bug if it recurs.
- The fix is the smallest change that resolves the issue without introducing new problems.
- Root cause is identified and documented, not just the symptom.
- Tests cover the fix, the regression, and at least one edge case.
- The change is reviewable in under 10 minutes.
## Related workflows
- Debug chain: `eng_bug_triage` → `eng_debug_systematically` → `eng_minimal_patch` → `eng_test_strategy`
- Release safety: `eng_release_readiness` → `eng_code_review_pass` → `eng_feature_flag_rollout`

---
name: eng_ci_failure_triage
description: "Turn a failing CI run into a narrowed cause, likely fix path, and safe next step."
user-invocable: true
---

## Purpose
- Turn a failing CI run into a narrowed cause, likely fix path, and safe next step.

## Use when
- Use when tests, builds, lint, or deploy checks fail in CI and the cause is not yet pinned down.

## Avoid when
- Do not paper over flaky or failing checks by disabling them without evidence.

## Inputs to gather

- CI pipeline output: which stage failed, error messages, logs.
- Recent commits: what changed since the last green build?
- Flaky test history: has this failure pattern appeared before?
- Branch and environment: which branch, which CI runner, any config differences?

## Operating rules
- Classify the failure before touching code.
- Separate deterministic breakage from environmental flakiness.
- Keep the fix path minimal and verifiable.

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
1. Classify the failing stage and signal.
2. Narrow the failure to code, config, dependency, or environment.
3. Propose and apply the smallest plausible fix path.
4. Verify the restored check and adjacent risk areas.
## Output contract
- Failure summary
- Likely cause
- Fix path
- Verification plan
- Implementation note, review note, or fix plan tied to specific files and checks.
- Verification evidence, remaining risks, and rollback or next-step notes when relevant.

## Failure modes to avoid

- Re-running CI without investigating — flaky tests hide real failures.
- Assuming the failure is flaky without checking the failure history.
- Ignoring environment-specific failures (OS, dependency version, timing).
- Fixing symptoms in CI config instead of the underlying test or code issue.
- No documentation of flaky tests — same failures repeat without tracking.

## Handoff cues

- Failure classification: real bug, flaky test, or environment issue.
- Root cause and the specific fix applied.
- Any new flaky tests added to the tracking list.
- Verification that the pipeline is green post-fix.

## Example invocation
- Slash: `/eng_ci_failure_triage <task>`
- Natural language: "Use cI Failure Triage to turn a failing ci run into a narrowed cause, likely fix path, and safe next step."
- Example: "Use this before editing code so we touch the minimum safe surface."
- Example: "Review the change and tell me what could break, not just what looks nice."
- Often paired with: `eng_repo_onboarding`, `eng_minimal_patch`, `eng_test_strategy`

## Quality bar
- A CI triage pass is good when it reduces noise fast and avoids speculative churn.
- The fix is the smallest change that resolves the issue without introducing new problems.
- Root cause is identified and documented, not just the symptom.
- Tests cover the fix, the regression, and at least one edge case.
- The change is reviewable in under 10 minutes.
## Related workflows
- Debug chain: `eng_bug_triage` → `eng_debug_systematically` → `eng_minimal_patch` → `eng_test_strategy`
- Release safety: `eng_release_readiness` → `eng_code_review_pass` → `eng_feature_flag_rollout`

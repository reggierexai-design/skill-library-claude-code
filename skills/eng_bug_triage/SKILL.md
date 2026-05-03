---
name: eng_bug_triage
description: "Turn a vague bug report into a reproducible problem statement, likely surface area, and next action."
user-invocable: true
---

## Purpose
- Turn a vague bug report into a reproducible problem statement, likely surface area, and next action.

## Use when
- Use when a defect is reported but the cause, scope, or reproduction path is unclear.

## Avoid when
- Do not use when the root cause is already known and the task is just to patch it.

## Inputs to gather

- Bug report: what was expected vs what happened.
- Reproduction steps: can the bug be reliably reproduced?
- Environment: OS, browser, version, config, and recent changes.
- Impact scope: how many users affected? Severity of the impact.
- Recent deployments: what changed around when the bug appeared?

## Operating rules
- Clarify impact, severity, and reproducibility before patching.
- Separate symptom from root cause.
- Reduce the bug to the smallest stable repro.

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
1. Define the expected behavior and the observed behavior.
2. Establish reproduction steps and scope.
3. Locate the most likely surface area.
4. Choose patch, deeper debugging, or containment.
## Output contract
- Bug statement
- Reproduction status
- Likely surface area
- Recommended next action
- Implementation note, review note, or fix plan tied to specific files and checks.
- Verification evidence, remaining risks, and rollback or next-step notes when relevant.

## Failure modes to avoid

- Jumping to fix before reproducing — unreproducible fixes waste time.
- Treating symptoms as root causes — the visible error is often downstream.
- Ignoring intermittent bugs — flaky tests and race conditions are real bugs.
- Triage paralysis — spending more time classifying than fixing.
- No severity prioritization — all bugs treated equally means critical ones wait.

## Handoff cues

- Bug statement: expected vs observed behavior, reproduction steps, root cause hypothesis.
- Severity and scope assessment.
- Recommended next action and who should own it.
- Any workarounds identified for affected users.

## Example invocation
- Slash: `/eng_bug_triage <task>`
- Natural language: "Use bug Triage to turn a vague bug report into a reproducible problem statement, likely surface area, and next action."
- Example: "Use this before editing code so we touch the minimum safe surface."
- Example: "Review the change and tell me what could break, not just what looks nice."
- Often paired with: `eng_repo_onboarding`, `eng_minimal_patch`, `eng_test_strategy`

## Quality bar
- Good triage makes the fix smaller and more reliable.
- The fix is the smallest change that resolves the issue without introducing new problems.
- Root cause is identified and documented, not just the symptom.
- Tests cover the fix, the regression, and at least one edge case.
- The change is reviewable in under 10 minutes.
## Related workflows
- Debug chain: `eng_bug_triage` → `eng_debug_systematically` → `eng_minimal_patch` → `eng_test_strategy`
- Release safety: `eng_release_readiness` → `eng_code_review_pass` → `eng_feature_flag_rollout`

---
name: eng_code_review_pass
description: "Review a change for correctness, regressions, maintainability, and deployment safety before merge."
user-invocable: true
---

## Purpose
- Review a change for correctness, regressions, maintainability, and deployment safety before merge.

## Use when
- Use before merging or shipping a meaningful code change.

## Avoid when
- Do not turn review into style nitpicks that ignore real risk.

## Inputs to gather

- The diff: what changed and why (PR description, linked issue).
- Test coverage: are the changes tested? What scenarios are covered?
- Blast radius: what else depends on the changed code?
- Coding standards: project conventions, linting rules, style guide.
- Security and performance considerations for the changed area.

## Operating rules
- Review the intent, not just the diff.
- Focus first on correctness, regressions, and operational risk.
- Call out missing tests, docs, or migration notes when they matter.

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
1. Understand the intended behavior change.
2. Review the diff in the context of the system.
3. Identify correctness, safety, and maintainability concerns.
4. Recommend the smallest set of fixes before merge.
## Output contract
- Intent summary
- Major risks
- Minor issues
- Merge recommendation
- Implementation note, review note, or fix plan tied to specific files and checks.
- Verification evidence, remaining risks, and rollback or next-step notes when relevant.

## Failure modes to avoid

- Rubber-stamping without reading the diff — approve is not a formality.
- Nitpicking style while missing logic bugs — style is linting's job; logic is the reviewer's job.
- Ignoring test coverage — untested changes ship bugs.
- Reviewing too late — the longer the delay, the more context the author loses.
- Scope creep in review — requesting changes beyond the PR's intent.

## Handoff cues

- Review summary: approved, changes requested, or blocked.
- List specific concerns that must be addressed before merge.
- Note any follow-up issues discovered that are out of scope for this PR.

## Example invocation
- Slash: `/eng_code_review_pass <task>`
- Natural language: "Use code Review Pass to review a change for correctness, regressions, maintainability, and deployment safety before merge."
- Example: "Use this before editing code so we touch the minimum safe surface."
- Example: "Review the change and tell me what could break, not just what looks nice."
- Often paired with: `eng_repo_onboarding`, `eng_minimal_patch`, `eng_test_strategy`

## Quality bar
- A strong review catches real problems early without flooding the team with low-value comments.
- The fix is the smallest change that resolves the issue without introducing new problems.
- Root cause is identified and documented, not just the symptom.
- Tests cover the fix, the regression, and at least one edge case.
- The change is reviewable in under 10 minutes.
## Related workflows
- Debug chain: `eng_bug_triage` → `eng_debug_systematically` → `eng_minimal_patch` → `eng_test_strategy`
- Release safety: `eng_release_readiness` → `eng_code_review_pass` → `eng_feature_flag_rollout`

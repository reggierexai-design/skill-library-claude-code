---
name: eng_minimal_patch
description: "Fix the problem with the smallest clean diff that preserves readability and future changeability."
user-invocable: true
---

## Purpose
- Fix the problem with the smallest clean diff that preserves readability and future changeability.

## Use when
- Use when the task is to correct behavior without broad redesign.

## Avoid when
- Do not use when the code structure itself is the main problem and must change first.

## Inputs to gather

- The bug or vulnerability: what's broken and what's the root cause.
- Current code: the specific files and functions involved.
- Blast radius: what else depends on the code being changed?
- Test coverage: existing tests that cover the affected area.
- Urgency: is this a hotfix, a scheduled fix, or a backlog item?

## Operating rules
- Patch the cause, not only the visible symptom.
- Keep unrelated cleanup out of the diff.
- Respect local patterns unless they are the defect.

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
1. Identify the smallest safe edit surface.
2. Implement the patch with clean local naming and structure.
3. Review the diff for accidental scope creep.
4. Verify the behavior and adjacent cases.
## Output contract
- Cause addressed
- Patch summary
- Diff scope
- Verification note
- Implementation note, review note, or fix plan tied to specific files and checks.
- Verification evidence, remaining risks, and rollback or next-step notes when relevant.

## Failure modes to avoid

- Over-fixing — refactoring surrounding code while patching the bug increases risk.
- Patching the symptom instead of the root cause — the bug recurs differently.
- No regression test — the fix isn't verified and the same bug can reappear.
- Ignoring downstream effects — the fix in module A breaks the contract module B depends on.
- Shipping without a rollback plan — even minimal patches can have unexpected effects.

## Handoff cues

- Patch description: what changed and why.
- Regression test added.
- Verification that downstream dependencies still work.
- Rollback plan if the patch causes unexpected issues.

## Example invocation
- Slash: `/eng_minimal_patch <task>`
- Natural language: "Use minimal Patch to fix the problem with the smallest clean diff that preserves readability and future changeability."
- Example: "Use this before editing code so we touch the minimum safe surface."
- Example: "Review the change and tell me what could break, not just what looks nice."
- Often paired with: `eng_repo_onboarding`, `eng_test_strategy`

## Quality bar
- A minimal patch should feel inevitable when reviewed.
- The fix is the smallest change that resolves the issue without introducing new problems.
- Root cause is identified and documented, not just the symptom.
- Tests cover the fix, the regression, and at least one edge case.
- The change is reviewable in under 10 minutes.
## Related workflows
- Debug chain: `eng_bug_triage` → `eng_debug_systematically` → `eng_minimal_patch` → `eng_test_strategy`
- Release safety: `eng_release_readiness` → `eng_code_review_pass` → `eng_feature_flag_rollout`

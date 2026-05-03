---
name: eng_docs_for_change
description: "Write or update technical docs, migration notes, and operator guidance for a code change."
user-invocable: true
---

## Purpose
- Write or update technical docs, migration notes, and operator guidance for a code change.

## Use when
- Use when a code change, release, migration, or new workflow needs technical documentation or operator-facing guidance.

## Avoid when
- Do not use when the code itself is still unstable or the behavior is not yet understood.

## Inputs to gather

- The change: what was modified, added, or deprecated?
- User impact: who is affected and what do they need to do differently?
- Existing docs: what documentation exists that needs updating?
- Breaking changes: any behavior that changes for existing users?
- Migration steps: if behavior changed, how do users migrate?

## Operating rules
- Document user-visible change, operator impact, and failure handling.
- Keep docs aligned with the actual implementation, not the intended one.
- Favor concise, task-oriented docs over narrative filler.

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
1. Define the audience and the exact change being documented.
2. Extract the facts that an operator or developer must know.
3. Draft or update the doc in the smallest logical location.
4. Return the doc change plus any unresolved gaps.
## Output contract
- Audience
- Scope of documented change
- Updated doc sections
- Remaining gaps or assumptions
- Implementation note, review note, or fix plan tied to specific files and checks.
- Verification evidence, remaining risks, and rollback or next-step notes when relevant.

## Failure modes to avoid

- Documenting the implementation instead of the user experience — users don't care about internal architecture.
- Skipping docs for 'small' changes — small changes cause the most confusion because nobody expects them.
- No migration guide for breaking changes — users discover breakage in production.
- Stale docs that contradict the new behavior — worse than no docs.
- Forgetting changelog, API docs, and README when they all need updates.

## Handoff cues

- List all docs updated: changelog, README, API docs, guides, inline comments.
- Flag any breaking changes and their migration paths.
- Note any docs that still need updating but are out of scope.

## Example invocation
- Slash: `/eng_docs_for_change <task>`
- Natural language: "Use docs for Change to write or update technical docs, migration notes, and operator guidance for a code change."
- Example: "Use this before editing code so we touch the minimum safe surface."
- Example: "Review the change and tell me what could break, not just what looks nice."
- Often paired with: `eng_repo_onboarding`, `eng_minimal_patch`, `eng_test_strategy`

## Quality bar
- Good documentation reduces repeated human support.
- The fix is the smallest change that resolves the issue without introducing new problems.
- Root cause is identified and documented, not just the symptom.
- Tests cover the fix, the regression, and at least one edge case.
- The change is reviewable in under 10 minutes.
## Related workflows
- Debug chain: `eng_bug_triage` → `eng_debug_systematically` → `eng_minimal_patch` → `eng_test_strategy`
- Release safety: `eng_release_readiness` → `eng_code_review_pass` → `eng_feature_flag_rollout`

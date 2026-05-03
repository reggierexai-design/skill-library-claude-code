---
name: eng_api_review
description: "Review API shape, contracts, error behavior, and change safety before implementation or release."
user-invocable: true
metadata: {"openclaw":{"emoji":"🛠️"}}
---

## Purpose
- Review API shape, contracts, error behavior, and change safety before implementation or release.

## Use when
- Use for endpoint design, SDK changes, request and response contracts, or breaking-change review.

## Avoid when
- Do not use for purely internal code with no meaningful interface boundary.

## Inputs to gather

- API surface: endpoints, methods, parameters, response schemas.
- Breaking change checklist: any removals, renames, type changes, or behavioral shifts.
- Client consumers: who calls this API and what would break?
- Auth and rate limit model: how is access controlled and throttled?
- Existing API docs and changelog.

## Operating rules
- Design for caller clarity, not only server convenience.
- Make error and edge behavior explicit.
- Protect compatibility when real consumers already exist.

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
1. Define the consumer and core use cases.
2. Review the contract for clarity, consistency, and failure behavior.
3. Check compatibility and migration risk.
4. Return changes needed before implementation or release.
## Output contract
- Contract review
- Error and edge analysis
- Compatibility risk
- Recommended revisions
- Implementation note, review note, or fix plan tied to specific files and checks.
- Verification evidence, remaining risks, and rollback or next-step notes when relevant.

## Failure modes to avoid

- Approving breaking changes without version bumps or migration paths.
- Ignoring pagination, filtering, or error contract consistency across endpoints.
- Missing idempotency for write operations that clients might retry.
- No rate limiting or abuse protection on new endpoints.
- Inconsistent error response formats between endpoints.

## Handoff cues

- List all endpoints reviewed with pass/fail per check.
- Flag breaking changes and their migration paths.
- Note any endpoints that need client communication before shipping.

## Example invocation
- Slash: `/eng_api_review <task>`
- Natural language: "Use aPI Review to review api shape, contracts, error behavior, and change safety before implementation or release."
- Example: "Use this before editing code so we touch the minimum safe surface."
- Example: "Review the change and tell me what could break, not just what looks nice."
- Often paired with: `eng_repo_onboarding`, `eng_minimal_patch`, `eng_test_strategy`

## Quality bar
- An API review should save future consumers from ambiguity.
- The fix is the smallest change that resolves the issue without introducing new problems.
- Root cause is identified and documented, not just the symptom.
- Tests cover the fix, the regression, and at least one edge case.
- The change is reviewable in under 10 minutes.
## Related workflows
- Debug chain: `eng_bug_triage` → `eng_debug_systematically` → `eng_minimal_patch` → `eng_test_strategy`
- Release safety: `eng_release_readiness` → `eng_code_review_pass` → `eng_feature_flag_rollout`

---
name: eng_test_strategy
description: "Design the smallest reliable test set that protects the important behavior of the change."
user-invocable: true
---

## Purpose
- Design the smallest reliable test set that protects the important behavior of the change.

## Use when
- Use when adding, updating, or evaluating tests around new work or a bug fix.

## Avoid when
- Do not use to justify massive test suites with weak signal.

## Inputs to gather
- Feature or system under test: what needs testing?
- Risk areas: what's most likely to break? What would be most impactful if it broke?
- Current test coverage: what's already tested and where are the gaps?
- Test environment: what infrastructure is available for testing?
- Time constraints: how much testing is feasible before the deadline?

## Operating rules
- Test the behavior that matters most to users and future maintenance.
- Prefer a balanced mix of fast, focused checks and a small number of integration proofs.
- Do not duplicate the implementation inside the test.

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
1. Define the risks introduced or addressed by the change.
2. Pick the minimum tests that cover those risks.
3. Name what will not be tested and why.
4. Write or recommend the tests in project-native style.
## Output contract
- Risk list
- Recommended test cases
- Chosen test level
- Coverage gaps
- Implementation note, review note, or fix plan tied to specific files and checks.
- Verification evidence, remaining risks, and rollback or next-step notes when relevant.

## Failure modes to avoid
- Testing everything equally — low-risk areas don't need the same depth as high-risk ones.
- Only testing the happy path — errors, edge cases, and failure modes are where bugs hide.
- No integration or end-to-end tests — unit tests pass but the system still breaks.
- Flaky test suites — tests that sometimes fail erode confidence and get ignored.
- Testing implementation details instead of behavior — refactoring breaks tests that shouldn't care.

## Handoff cues
- Test strategy document: risk areas, test types, coverage targets.
- List of critical test cases that must pass before shipping.
- Known test gaps and the plan to close them.
- Flaky test tracking mechanism.

## Example invocation
- Slash: `/eng_test_strategy <task>`
- Natural language: "Use test Strategy to design the smallest reliable test set that protects the important behavior of the change."
- Example: "Use this before editing code so we touch the minimum safe surface."
- Example: "Review the change and tell me what could break, not just what looks nice."
- Often paired with: `eng_repo_onboarding`, `eng_minimal_patch`

## Quality bar

- Test depth is proportional to risk: critical paths get thorough coverage, low-risk areas get smoke tests.
- Happy path AND error paths are tested.
- Integration tests cover service boundaries.
- Flaky tests are tracked and fixed, not tolerated.
- Tests verify behavior, not implementation.
- The fix is the smallest change that resolves the issue without introducing new problems.
- Root cause is identified and documented, not just the symptom.
- Tests cover the fix, the regression, and at least one edge case.
- The change is reviewable in under 10 minutes.
## Related workflows
- Debug chain: `eng_bug_triage` → `eng_debug_systematically` → `eng_minimal_patch` → `eng_test_strategy`
- Release safety: `eng_release_readiness` → `eng_code_review_pass` → `eng_feature_flag_rollout`

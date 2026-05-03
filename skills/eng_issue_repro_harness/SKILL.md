---
name: eng_issue_repro_harness
description: "Build the smallest reproducible harness for a bug so fixes can be tested without guesswork."
user-invocable: true
metadata: {"openclaw":{"emoji":"🛠️"}}
---

## Purpose
- Build the smallest reproducible harness for a bug so fixes can be tested without guesswork.

## Use when
- Use when a bug is intermittent, environment-dependent, or hard to reason about from reports alone.

## Avoid when
- Do not build a giant debug scaffold when a tiny focused repro will do.

## Inputs to gather

- Bug description: expected vs observed behavior, conditions.
- Environment details: platform, version, config, dependencies.
- Frequency: always reproducible, intermittent, or conditional?
- Related test cases: any existing tests that exercise the same area.
- Code area: which module, function, or component is likely involved?

## Operating rules
- A repro should isolate the failure, not mirror the whole product.
- Keep inputs, state, and assertions explicit.
- Once the issue is reproducible, use the harness to verify the fix.

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
1. Define the failure signal precisely.
2. Strip the problem down to the smallest reproducible setup.
3. Confirm the harness reproduces the bug.
4. Use it to verify the patch and decide whether to keep it.
## Output contract
- Failure signal
- Minimal setup
- Repro steps
- Verification use
- Implementation note, review note, or fix plan tied to specific files and checks.
- Verification evidence, remaining risks, and rollback or next-step notes when relevant.

## Failure modes to avoid

- Writing a harness that proves the happy path — you need the failure path.
- Over-engineering the harness — a 10-line test beats a 100-line framework for reproduction.
- Making the harness dependent on specific test data that doesn't represent real conditions.
- No assertion on the actual failure — the test must fail for the right reason.
- Ignoring timing and state dependencies — race conditions need realistic timing.

## Handoff cues

- Reproduction harness with clear setup, execution, and assertion.
- Instructions for running the harness.
- Plan to promote the harness to a permanent regression test post-fix.

## Example invocation
- Slash: `/eng_issue_repro_harness <task>`
- Natural language: "Use issue Repro Harness to build the smallest reproducible harness for a bug so fixes can be tested without guesswork."
- Example: "Use this before editing code so we touch the minimum safe surface."
- Example: "Review the change and tell me what could break, not just what looks nice."
- Often paired with: `eng_repo_onboarding`, `eng_minimal_patch`, `eng_test_strategy`

## Quality bar
- A repro harness is successful when it turns a vague bug into a controlled experiment.
- The fix is the smallest change that resolves the issue without introducing new problems.
- Root cause is identified and documented, not just the symptom.
- Tests cover the fix, the regression, and at least one edge case.
- The change is reviewable in under 10 minutes.
## Related workflows
- Debug chain: `eng_bug_triage` → `eng_debug_systematically` → `eng_minimal_patch` → `eng_test_strategy`
- Release safety: `eng_release_readiness` → `eng_code_review_pass` → `eng_feature_flag_rollout`

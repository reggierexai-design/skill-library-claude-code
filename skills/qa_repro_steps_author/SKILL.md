---
name: qa_repro_steps_author
description: "Write exact reproduction steps for a bug, edge case, or flaky failure without guesswork."
user-invocable: true
---

## Purpose
- Write exact reproduction steps for a bug, edge case, or flaky failure without guesswork.
- This is a **quality specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when engineering needs crisp repro steps or support needs a validated escalation.

## Avoid when
- Do not use when the issue is already reproducible and documented precisely.

## Inputs to gather
- Feature, build, environment matrix, acceptance criteria, and the highest-risk user flows.
- Known regressions, supported platforms, recent changes, and release timing pressure.
- Whether the task needs a test plan, smoke sweep, bug report, or exploratory charter.

## Operating rules
- Steps must be numbered and minimal. Remove steps that don't affect outcome.
- Specify exact values, not approximations.
- Include the starting state and prerequisites.
- Verify with a second person.

- Test the risk, not the coverage. 80% of bugs come from 20% of the code. Focus testing where failures hurt most.
- Distinguish between testing that the feature works and testing that nothing else broke. Both matter.
- Every test case should have an explicit pass/fail criterion. Vague assertions produce vague confidence.
- Automate regression tests. Manual regression testing is slow, error-prone, and demoralizing.
- Test the edges and error paths, not just the happy path. Users will find the error paths even if testers do not.
## Claude Code tool pattern
- Read the intended behavior, recent changes, and bug history before defining tests.
- Prioritize risk and user impact over exhaustive but low-yield test volume.
- Capture defects and checks in a form engineering and release owners can act on quickly.

## Expanded workflow
1. Reproduce the bug from scratch.
2. Note every step required â€” remove any that aren't.
3. Replace vague instructions with specific values.
4. Document starting state and prerequisites.
5. Have someone else verify the steps.
6. Test variations: browsers, data states, accounts.

## Output contract
- Risk-based test artifact with clear pass or fail criteria.
- Coverage gaps, release risk, and the most important next validation step.

## Failure modes to avoid
- Treating test coverage as a substitute for risk thinking.
- Writing bugs with no reproduction clarity, impact framing, or environment details.
- Running a release check that never states what would block the release.

## Handoff cues
- Reproduction steps: numbered, minimal, environment-specific, verified by a second person.
- Environmental requirements documented.
- Variations tested (different browsers, data states).

## Example invocation
- Slash: `/qa_repro_steps_author <task>`
- Natural language: "Use qA Repro Steps Author to write exact reproduction steps for a bug, edge case, or flaky failure without guesswork."
- Example: "Give me the highest-leverage test plan for this change, not a giant generic checklist."
- Example: "Refine this bug or release check so an engineer can act on it immediately."
- Often paired with: `qa_risk_based_testing`, `qa_release_smoke_test`, `eng_release_readiness`

## Quality bar
## Related workflows
- Test planning: `qa_risk_based_testing` â†’ `qa_acceptance_test_plan` â†’ `qa_test_case_matrix`
- Release check: `qa_release_smoke_test` â†’ `qa_regression_sweep` â†’ `eng_release_readiness`
- Test cases cover the highest-risk areas first, not just the easiest to test.
- Pass/fail criteria are explicit and unambiguous.
- Regression tests are automated.
- Edge cases and error paths have explicit test coverage.

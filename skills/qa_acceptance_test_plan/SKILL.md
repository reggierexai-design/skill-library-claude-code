---
name: qa_acceptance_test_plan
description: "Turn requirements into a lean acceptance plan that proves the change works for real users."
user-invocable: true
---

## Purpose
- Turn requirements into a lean acceptance plan that proves the change works for real users.
- This is a **quality specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use before shipping meaningful product, workflow, UI, or API changes.

## Avoid when
- Do not use for microscopic edits where the acceptance path is already obvious.

## Inputs to gather
- Feature, build, environment matrix, acceptance criteria, and the highest-risk user flows.
- Known regressions, supported platforms, recent changes, and release timing pressure.
- Whether the task needs a test plan, smoke sweep, bug report, or exploratory charter.

## Operating rules
- Test against acceptance criteria, not implementation details.
- Prioritize by user impact. Most-used flows get deepest testing.
- Include negative tests. Happy path only misses 40%+ of bugs.
- Each test case independently reproducible.

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
1. Extract acceptance criteria from the feature spec.
2. Map criteria to test scenarios: happy, error, edge cases.
3. Prioritize scenarios by user impact and risk.
4. Write test cases with steps, expected results, pass/fail criteria.
5. Execute high-priority tests first.
6. Report results with traceability: test case -> criterion -> pass/fail.

## Output contract
- Risk-based test artifact with clear pass or fail criteria.
- Coverage gaps, release risk, and the most important next validation step.

## Failure modes to avoid
- Treating test coverage as a substitute for risk thinking.
- Writing bugs with no reproduction clarity, impact framing, or environment details.
- Running a release check that never states what would block the release.

## Handoff cues
- Acceptance test plan: scenarios, expected results, pass/fail criteria, priority.
- Traceability to requirements/user stories.
- Execution schedule and responsible testers.

## Example invocation
- Slash: `/qa_acceptance_test_plan <task>`
- Natural language: "Use qA Acceptance Test Plan to turn requirements into a lean acceptance plan that proves the change works for real users."
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

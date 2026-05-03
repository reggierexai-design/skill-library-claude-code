---
name: qa_test_case_matrix
description: "Build a compact matrix of states, roles, inputs, and environments that must be tested."
user-invocable: true
---

## Purpose
- Build a compact matrix of states, roles, inputs, and environments that must be tested.
- This is a **quality specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a feature varies by role, state, plan, locale, browser, or device.

## Avoid when
- Do not use when a single linear path captures the whole behavior.

## Inputs to gather
- Feature, build, environment matrix, acceptance criteria, and the highest-risk user flows.
- Known regressions, supported platforms, recent changes, and release timing pressure.
- Whether the task needs a test plan, smoke sweep, bug report, or exploratory charter.

## Operating rules
- Matrix maps features to test types. Gaps = untested combinations = risk.
- Not every cell needs same depth. Critical features need all types.
- Coverage does not equal quality. Deep, focused tests beat shallow broad ones.
- Update the matrix when features change.

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
1. List feature areas on one axis, test types on the other.
2. Mark existing coverage for each cell.
3. Identify gaps: cells with no coverage for critical features.
4. Prioritize gap-filling by feature criticality.
5. Write tests for high-priority gaps first.
6. Update the matrix as coverage changes.

## Output contract
- Risk-based test artifact with clear pass or fail criteria.
- Coverage gaps, release risk, and the most important next validation step.

## Failure modes to avoid
- Treating test coverage as a substitute for risk thinking.
- Writing bugs with no reproduction clarity, impact framing, or environment details.
- Running a release check that never states what would block the release.

## Handoff cues
- Test case matrix: feature areas, test types, coverage status, gap analysis.
- Priority ordering for execution.
- Traceability to requirements and risk areas.

## Example invocation
- Slash: `/qa_test_case_matrix <task>`
- Natural language: "Use qA Test Case Matrix to build a compact matrix of states, roles, inputs, and environments that must be tested."
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

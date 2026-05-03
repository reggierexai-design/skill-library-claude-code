---
name: qa_regression_sweep
description: "Define a fast regression sweep around a change so adjacent breakage is caught before release."
user-invocable: true
---

## Purpose
- Define a fast regression sweep around a change so adjacent breakage is caught before release.
- This is a **quality specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use after a fix or change that might affect nearby flows, permissions, data, or UI states.

## Avoid when
- Do not use when no surrounding behavior could plausibly be affected.

## Inputs to gather
- Feature, build, environment matrix, acceptance criteria, and the highest-risk user flows.
- Known regressions, supported platforms, recent changes, and release timing pressure.
- Whether the task needs a test plan, smoke sweep, bug report, or exploratory charter.

## Operating rules
- Focus on what changed AND what's connected. Bugs hide in integration points.
- Risk-prioritize: high-impact deep, low-impact smoke.
- Don't skip regression for 'small changes.'
- Document any skipped areas with risk acceptance.

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
1. Analyze release scope: what changed and what's connected.
2. Map changes to risk areas: high (deep), medium (focused), low (smoke).
3. Execute automated regression suite first.
4. Execute manual regression for gaps and high-risk integrations.
5. Document skipped areas with risk rationale.
6. Report: pass/fail by area, issues found, risk gaps.

## Output contract
- Risk-based test artifact with clear pass or fail criteria.
- Coverage gaps, release risk, and the most important next validation step.

## Failure modes to avoid
- Treating test coverage as a substitute for risk thinking.
- Writing bugs with no reproduction clarity, impact framing, or environment details.
- Running a release check that never states what would block the release.

## Handoff cues
- Regression sweep results: areas tested, issues found, severity, pass/fail by area.
- Risk assessment for any skipped areas.
- Recommended additional testing based on findings.

## Example invocation
- Slash: `/qa_regression_sweep <task>`
- Natural language: "Use qA Regression Sweep to define a fast regression sweep around a change so adjacent breakage is caught before release."
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

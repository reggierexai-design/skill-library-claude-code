---
name: qa_risk_based_testing
description: "Prioritize testing by user impact, change risk, and failure cost instead of equal treatment."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udcc9"}}
---

## Purpose
- Prioritize testing by user impact, change risk, and failure cost instead of equal treatment.
- This is a **quality specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when time is limited and the team must test the most dangerous surfaces first.

## Avoid when
- Do not use when the scope is tiny and full testing is trivial.

## Inputs to gather
- Feature, build, environment matrix, acceptance criteria, and the highest-risk user flows.
- Known regressions, supported platforms, recent changes, and release timing pressure.
- Whether the task needs a test plan, smoke sweep, bug report, or exploratory charter.

## Operating rules
- Test depth proportional to risk. Equal depth = insufficient where it matters.
- Risk = probability x impact.
- Include historical risk â€” buggy areas repeat.
- Document what you're NOT testing and why.

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
1. List all testable areas for the release.
2. Score each area: probability x impact.
3. Add historical risk weight.
4. Allocate test time: high-risk 60%, medium 30%, low 10%.
5. Execute high-risk tests first.
6. Document untested areas with risk acceptance.

## Output contract
- Risk-based test artifact with clear pass or fail criteria.
- Coverage gaps, release risk, and the most important next validation step.

## Failure modes to avoid
- Treating test coverage as a substitute for risk thinking.
- Writing bugs with no reproduction clarity, impact framing, or environment details.
- Running a release check that never states what would block the release.

## Handoff cues
- Risk-based test plan: risk areas, test depth per risk, priority order, time allocation.
- Coverage matrix: what's tested deeply vs sampled vs deferred.
- Justification for any untested areas.

## Example invocation
- Slash: `/qa_risk_based_testing <task>`
- Natural language: "Use qA Risk-Based Testing to prioritize testing by user impact, change risk, and failure cost instead of equal treatment."
- Example: "Give me the highest-leverage test plan for this change, not a giant generic checklist."
- Example: "Refine this bug or release check so an engineer can act on it immediately."
- Often paired with: `qa_release_smoke_test`, `eng_release_readiness`

## Quality bar
## Related workflows
- Test planning: `qa_risk_based_testing` â†’ `qa_acceptance_test_plan` â†’ `qa_test_case_matrix`
- Release check: `qa_release_smoke_test` â†’ `qa_regression_sweep` â†’ `eng_release_readiness`
- Test cases cover the highest-risk areas first, not just the easiest to test.
- Pass/fail criteria are explicit and unambiguous.
- Regression tests are automated.
- Edge cases and error paths have explicit test coverage.
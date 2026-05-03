---
name: qa_bug_report_refine
description: "Turn a messy bug note into a clear report with environment, repro steps, and expected behavior."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udc1e"}}
---

## Purpose
- Turn a messy bug note into a clear report with environment, repro steps, and expected behavior.
- This is a **quality specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a bug report is vague, emotional, incomplete, or hard to reproduce.

## Avoid when
- Do not use when a precise repro already exists and engineering can act immediately.

## Inputs to gather
- Feature, build, environment matrix, acceptance criteria, and the highest-risk user flows.
- Known regressions, supported platforms, recent changes, and release timing pressure.
- Whether the task needs a test plan, smoke sweep, bug report, or exploratory charter.

## Operating rules
- A bug report is communication to a future developer with zero context.
- Title = the problem, not the feature.
- Reproduction steps must be numbered, specific, and minimal.
- Severity = user impact x frequency.
- Include what you tried to save developer time.

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
1. Read the original report and identify what's missing.
2. Reproduce the bug. If you can't, note that explicitly.
3. Minimize the reproduction: fewest steps that trigger the bug.
4. Write refined report: clear title, numbered steps, expected vs actual.
5. Add related context: recent changes, similar bugs.
6. Verify the report is actionable.

## Output contract
- Risk-based test artifact with clear pass or fail criteria.
- Coverage gaps, release risk, and the most important next validation step.

## Failure modes to avoid
- Treating test coverage as a substitute for risk thinking.
- Writing bugs with no reproduction clarity, impact framing, or environment details.
- Running a release check that never states what would block the release.

## Handoff cues
- Refined bug report: clear title, reproduction steps, expected vs actual, environment, severity.
- Minimum information checklist for developers to act on.
- Related bugs or regression patterns noted.

## Example invocation
- Slash: `/qa_bug_report_refine <task>`
- Natural language: "Use qA Bug Report Refine to turn a messy bug note into a clear report with environment, repro steps, and expected behavior."
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
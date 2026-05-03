---
name: qa_ui_state_check
description: "Review UI states so loading, empty, error, success, and permission cases all behave coherently."
user-invocable: true
---

## Purpose
- Review UI states so loading, empty, error, success, and permission cases all behave coherently.
- This is a **quality specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when shipping or reviewing user interfaces with asynchronous or permissioned states.

## Avoid when
- Do not use for backend-only changes with no user-visible state.

## Inputs to gather
- Feature, build, environment matrix, acceptance criteria, and the highest-risk user flows.
- Known regressions, supported platforms, recent changes, and release timing pressure.
- Whether the task needs a test plan, smoke sweep, bug report, or exploratory charter.

## Operating rules
- Check EVERY state, not just happy. Empty, error, loading states hide bugs.
- Verify across device matrix. Chrome Desktop working doesn't mean Safari Mobile works.
- Check transitions between states, not just static states.
- Accessibility is a state check too.

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
1. Inventory all screens and possible states.
2. Create state check matrix: screens x states x devices.
3. Check happy states first, then empty/error/loading.
4. Verify state transitions.
5. Run accessibility checks on each state.
6. Report: pass/fail per cell, issues by severity.

## Output contract
- Risk-based test artifact with clear pass or fail criteria.
- Coverage gaps, release risk, and the most important next validation step.

## Failure modes to avoid
- Treating test coverage as a substitute for risk thinking.
- Writing bugs with no reproduction clarity, impact framing, or environment details.
- Running a release check that never states what would block the release.

## Handoff cues
- UI state check results: states tested, visual issues, functional issues, accessibility findings.
- Priority-ordered fix list.
- Cross-browser/device results summary.

## Example invocation
- Slash: `/qa_ui_state_check <task>`
- Natural language: "Use qA UI State Check to review ui states so loading, empty, error, success, and permission cases all behave coherently."
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

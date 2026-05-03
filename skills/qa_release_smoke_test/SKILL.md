---
name: qa_release_smoke_test
description: "Create a minimal post-build smoke test that catches obvious breakage before wider rollout."
user-invocable: true
---

## Purpose
- Create a minimal post-build smoke test that catches obvious breakage before wider rollout.
- This is a **quality specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use before release, deployment, or demo when a fast confidence check is needed.

## Avoid when
- Do not use as the only testing strategy for high-risk changes.

## Inputs to gather
- Feature, build, environment matrix, acceptance criteria, and the highest-risk user flows.
- Known regressions, supported platforms, recent changes, and release timing pressure.
- Whether the task needs a test plan, smoke sweep, bug report, or exploratory charter.

## Operating rules
- Smoke tests verify the system works, not that it's perfect.
- Every critical user path must be in the smoke test.
- Smoke tests should complete in under 30 minutes.
- Automated > manual for repeated smoke tests.

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
1. Define critical user paths: login, core workflow, payment, export.
2. Execute each path and verify expected outcome.
3. Check infrastructure health: services, error rates, response times.
4. Verify the release version deployed correctly.
5. Report: go/no-go with specific evidence.
6. If no-go, list blockers and recommend rollback or hotfix.

## Output contract
- Risk-based test artifact with clear pass or fail criteria.
- Coverage gaps, release risk, and the most important next validation step.

## Failure modes to avoid
- Treating test coverage as a substitute for risk thinking.
- Writing bugs with no reproduction clarity, impact framing, or environment details.
- Running a release check that never states what would block the release.

## Handoff cues
- Smoke test results: critical paths verified, environment health confirmed, blockers identified.
- Go/no-go recommendation for release.
- Known issues that should ship with workarounds.

## Example invocation
- Slash: `/qa_release_smoke_test <task>`
- Natural language: "Use qA Release Smoke Test to create a minimal post-build smoke test that catches obvious breakage before wider rollout."
- Example: "Give me the highest-leverage test plan for this change, not a giant generic checklist."
- Example: "Refine this bug or release check so an engineer can act on it immediately."
- Often paired with: `qa_risk_based_testing`, `eng_release_readiness`

## Quality bar
## Related workflows
- Test planning: `qa_risk_based_testing` â†’ `qa_acceptance_test_plan` â†’ `qa_test_case_matrix`
- Release check: `qa_release_smoke_test` â†’ `qa_regression_sweep` â†’ `eng_release_readiness`
- Test cases cover the highest-risk areas first, not just the easiest to test.
- Pass/fail criteria are explicit and unambiguous.
- Regression tests are automated.
- Edge cases and error paths have explicit test coverage.

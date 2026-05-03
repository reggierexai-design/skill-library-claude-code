---
name: eng_repo_onboarding
description: "Understand a codebase fast enough to work safely without pretending to know more than you do."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udee0\ufe0f"}}
---

## Purpose
- Understand a codebase fast enough to work safely without pretending to know more than you do.

## Use when
- Use when entering a new repository or a part of the codebase that has not been mapped yet.

## Avoid when
- Do not use after the relevant architecture has already been scouted and documented for the current task.

## Inputs to gather

- Repository URL and main branch.
- Project purpose: what does this codebase do and who uses it?
- Tech stack: language, framework, database, infrastructure.
- Development setup: prerequisites, local dev instructions, test commands.
- Key directories: where is the core logic, tests, config, docs?

## Operating rules
- Seek the execution path, state model, and dependency boundaries first.
- Prefer representative files over large unfocused dumps.
- Explain the repository in terms of how work actually moves through it.

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
1. Map the stack, runtime, and package layout.
2. Find the user-facing entry points and internal boundaries.
3. Identify test, build, and local run paths.
4. Summarize the architecture relevant to the task.
## Output contract
- Stack summary
- Key directories and files
- Execution path
- Safe starting points for changes
- Implementation note, review note, or fix plan tied to specific files and checks.
- Verification evidence, remaining risks, and rollback or next-step notes when relevant.

## Failure modes to avoid

- Diving into code without understanding the project's purpose first.
- Ignoring the README and docs — they exist to save you time.
- Skipping the test suite — you can't safely change code you can't verify.
- Not understanding the deployment pipeline — where does code go after merge?
- Overloading on context — read enough to be productive, not enough to be an expert on day one.

## Handoff cues

- Onboarding summary: purpose, stack, architecture, key areas.
- Local setup verification: all tests passing.
- Any setup issues or documentation gaps discovered.
- Questions or areas that need clarification from the team.

## Example invocation
- Slash: `/eng_repo_onboarding <task>`
- Natural language: "Use repo Onboarding to understand a codebase fast enough to work safely without pretending to know more than you do."
- Example: "Use this before editing code so we touch the minimum safe surface."
- Example: "Review the change and tell me what could break, not just what looks nice."
- Often paired with: `eng_minimal_patch`, `eng_test_strategy`

## Quality bar
- Onboarding is successful when edits can start with confidence and minimal surprise.
- The fix is the smallest change that resolves the issue without introducing new problems.
- Root cause is identified and documented, not just the symptom.
- Tests cover the fix, the regression, and at least one edge case.
- The change is reviewable in under 10 minutes.
## Related workflows
- Debug chain: `eng_bug_triage` → `eng_debug_systematically` → `eng_minimal_patch` → `eng_test_strategy`
- Release safety: `eng_release_readiness` → `eng_code_review_pass` → `eng_feature_flag_rollout`

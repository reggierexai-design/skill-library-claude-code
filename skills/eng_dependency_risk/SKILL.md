---
name: eng_dependency_risk
description: "Evaluate whether a new package, SDK, or external service is worth its complexity and trust cost."
user-invocable: true
---

## Purpose
- Evaluate whether a new package, SDK, or external service is worth its complexity and trust cost.

## Use when
- Use before adding major dependencies or when a build already feels fragile or over-composed.

## Avoid when
- Do not use for routine patch upgrades with low surface area and low risk.

## Inputs to gather
- Dependency list: direct and transitive dependencies with versions.
- Vulnerability database: known CVEs for current versions.
- License inventory: license type for each dependency.
- Maintenance status: last release, commit frequency, open issues, maintainer count.
- Dependency depth: how many levels of transitive dependencies?

## Operating rules
- Every dependency adds operational and security weight.
- Prefer fewer, well-understood pieces over fashionable stacks.
- Measure adoption value against lock-in, maintenance, and risk.

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
1. State the real problem the dependency would solve.
2. Compare dependency, built-in, and lighter alternatives.
3. Assess security, maintenance, and migration risk.
4. Give a go, no-go, or defer recommendation.
## Output contract
- Problem statement
- Options compared
- Risk assessment
- Recommendation
- Implementation note, review note, or fix plan tied to specific files and checks.
- Verification evidence, remaining risks, and rollback or next-step notes when relevant.

## Failure modes to avoid
- Ignoring transitive dependencies — the vulnerability is often two levels deep.
- Upgrading without testing — major version bumps can break APIs silently.
- No license audit — GPL dependencies in proprietary code are legal time bombs.
- Assuming popular = maintained — popular packages can be abandoned.
- Pinning without a refresh strategy — locked dependencies accumulate CVEs over time.

## Handoff cues
- Dependency risk report: CVEs, license issues, unmaintained packages.
- Recommended upgrades with version targets.
- Flag any dependencies that need replacement (not just upgrade).
- Note the dependency refresh cadence agreed on.

## Example invocation
- Slash: `/eng_dependency_risk <task>`
- Natural language: "Use dependency Risk to evaluate whether a new package, sdk, or external service is worth its complexity and trust cost."
- Example: "Use this before editing code so we touch the minimum safe surface."
- Example: "Review the change and tell me what could break, not just what looks nice."
- Often paired with: `eng_repo_onboarding`, `eng_minimal_patch`, `eng_test_strategy`

## Quality bar

- All direct and transitive dependencies inventoried with versions.
- Known CVEs flagged with severity and remediation path.
- License audit complete — no legal conflicts.
- Unmaintained dependencies flagged for replacement.
- Dependency refresh cadence defined.
- The fix is the smallest change that resolves the issue without introducing new problems.
- Root cause is identified and documented, not just the symptom.
- Tests cover the fix, the regression, and at least one edge case.
- The change is reviewable in under 10 minutes.
## Related workflows
- Debug chain: `eng_bug_triage` → `eng_debug_systematically` → `eng_minimal_patch` → `eng_test_strategy`
- Release safety: `eng_release_readiness` → `eng_code_review_pass` → `eng_feature_flag_rollout`

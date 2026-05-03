---
name: eng_data_model_review
description: "Review schemas, entities, and state shape for consistency, change safety, and future query patterns."
user-invocable: true
metadata: {"openclaw":{"emoji":"🛠️"}}
---

## Purpose
- Review schemas, entities, and state shape for consistency, change safety, and future query patterns.

## Use when
- Use before changing database schemas, APIs, event shapes, or important in-memory state models.

## Avoid when
- Do not optimize for hypothetical future complexity with no evidence.

## Inputs to gather

- Schema or model definition: tables, fields, types, constraints, relationships.
- Access patterns: how is this data read and written? Query volume?
- Migration plan: how do we get from current schema to proposed?
- Data volume estimates: current and projected scale.
- Regulatory requirements: PII, retention, compliance constraints.

## Operating rules
- Model names should match the business meaning.
- Prefer structures that make valid states easier and invalid states harder.
- Consider migration, query, and lifecycle costs together.

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
1. Map the current model and its pressures.
2. Identify ambiguity, duplication, or awkward lifecycle states.
3. Evaluate candidate changes against real access patterns.
4. Recommend the cleanest safe model evolution.
## Output contract
- Current model risks
- Candidate changes
- Tradeoffs
- Recommended direction
- Implementation note, review note, or fix plan tied to specific files and checks.
- Verification evidence, remaining risks, and rollback or next-step notes when relevant.

## Failure modes to avoid

- Designing for today's scale only — models that can't evolve require painful migrations later.
- Missing indexes for primary query patterns — correct schema, terrible performance.
- No migration strategy — schema changes without a migration plan are deployment blockers.
- Ignoring soft delete vs hard delete implications for related data.
- Over-normalizing for theoretical purity at the cost of query simplicity.

## Handoff cues

- Schema review: approved with modifications or blocked.
- List required index additions.
- Flag migration steps and rollback plan.
- Note any regulatory considerations (PII fields, retention).

## Example invocation
- Slash: `/eng_data_model_review <task>`
- Natural language: "Use data Model Review to review schemas, entities, and state shape for consistency, change safety, and future query patterns."
- Example: "Use this before editing code so we touch the minimum safe surface."
- Example: "Review the change and tell me what could break, not just what looks nice."
- Often paired with: `eng_repo_onboarding`, `eng_minimal_patch`, `eng_test_strategy`

## Quality bar
- A good model review makes future changes easier instead of hiding complexity under new names.
- The fix is the smallest change that resolves the issue without introducing new problems.
- Root cause is identified and documented, not just the symptom.
- Tests cover the fix, the regression, and at least one edge case.
- The change is reviewable in under 10 minutes.
## Related workflows
- Debug chain: `eng_bug_triage` → `eng_debug_systematically` → `eng_minimal_patch` → `eng_test_strategy`
- Release safety: `eng_release_readiness` → `eng_code_review_pass` → `eng_feature_flag_rollout`

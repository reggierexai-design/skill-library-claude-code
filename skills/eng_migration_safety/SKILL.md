---
name: eng_migration_safety
description: "Plan schema, data, config, or API migrations with rollout steps, compatibility, and rollback in mind."
user-invocable: true
disable-model-invocation: false
---


# Migration Safety

## Purpose
- Plan schema, data, config, or API migrations with rollout steps, compatibility, and rollback in mind.
- This is an **engineering specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use when a change affects stored data, external contracts, config formats, or deployment order.
- The main bottleneck is best solved through engineering work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not treat a migration as a normal code-only change.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Target system, repo area, environment, and the concrete failure, change, or performance goal.
- Relevant files, logs, tests, stack traces, commands, and deployment constraints.
- Definition of done: fix, refactor, review, migration plan, or release-safety decision.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- Backward compatibility matters unless proven unnecessary.
- Separate migration mechanics from product logic where possible.
- A safe migration has an explicit rollback or containment story.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Scout the repo before editing; read the nearest implementation, tests, and docs that define current behavior.
- Use minimal diffs, bounded commands, and targeted verification instead of broad speculative changes.
- When code is touched, explain what changed, why it is safe, and how it was verified.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Map the affected data or contract surface.
2. Design rollout, compatibility, and rollback steps.
3. Identify verification points before and after the change.
4. Recommend the safest implementation sequence.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

## Output contract
- Migration surface
- Rollout plan
- Compatibility notes
- Rollback plan
- Verification checks
- Implementation note, review note, or fix plan tied to specific files and checks.
- Verification evidence, remaining risks, and rollback or next-step notes when relevant.

## Failure modes to avoid
- Patching symptoms without proving the cause or expected behavior.
- Bundling unrelated cleanup into a debugging or release task.
- Stopping after the code compiles without checking the user-visible outcome.
- Declaring success before the output is usable by the next operator, owner, or decision-maker.

## Handoff cues
- State current status, remaining blockers, and the smallest next move.
- Name the files, pages, systems, or source material that another operator should read first.
- Flag approvals, missing evidence, or live-system access that still require a human decision.

## Example invocation
- Slash: `/eng_migration_safety <task>`
- Natural language: "Use migration Safety to plan schema, data, config, or api migrations with rollout steps, compatibility, and rollback in mind."
- Example: "Use this before editing code so we touch the minimum safe surface."
- Example: "Review the change and tell me what could break, not just what looks nice."
- Often paired with: `eng_repo_onboarding`, `eng_minimal_patch`, `eng_test_strategy`

## Quality bar
- A migration plan is good when it reduces the chance of irreversible surprises.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.

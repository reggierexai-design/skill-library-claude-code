---
name: eng_debug_systematically
description: "Debug in ordered phases: reproduce, isolate, explain, patch, and verify."
user-invocable: true
disable-model-invocation: false
---


# Debug Systematically

## Purpose
- Debug in ordered phases: reproduce, isolate, explain, patch, and verify.
- This is an **engineering specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use when a bug is real but the cause is not yet proven.
- The main bottleneck is best solved through engineering work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not use as a cover for random patch attempts.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Target system, repo area, environment, and the concrete failure, change, or performance goal.
- Relevant files, logs, tests, stack traces, commands, and deployment constraints.
- Definition of done: fix, refactor, review, migration plan, or release-safety decision.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- No fix without a real cause story.
- Change one thing at a time when isolating.
- Prefer instrumentation and evidence over intuition alone.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Scout the repo before editing; read the nearest implementation, tests, and docs that define current behavior.
- Use minimal diffs, bounded commands, and targeted verification instead of broad speculative changes.
- When code is touched, explain what changed, why it is safe, and how it was verified.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Reproduce the issue clearly.
2. Isolate the failing boundary or condition.
3. Explain the root cause in concrete terms.
4. Apply the minimal patch and verify the outcome.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

## Output contract
- Reproduction
- Root cause
- Patch summary
- Verification
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
- Slash: `/eng_debug_systematically <task>`
- Natural language: "Use debug Systematically to debug in ordered phases: reproduce, isolate, explain, patch, and verify."
- Example: "Use this before editing code so we touch the minimum safe surface."
- Example: "Review the change and tell me what could break, not just what looks nice."
- Often paired with: `eng_repo_onboarding`, `eng_minimal_patch`, `eng_test_strategy`

## Quality bar
- A debugging pass fails when it ends in a guess.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.

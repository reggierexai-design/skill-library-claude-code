---
name: eng_docs_for_change
description: "Write or update technical docs, migration notes, and operator guidance for a code change."
user-invocable: true
disable-model-invocation: true
---


# Docs for Change

## Purpose
- Write or update technical docs, migration notes, and operator guidance for a code change.
- This is an **engineering specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use when a code change, release, migration, or new workflow needs technical documentation or operator-facing guidance.
- The main bottleneck is best solved through engineering work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not use when the code itself is still unstable or the behavior is not yet understood.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Target system, repo area, environment, and the concrete failure, change, or performance goal.
- Relevant files, logs, tests, stack traces, commands, and deployment constraints.
- Definition of done: fix, refactor, review, migration plan, or release-safety decision.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- Document user-visible change, operator impact, and failure handling.
- Keep docs aligned with the actual implementation, not the intended one.
- Favor concise, task-oriented docs over narrative filler.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Scout the repo before editing; read the nearest implementation, tests, and docs that define current behavior.
- Use minimal diffs, bounded commands, and targeted verification instead of broad speculative changes.
- When code is touched, explain what changed, why it is safe, and how it was verified.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Define the audience and the exact change being documented.
2. Extract the facts that an operator or developer must know.
3. Draft or update the doc in the smallest logical location.
4. Return the doc change plus any unresolved gaps.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

## Output contract
- Audience
- Scope of documented change
- Updated doc sections
- Remaining gaps or assumptions
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
- Slash: `/eng_docs_for_change <task>`
- Natural language: "Use docs for Change to write or update technical docs, migration notes, and operator guidance for a code change."
- Example: "Use this before editing code so we touch the minimum safe surface."
- Example: "Review the change and tell me what could break, not just what looks nice."
- Often paired with: `eng_repo_onboarding`, `eng_minimal_patch`, `eng_test_strategy`

## Quality bar
- Good documentation reduces repeated human support.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.

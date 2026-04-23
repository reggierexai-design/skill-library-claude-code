---
name: ai_tool_schema_review
description: "Review tool names, arguments, and failure contracts so agents can use them reliably."
user-invocable: true
disable-model-invocation: true
---


# AI Tool Schema Review

## Purpose
- Review tool names, arguments, and failure contracts so agents can use them reliably.
- This is an **AI specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use when tools exist but the agent struggles to pick or call them correctly.
- The main bottleneck is best solved through ai work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not blame the model before checking whether the tool surface is coherent.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Target workflow, users, models, tools, context sources, and failure tolerance.
- Existing prompts, evals, logs, incidents, or product requirements that define the current system.
- What is needed now: system design, routing logic, evals, memory policy, or guardrail review.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- Tools should advertise intent, not implementation trivia.
- Arguments should be minimal, typed, and hard to misuse.
- Failure modes should be explicit and recoverable.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Treat agent behavior as a system: prompts, tools, context, memory, evals, and failure handling must agree.
- Read the current prompt, tool schema, examples, and runtime constraints before proposing architecture changes.
- Prefer designs that are testable, observable, and cheap to iterate rather than clever but fragile.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Inspect the tool set and common failure points.
2. Identify naming, argument, or contract problems.
3. Recommend schema, docs, or example changes.
4. Return the highest-leverage fixes first.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

## Output contract
- Schema issues
- Suggested changes
- Examples
- Expected agent improvements
- System recommendation, policy, or design doc with clear evaluation hooks.
- Failure modes, guardrails, and the smallest next experiment to de-risk the design.

## Failure modes to avoid
- Trying to solve a systems problem with prompt wording alone.
- Adding retrieval, memory, or tools without a concrete failure mode they must solve.
- Skipping eval design and then guessing whether the change helped.
- Declaring success before the output is usable by the next operator, owner, or decision-maker.

## Handoff cues
- State current status, remaining blockers, and the smallest next move.
- Name the files, pages, systems, or source material that another operator should read first.
- Flag approvals, missing evidence, or live-system access that still require a human decision.

## Example invocation
- Slash: `/ai_tool_schema_review <task>`
- Natural language: "Use aI Tool Schema Review to review tool names, arguments, and failure contracts so agents can use them reliably."
- Example: "Design the agent path so it is testable, safe, and not dependent on luck."
- Example: "Review this prompt or tool system and tell me the real failure modes and fixes."
- Often paired with: `ai_prompt_system`, `ai_eval_harness`, `ai_guardrail_review`

## Quality bar
- A good tool surface lets the model choose the right action with less guesswork.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.

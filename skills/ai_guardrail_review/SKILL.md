---
name: ai_guardrail_review
description: "Review an agent for risky behaviors, abuse paths, and missing refusals before wider use."
user-invocable: true
disable-model-invocation: true
---


# AI Guardrail Review

## Purpose
- Review an agent for risky behaviors, abuse paths, and missing refusals before wider use.
- This is an **AI specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use before launching or widening access to an agent that can browse, execute, or message users.
- The main bottleneck is best solved through ai work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not confuse a style review with a real guardrail review.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Target workflow, users, models, tools, context sources, and failure tolerance.
- Existing prompts, evals, logs, incidents, or product requirements that define the current system.
- What is needed now: system design, routing logic, evals, memory policy, or guardrail review.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- Model helpfulness is never an excuse for unsafe defaults.
- Check misuse, not just intended use.
- Prefer design constraints over brittle warnings.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Treat agent behavior as a system: prompts, tools, context, memory, evals, and failure handling must agree.
- Read the current prompt, tool schema, examples, and runtime constraints before proposing architecture changes.
- Prefer designs that are testable, observable, and cheap to iterate rather than clever but fragile.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Map the agent capabilities and sensitive surfaces.
2. Enumerate credible misuse and failure paths.
3. Recommend tighter controls, checks, or refusals.
4. Return a risk-ranked review with next actions.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

## Output contract
- Capability map
- Risk paths
- Recommended controls
- Launch blockers
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
- Slash: `/ai_guardrail_review <task>`
- Natural language: "Use aI Guardrail Review to review an agent for risky behaviors, abuse paths, and missing refusals before wider use."
- Example: "Design the agent path so it is testable, safe, and not dependent on luck."
- Example: "Review this prompt or tool system and tell me the real failure modes and fixes."
- Often paired with: `ai_prompt_system`, `ai_eval_harness`

## Quality bar
- A strong guardrail review narrows the blast radius before the first incident.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.

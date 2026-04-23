---
name: prod_ux_flow_design
description: "Design the task flow, screen sequence, and user decisions before polishing UI details."
user-invocable: true
disable-model-invocation: false
---


# UX Flow Design

## Purpose
- Design the task flow, screen sequence, and user decisions before polishing UI details.
- This is a **product specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use when a user journey, feature flow, or onboarding path needs structure.
- The main bottleneck is best solved through product work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not use when the flow already works and the task is only copy cleanup.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Target user, job to be done, current behavior, and the decision or artifact needed.
- Known constraints around scope, timing, engineering capacity, and metrics.
- Existing feedback, research, retention data, or pricing context that should shape the recommendation.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- Start with the user goal and the fewest steps to it.
- Remove unnecessary choices and dead ends.
- Design for recovery from mistakes, not only the happy path.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Read source material such as feedback notes, specs, roadmap items, or analytics before jumping to solutions.
- Keep recommendations tied to user behavior, value delivery, and the smallest coherent product move.
- Pair opinionated recommendations with assumptions and the signal that would validate them.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Define the starting trigger and end state.
2. Map the main path and edge paths.
3. Tighten decisions, transitions, and feedback.
4. Return the recommended flow with rationale.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

## Output contract
- Main flow
- Edge cases
- State transitions
- Why this flow is better
- Prioritized recommendation with rationale and tradeoffs.
- Metric, experiment, or follow-up signal that would confirm the decision.

## Failure modes to avoid
- Optimizing for feature volume instead of user value or learning speed.
- Treating personas or journeys as decorative documents rather than decision tools.
- Returning a strategy answer with no testable next step.
- Declaring success before the output is usable by the next operator, owner, or decision-maker.

## Handoff cues
- State current status, remaining blockers, and the smallest next move.
- Name the files, pages, systems, or source material that another operator should read first.
- Flag approvals, missing evidence, or live-system access that still require a human decision.

## Example invocation
- Slash: `/prod_ux_flow_design <task>`
- Natural language: "Use uX Flow Design to design the task flow, screen sequence, and user decisions before polishing ui details."
- Example: "Shape this product decision around the user problem and the fastest path to learning."
- Example: "Turn scattered product input into one recommendation we can actually act on."
- Often paired with: `prod_feature_priority`, `prod_experiment_design`, `prod_metric_tree`

## Quality bar
- A flow is good when users need less thinking to succeed.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.

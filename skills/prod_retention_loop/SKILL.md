---
name: prod_retention_loop
description: "Find the repeat-use loop that makes the product worth returning to and worth keeping."
user-invocable: true
disable-model-invocation: true
---


# Retention Loop

## Purpose
- Find the repeat-use loop that makes the product worth returning to and worth keeping.
- This is a **product specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use when activation exists but repeat usage, habit, or expansion is weak.
- The main bottleneck is best solved through product work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not force retention tactics onto a product that still lacks core value.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Target user, job to be done, current behavior, and the decision or artifact needed.
- Known constraints around scope, timing, engineering capacity, and metrics.
- Existing feedback, research, retention data, or pricing context that should shape the recommendation.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- Retention follows recurring value, not reminders alone.
- Look for triggers, routines, payoff, and switching cost together.
- Tie retention work to a specific user segment and use case.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Read source material such as feedback notes, specs, roadmap items, or analytics before jumping to solutions.
- Keep recommendations tied to user behavior, value delivery, and the smallest coherent product move.
- Pair opinionated recommendations with assumptions and the signal that would validate them.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Define the segment and repeat-value job.
2. Map current return triggers and drop-off points.
3. Design a stronger loop with clear behaviors and prompts.
4. Recommend product and lifecycle changes to support the loop.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

## Output contract
- Segment and repeat-value job
- Current loop weaknesses
- Proposed retention loop
- Measurement ideas
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
- Slash: `/prod_retention_loop <task>`
- Natural language: "Use retention Loop to find the repeat-use loop that makes the product worth returning to and worth keeping."
- Example: "Shape this product decision around the user problem and the fastest path to learning."
- Example: "Turn scattered product input into one recommendation we can actually act on."
- Often paired with: `prod_feature_priority`, `prod_experiment_design`, `prod_metric_tree`

## Quality bar
- A retention loop is strong when it is rooted in user value and can be observed in behavior.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.

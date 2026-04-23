---
name: prod_experiment_design
description: "Turn a hypothesis into a clean experiment with decision criteria and minimum measurement."
user-invocable: true
disable-model-invocation: false
---


# Experiment Design

## Purpose
- Turn a hypothesis into a clean experiment with decision criteria and minimum measurement.
- This is a **product specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use when the team wants to test a change instead of debating it abstractly.
- The main bottleneck is best solved through product work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not use for changes that are already obviously required or clearly harmful.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Target user, job to be done, current behavior, and the decision or artifact needed.
- Known constraints around scope, timing, engineering capacity, and metrics.
- Existing feedback, research, retention data, or pricing context that should shape the recommendation.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- One experiment should answer one meaningful question.
- Pick the smallest test that can change a decision.
- Define the kill condition as clearly as the success condition.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Read source material such as feedback notes, specs, roadmap items, or analytics before jumping to solutions.
- Keep recommendations tied to user behavior, value delivery, and the smallest coherent product move.
- Pair opinionated recommendations with assumptions and the signal that would validate them.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. State the decision the experiment supports.
2. Define hypothesis, audience, metric, and timeline.
3. Describe execution details and guardrails.
4. Return what to do if it wins, loses, or is inconclusive.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

## Output contract
- Decision question
- Experiment design
- Metrics and guardrails
- Decision rules
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
- Slash: `/prod_experiment_design <task>`
- Natural language: "Use experiment Design to turn a hypothesis into a clean experiment with decision criteria and minimum measurement."
- Example: "Shape this product decision around the user problem and the fastest path to learning."
- Example: "Turn scattered product input into one recommendation we can actually act on."
- Often paired with: `prod_feature_priority`, `prod_metric_tree`

## Quality bar
- A good experiment reduces argument, not only generates data.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.

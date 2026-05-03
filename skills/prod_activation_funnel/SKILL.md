---
name: prod_activation_funnel
description: "Improve first-run and early-return behavior so users reach value faster and more often."
user-invocable: true
---

## Purpose
- Improve first-run and early-return behavior so users reach value faster and more often.
- This is a **product specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when onboarding, setup, first success, or retention activation needs work.

## Avoid when
- Do not use when the product lacks a clear core value moment at all.

## Inputs to gather
- Target user, job to be done, current behavior, and the decision or artifact needed.
- Known constraints around scope, timing, engineering capacity, and metrics.
- Existing feedback, research, retention data, or pricing context that should shape the recommendation.

## Operating rules
- Map the earliest believable value moment.
- Remove friction before adding persuasion.
- Teach only what the user needs now.

- Start from user problems, not feature ideas. A feature without a user problem is a solution looking for a problem.
- Quantify the impact before prioritizing. How many users does this affect? How severely? How often?
- Distinguish between must-have, nice-to-have, and distraction. Ship must-haves, queue nice-to-haves, kill distractions.
- Every product decision should be falsifiable. State what evidence would prove the decision wrong.
- Prototype before building. A prototype that takes 2 hours saves 2 weeks of building the wrong thing.
## Claude Code tool pattern
- Read source material such as feedback notes, specs, roadmap items, or analytics before jumping to solutions.
- Keep recommendations tied to user behavior, value delivery, and the smallest coherent product move.
- Pair opinionated recommendations with assumptions and the signal that would validate them.

## Expanded workflow
1. Define the activation event.
2. Map the path from signup to that event.
3. Find friction, confusion, and trust gaps.
4. Recommend product, copy, and lifecycle fixes.
## Output contract
- Activation definition
- Friction map
- High-leverage fixes
- Measurement suggestions
- Prioritized recommendation with rationale and tradeoffs.
- Metric, experiment, or follow-up signal that would confirm the decision.

## Failure modes to avoid
- Optimizing for feature volume instead of user value or learning speed.
- Treating personas or journeys as decorative documents rather than decision tools.
- Returning a strategy answer with no testable next step.

## Handoff cues

- Activation funnel analysis: steps, drop-off rates, root causes, improvement priorities.
- A/B test plan for top improvement opportunity.
- Success metric and target.

## Example invocation
- Slash: `/prod_activation_funnel <task>`
- Natural language: "Use activation Funnel to improve first-run and early-return behavior so users reach value faster and more often."
- Example: "Shape this product decision around the user problem and the fastest path to learning."
- Example: "Turn scattered product input into one recommendation we can actually act on."
- Often paired with: `prod_feature_priority`, `prod_experiment_design`, `prod_metric_tree`

## Quality bar
- Activation work should shorten time-to-value, not add onboarding theater.
- Every feature traces back to a specific user problem with evidence.
- Priority is based on user impact x effort, not internal politics or founder preference.
- The scope is small enough to ship and learn from within one cycle.
- Success metrics are defined before building begins.
## Related workflows
- Product build: `prod_product_brief` → `prod_jobs_to_be_done` → `prod_feature_priority` → `prod_activation_funnel`
- Retention loop: `prod_retention_loop` → `prod_feedback_synthesis` → `prod_experiment_design`

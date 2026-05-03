---
name: prod_retention_loop
description: "Find the repeat-use loop that makes the product worth returning to and worth keeping."
user-invocable: true
---

## Purpose
- Find the repeat-use loop that makes the product worth returning to and worth keeping.
- This is a **product specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when activation exists but repeat usage, habit, or expansion is weak.

## Avoid when
- Do not force retention tactics onto a product that still lacks core value.

## Inputs to gather
- Target user, job to be done, current behavior, and the decision or artifact needed.
- Known constraints around scope, timing, engineering capacity, and metrics.
- Existing feedback, research, retention data, or pricing context that should shape the recommendation.

## Operating rules
- Retention follows recurring value, not reminders alone.
- Look for triggers, routines, payoff, and switching cost together.
- Tie retention work to a specific user segment and use case.

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
1. Define the segment and repeat-value job.
2. Map current return triggers and drop-off points.
3. Design a stronger loop with clear behaviors and prompts.
4. Recommend product and lifecycle changes to support the loop.
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

## Handoff cues

- Retention loop design: trigger, action, reward, investment for each loop.
- Retention metrics and cohort analysis approach.
- Improvement priorities based on loop health.

## Example invocation
- Slash: `/prod_retention_loop <task>`
- Natural language: "Use retention Loop to find the repeat-use loop that makes the product worth returning to and worth keeping."
- Example: "Shape this product decision around the user problem and the fastest path to learning."
- Example: "Turn scattered product input into one recommendation we can actually act on."
- Often paired with: `prod_feature_priority`, `prod_experiment_design`, `prod_metric_tree`

## Quality bar
- A retention loop is strong when it is rooted in user value and can be observed in behavior.
- Every feature traces back to a specific user problem with evidence.
- Priority is based on user impact x effort, not internal politics or founder preference.
- The scope is small enough to ship and learn from within one cycle.
- Success metrics are defined before building begins.
## Related workflows
- Product build: `prod_product_brief` → `prod_jobs_to_be_done` → `prod_feature_priority` → `prod_activation_funnel`
- Retention loop: `prod_retention_loop` → `prod_feedback_synthesis` → `prod_experiment_design`

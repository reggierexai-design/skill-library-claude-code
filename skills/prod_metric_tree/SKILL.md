---
name: prod_metric_tree
description: "Turn a goal into leading metrics, diagnostic signals, and ownership paths instead of vanity numbers."
user-invocable: true
---

## Purpose
- Turn a goal into leading metrics, diagnostic signals, and ownership paths instead of vanity numbers.
- This is a **product specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a team knows the goal but not which signals to watch or improve first.

## Avoid when
- Do not produce a metric tree with no link to actual decisions or owners.

## Inputs to gather
- Target user, job to be done, current behavior, and the decision or artifact needed.
- Known constraints around scope, timing, engineering capacity, and metrics.
- Existing feedback, research, retention data, or pricing context that should shape the recommendation.

## Operating rules
- Metrics are useful only when they change behavior.
- Prefer a small tree with real levers over a giant reporting taxonomy.
- Separate outcome metrics from diagnostic inputs.

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
1. Define the top goal and decision cadence.
2. Break it into leading and diagnostic signals.
3. Assign likely owners and action levers.
4. Recommend the smallest useful measurement system.
## Output contract
- Top goal
- Metric tree
- Owners
- Action levers
- Instrumentation gaps
- Prioritized recommendation with rationale and tradeoffs.
- Metric, experiment, or follow-up signal that would confirm the decision.

## Failure modes to avoid
- Optimizing for feature volume instead of user value or learning speed.
- Treating personas or journeys as decorative documents rather than decision tools.
- Returning a strategy answer with no testable next step.

## Handoff cues

- Metric tree: north star, drivers, inputs, ownership mapping.
- Thresholds and alert levels per metric.
- Review cadence and responsible owners.

## Example invocation
- Slash: `/prod_metric_tree <task>`
- Natural language: "Use metric Tree to turn a goal into leading metrics, diagnostic signals, and ownership paths instead of vanity numbers."
- Example: "Shape this product decision around the user problem and the fastest path to learning."
- Example: "Turn scattered product input into one recommendation we can actually act on."
- Often paired with: `prod_feature_priority`, `prod_experiment_design`

## Quality bar
- A metric tree is good when it points the team toward better decisions rather than prettier dashboards.
- Every feature traces back to a specific user problem with evidence.
- Priority is based on user impact x effort, not internal politics or founder preference.
- The scope is small enough to ship and learn from within one cycle.
- Success metrics are defined before building begins.
## Related workflows
- Product build: `prod_product_brief` → `prod_jobs_to_be_done` → `prod_feature_priority` → `prod_activation_funnel`
- Retention loop: `prod_retention_loop` → `prod_feedback_synthesis` → `prod_experiment_design`

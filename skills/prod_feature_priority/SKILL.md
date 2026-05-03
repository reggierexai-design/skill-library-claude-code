---
name: prod_feature_priority
description: "Prioritize features by user value, strategic fit, effort, and timing instead of loud opinions."
user-invocable: true
---

## Purpose
- Prioritize features by user value, strategic fit, effort, and timing instead of loud opinions.
- This is a **product specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when there are more ideas than capacity or when a roadmap needs focus.

## Avoid when
- Do not use when the task is to fully design a single already-chosen feature.

## Inputs to gather
- Target user, job to be done, current behavior, and the decision or artifact needed.
- Known constraints around scope, timing, engineering capacity, and metrics.
- Existing feedback, research, retention data, or pricing context that should shape the recommendation.

## Operating rules
- Prioritize around user pain and strategic leverage.
- Separate importance from urgency.
- Kill low-leverage nice-to-haves early.

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
1. List the candidate features.
2. Score them on value, fit, effort, and timing.
3. Rank them with rationale and tradeoffs.
4. Recommend what to do now, later, or not at all.
## Output contract
- Priority ranking
- Why now
- Why later
- What to cut
- Prioritized recommendation with rationale and tradeoffs.
- Metric, experiment, or follow-up signal that would confirm the decision.

## Failure modes to avoid
- Optimizing for feature volume instead of user value or learning speed.
- Treating personas or journeys as decorative documents rather than decision tools.
- Returning a strategy answer with no testable next step.

## Handoff cues
- Feature priority matrix: features scored on impact, effort, strategic fit.
- Recommended next 3-5 features with rationale.
- Trade-off analysis if capacity is constrained.

## Example invocation
- Slash: `/prod_feature_priority <task>`
- Natural language: "Use feature Priority to prioritize features by user value, strategic fit, effort, and timing instead of loud opinions."
- Example: "Shape this product decision around the user problem and the fastest path to learning."
- Example: "Turn scattered product input into one recommendation we can actually act on."
- Often paired with: `prod_experiment_design`, `prod_metric_tree`

## Quality bar

- Every feature is scored on at least 3 dimensions: impact, effort, and strategic fit.
- The top 3-5 features have clear rationale that another PM could evaluate.
- Low-priority features have explicit reasons, not just deferred.
- Priority reflects user value and business impact, not stakeholder volume.
- Every feature traces back to a specific user problem with evidence.
- Priority is based on user impact x effort, not internal politics or founder preference.
- The scope is small enough to ship and learn from within one cycle.
- Success metrics are defined before building begins.
## Related workflows
- Product build: `prod_product_brief` → `prod_jobs_to_be_done` → `prod_feature_priority` → `prod_activation_funnel`
- Retention loop: `prod_retention_loop` → `prod_feedback_synthesis` → `prod_experiment_design`

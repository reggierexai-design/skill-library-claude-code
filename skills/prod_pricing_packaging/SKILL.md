---
name: prod_pricing_packaging
description: "Shape plans, limits, and upgrade logic so pricing matches value and buying psychology."
user-invocable: true
---

## Purpose
- Shape plans, limits, and upgrade logic so pricing matches value and buying psychology.
- This is a **product specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when evaluating tiers, free limits, premium value, or packaging changes.

## Avoid when
- Do not use when there is no clear product value proposition yet.

## Inputs to gather
- Target user, job to be done, current behavior, and the decision or artifact needed.
- Known constraints around scope, timing, engineering capacity, and metrics.
- Existing feedback, research, retention data, or pricing context that should shape the recommendation.

## Operating rules
- Package around value moments, not internal cost accounting alone.
- Make upgrade triggers legible and fair.
- Avoid feature soup across tiers.

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
1. Define buyer segments and value anchors.
2. Review current or proposed tiers and limits.
3. Find confusion, cannibalization, and weak upgrade logic.
4. Return a tighter packaging recommendation.
## Output contract
- Buyer segments
- Packaging issues
- Recommended plan structure
- Upgrade triggers
- Prioritized recommendation with rationale and tradeoffs.
- Metric, experiment, or follow-up signal that would confirm the decision.

## Failure modes to avoid
- Optimizing for feature volume instead of user value or learning speed.
- Treating personas or journeys as decorative documents rather than decision tools.
- Returning a strategy answer with no testable next step.

## Handoff cues

- Pricing recommendation: model, tiers, anchor price, feature boundaries, upgrade paths.
- Competitive pricing analysis.
- A/B test plan for price sensitivity.

## Example invocation
- Slash: `/prod_pricing_packaging <task>`
- Natural language: "Use pricing and Packaging to shape plans, limits, and upgrade logic so pricing matches value and buying psychology."
- Example: "Shape this product decision around the user problem and the fastest path to learning."
- Example: "Turn scattered product input into one recommendation we can actually act on."
- Often paired with: `prod_feature_priority`, `prod_experiment_design`, `prod_metric_tree`

## Quality bar
- Good packaging makes the right customer self-select quickly.
- Every feature traces back to a specific user problem with evidence.
- Priority is based on user impact x effort, not internal politics or founder preference.
- The scope is small enough to ship and learn from within one cycle.
- Success metrics are defined before building begins.
## Related workflows
- Product build: `prod_product_brief` → `prod_jobs_to_be_done` → `prod_feature_priority` → `prod_activation_funnel`
- Retention loop: `prod_retention_loop` → `prod_feedback_synthesis` → `prod_experiment_design`

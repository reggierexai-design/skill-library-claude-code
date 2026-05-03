---
name: prod_feedback_synthesis
description: "Turn scattered feedback into patterns, priorities, and product actions."
user-invocable: true
---

## Purpose
- Turn scattered feedback into patterns, priorities, and product actions.
- This is a **product specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when support tickets, user notes, reviews, or comments are piling up without a clear signal.

## Avoid when
- Do not use when there is no actual source material to synthesize.

## Inputs to gather
- Target user, job to be done, current behavior, and the decision or artifact needed.
- Known constraints around scope, timing, engineering capacity, and metrics.
- Existing feedback, research, retention data, or pricing context that should shape the recommendation.

## Operating rules
- Frequency matters, but so does severity and user segment.
- Separate product flaws from education gaps.
- Tie themes to actions, not only labels.

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
1. Inventory the feedback sources.
2. Group and rank themes.
3. Separate quick wins from structural issues.
4. Recommend product, docs, or support actions.
## Output contract
- Top themes
- Who is affected
- Recommended actions
- What needs more evidence
- Prioritized recommendation with rationale and tradeoffs.
- Metric, experiment, or follow-up signal that would confirm the decision.

## Failure modes to avoid
- Optimizing for feature volume instead of user value or learning speed.
- Treating personas or journeys as decorative documents rather than decision tools.
- Returning a strategy answer with no testable next step.

## Handoff cues

- Feedback synthesis: themes, frequency, sentiment, actionable insights.
- Priority improvements based on feedback volume and severity.
- Feedback routing: product, support, or sales.

## Example invocation
- Slash: `/prod_feedback_synthesis <task>`
- Natural language: "Use feedback Synthesis to turn scattered feedback into patterns, priorities, and product actions."
- Example: "Shape this product decision around the user problem and the fastest path to learning."
- Example: "Turn scattered product input into one recommendation we can actually act on."
- Often paired with: `prod_feature_priority`, `prod_experiment_design`, `prod_metric_tree`

## Quality bar
- Synthesis should help the roadmap and the support queue at the same time.
- Every feature traces back to a specific user problem with evidence.
- Priority is based on user impact x effort, not internal politics or founder preference.
- The scope is small enough to ship and learn from within one cycle.
- Success metrics are defined before building begins.
## Related workflows
- Product build: `prod_product_brief` → `prod_jobs_to_be_done` → `prod_feature_priority` → `prod_activation_funnel`
- Retention loop: `prod_retention_loop` → `prod_feedback_synthesis` → `prod_experiment_design`

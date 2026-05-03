---
name: prod_experiment_design
description: "Turn a hypothesis into a clean experiment with decision criteria and minimum measurement."
user-invocable: true
---

## Purpose
- Turn a hypothesis into a clean experiment with decision criteria and minimum measurement.
- This is a **product specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when the team wants to test a change instead of debating it abstractly.

## Avoid when
- Do not use for changes that are already obviously required or clearly harmful.

## Inputs to gather
- Target user, job to be done, current behavior, and the decision or artifact needed.
- Known constraints around scope, timing, engineering capacity, and metrics.
- Existing feedback, research, retention data, or pricing context that should shape the recommendation.

## Operating rules
- One experiment should answer one meaningful question.
- Pick the smallest test that can change a decision.
- Define the kill condition as clearly as the success condition.

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
1. State the decision the experiment supports.
2. Define hypothesis, audience, metric, and timeline.
3. Describe execution details and guardrails.
4. Return what to do if it wins, loses, or is inconclusive.
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

## Handoff cues
- Experiment design: hypothesis, variants, sample size, duration, primary metric.
- Segmentation plan for analysis.
- Decision criteria: ship, iterate, or kill.

## Example invocation
- Slash: `/prod_experiment_design <task>`
- Natural language: "Use experiment Design to turn a hypothesis into a clean experiment with decision criteria and minimum measurement."
- Example: "Shape this product decision around the user problem and the fastest path to learning."
- Example: "Turn scattered product input into one recommendation we can actually act on."
- Often paired with: `prod_feature_priority`, `prod_metric_tree`

## Quality bar

- The hypothesis is falsifiable: there's a result that would make you not ship.
- Sample size is calculated before the experiment starts.
- Primary metric is singular; supporting metrics provide context but don't override.
- Decision criteria are defined before results are seen — no post-hoc rationalization.
- Every feature traces back to a specific user problem with evidence.
- Priority is based on user impact x effort, not internal politics or founder preference.
- The scope is small enough to ship and learn from within one cycle.
- Success metrics are defined before building begins.
## Related workflows
- Product build: `prod_product_brief` → `prod_jobs_to_be_done` → `prod_feature_priority` → `prod_activation_funnel`
- Retention loop: `prod_retention_loop` → `prod_feedback_synthesis` → `prod_experiment_design`

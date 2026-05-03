---
name: prod_customer_journey
description: "Map the path from first awareness to repeated value so friction, proof gaps, and drop-offs become visible."
user-invocable: true
metadata: {"openclaw":{"emoji":"📦"}}
---

## Purpose
- Map the path from first awareness to repeated value so friction, proof gaps, and drop-offs become visible.
- This is a **product specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when the team needs a clearer view of the end-to-end user path across marketing, product, and support.

## Avoid when
- Do not confuse a journey map with a fantasy flow that real users never take.

## Inputs to gather
- Target user, job to be done, current behavior, and the decision or artifact needed.
- Known constraints around scope, timing, engineering capacity, and metrics.
- Existing feedback, research, retention data, or pricing context that should shape the recommendation.

## Operating rules
- Map actual behavior, not idealized funnels.
- Include emotions, doubts, and switching costs where they affect decisions.
- Show where proof, onboarding, and follow-up matter most.

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
1. Define the starting trigger and desired repeated value.
2. Map the major stages, decisions, and drop-offs.
3. Identify friction, proof gaps, and support needs.
4. Recommend the next few improvements with the highest leverage.
## Output contract
- Journey stages
- Key questions and frictions
- Proof gaps
- Priority improvements
- Prioritized recommendation with rationale and tradeoffs.
- Metric, experiment, or follow-up signal that would confirm the decision.

## Failure modes to avoid
- Optimizing for feature volume instead of user value or learning speed.
- Treating personas or journeys as decorative documents rather than decision tools.
- Returning a strategy answer with no testable next step.

## Handoff cues
- Customer journey map: stages, touchpoints, emotions, pain points, opportunities.
- Priority improvements ranked by impact.
- Measurement plan for journey health.

## Example invocation
- Slash: `/prod_customer_journey <task>`
- Natural language: "Use customer Journey to map the path from first awareness to repeated value so friction, proof gaps, and drop-offs become visible."
- Example: "Shape this product decision around the user problem and the fastest path to learning."
- Example: "Turn scattered product input into one recommendation we can actually act on."
- Often paired with: `prod_feature_priority`, `prod_experiment_design`, `prod_metric_tree`

## Quality bar

- Every journey stage has a measurable success metric.
- Pain points are validated with user data, not assumed.
- The map covers the full journey from awareness to advocacy, not just product usage.
- Improvement priorities are ranked by user impact and business value.
- Every feature traces back to a specific user problem with evidence.
- Priority is based on user impact x effort, not internal politics or founder preference.
- The scope is small enough to ship and learn from within one cycle.
- Success metrics are defined before building begins.
## Related workflows
- Product build: `prod_product_brief` → `prod_jobs_to_be_done` → `prod_feature_priority` → `prod_activation_funnel`
- Retention loop: `prod_retention_loop` → `prod_feedback_synthesis` → `prod_experiment_design`

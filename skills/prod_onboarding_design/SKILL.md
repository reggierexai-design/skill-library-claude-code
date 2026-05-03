---
name: prod_onboarding_design
description: "Design first-run guidance so new users reach value quickly without excess friction or explanation."
user-invocable: true
---

## Purpose
- Design first-run guidance so new users reach value quickly without excess friction or explanation.
- This is a **product specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when new users are confused, drop early, or fail to reach the first meaningful outcome.

## Avoid when
- Do not add tutorial clutter to hide product confusion that should be fixed directly.

## Inputs to gather
- Target user, job to be done, current behavior, and the decision or artifact needed.
- Known constraints around scope, timing, engineering capacity, and metrics.
- Existing feedback, research, retention data, or pricing context that should shape the recommendation.

## Operating rules
- Onboarding should get users to value, not just tour features.
- Ask only for information that unlocks the next step.
- Use defaults, examples, and progressive disclosure where possible.

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
1. Identify the first meaningful user outcome.
2. Map current first-run friction and confusion.
3. Design the smallest path to value.
4. Recommend copy, UX, and instrumentation changes.
## Output contract
- First-value target
- Current friction
- Proposed onboarding flow
- Test ideas
- Prioritized recommendation with rationale and tradeoffs.
- Metric, experiment, or follow-up signal that would confirm the decision.

## Failure modes to avoid
- Optimizing for feature volume instead of user value or learning speed.
- Treating personas or journeys as decorative documents rather than decision tools.
- Returning a strategy answer with no testable next step.

## Handoff cues

- Onboarding design: steps, aha moment, success metric, drop-off checkpoints.
- A/B test plan for onboarding variants.
- Personalization rules by user segment.

## Example invocation
- Slash: `/prod_onboarding_design <task>`
- Natural language: "Use onboarding Design to design first-run guidance so new users reach value quickly without excess friction or explanation."
- Example: "Shape this product decision around the user problem and the fastest path to learning."
- Example: "Turn scattered product input into one recommendation we can actually act on."
- Often paired with: `prod_feature_priority`, `prod_experiment_design`, `prod_metric_tree`

## Quality bar
- Good onboarding removes hesitation and helps users succeed with less effort.
- Every feature traces back to a specific user problem with evidence.
- Priority is based on user impact x effort, not internal politics or founder preference.
- The scope is small enough to ship and learn from within one cycle.
- Success metrics are defined before building begins.
## Related workflows
- Product build: `prod_product_brief` → `prod_jobs_to_be_done` → `prod_feature_priority` → `prod_activation_funnel`
- Retention loop: `prod_retention_loop` → `prod_feedback_synthesis` → `prod_experiment_design`

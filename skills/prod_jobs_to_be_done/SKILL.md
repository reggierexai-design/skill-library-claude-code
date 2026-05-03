---
name: prod_jobs_to_be_done
description: "Frame the product around the user job, context, forces, and switching logic instead of feature lists."
user-invocable: true
---

## Purpose
- Frame the product around the user job, context, forces, and switching logic instead of feature lists.
- This is a **product specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when product strategy or messaging is fuzzy because the real user job is not sharply framed.

## Avoid when
- Do not reduce a nuanced market to one generic job statement.

## Inputs to gather
- Target user, job to be done, current behavior, and the decision or artifact needed.
- Known constraints around scope, timing, engineering capacity, and metrics.
- Existing feedback, research, retention data, or pricing context that should shape the recommendation.

## Operating rules
- The job includes context, progress sought, and tradeoffs accepted.
- Competing alternatives include workarounds, not only direct competitors.
- Good job framing sharpens both product and positioning.

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
1. Identify the triggering situation.
2. Define the progress the user is trying to make.
3. Map alternatives, anxieties, and adoption forces.
4. Turn the job framing into product and messaging implications.
## Output contract
- Job statement
- Trigger context
- Alternatives and forces
- Implications
- Prioritized recommendation with rationale and tradeoffs.
- Metric, experiment, or follow-up signal that would confirm the decision.

## Failure modes to avoid
- Optimizing for feature volume instead of user value or learning speed.
- Treating personas or journeys as decorative documents rather than decision tools.
- Returning a strategy answer with no testable next step.

## Handoff cues

- JTBD framework: jobs, outcomes, current solutions, frustrations, opportunities.
- Job priority based on frequency and importance.
- Feature mapping to high-priority jobs.

## Example invocation
- Slash: `/prod_jobs_to_be_done <task>`
- Natural language: "Use jobs To Be Done to frame the product around the user job, context, forces, and switching logic instead of feature lists."
- Example: "Shape this product decision around the user problem and the fastest path to learning."
- Example: "Turn scattered product input into one recommendation we can actually act on."
- Often paired with: `prod_feature_priority`, `prod_experiment_design`, `prod_metric_tree`

## Quality bar
- A strong JTBD pass makes the product easier to explain and easier to prioritize.
- Every feature traces back to a specific user problem with evidence.
- Priority is based on user impact x effort, not internal politics or founder preference.
- The scope is small enough to ship and learn from within one cycle.
- Success metrics are defined before building begins.
## Related workflows
- Product build: `prod_product_brief` → `prod_jobs_to_be_done` → `prod_feature_priority` → `prod_activation_funnel`
- Retention loop: `prod_retention_loop` → `prod_feedback_synthesis` → `prod_experiment_design`

---
name: prod_persona_snapshot
description: "Synthesize the target user, buying context, pains, triggers, and objections."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udce6"}}
---

## Purpose
- Synthesize the target user, buying context, pains, triggers, and objections.
- This is a **product specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when product, messaging, or launch work needs a sharper picture of the target user and buying context.

## Avoid when
- Do not treat a persona snapshot as a substitute for direct research when primary evidence is available and needed.

## Inputs to gather
- Target user, job to be done, current behavior, and the decision or artifact needed.
- Known constraints around scope, timing, engineering capacity, and metrics.
- Existing feedback, research, retention data, or pricing context that should shape the recommendation.

## Operating rules
- Focus on decision-relevant behavior, not demographic theater.
- Capture context, triggers, pains, desired outcomes, and objections.
- Keep the snapshot actionable for product, copy, and distribution choices.

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
1. Define the target segment and decision context.
2. Summarize pains, triggers, desired outcomes, and blockers.
3. Note the strongest supporting evidence and biggest unknowns.
4. Return a compact persona snapshot.
## Output contract
- Target segment
- Buying context
- Core pains and desired outcomes
- Objections and evidence notes
- Prioritized recommendation with rationale and tradeoffs.
- Metric, experiment, or follow-up signal that would confirm the decision.

## Failure modes to avoid
- Optimizing for feature volume instead of user value or learning speed.
- Treating personas or journeys as decorative documents rather than decision tools.
- Returning a strategy answer with no testable next step.

## Handoff cues

- Persona snapshot: demographics, goals, frustrations, current solutions, buying triggers.
- Validation: data sources supporting each attribute.
- Feature and messaging implications per persona.

## Example invocation
- Slash: `/prod_persona_snapshot <task>`
- Natural language: "Use persona Snapshot to synthesize the target user, buying context, pains, triggers, and objections."
- Example: "Shape this product decision around the user problem and the fastest path to learning."
- Example: "Turn scattered product input into one recommendation we can actually act on."
- Often paired with: `prod_feature_priority`, `prod_experiment_design`, `prod_metric_tree`

## Quality bar
- A useful persona snapshot changes what gets built and how it is presented.
- Every feature traces back to a specific user problem with evidence.
- Priority is based on user impact x effort, not internal politics or founder preference.
- The scope is small enough to ship and learn from within one cycle.
- Success metrics are defined before building begins.
## Related workflows
- Product build: `prod_product_brief` → `prod_jobs_to_be_done` → `prod_feature_priority` → `prod_activation_funnel`
- Retention loop: `prod_retention_loop` → `prod_feedback_synthesis` → `prod_experiment_design`

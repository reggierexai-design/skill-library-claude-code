---
name: prod_ui_copy_polish
description: "Upgrade product copy so the interface feels clear, confident, trustworthy, and on-brand."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udce6"}}
---

## Purpose
- Upgrade product copy so the interface feels clear, confident, trustworthy, and on-brand.
- This is a **product specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use for buttons, onboarding, empty states, settings, prompts, and other UI language.

## Avoid when
- Do not use when the underlying product logic or flow is the real problem.

## Inputs to gather
- Target user, job to be done, current behavior, and the decision or artifact needed.
- Known constraints around scope, timing, engineering capacity, and metrics.
- Existing feedback, research, retention data, or pricing context that should shape the recommendation.

## Operating rules
- Clarity beats cleverness.
- Every screen should explain what matters now.
- Trust language matters most where users hesitate.

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
1. Identify the user moment and its friction.
2. Rewrite for clarity, trust, and momentum.
3. Check consistency across related states.
4. Return final copy plus any structural notes.
## Output contract
- Improved strings
- Voice notes
- Trust gaps fixed
- Any flow issues uncovered
- Prioritized recommendation with rationale and tradeoffs.
- Metric, experiment, or follow-up signal that would confirm the decision.

## Failure modes to avoid
- Optimizing for feature volume instead of user value or learning speed.
- Treating personas or journeys as decorative documents rather than decision tools.
- Returning a strategy answer with no testable next step.

## Handoff cues
- UI copy inventory: screens, elements, current copy, recommended copy, rationale.
- Tone consistency check across all screens.
- Accessibility review of copy.

## Example invocation
- Slash: `/prod_ui_copy_polish <task>`
- Natural language: "Use uI Copy Polish to upgrade product copy so the interface feels clear, confident, trustworthy, and on-brand."
- Example: "Shape this product decision around the user problem and the fastest path to learning."
- Example: "Turn scattered product input into one recommendation we can actually act on."
- Often paired with: `prod_feature_priority`, `prod_experiment_design`, `prod_metric_tree`

## Quality bar

- Every screen copy is reviewed for clarity, brevity, and tone consistency.
- No orphaned placeholder text or Lorem ipsum remains.
- Error messages tell the user what happened and what to do next.
- Copy is tested with at least 1 user who is not on the team.
- Every feature traces back to a specific user problem with evidence.
- Priority is based on user impact x effort, not internal politics or founder preference.
- The scope is small enough to ship and learn from within one cycle.
- Success metrics are defined before building begins.
## Related workflows
- Product build: `prod_product_brief` → `prod_jobs_to_be_done` → `prod_feature_priority` → `prod_activation_funnel`
- Retention loop: `prod_retention_loop` → `prod_feedback_synthesis` → `prod_experiment_design`

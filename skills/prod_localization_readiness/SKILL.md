---
name: prod_localization_readiness
description: "Review a product or launch for localization, i18n, and translation-readiness gaps."
user-invocable: true
---

## Purpose
- Review a product or launch for localization, i18n, and translation-readiness gaps.
- This is a **product specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use before supporting new languages, locales, regions, or translated content flows.

## Avoid when
- Do not use when the product will remain intentionally single-locale.

## Inputs to gather
- Target user, job to be done, current behavior, and the decision or artifact needed.
- Known constraints around scope, timing, engineering capacity, and metrics.
- Existing feedback, research, retention data, or pricing context that should shape the recommendation.

## Operating rules
- Audit before you translate. Hardcoded strings, inflexible layouts, and culture-specific imagery will block localization faster than translation speed.
- Design for the longest text. German labels are 30% longer than English. Layouts that break with longer text aren't localization-ready.
- Externalize all strings. Every user-facing string should be in a resource file, not in code.
- Plan for ongoing maintenance. Strings change every release; localization isn't a one-time project.

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
1. Audit all user-facing content: strings, emails, docs, images.
2. Check for hardcoded strings and externalize them.
3. Test layouts with 30% longer text (German/French simulation).
4. Check date, number, and currency format handling.
5. Assess culture-specific imagery and color choices.
6. Estimate localization effort per target market.
7. Set up the translation workflow and maintenance plan.

## Output contract
- Prioritized recommendation with rationale and tradeoffs.
- Metric, experiment, or follow-up signal that would confirm the decision.

## Failure modes to avoid
- Optimizing for feature volume instead of user value or learning speed.
- Treating personas or journeys as decorative documents rather than decision tools.
- Returning a strategy answer with no testable next step.

## Handoff cues
- Localization readiness audit: hardcoded strings, date/number formats, layout flexibility, content inventory.
- Priority fixes before translation can begin.
- Estimated localization effort by market.

## Example invocation
- Slash: `/prod_localization_readiness <task>`
- Natural language: "Use product Localization Readiness to review a product or launch for localization, i18n, and translation-readiness gaps."
- Example: "Shape this product decision around the user problem and the fastest path to learning."
- Example: "Turn scattered product input into one recommendation we can actually act on."
- Often paired with: `prod_feature_priority`, `prod_experiment_design`, `prod_metric_tree`

## Quality bar
## Related workflows
- Product build: `prod_product_brief` â†’ `prod_jobs_to_be_done` â†’ `prod_feature_priority` â†’ `prod_activation_funnel`
- Retention loop: `prod_retention_loop` â†’ `prod_feedback_synthesis` â†’ `prod_experiment_design`
- Every feature traces back to a specific user problem with evidence.
- Priority is based on user impact x effort, not internal politics or founder preference.
- The scope is small enough to ship and learn from within one cycle.
- Success metrics are defined before building begins.

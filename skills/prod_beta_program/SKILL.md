---
name: prod_beta_program
description: "Design a beta program with candidate criteria, learning goals, guardrails, and feedback loops."
user-invocable: true
---

## Purpose
- Design a beta program with candidate criteria, learning goals, guardrails, and feedback loops.
- This is a **product specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use before inviting early users into a feature, product, or workflow that still needs structured learning.

## Avoid when
- Do not use when the product is ready for broad launch and no special cohort is needed.

## Inputs to gather
- Target user, job to be done, current behavior, and the decision or artifact needed.
- Known constraints around scope, timing, engineering capacity, and metrics.
- Existing feedback, research, retention data, or pricing context that should shape the recommendation.

## Operating rules
- Beta is for learning, not for selling. If you're using beta as a sales tool, call it an early access program.
- Define success criteria before the beta starts. Otherwise you'll declare success based on vibes, not data.
- Include both qualitative and quantitative feedback. Numbers tell you what; interviews tell you why.
- Set a beta duration. Open-ended betas never end â€” they just slowly die.

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
1. Define beta goals: what you need to learn or validate.
2. Recruit participants who match the target user profile.
3. Set up feedback channels: in-app, email, scheduled interviews.
4. Define success criteria and graduation requirements.
5. Launch with a fixed duration (typically 4-8 weeks).
6. Collect feedback, triage issues, and iterate.
7. Evaluate against success criteria and decide: graduate, extend, or kill.

## Output contract
- Prioritized recommendation with rationale and tradeoffs.
- Metric, experiment, or follow-up signal that would confirm the decision.

## Failure modes to avoid
- Optimizing for feature volume instead of user value or learning speed.
- Treating personas or journeys as decorative documents rather than decision tools.
- Returning a strategy answer with no testable next step.

## Handoff cues
- Beta program plan: participants, timeline, feedback mechanisms, success criteria.
- Communication cadence and channels.
- Graduation criteria from beta to GA.

## Example invocation
- Slash: `/prod_beta_program <task>`
- Natural language: "Use product Beta Program to design a beta program with candidate criteria, learning goals, guardrails, and feedback loops."
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

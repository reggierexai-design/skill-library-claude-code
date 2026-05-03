---
name: prod_product_brief
description: "Turn an idea or request into a crisp product brief with users, problem, outcome, scope, and constraints."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udce6"}}
---

## Purpose
- Turn an idea or request into a crisp product brief with users, problem, outcome, scope, and constraints.
- This is a **product specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a feature, product idea, or initiative is still fuzzy and needs a shared frame.

## Avoid when
- Do not use once the project already has a current, high-quality brief for the same scope.

## Inputs to gather
- Target user, job to be done, current behavior, and the decision or artifact needed.
- Known constraints around scope, timing, engineering capacity, and metrics.
- Existing feedback, research, retention data, or pricing context that should shape the recommendation.

## Operating rules
- Anchor the brief in user pain and intended outcome.
- Separate must-have scope from attractive extras.
- Make constraints explicit so the plan is honest.

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
1. Define the user, problem, and desired outcome.
2. Set scope, constraints, and success metrics.
3. Note assumptions and open questions.
4. Return a brief that can guide design or engineering.
## Output contract
- Audience
- Problem
- Outcome
- Scope and constraints
- Prioritized recommendation with rationale and tradeoffs.
- Metric, experiment, or follow-up signal that would confirm the decision.

## Failure modes to avoid
- Optimizing for feature volume instead of user value or learning speed.
- Treating personas or journeys as decorative documents rather than decision tools.
- Returning a strategy answer with no testable next step.

## Handoff cues
- Product brief: problem, target user, solution outline, success metrics, constraints.
- Scope boundaries: what's in v1 and what's deferred.
- Assumptions that need validation.

## Example invocation
- Slash: `/prod_product_brief <task>`
- Natural language: "Use product Brief to turn an idea or request into a crisp product brief with users, problem, outcome, scope, and constraints."
- Example: "Shape this product decision around the user problem and the fastest path to learning."
- Example: "Turn scattered product input into one recommendation we can actually act on."
- Often paired with: `prod_feature_priority`, `prod_experiment_design`, `prod_metric_tree`

## Quality bar

- The problem is specific enough that a stranger could understand it in one reading.
- Success metrics are measurable and time-bound.
- Scope boundaries are explicit: what's in v1 and what's explicitly deferred.
- Assumptions that need validation are flagged, not treated as facts.
- Every feature traces back to a specific user problem with evidence.
- Priority is based on user impact x effort, not internal politics or founder preference.
- The scope is small enough to ship and learn from within one cycle.
- Success metrics are defined before building begins.
## Related workflows
- Product build: `prod_product_brief` → `prod_jobs_to_be_done` → `prod_feature_priority` → `prod_activation_funnel`
- Retention loop: `prod_retention_loop` → `prod_feedback_synthesis` → `prod_experiment_design`

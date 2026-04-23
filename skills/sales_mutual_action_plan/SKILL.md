---
name: sales_mutual_action_plan
description: "Create a buyer-facing action plan with milestones, dependencies, and next commitments."
user-invocable: true
disable-model-invocation: true
---


# Sales Mutual Action Plan

## Purpose
- Create a buyer-facing action plan with milestones, dependencies, and next commitments.
- This is a **sales specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use when a deal needs structure across stakeholders, procurement, security, or rollout steps.
- The main bottleneck is best solved through sales work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not use for very early discovery where no real buying process exists yet.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Account or pipeline context, stakeholder roles, deal stage, timeline, and next commitment needed.
- Known pains, objections, proof assets, pricing context, and competitive pressure.
- Whether the output should support discovery, demo, follow-up, proposal, or forecast discipline.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- Work from evidence in the workspace, the prompt, or verified sources.
- Keep the output decision-oriented rather than bloated.
- Name assumptions, risks, and unresolved questions explicitly.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Read the account notes, product truth, and available proof before writing buyer-facing material.
- Keep recommendations tied to buyer movement: trust, urgency, qualification, and next step quality.
- Use specific pain language and proof instead of generic persuasion tropes.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Define the exact slice of work in scope.
2. Gather the minimum evidence needed to reason safely.
3. Produce the plan, review, or artifact that best fits the task.
4. Check the output for gaps, regressions, or overclaiming.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

## Output contract
- Scope
- Key findings or plan
- Risks and assumptions
- Recommended next actions
- Deal-moving artifact: account brief, sequence, demo flow, proposal outline, or pipeline review.
- Stage risk, missing proof, and the strongest next-step recommendation.

## Failure modes to avoid
- Writing persuasive copy that ignores deal stage or actual buyer risk.
- Confusing activity with movement or overtrusting pipeline labels.
- Promising proof, timelines, or product capabilities that are not verified.
- Declaring success before the output is usable by the next operator, owner, or decision-maker.

## Handoff cues
- State current status, remaining blockers, and the smallest next move.
- Name the files, pages, systems, or source material that another operator should read first.
- Flag approvals, missing evidence, or live-system access that still require a human decision.

## Example invocation
- Slash: `/sales_mutual_action_plan <task>`
- Natural language: "Use sales Mutual Action Plan to create a buyer-facing action plan with milestones, dependencies, and next commitments."
- Example: "Help move this deal forward with better qualification, proof, and next steps."
- Example: "Review the pipeline or account and tell me what is real, risky, or stuck."
- Often paired with: `sales_account_research`, `sales_discovery_call_plan`, `sales_pipeline_review`

## Quality bar
- The result should be specific enough that another operator could act on it without guessing.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.

---
name: sales_demo_flow
description: "Shape a demo around the buyer problem, proof points, and next commitment instead of a product tour."
user-invocable: true
disable-model-invocation: true
---


# Sales Demo Flow

## Purpose
- Shape a demo around the buyer problem, proof points, and next commitment instead of a product tour.
- This is a **sales specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use before demonstrating a product to prospects, partners, or internal champions.
- The main bottleneck is best solved through sales work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not let the demo become an exhaustive feature walk-through.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Account or pipeline context, stakeholder roles, deal stage, timeline, and next commitment needed.
- Known pains, objections, proof assets, pricing context, and competitive pressure.
- Whether the output should support discovery, demo, follow-up, proposal, or forecast discipline.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- Lead with the buyer problem and the payoff.
- Show the smallest set of proof points that matter.
- Land on a concrete next commitment.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Read the account notes, product truth, and available proof before writing buyer-facing material.
- Keep recommendations tied to buyer movement: trust, urgency, qualification, and next step quality.
- Use specific pain language and proof instead of generic persuasion tropes.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Define the audience, goal, and likely concerns.
2. Sequence the narrative, proof points, and transitions.
3. Plan the close and next step ask.
4. Return a demo flow with talking notes.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

## Output contract
- Audience and goal
- Demo sequence
- Proof points
- Close and next step
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
- Slash: `/sales_demo_flow <task>`
- Natural language: "Use sales Demo Flow to shape a demo around the buyer problem, proof points, and next commitment instead of a product tour."
- Example: "Help move this deal forward with better qualification, proof, and next steps."
- Example: "Review the pipeline or account and tell me what is real, risky, or stuck."
- Often paired with: `sales_account_research`, `sales_discovery_call_plan`, `sales_pipeline_review`

## Quality bar
- A good demo flow makes the product feel like the answer to a live problem.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.

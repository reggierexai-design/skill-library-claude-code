---
name: sales_followup_sequence
description: "Write a short follow-up sequence that moves a deal forward without sounding automated."
user-invocable: true
disable-model-invocation: true
---


# Sales Follow-up Sequence

## Purpose
- Write a short follow-up sequence that moves a deal forward without sounding automated.
- This is a **sales specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use after a call, demo, proposal, or quiet period when the next step needs a nudge.
- The main bottleneck is best solved through sales work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not spam follow-ups that add no new value.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Account or pipeline context, stakeholder roles, deal stage, timeline, and next commitment needed.
- Known pains, objections, proof assets, pricing context, and competitive pressure.
- Whether the output should support discovery, demo, follow-up, proposal, or forecast discipline.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- Each message should earn another read.
- Reinforce the buyer problem, next step, or proof.
- Keep pressure low and clarity high.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Read the account notes, product truth, and available proof before writing buyer-facing material.
- Keep recommendations tied to buyer movement: trust, urgency, qualification, and next step quality.
- Use specific pain language and proof instead of generic persuasion tropes.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Define the deal stage and desired next action.
2. Draft a short sequence with distinct angles.
3. Check tone, timing, and proof use.
4. Return a ready-to-send sequence.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

## Output contract
- Stage and goal
- Message sequence
- Timing notes
- Proof or CTA angles
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
- Slash: `/sales_followup_sequence <task>`
- Natural language: "Use sales Follow-up Sequence to write a short follow-up sequence that moves a deal forward without sounding automated."
- Example: "Help move this deal forward with better qualification, proof, and next steps."
- Example: "Review the pipeline or account and tell me what is real, risky, or stuck."
- Often paired with: `sales_account_research`, `sales_discovery_call_plan`, `sales_pipeline_review`

## Quality bar
- Good follow-up respects attention while keeping momentum alive.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.

---
name: sales_discovery_call_plan
description: "Prepare a discovery call that surfaces pain, urgency, fit, and buying constraints."
user-invocable: true
---

## Purpose
- Prepare a discovery call that surfaces pain, urgency, fit, and buying constraints.
- This is a **sales specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use before a sales or partnership call where qualification and learning matter.

## Avoid when
- Do not turn discovery into a feature recital.

## Inputs to gather
- Account context: what do you already know about the prospect?
- Discovery objectives: what do you need to learn to qualify or advance the deal?
- Question categories: pain, impact, urgency, decision process, competition.
- Time available and participant list.

## Operating rules
- Ask toward a decision, not toward chatter.
- Uncover pain, stakes, timing, and blockers.
- Listen for disqualifiers as well as buying signals.
- Ask, then listen. The discovery call is 80% listening, 20% asking. If you're talking more than the prospect, it's a pitch, not a discovery.
- Sequence questions: pain -> impact -> urgency -> decision process. Skip impact and urgency, and you have a nice chat but no deal.
- Don't pitch during discovery. Discovery is for learning; the pitch comes after you understand the problem.
- End with a commitment. 'I'll send you some info' is not a commitment. 'Can we schedule a demo with your team next week?' is.

- Discovery before pitch. Understand the prospect's actual problem before presenting your solution. Pitching without discovery is guessing.
- Lead with the problem you solve, not the features you have. Buyers buy outcomes, not capabilities.
- Handle objections with proof, not pressure. A prospect who feels pressured will agree and then ghost.
- Track conversion at each stage of the funnel. A leak at any stage kills the pipeline regardless of top-of-funnel volume.
- Follow-up is where deals are won or lost. 80% of sales require 5+ touches but most sellers stop after 2.
## Claude Code tool pattern
- Use `WebFetch` to research prospect companies, news, and relevant context before outreach.
- Use `Read` to load CRM data, call notes, and deal history.
- After sales planning, use `att_proof_mining` to ensure every claim in materials is backed.

## Expanded workflow
1. Define the account context and goal for the call.
2. Prepare question themes and signal checks.
3. Plan the close, next step, and note template.
4. Return a discovery plan ready to use live.
## Output contract
- Call goal
- Question themes
- Signal checklist
- Close and next step
- Deal-moving artifact: account brief, sequence, demo flow, proposal outline, or pipeline review.
- Stage risk, missing proof, and the strongest next-step recommendation.

## Failure modes to avoid
- Talking more than listening â€” it's a pitch, not discovery.
- Skipping impact and urgency â€” nice chat, no deal.
- Pitching during discovery â€” you can't pitch a solution you haven't diagnosed.
- No commitment at the end â€” 'I'll follow up' is not a next step.
- Asking only surface questions â€” 'tell me about your challenges' is too vague.

## Handoff cues
- Discovery call plan: objectives, questions by category, listening cues, qualification criteria.
- Stakeholder mapping for the account.
- Next step options based on call outcomes.

## Example invocation
- Slash: `/sales_discovery_call_plan <task>`
- Natural language: "Use sales Discovery Call Plan to prepare a discovery call that surfaces pain, urgency, fit, and buying constraints."
- Example: "Help move this deal forward with better qualification, proof, and next steps."
- Example: "Review the pipeline or account and tell me what is real, risky, or stuck."
- Often paired with: `sales_account_research`, `sales_pipeline_review`

## Quality bar
- 80% listening, 20% asking.
- Pain, impact, urgency, and decision process all explored.
- No pitching during discovery.
- A specific next step committed by both sides.
- Every outreach starts with the prospect's context, not your product pitch.
- Objection handling uses proof and reframing, not pressure.
- The funnel has measurable conversion rates at each stage.
- Follow-up cadence is defined and adhered to.
## Related workflows
- Sales flow: `sales_account_research` â†’ `sales_discovery_call_plan` â†’ `sales_demo_flow` â†’ `sales_mutual_action_plan`

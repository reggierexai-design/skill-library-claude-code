---
name: sales_followup_sequence
description: "Write a short follow-up sequence that moves a deal forward without sounding automated."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udce8"}}
---

## Purpose
- Write a short follow-up sequence that moves a deal forward without sounding automated.
- This is a **sales specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use after a call, demo, proposal, or quiet period when the next step needs a nudge.

## Avoid when
- Do not spam follow-ups that add no new value.

## Inputs to gather
- Discovery findings: what did you learn about the prospect's pain and process?
- Decision timeline: when are they looking to make a decision?
- Content inventory: what proof assets, case studies, or demos are available?
- Previous touchpoints: what's been discussed and what's been sent?

## Operating rules
- Each message should earn another read.
- Reinforce the buyer problem, next step, or proof.
- Keep pressure low and clarity high.
- Every follow-up must add new value. If you're just 'checking in,' you're being annoying.
- Match follow-up content to where the buyer is in their process. Early stage = education; late stage = proof and urgency.
- Sequence length matches deal complexity: 3 touches for simple deals, 7+ for enterprise.
- Have a break-up email. Not every prospect is ready, and a respectful close is better than being ignored forever.

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
1. Define the deal stage and desired next action.
2. Draft a short sequence with distinct angles.
3. Check tone, timing, and proof use.
4. Return a ready-to-send sequence.
## Output contract
- Stage and goal
- Message sequence
- Timing notes
- Proof or CTA angles
- Deal-moving artifact: account brief, sequence, demo flow, proposal outline, or pipeline review.
- Stage risk, missing proof, and the strongest next-step recommendation.

## Failure modes to avoid
- 'Just checking in' follow-ups â€” add value or don't send.
- Same angle repeated in every touch â€” each must add something new.
- No break-up email â€” endless follow-up to a disengaged prospect is spam.
- Content mismatch â€” sending case studies to someone who needs a technical demo.
- No exit conditions â€” converted prospects still getting follow-up.

## Handoff cues
- Follow-up sequence: touch plan, content per touch, timing, exit conditions.
- Personalization points based on discovery findings.
- Success metric and tracking plan.

## Example invocation
- Slash: `/sales_followup_sequence <task>`
- Natural language: "Use sales Follow-up Sequence to write a short follow-up sequence that moves a deal forward without sounding automated."
- Example: "Help move this deal forward with better qualification, proof, and next steps."
- Example: "Review the pipeline or account and tell me what is real, risky, or stuck."
- Often paired with: `sales_account_research`, `sales_discovery_call_plan`, `sales_pipeline_review`

## Quality bar
- Good follow-up respects attention while keeping momentum alive.
- Every outreach starts with the prospect's context, not your product pitch.
- Objection handling uses proof and reframing, not pressure.
- The funnel has measurable conversion rates at each stage.
- Follow-up cadence is defined and adhered to.
## Related workflows
- Sales flow: `sales_account_research` â†’ `sales_discovery_call_plan` â†’ `sales_demo_flow` â†’ `sales_mutual_action_plan`

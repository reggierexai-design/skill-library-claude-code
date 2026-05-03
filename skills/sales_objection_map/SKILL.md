---
name: sales_objection_map
description: "Turn recurring objections into clearer responses, proof paths, and qualification cues."
user-invocable: true
---

## Purpose
- Turn recurring objections into clearer responses, proof paths, and qualification cues.
- This is a **sales specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when deals stall on price, trust, timing, integration, or change-management concerns.

## Avoid when
- Do not memorize rebuttals without understanding the underlying concern.

## Inputs to gather
- Top objections from discovery calls and lost deals.
- Root causes: what underlies each objection (price, trust, timing, fit)?
- Proof inventory: what evidence addresses each root cause?
- Sales team input: what objections come up most frequently?

## Operating rules
- An objection is information, not resistance theater.
- Answer with proof and fit, not pressure.
- Know when an objection is a real disqualifier.
- Objections are buying signals in disguise. If they're objecting, they're engaged. Silence is the real enemy.
- Address the root cause, not the surface objection. 'Too expensive' usually means 'I don't see enough value.'
- Every objection needs three things: acknowledge, reframe, prove. Skip any step and the objection recurs.
- Track which objections kill deals vs which are just noise. Focus on the deal-killers.

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
1. List the common objections and context.
2. Name the likely root concern behind each one.
3. Write proof-backed responses and follow-up questions.
4. Return an objection map with disqualifiers.
## Output contract
- Objection list
- Root concerns
- Responses and proof
- Disqualifiers
- Deal-moving artifact: account brief, sequence, demo flow, proposal outline, or pipeline review.
- Stage risk, missing proof, and the strongest next-step recommendation.

## Failure modes to avoid
- Treating the surface objection as the real objection â€” 'too expensive' is rarely about price.
- Arguing instead of acknowledging â€” 'actually, our price is competitive' feels combative.
- Generic proof that doesn't address the specific concern.
- Treating all objections equally â€” focus on deal-killers, not noise.
- Never updating the map â€” new product capabilities change the objection landscape.

## Handoff cues
- Objection map: objections, root causes, responses, proof, escalation paths.
- Priority objections by frequency and deal impact.
- Integration with FAQ and sales deck.

## Example invocation
- Slash: `/sales_objection_map <task>`
- Natural language: "Use sales Objection Map to turn recurring objections into clearer responses, proof paths, and qualification cues."
- Example: "Help move this deal forward with better qualification, proof, and next steps."
- Example: "Review the pipeline or account and tell me what is real, risky, or stuck."
- Often paired with: `sales_account_research`, `sales_discovery_call_plan`, `sales_pipeline_review`

## Quality bar
- A useful objection map improves honesty and close quality at the same time.
- Every outreach starts with the prospect's context, not your product pitch.
- Objection handling uses proof and reframing, not pressure.
- The funnel has measurable conversion rates at each stage.
- Follow-up cadence is defined and adhered to.
## Related workflows
- Sales flow: `sales_account_research` â†’ `sales_discovery_call_plan` â†’ `sales_demo_flow` â†’ `sales_mutual_action_plan`

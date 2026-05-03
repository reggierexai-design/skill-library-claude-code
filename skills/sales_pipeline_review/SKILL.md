---
name: sales_pipeline_review
description: "Review a pipeline for deal quality, bottlenecks, forecast risk, and next actions."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udcc9"}}
---

## Purpose
- Review a pipeline for deal quality, bottlenecks, forecast risk, and next actions.
- This is a **sales specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a team needs a clearer read on pipeline health and where deals are really stuck.

## Avoid when
- Do not treat stage counts as pipeline truth.

## Inputs to gather
- Current pipeline: deals by stage, value, and expected close dates.
- Historical conversion rates: what % of deals move from each stage?
- At-risk deals: any deals with stalled momentum or missed milestones?
- Capacity: how many deals can the team actively manage?
- Forecast accuracy: how accurate have recent forecasts been?

## Operating rules
- A pipeline review should challenge assumptions, not just total them.
- Look for aging, weak next steps, and false optimism.
- Separate activity from movement.
- Review the pipeline for momentum, not just volume. A fat pipeline with no movement is a graveyard, not a forecast.
- Flag at-risk deals early. A deal that's been in 'proposal' for 60 days is not a proposal deal â€” it's a stalled deal.
- Base forecasts on evidence, not optimism. If close probability is 75%, what specific evidence supports that number?
- Conversion rates are more useful than pipeline value. $1M pipeline with 5% conversion is worth less than $200K with 30%.

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
1. Define the review horizon and goals.
2. Inspect deal clusters, age, and next-step quality.
3. Flag forecast risks and bottlenecks.
4. Return a concise pipeline review with actions.
## Output contract
- Pipeline health summary
- Bottlenecks
- Forecast risks
- Next actions
- Deal-moving artifact: account brief, sequence, demo flow, proposal outline, or pipeline review.
- Stage risk, missing proof, and the strongest next-step recommendation.

## Failure modes to avoid
- Volume without momentum â€” a fat pipeline with no movement is a graveyard.
- Optimistic close probabilities not backed by evidence.
- Ignoring deal age â€” a deal in 'proposal' for 60 days is stalled, not progressing.
- No action items â€” reviewing without deciding what to do next.
- Confusing pipeline value with forecast value.

## Handoff cues
- Pipeline review: deal stages, velocity, blockers, forecast, action items.
- At-risk deals with recommended interventions.
- Pipeline health metrics and trends.

## Example invocation
- Slash: `/sales_pipeline_review <task>`
- Natural language: "Use sales Pipeline Review to review a pipeline for deal quality, bottlenecks, forecast risk, and next actions."
- Example: "Help move this deal forward with better qualification, proof, and next steps."
- Example: "Review the pipeline or account and tell me what is real, risky, or stuck."
- Often paired with: `sales_account_research`, `sales_discovery_call_plan`

## Quality bar
- Every deal has evidence-based close probability.
- At-risk deals flagged with intervention actions.
- Pipeline momentum tracked (deals moved forward in last 2 weeks).
- Forecast based on evidence, not optimism.
- Every outreach starts with the prospect's context, not your product pitch.
- Objection handling uses proof and reframing, not pressure.
- The funnel has measurable conversion rates at each stage.
- Follow-up cadence is defined and adhered to.
## Related workflows
- Sales flow: `sales_account_research` â†’ `sales_discovery_call_plan` â†’ `sales_demo_flow` â†’ `sales_mutual_action_plan`

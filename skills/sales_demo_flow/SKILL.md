---
name: sales_demo_flow
description: "Shape a demo around the buyer problem, proof points, and next commitment instead of a product tour."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udda5\ufe0f"}}
---

## Purpose
- Shape a demo around the buyer problem, proof points, and next commitment instead of a product tour.
- This is a **sales specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use before demonstrating a product to prospects, partners, or internal champions.

## Avoid when
- Do not let the demo become an exhaustive feature walk-through.

## Inputs to gather
- Buyer persona: technical, business, or executive?
- Their pain point: what problem are they trying to solve?
- Proof points: what results can you show that match their context?
- Known objections: what are they skeptical about?
- Time available: 15 min, 30 min, or 60 min?

## Operating rules
- Lead with the buyer problem and the payoff.
- Show the smallest set of proof points that matter.
- Land on a concrete next commitment.
- Demo the outcome, not the features. Show them getting what they want, not you showing what the product does.
- Customize every demo. A generic demo is a sales pitch; a customized demo is a consultation.
- One demo, one story. Show the single most relevant workflow, not every feature.
- End with a clear next step. 'Any questions?' is not a close. 'Shall we discuss pilot timing?' is.

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
1. Define the audience, goal, and likely concerns.
2. Sequence the narrative, proof points, and transitions.
3. Plan the close and next step ask.
4. Return a demo flow with talking notes.
## Output contract
- Audience and goal
- Demo sequence
- Proof points
- Close and next step
- Deal-moving artifact: account brief, sequence, demo flow, proposal outline, or pipeline review.
- Stage risk, missing proof, and the strongest next-step recommendation.

## Failure modes to avoid
- Feature tour â€” showing everything, solving nothing.
- Generic demo â€” same flow for every buyer regardless of context.
- No problem setup â€” jumping to the solution before establishing the pain.
- Ending with 'any questions?' instead of a clear next step.
- Running over time â€” respect the buyer's schedule.

## Handoff cues
- Demo flow: objectives, story arc, key moments, objection handling, CTA.
- Customization points for different buyer personas.
- Fallback plan if the demo encounters issues.

## Example invocation
- Slash: `/sales_demo_flow <task>`
- Natural language: "Use sales Demo Flow to shape a demo around the buyer problem, proof points, and next commitment instead of a product tour."
- Example: "Help move this deal forward with better qualification, proof, and next steps."
- Example: "Review the pipeline or account and tell me what is real, risky, or stuck."
- Often paired with: `sales_account_research`, `sales_discovery_call_plan`, `sales_pipeline_review`

## Quality bar
- Demo shows one relevant outcome for the specific buyer.
- Demo data and scenario match the buyer's context.
- Problem setup before solution.
- Clear next step proposed at the end.
- Demo fits within the allotted time.
- Every outreach starts with the prospect's context, not your product pitch.
- Objection handling uses proof and reframing, not pressure.
- The funnel has measurable conversion rates at each stage.
- Follow-up cadence is defined and adhered to.
## Related workflows
- Sales flow: `sales_account_research` â†’ `sales_discovery_call_plan` â†’ `sales_demo_flow` â†’ `sales_mutual_action_plan`

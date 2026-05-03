---
name: sales_proposal_outline
description: "Outline a proposal around goals, scope, proof, pricing, and mutual next steps."
user-invocable: true
---

## Purpose
- Outline a proposal around goals, scope, proof, pricing, and mutual next steps.
- This is a **sales specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when turning a conversation into a written proposal or commercial summary.

## Avoid when
- Do not send a proposal before the buyer goals and scope are understood.

## Inputs to gather
- Discovery findings: what's the prospect's problem, desired outcome, and timeline?
- Solution fit: how does your product specifically address their needs?
- Pricing: what's the investment and what's included?
- Decision criteria: how will they evaluate the proposal?
- Competitive context: what alternatives are they considering?

## Operating rules
- Proposals should reflect the buyer problem, not just your offer.
- Make assumptions, scope, and next steps explicit.
- Reduce room for silent misunderstanding.
- Lead with their problem, not your product. The first page should make the prospect feel understood, not sold to.
- Tie every feature to a specific discovery finding. If you can't trace a feature back to something the prospect said, it doesn't belong in the proposal.
- Make the ROI explicit. The prospect should be able to calculate the return without help.
- Include a mutual action plan in the proposal. What happens after they say yes?

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
1. Define the buyer goal and proposed scope.
2. Outline the proof, pricing, and assumptions.
3. Write the acceptance path and next steps.
4. Return a proposal outline or draft structure.
## Output contract
- Goal and context
- Scope and assumptions
- Proof and pricing
- Next steps
- Deal-moving artifact: account brief, sequence, demo flow, proposal outline, or pipeline review.
- Stage risk, missing proof, and the strongest next-step recommendation.

## Failure modes to avoid
- Leading with the product instead of the prospect's problem.
- Feature lists not tied to specific discovery findings.
- No ROI calculation â€” the prospect has to figure out the value themselves.
- Missing the 'what happens next' after signing.
- No deadline or urgency â€” the proposal drifts without a close date.

## Handoff cues
- Proposal outline: executive summary, problem statement, solution, pricing, timeline, terms.
- Differentiation points highlighted.
- Risk mitigation and success criteria included.

## Example invocation
- Slash: `/sales_proposal_outline <task>`
- Natural language: "Use sales Proposal Outline to outline a proposal around goals, scope, proof, pricing, and mutual next steps."
- Example: "Help move this deal forward with better qualification, proof, and next steps."
- Example: "Review the pipeline or account and tell me what is real, risky, or stuck."
- Often paired with: `sales_account_research`, `sales_discovery_call_plan`, `sales_pipeline_review`

## Quality bar
- Opens with the prospect's problem in their language.
- Every capability tied to a discovery finding.
- ROI calculated with explicit assumptions.
- Mutual action plan included.
- Clear next step and deadline.
- Every outreach starts with the prospect's context, not your product pitch.
- Objection handling uses proof and reframing, not pressure.
- The funnel has measurable conversion rates at each stage.
- Follow-up cadence is defined and adhered to.
## Related workflows
- Sales flow: `sales_account_research` â†’ `sales_discovery_call_plan` â†’ `sales_demo_flow` â†’ `sales_mutual_action_plan`

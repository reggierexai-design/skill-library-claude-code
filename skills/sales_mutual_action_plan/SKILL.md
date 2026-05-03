---
name: sales_mutual_action_plan
description: "Create a buyer-facing action plan with milestones, dependencies, and next commitments."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83e\udd1d"}}
---

## Purpose
- Create a buyer-facing action plan with milestones, dependencies, and next commitments.
- This is a **sales specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a deal needs structure across stakeholders, procurement, security, or rollout steps.

## Avoid when
- Do not use for very early discovery where no real buying process exists yet.

## Inputs to gather
- Deal stage: where are you in the sales process?
- Buyer commitments: what has the buyer agreed to do?
- Seller commitments: what have you agreed to deliver?
- Decision criteria: how will the buyer evaluate and decide?
- Timeline: target close date and key milestones.

## Operating rules
- Mutual means mutual. If the buyer has no commitments, it's your plan, not ours.
- Every milestone has an owner, a deadline, and a verification method.
- The plan should survive the first missed milestone. Build in buffer and escalation triggers.
- Share the plan visibly. A MAP that lives only in your CRM is a tracking exercise; one the buyer can see is a commitment device.

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
1. Define the target close date and work backward.
2. List milestones: technical evaluation, security review, legal, procurement, executive sign-off.
3. Assign owners and deadlines for each milestone (buyer and seller).
4. Define verification: how do we know each milestone is complete?
5. Build in buffer: 20% more time than expected per milestone.
6. Share the plan with the buyer and get their explicit agreement.

## Output contract
- Deal-moving artifact: account brief, sequence, demo flow, proposal outline, or pipeline review.
- Stage risk, missing proof, and the strongest next-step recommendation.

## Failure modes to avoid
- One-sided plans â€” no buyer commitments means no mutual accountability.
- Milestones without owners or deadlines.
- No buffer â€” the first slip cascades through the entire plan.
- Hidden plans â€” a MAP the buyer can't see is just internal tracking.
- No escalation triggers â€” when milestones slip, nobody notices until the deal dies.

## Handoff cues
- Mutual action plan: milestones, owner, deadline, verification for each step.
- Buyer and seller commitments documented.
- Escalation path if milestones slip.

## Example invocation
- Slash: `/sales_mutual_action_plan <task>`
- Natural language: "Use sales Mutual Action Plan to create a buyer-facing action plan with milestones, dependencies, and next commitments."
- Example: "Help move this deal forward with better qualification, proof, and next steps."
- Example: "Review the pipeline or account and tell me what is real, risky, or stuck."
- Often paired with: `sales_account_research`, `sales_discovery_call_plan`, `sales_pipeline_review`

## Quality bar
## Related workflows
- Sales flow: `sales_account_research` â†’ `sales_discovery_call_plan` â†’ `sales_demo_flow` â†’ `sales_mutual_action_plan`
- Every outreach starts with the prospect's context, not your product pitch.
- Objection handling uses proof and reframing, not pressure.
- The funnel has measurable conversion rates at each stage.
- Follow-up cadence is defined and adhered to.
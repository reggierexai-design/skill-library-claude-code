---
name: sales_account_plan
description: "Build an account plan covering stakeholders, pain, timing, deal strategy, and expansion paths."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83c\udfe2"}}
---

## Purpose
- Build an account plan covering stakeholders, pain, timing, deal strategy, and expansion paths.
- This is a **sales specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when working a complex account with multiple stakeholders or a long decision path.

## Avoid when
- Do not use for tiny transactional deals with no strategic account motion.

## Inputs to gather
- Account profile: company, industry, size, tech stack, initiatives.
- Stakeholder map: decision makers, influencers, champions, blockers.
- Current relationship: existing customer, prospect, or partner?
- Competitive presence: are competitors already in the account?
- Revenue potential: deal size, expansion opportunities, timeline.

## Operating rules
- Multi-thread every account. If your only contact leaves, you start from zero.
- Map the buying committee, not just the decision maker. Influencers and blockers matter as much as the signer.
- Anchor the plan in the account's objectives, not your product's features.
- Review and update the plan quarterly. Stale account plans are fiction.

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
1. Research the account: company context, initiatives, tech stack.
2. Map the buying committee: decision maker, influencers, champion, blockers.
3. Identify the account's objectives and how your solution aligns.
4. Define engagement strategy: who to meet, what to prove, what to ask.
5. Set milestones: first meeting, demo, proposal, close.
6. Review and update quarterly.

## Output contract
- Deal-moving artifact: account brief, sequence, demo flow, proposal outline, or pipeline review.
- Stage risk, missing proof, and the strongest next-step recommendation.

## Failure modes to avoid
- Single-threaded accounts â€” one contact leaving kills the deal.
- Feature-selling instead of objective-aligning.
- Ignoring the competitive presence.
- Stale account plans not updated when circumstances change.
- No milestone timeline â€” deals drift without urgency.

## Handoff cues
- Account plan: objectives, stakeholders, engagement strategy, timeline, success criteria.
- Key contacts and their priorities.
- Competitive positioning for this account.

## Example invocation
- Slash: `/sales_account_plan <task>`
- Natural language: "Use sales Account Plan to build an account plan covering stakeholders, pain, timing, deal strategy, and expansion paths."
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
---
name: sales_account_research
description: "Summarize an account in terms of likely pain, stakeholders, timing, and approach angles."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83c\udfe2","requires":{"config":["browser.enabled"]}}}
---

## Purpose
- Summarize an account in terms of likely pain, stakeholders, timing, and approach angles.
- This is a **sales specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use before outreach, a demo, or account planning for a named company or organization.

## Avoid when
- Do not confuse random facts with buying relevance.

## Inputs to gather
- Company name and industry.
- Target contacts: who should we be talking to?
- Known initiatives or pain points from public sources.
- Competitive landscape: who else serves this account?
- Timing triggers: funding, leadership changes, product launches.

## Operating rules
- Research for relevance, not trivia.
- Focus on pain, change, fit, and stakeholders.
- Separate facts from inference clearly.
- Research should inform the outreach, not replace it. 15 minutes of focused research beats 2 hours of exhaustive research if it leads to a relevant first message.
- Look for trigger events: funding rounds, leadership changes, product launches, regulatory shifts. These create urgency and relevance.
- Cross-reference multiple sources. LinkedIn says one thing; the company blog says another; job postings reveal what they're building.
- End research with a specific outreach hypothesis: what angle, for whom, based on what evidence.

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
1. Define the target account and motion.
2. Collect facts relevant to likely pain and timing.
3. Infer potential stakeholders and approach angles.
4. Return a compact account brief with cautions.
## Output contract
- Account context
- Likely pain and triggers
- Possible stakeholders
- Approach angles and cautions
- Deal-moving artifact: account brief, sequence, demo flow, proposal outline, or pipeline review.
- Stage risk, missing proof, and the strongest next-step recommendation.

## Failure modes to avoid
- Researching everything without forming an outreach hypothesis.
- Missing trigger events that create urgency.
- Relying on a single source â€” cross-reference for accuracy.
- Researching the company but not the specific contacts.
- No competitive context â€” you're selling against alternatives you haven't identified.

## Handoff cues
- Account research: company profile, tech stack, initiatives, pain points, key contacts.
- Relevance assessment: how your solution fits their needs.
- Recommended outreach angle and timing.

## Example invocation
- Slash: `/sales_account_research <task>`
- Natural language: "Use sales Account Research to summarize an account in terms of likely pain, stakeholders, timing, and approach angles."
- Example: "Help move this deal forward with better qualification, proof, and next steps."
- Example: "Review the pipeline or account and tell me what is real, risky, or stuck."
- Often paired with: `sales_discovery_call_plan`, `sales_pipeline_review`

## Quality bar
- Good account research sharpens the conversation instead of bloating it.
- Every outreach starts with the prospect's context, not your product pitch.
- Objection handling uses proof and reframing, not pressure.
- The funnel has measurable conversion rates at each stage.
- Follow-up cadence is defined and adhered to.
## Related workflows
- Sales flow: `sales_account_research` â†’ `sales_discovery_call_plan` â†’ `sales_demo_flow` â†’ `sales_mutual_action_plan`

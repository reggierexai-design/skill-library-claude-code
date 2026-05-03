---
name: comm_feedback_system
description: "Build a system to collect, organize, and act on community feedback and feature requests."
user-invocable: true
---

# Feedback System

## Purpose
Build a system to collect, organize, and act on community feedback and feature requests. Feedback is the lifeblood of a community-driven product — but unorganized feedback is just noise. A good system turns scattered suggestions into actionable product direction.

## Use when
Use when your community is giving feedback in too many places to track. Use when you're not sure what to build next. Use when community members feel unheard. Use when launching a community alongside a product.

## Avoid when
Don't use when you already have a product feedback system that's working. Don't use as a substitute for making decisions — collecting feedback is easy; acting on it is hard.

## Inputs to gather
- Current feedback channels: where does feedback come from? Discord, email, social, support tickets, in-app?
- Feedback volume: how much feedback do you get per week?
- Existing triage process: how is feedback currently handled?
- Product roadmap: what's already planned?
- Community priorities: what do members ask for most?

## Operating rules
- One source of truth for all feedback. Multiple channels are fine, but they should all feed into one organized system.
- Acknowledge every piece of feedback. Not "we'll build it" — just "we heard you." Silence feels like ignoring.
- Categorize by theme, not by channel. Feature requests, bugs, experience issues, praise — each type gets different treatment.
- Close the loop. When you build something the community requested, tell them. "You asked, we built it" is the most powerful community message.
- Don't promise what you won't deliver. "We'll consider it" is honest. "It's on the roadmap" when it's not is a trust breaker.

## Claude Code tool pattern
- Use `prod_feedback_synthesis` for synthesizing feedback into product direction.
- Use `prod_feature_priority` for prioritizing feature requests.
- Use `ops_support_triage` for urgent feedback that needs immediate response.

## Expanded workflow
1. **Map all feedback channels.** Where does feedback come from? List every channel.
2. **Choose a central system.** Notion, Canny, GitHub Discussions, Linear — whatever works. One place for everything.
3. **Set up feedback intake.** How does feedback from each channel get into the central system? Automate where possible.
4. **Create a categorization system.** Feature request, bug, experience issue, praise, question. Tags for product area.
5. **Establish a triage cadence.** Weekly review of new feedback. Categorize, prioritize, respond.
6. **Build a public-facing view.** Let the community see what's been requested and what's planned. Transparency builds trust.
7. **Close the loop regularly.** Monthly: "You asked for X. Here's what we did." Even for things you decided not to build, explain why.

## Output contract
- Feedback channel map with intake process per channel
- Central feedback system with categorization
- Triage cadence and responsible party
- Public-facing feedback view (if applicable)
- Loop-closing communication schedule

## Failure modes to avoid
- Feedback scattered across channels with no central system — you can't act on what you can't see.
- No acknowledgment — silence feels like ignoring, even if you're tracking it internally.
- Promising features you won't build — "it's on the roadmap" when it's not destroys trust.
- No triage cadence — feedback piles up until it's overwhelming.
- Not closing the loop — building what was asked for without telling the askers.

## Handoff cues
- Feedback system status: channels mapped, central system set up, triage running.
- Top 5 feature requests by community demand.
- Last loop-closing communication date.
- Next triage date.

## Example invocation
- Slash: `/comm_feedback_system <task>`
- Natural language: "Use comm_feedback_system to build a system to collect, organize, and act on community feedback and feature requests."

## Quality bar
All feedback channels feed into one central system. Every piece of feedback is acknowledged within 48 hours. Feedback is categorized and triaged weekly. The community can see what's been requested. Loop-closing happens monthly.

## Related workflows
- **Feedback to product:** `comm_feedback_system` → `prod_feedback_synthesis` → `prod_feature_priority` → build
- **Community health:** `comm_feedback_system` → `comm_retention_audit` → `comm_conflict_resolution`
- **Voice of customer:** `comm_feedback_system` → `att_message_house` → `att_proof_mining`

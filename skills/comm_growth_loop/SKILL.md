---
name: comm_growth_loop
description: "Design a viral loop where community members naturally invite others, growing the community organically."
user-invocable: true
---

# Growth Loop

## Purpose
Design a viral loop where community members naturally invite others, growing the community organically. The best communities grow because members want to share them, not because the founder runs ads. A growth loop makes sharing automatic and rewarding.

## Use when
Use when your community has product-market fit but needs to grow. Use when organic growth has plateaued. Use when you want to reduce dependency on paid acquisition.

## Avoid when
Don't use when the community isn't worth sharing yet — fix the value before amplifying it. Don't use when growth would break the community culture — quality over quantity.

## Inputs to gather
- Current growth rate: how many new members per week and where do they come from?
- Current referral behavior: do members already invite others? How?
- Community value proposition: why would someone invite a friend?
- Platform capabilities: invite links, referral tracking, guest access?
- Member motivations: what do members get from the community? What would motivate them to share?

## Operating rules
- The community must be worth sharing before you build a growth loop. If members don't naturally mention the community to friends, the loop won't work.
- Make sharing easy and natural. One-click invite links, shareable content, and frictionless onboarding.
- Incentivize the inviter, not just the invitee. Both should benefit from the connection.
- Don't incentivize with cash unless you can sustain it. Status, access, and recognition are cheaper and more sustainable.
- Monitor quality as you grow. Fast growth with declining quality is worse than slow growth with maintained quality.

## Claude Code tool pattern
- Use `comm_onboarding_flow` to ensure new members from the growth loop are activated.
- Use `comm_retention_audit` to monitor quality as the community grows.
- Use `prod_activation_funnel` for growth loop conversion tracking.

## Expanded workflow
1. **Audit current referral behavior.** Do members already invite others? What prompts them? What's the natural sharing moment?
2. **Identify shareable moments.** When does a member experience something worth sharing? A great answer, a breakthrough, a connection made?
3. **Make sharing frictionless.** One-click invite links, shareable content snippets, easy onboarding for invitees.
4. **Design the incentive.** What does the inviter get? Status, access, recognition? What does the invitee get? Warm welcome, quick value?
5. **Build the loop mechanics.** Invite → onboarding → value realization → natural sharing moment → invite.
6. **Measure the viral coefficient.** How many new members does each existing member bring? Target: >1.0 for organic growth.
7. **Monitor quality metrics.** As growth accelerates, are engagement and retention holding? If not, slow down and fix quality.

## Output contract
- Growth loop design: shareable moments, sharing mechanics, incentives
- Viral coefficient measurement plan
- Quality monitoring metrics alongside growth metrics
- Onboarding integration: how new members from the loop get activated
- Growth ceiling analysis: what would break if growth 10x'd?

## Failure modes to avoid
- Building a growth loop before the community is worth sharing.
- Cash incentives you can't sustain — when the money stops, the growth stops.
- Growing too fast without quality controls — a big empty community is worse than a small active one.
- Not measuring the viral coefficient — you're guessing, not optimizing.
- Ignoring the onboarding gap — new members who aren't activated leave immediately.

## Handoff cues
- Growth loop design and mechanics.
- Viral coefficient baseline and target.
- Quality metrics to watch as growth accelerates.
- Onboarding flow for growth loop members.

## Example invocation
- Slash: `/comm_growth_loop <task>`
- Natural language: "Use comm_growth_loop to design a viral loop where community members naturally invite others, growing the community organically."

## Quality bar
The community is worth sharing before the growth loop is built. Sharing is frictionless — one click. The inviter gets value from sharing, not just the invitee. Quality metrics are monitored alongside growth metrics. The viral coefficient is measured and tracked.

## Related workflows
- **Community growth system:** `comm_growth_loop` → `comm_onboarding_flow` → `comm_ritual_design` → `comm_retention_audit`
- **Product-community growth:** `prod_activation_funnel` → `comm_growth_loop` → unified growth engine
- **Quality-controlled growth:** `comm_growth_loop` → `comm_retention_audit` → `comm_feedback_system`

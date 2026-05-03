---
name: comm_retention_audit
description: "Audit why community members leave and design interventions to improve retention."
user-invocable: true
metadata: {"openclaw":{"emoji":"📌"}}
---

# Retention Audit

## Purpose
Audit why community members leave and design interventions to improve retention. A community that loses members faster than it gains them is shrinking, regardless of how many new members join. Retention is the real growth metric.

## Use when
Use when your community's active member count is declining despite new joins. Use when you want to understand why people go silent. Use quarterly as a community health check.

## Avoid when
Don't use when the community is small and growing naturally — don't over-optimize early. Don't use as a substitute for talking to members directly — data tells you what, people tell you why.

## Inputs to gather
- Membership data: joins, leaves, and active members per month.
- Engagement data: posts, reactions, event attendance per member per month.
- Churn interviews: exit surveys or conversations with departing members.
- Cohort analysis: when do members typically go silent? Week 1? Month 3?
- Competitor communities: where do departing members go?

## Operating rules
- Measure retention by cohort, not aggregate. When did each group join and how many are still active?
- The first 7 days determine long-term retention. If someone doesn't engage in week 1, they won't be there in month 3.
- Churn has leading indicators. Declining post frequency, fewer event attendances, shorter messages — these predict departure.
- Ask departing members directly. Exit surveys, personal messages, or quick calls. The data won't tell you the emotional reasons.
- Not all churn is bad. Members who got what they needed and moved on are success stories, not failures.

## Claude Code tool pattern
- Use `comm_onboarding_flow` to fix retention problems at the source.
- Use `comm_ritual_design` to create reasons for members to return.
- Use `comm_feedback_system` to surface retention issues before they become departures.

## Expanded workflow
1. **Calculate cohort retention curves.** Month 1, month 2, month 3 retention for each join cohort. Where's the cliff?
2. **Identify the typical churn point.** When do most members go silent? This is where to focus intervention.
3. **Interview departed or silent members.** Why did they stop engaging? What would have kept them?
4. **Analyze leading indicators.** What behavior predicts departure? Declining activity? No connections made? No ritual participation?
5. **Design interventions at each churn point.** Week 1: better onboarding. Month 1: first contribution recognition. Month 3: deeper engagement opportunity.
6. **Implement and measure.** Run the intervention for a cohort. Compare retention to the previous cohort.
7. **Iterate.** Retention is an ongoing optimization, not a one-time fix.

## Output contract
- Cohort retention curves with churn points identified
- Departing member interview summaries
- Leading indicators of churn
- Interventions designed for each churn point
- Measurement plan for intervention effectiveness

## Failure modes to avoid
- Measuring aggregate retention instead of cohort retention — the average hides the truth.
- Not talking to departing members — data tells you what, interviews tell you why.
- Fixing churn at the wrong point — if the cliff is in week 1, month 3 interventions won't help.
- Treating all churn as bad — some members leave because they got what they needed.
- One intervention and done — retention requires ongoing optimization.

## Handoff cues
- Cohort retention data with key churn points.
- Top 3 reasons members leave.
- Interventions designed and their target churn points.
- Next measurement date for intervention effectiveness.

## Example invocation
- Slash: `/comm_retention_audit <task>`
- Natural language: "Use comm_retention_audit to audit why community members leave and design interventions to improve retention."

## Quality bar
Retention is measured by cohort, not just aggregate. The primary churn point is identified. At least 5 departing members have been interviewed. Interventions target the actual churn points, not assumptions. Intervention effectiveness is measured.

## Related workflows
- **Retention improvement:** `comm_retention_audit` → `comm_onboarding_flow` (fix early churn) → `comm_ritual_design` (create return reasons)
- **Community health check:** `comm_retention_audit` → `comm_feedback_system` → `comm_conflict_resolution`
- **Growth-quality balance:** `comm_growth_loop` → `comm_retention_audit` → quality gates

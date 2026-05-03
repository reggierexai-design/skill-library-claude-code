---
name: finance_burn_rate
description: "Track cash burn, calculate runway, and identify levers to extend it."
user-invocable: true
metadata: {"openclaw":{"emoji":"🔥"}}
---

# Burn Rate

## Purpose
Track cash burn, calculate runway, and identify levers to extend it. Runway is the only number that matters when you're pre-profitability — everything else is noise until you know how long you have. A founder who doesn't know their runway is flying blind.

## Use when
Use monthly as a standard financial check. Use when considering any significant spending decision. Use when runway drops below 12 months.

## Avoid when
Don't use optimistic revenue projections to extend runway calculations. Don't confuse revenue with cash — timing matters. Don't use this to justify unsustainable spending.

## Inputs to gather
- Current cash balance: how much money do you have right now?
- Monthly burn: how much cash are you spending per month?
- Revenue: how much cash is coming in per month?
- Net burn: monthly burn minus monthly revenue.
- Fixed vs variable costs: which costs are committed vs discretionary?

## Operating rules
- Calculate runway conservatively. Use net burn, not gross burn. Assume revenue stays flat — that's your real runway.
- Separate fixed from variable costs. Fixed costs define your minimum burn; variable costs are your levers.
- Plan for 18+ months of runway. Below 12 months, you're in emergency mode. Below 6 months, you're in survival mode.
- Revenue projections don't count toward runway until they're in the bank. Booked but unpaid is not cash.
- Review monthly. Burn rate changes — sometimes quickly. A quarterly review isn't frequent enough.

## Claude Code tool pattern
- Use `finance_revenue_forecast` for revenue projections.
- Use `finance_unit_economics` to verify unit economics support profitability.
- Use `ops_kpi_review` to connect financial metrics to operational ones.

## Expanded workflow
1. **Calculate current cash balance.** Actual money in the bank, not projected. Include only liquid funds.
2. **Calculate monthly net burn.** Total spending minus total revenue. This is your actual cash consumption rate.
3. **Calculate runway.** Cash balance / net burn = months remaining. Round down.
4. **Separate fixed from variable costs.** What can you cut if needed? Hosting? Tools? Contractors? Marketing?
5. **Identify burn reduction levers.** Rank by impact and reversibility. Cut reversible low-impact first.
6. **Set runway thresholds.** 18+ months: normal operations. 12-18: cautious, reduce variable spend. <12: emergency, cut to minimum viable.
7. **Create a burn dashboard.** Monthly update: cash, burn, runway, trend. One page, always current.

## Output contract
- Current cash balance and net burn rate
- Runway calculation in months
- Fixed vs variable cost breakdown
- Burn reduction levers ranked by impact
- Runway thresholds and action triggers

## Failure modes to avoid
- Using gross burn instead of net burn — revenue offsets some spending.
- Counting projected revenue as cash — it doesn't count until it's in the bank.
- Not separating fixed from variable costs — you need to know what you can cut.
- Only reviewing quarterly — burn rate can change fast enough to surprise you.
- No emergency plan for when runway drops below 12 months.

## Handoff cues
- Cash balance, net burn, and runway in months.
- Burn reduction levers if runway drops below threshold.
- Next monthly review date.

## Example invocation
- Slash: `/finance_burn_rate <task>`
- Natural language: "Use finance_burn_rate to track cash burn, calculate runway, and identify levers to extend it."

## Quality bar
Runway is calculated from actual cash and net burn. Fixed and variable costs are separated. Burn reduction levers are identified. Runway thresholds are set with action triggers. Review happens monthly.

## Related workflows
- **Financial health:** `finance_burn_rate` → `finance_unit_economics` → `finance_revenue_forecast` → decision
- **Emergency planning:** `finance_burn_rate` → `solo_scope_guard` (cut scope) → `ops_kpi_review`
- **Runway management:** `finance_burn_rate` → `finance_pricing_model` (increase revenue) → `finance_revenue_forecast`

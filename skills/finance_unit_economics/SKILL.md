---
name: finance_unit_economics
description: "Verify that each customer relationship is financially sustainable on a per-unit basis."
user-invocable: true
---

# Unit Economics

## Purpose
Verify that each customer relationship is financially sustainable. If it costs more to acquire and serve a customer than they pay you over their lifetime, growth just accelerates failure. Unit economics are the truth teller that cuts through vanity metrics.

## Use when
Use before scaling acquisition spend. Use when evaluating pricing changes. Use quarterly as a health check.

## Avoid when
Don't calculate LTV without including churn. Don't use blended CAC when segment-level data is available. Don't use this as an excuse to delay growth if unit economics are healthy.

## Inputs to gather
- CAC: customer acquisition cost by channel and segment.
- ARPU: average revenue per user per month.
- LTV: lifetime value (ARPU × gross margin × (1/churn rate)).
- Gross margin: revenue minus cost of goods sold.
- Payback period: months to recover CAC from gross margin.

## Operating rules
- LTV/CAC ratio should be at least 3:1. Below that, you're spending too much to acquire customers relative to their value.
- Payback period should be under 12 months. Longer payback periods create cash flow problems even with good LTV/CAC.
- Calculate by segment, not just blended. Some customer segments may have terrible unit economics hidden by better segments.
- Include all costs in CAC: ad spend, sales time, onboarding effort, support ramp-up.
- Churn is the most powerful lever. Reducing churn by 10% can double LTV. Focus on retention before acquisition.

## Claude Code tool pattern
- Use `finance_pricing_model` to verify pricing supports healthy unit economics.
- Use `prod_activation_funnel` for conversion data feeding CAC calculations.
- Use `prod_retention_loop` for retention improvement strategies.

## Expanded workflow
1. **Calculate CAC by channel and segment.** Total acquisition cost / customers acquired. Include all costs.
2. **Calculate ARPU by segment.** Revenue per user per month. Separate by plan if tiers exist.
3. **Calculate LTV.** ARPU × gross margin × (1/churn rate). Show the churn assumption explicitly.
4. **Calculate LTV/CAC ratio.** Target: 3:1 or better. Below 1:1 means you lose money on every customer.
5. **Calculate payback period.** CAC / (ARPU × gross margin). Target: <12 months.
6. **Compare by segment.** Are some segments unprofitable? Which segments subsidize others?
7. **Identify improvement levers.** Reduce CAC (better targeting), increase ARPU (upsell), reduce churn (improve retention), improve margin (reduce costs).

## Output contract
- CAC by channel and segment
- LTV by segment with assumptions
- LTV/CAC ratio per segment
- Payback period per segment
- Improvement levers ranked by impact

## Failure modes to avoid
- Blended unit economics hiding bad segments — average LTV/CAC of 3:1 could be 5:1 on one segment and 1:1 on another.
- Excluding costs from CAC — ad spend + sales time + onboarding + support ramp-up.
- Calculating LTV without churn — infinite LTV isn't real. Zero churn doesn't exist.
- Not calculating by segment — the aggregate hides the truth.
- Ignoring payback period — long payback creates cash flow problems even with good LTV/CAC.

## Handoff cues
- Unit economics by segment: CAC, LTV, LTV/CAC, payback period.
- Problem segments identified with improvement levers.
- Overall LTV/CAC and payback period.
- Next review date.

## Example invocation
- Slash: `/finance_unit_economics <task>`
- Natural language: "Use finance_unit_economics to verify that each customer relationship is financially sustainable on a per-unit basis."

## Quality bar
LTV/CAC is at least 3:1 for the primary segment. Payback period is under 12 months. Unit economics are calculated per segment, not just blended. All costs are included in CAC. Churn is factored into LTV.

## Related workflows
- **Unit economics verification:** `finance_unit_economics` → `finance_pricing_model` → `prod_retention_loop`
- **Acquisition decisions:** `finance_unit_economics` → `prod_activation_funnel` → spend decision
- **Financial health:** `finance_burn_rate` → `finance_unit_economics` → `finance_revenue_forecast`

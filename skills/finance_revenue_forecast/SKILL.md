---
name: finance_revenue_forecast
description: "Build a bottom-up revenue forecast grounded in real conversion and retention data."
user-invocable: true
---

# Revenue Forecast

## Purpose
Build a bottom-up revenue forecast grounded in real conversion and retention data. Forecasts based on vibes and hope are just wishes with spreadsheets. A real forecast lets you make decisions about hiring, spending, and fundraising with confidence instead of anxiety.

## Use when
Use when planning hiring or spending decisions. Use when fundraising. Use quarterly as a reality check against actuals.

## Avoid when
Don't build top-down forecasts ("if we capture 1% of a $10B market..."). Don't forecast without showing your assumptions. Don't treat a forecast as a promise.

## Inputs to gather
- Current MRR and growth rate.
- Conversion funnel data: visitor → signup → paid → retained.
- Churn rate: monthly and by cohort.
- Expansion revenue: upgrades and add-ons per month.
- Customer acquisition cost and payback period.

## Operating rules
- Bottom-up only. Start with real conversion data and build up. Top-down market sizing is for investor decks, not operational planning.
- Show every assumption. Every number in the forecast should be traceable to a data source or an explicitly labeled assumption.
- Plan scenarios: optimistic, expected, conservative. The spread between them shows your uncertainty.
- Update with actuals monthly. A forecast that isn't compared to reality is fiction.
- The most important variable is usually retention. Small changes in churn have outsized effects on long-term revenue.

## Claude Code tool pattern
- Use `finance_unit_economics` to verify that unit economics support the forecast.
- Use `prod_activation_funnel` for top-of-funnel conversion data.
- Use `data_metric_definition` to define forecast metrics consistently.

## Expanded workflow
1. **Gather actual funnel data.** Conversion rates at every stage, by cohort. Real numbers, not estimates.
2. **Set assumptions explicitly.** Growth rate, conversion improvement, churn reduction — each labeled as assumption or data.
3. **Build the base case.** Month-by-month: new users × conversion × ARPU, minus churn, plus expansion.
4. **Build optimistic and conservative scenarios.** What changes? By how much? Be specific about the drivers.
5. **Stress test the forecast.** What if churn doubles? What if conversion halves? When do you run out of money?
6. **Compare to actuals monthly.** Where did the forecast diverge? Why? Update assumptions.
7. **Update assumptions based on actuals.** The forecast is a living document, not a one-time exercise.

## Output contract
- 12-month revenue forecast: optimistic, expected, conservative
- Assumption log: every number with its source or label
- Sensitivity analysis: which variables matter most
- Monthly actuals vs forecast comparison (ongoing)
- Runway calculation under each scenario

## Failure modes to avoid
- Top-down forecasting ("if we capture 1% of the market...") — this is a pitch, not a plan.
- Hidden assumptions — every number should be traceable to a source or an explicit assumption label.
- Ignoring churn — it compounds in the wrong direction and dominates long-term revenue.
- No scenario planning — one forecast means one level of confidence, which is overconfidence.
- Never comparing to actuals — a forecast without a feedback loop is fiction.

## Handoff cues
- 12-month forecast with three scenarios.
- Assumption log with sources.
- Sensitivity analysis showing key variables.
- Runway calculation under each scenario.

## Example invocation
- Slash: `/finance_revenue_forecast <task>`
- Natural language: "Use finance_revenue_forecast to build a bottom-up revenue forecast grounded in real conversion and retention data."

## Quality bar
Forecast is bottom-up from real conversion data. Every assumption is labeled with its source. Three scenarios are modeled: optimistic, expected, conservative. Monthly actuals comparison is planned. Sensitivity analysis identifies the most impactful variables.

## Related workflows
- **Revenue planning:** `finance_revenue_forecast` → `finance_burn_rate` → `finance_unit_economics` → decision
- **Fundraising prep:** `finance_revenue_forecast` → `finance_unit_economics` → pitch deck
- **Operational review:** `finance_revenue_forecast` → actuals comparison → `ops_kpi_review`

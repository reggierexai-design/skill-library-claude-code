---
name: finance_pricing_model
description: "Design a pricing model that aligns revenue with value delivery and supports growth."
user-invocable: true
---

# Pricing Model

## Purpose
Design a pricing model that aligns revenue with value delivery and supports growth. Pricing is the single highest-leverage decision in a startup — a 1% price improvement beats a 1% cost cut every time. Most founders underprice because they're afraid of losing users they can't afford to serve.

## Use when
Use when launching a new product. Use when your current pricing doesn't align with value delivered. Use when expanding to new customer segments. Use when competitors change their pricing.

## Avoid when
Don't price based on cost-plus alone — users pay for value, not your expenses. Don't copy competitor pricing without understanding why they chose it. Don't price before you understand the value you deliver.

## Inputs to gather
- Value delivered: what measurable value does your product create for users?
- Customer segments: who pays the most and why?
- Competitive pricing: what do alternatives cost and what do they include?
- Cost structure: what does it cost to deliver the service per user?
- Willingness to pay: what have users actually paid or said they'd pay?

## Operating rules
- Price based on value, not cost. Cost-plus is safe but leaves money on the table. Value-based pricing captures what users are actually willing to pay.
- Anchor high, discount down. Your listed price sets the reference point. It's easier to discount from a premium price than to raise from a low one.
- Pricing tiers should be based on usage dimensions that align with value. More usage = more value = more revenue.
- Test pricing with real transactions. Survey data about willingness to pay is unreliable. Only real purchase decisions count.
- Include an expansion path. Your lowest tier should have a natural upgrade trigger — more users, more usage, more features.

## Claude Code tool pattern
- Use `prod_feature_priority` to decide what goes in each pricing tier.
- Use `finance_unit_economics` to verify pricing covers unit costs.
- Use `prod_activation_funnel` for conversion rate data at each price point.

## Expanded workflow
1. **Quantify the value you deliver.** Time saved, revenue generated, risk reduced — in dollars. This is your pricing ceiling.
2. **Research competitive pricing.** What do alternatives charge? What do they include? Where are the gaps?
3. **Identify pricing dimensions.** Per user, per usage, per feature, flat rate — what aligns with value delivery?
4. **Design 2-3 pricing tiers.** Entry, standard, premium. Each with clear value boundaries. No more than 4 tiers.
5. **Set anchor prices.** Start higher than you think — you can always discount. You can't easily raise.
6. **Test with real transactions.** Launch pricing, measure conversion, listen to pushback, iterate.
7. **Plan the expansion path.** What triggers an upgrade from each tier? Usage limits? Feature gates? User count?

## Output contract
- Value quantification: what users get in dollar terms
- Pricing tiers: features, price, and value boundaries per tier
- Competitive pricing comparison
- Conversion rate per tier (after launch)
- Expansion path: upgrade triggers between tiers

## Failure modes to avoid
- Pricing based on cost-plus — leaves value on the table and attracts price-sensitive users.
- Copying competitor pricing without understanding their cost structure and target segment.
- Too many tiers — more than 3-4 creates decision paralysis.
- Pricing that doesn't align with value delivery — per-seat pricing for a usage-based product.
- No expansion path — customers hit the top tier with nowhere to grow.

## Handoff cues
- Pricing tiers with features and prices.
- Value quantification per tier.
- Competitive pricing analysis.
- Expansion path with upgrade triggers.

## Example invocation
- Slash: `/finance_pricing_model <task>`
- Natural language: "Use finance_pricing_model to design a pricing model that aligns revenue with value delivery and supports growth."

## Quality bar
Pricing is based on value delivered, not cost-plus. 2-4 tiers with clear value boundaries. Competitive pricing is researched and considered. An expansion path exists between tiers. Pricing has been tested with real transactions.

## Related workflows
- **Pricing design:** `finance_pricing_model` → `prod_feature_priority` → `finance_unit_economics` → launch
- **Value-based pricing:** `prod_feature_priority` → `finance_pricing_model` → `prod_pricing_packaging`
- **Revenue optimization:** `finance_pricing_model` → `finance_revenue_forecast` → `finance_burn_rate`

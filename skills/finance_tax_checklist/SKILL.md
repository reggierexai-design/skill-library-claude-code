---
name: finance_tax_checklist
description: "Prepare tax obligations checklist for a small business or solo founder."
user-invocable: true
---

# Tax Checklist

## Purpose
Prepare tax obligations checklist for a small business or solo founder. Tax surprises are the most expensive surprises because they come with penalties and interest. The IRS doesn't care about your startup's cash flow problems — they want their money on their schedule.

## Use when
Use when starting a business. Use quarterly for estimated tax payments. Use annually before filing deadlines. Use when revenue crosses a new threshold.

## Avoid when
Don't use as a substitute for a CPA — this is a checklist, not tax advice. Don't assume last year's obligations match this year's. Don't skip professional review for complex situations.

## Inputs to gather
- Business entity type: LLC, S-Corp, sole proprietor — determines tax obligations.
- Revenue and expense records: accurate books for the period.
- Estimated tax payments: what's been paid and what's owed?
- Employee vs contractor classifications: affects withholding and 1099 requirements.
- State and local obligations: sales tax, franchise tax, local permits.

## Operating rules
- Set aside 25-30% of revenue for taxes. If you don't, you'll owe it later with penalties and interest.
- Pay estimated taxes quarterly. Waiting until April creates a cash flow crisis and underpayment penalties.
- Track deductible expenses in real-time. Trying to reconstruct expenses at year-end is unreliable and misses deductions.
- Understand your entity's obligations. LLC taxed as S-Corp has different requirements than sole proprietorship.
- Sales tax may apply even if you're digital. Economic nexus thresholds vary by state. Know where you have obligation.

## Claude Code tool pattern
- Use `finance_invoice_tracker` for revenue and expense tracking.
- Use `finance_burn_rate` for cash position awareness before tax payments.
- Use `legal_terms_review` for contractor vs employee classification guidance.

## Expanded workflow
1. **Identify your tax obligations by entity type.** Federal income tax, self-employment tax, state income tax, local taxes.
2. **Set up quarterly estimated tax schedule.** April 15, June 15, Sept 15, Jan 15. Put them on the calendar now.
3. **Calculate estimated tax liability.** Revenue × effective tax rate. Review quarterly as revenue changes.
4. **Set aside tax reserves.** 25-30% of revenue in a separate account. Don't touch it for operations.
5. **Track deductible expenses.** Business expenses, home office, equipment, travel, software, professional services.
6. **Check contractor 1099 requirements.** Any contractor paid $600+ in a year needs a 1099. Track payments from day 1.
7. **Review sales tax nexus.** Do you have economic nexus in any state? Thresholds vary — some states trigger at $100K in sales.
8. **Prepare filing documents.** Organize receipts, bank statements, and records by category. Don't wait until the deadline.

## Output contract
- Tax obligation checklist: federal, state, local
- Quarterly estimated tax schedule with amounts
- Tax reserve balance vs estimated liability
- Deductible expense tracker with categories
- 1099 requirements for contractors
- Sales tax nexus assessment

## Failure modes to avoid
- Not setting aside tax money — spending it and owing it later with penalties.
- Missing quarterly estimated tax deadlines — penalties accrue from the due date, not when you remember.
- Not tracking expenses — missing deductions means overpaying.
- Misclassifying employees as contractors — the IRS penalties are severe and include back taxes.
- Ignoring sales tax nexus — economic nexus can trigger obligations even in states where you have no physical presence.

## Handoff cues
- Tax checklist with obligations and due dates.
- Quarterly estimated tax amounts.
- Tax reserve balance vs estimated liability.
- 1099 contractor payment tracking status.

## Example invocation
- Slash: `/finance_tax_checklist <task>`
- Natural language: "Use finance_tax_checklist to prepare tax obligations checklist for a small business or solo founder."

## Quality bar
Tax obligations are identified by entity type. Quarterly estimated tax schedule is set. Tax reserves are at 25-30% of revenue. Deductible expenses are tracked in real-time. 1099 requirements are checked. Sales tax nexus is assessed.

## Related workflows
- **Tax planning:** `finance_tax_checklist` → `finance_invoice_tracker` → `finance_burn_rate`
- **Quarterly review:** `finance_tax_checklist` → `finance_burn_rate` → `ops_kpi_review`
- **Business setup:** `legal_terms_review` → `finance_tax_checklist` → `finance_pricing_model`

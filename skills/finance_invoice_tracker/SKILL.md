---
name: finance_invoice_tracker
description: "Track invoices, payment terms, and cash flow timing for a small operation."
user-invocable: true
metadata: {"openclaw":{"emoji":"🧾"}}
---

# Invoice Tracker

## Purpose
Track invoices, payment terms, and cash flow timing for a small operation. Late payments and forgotten invoices are the silent cash flow killers for solo founders and small teams. Money you've earned but haven't collected is money you can't spend — and you can't collect what you don't track.

## Use when
Use when you have more than a handful of invoices per month. Use when cash flow timing matters for paying bills. Use when you're unsure which invoices are outstanding.

## Avoid when
Don't use for complex accounting — that needs a real bookkeeper. Don't use as a substitute for tax-compliant record keeping. Don't use when a proper accounting system is already in place.

## Inputs to gather
- Outstanding invoices: what's owed to you, by whom, and when is it due?
- Payment terms: net-30, net-60, on receipt — what are your standard terms?
- Recurring expenses: what bills come due every month and when?
- Payment history: who pays on time and who's consistently late?
- Cash flow forecast: when does money come in vs go out?

## Operating rules
- Track every invoice from the moment it's sent. If it's not tracked, it's not getting paid.
- Standardize payment terms. Net-30 is reasonable; net-60 means you're financing their business. Don't accept terms you can't afford.
- Flag overdue invoices at day 1, not day 30. The longer you wait, the harder collection becomes.
- Know your cash flow gap. If your clients pay net-30 but your bills are due net-15, you have a 15-day gap to bridge.
- Separate tax money from operating money. Don't spend the tax man's share — he always collects.

## Claude Code tool pattern
- Use `finance_burn_rate` for the overall cash position.
- Use `finance_tax_checklist` for tax payment timing.
- Use `ops_vendor_eval` for vendor payment terms negotiation.

## Expanded workflow
1. **List all outstanding invoices.** Amount, client, sent date, due date, status.
2. **List all recurring expenses.** Amount, vendor, due date, payment method.
3. **Map the cash flow timeline.** Money in vs money out, week by week for the next 4 weeks.
4. **Flag overdue invoices.** Contact the client with a polite follow-up immediately. Don't wait.
5. **Identify the cash flow gap.** When does money go out before it comes in? How do you bridge it?
6. **Set up payment reminders.** 7 days before due, day of due, 1 day overdue. Automate if possible.
7. **Review weekly.** Update invoice statuses, flag new overdues, project next 4 weeks.

## Output contract
- Invoice tracker: all outstanding invoices with status
- Recurring expense calendar: what's due when
- Cash flow timeline: money in vs money out, week by week
- Overdue invoice follow-up queue
- Cash flow gap analysis

## Failure modes to avoid
- Not tracking invoices — if you don't know what's owed, you can't collect it.
- Letting overdue invoices sit — the longer you wait, the harder collection becomes.
- Not knowing your cash flow gap — bills due before payments arrive creates crises.
- Spending tax money on operations — the IRS doesn't care about your cash flow problems.
- No recurring expense calendar — surprised by bills you should have expected.

## Handoff cues
- Invoice tracker with current statuses.
- Cash flow timeline for the next 4 weeks.
- Overdue invoices requiring follow-up.
- Cash flow gap and the plan to bridge it.

## Example invocation
- Slash: `/finance_invoice_tracker <task>`
- Natural language: "Use finance_invoice_tracker to track invoices, payment terms, and cash flow timing for a small operation."

## Quality bar
Every invoice is tracked from the moment it's sent. Payment terms are standardized. Overdue invoices are flagged immediately. Cash flow gap is identified and managed. Tax money is separated from operating money.

## Related workflows
- **Cash flow management:** `finance_invoice_tracker` → `finance_burn_rate` → weekly review
- **Invoice lifecycle:** Send invoice → `finance_invoice_tracker` → flag overdue → follow up → `finance_burn_rate`
- **Tax planning:** `finance_invoice_tracker` → `finance_tax_checklist` → tax payment

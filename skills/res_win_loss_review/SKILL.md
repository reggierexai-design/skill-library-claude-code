---
name: res_win_loss_review
description: "Turn won and lost deals, pilots, or evaluations into patterns about value, objections, and timing."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udd0e"}}
---

## Purpose
- Turn won and lost deals, pilots, or evaluations into patterns about value, objections, and timing.
- This is a **research specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when the team has sales notes, trial outcomes, pilot feedback, or customer decisions to learn from.

## Avoid when
- Do not reduce complex buying decisions to one simplistic reason.

## Inputs to gather
- The research question, decision to support, and how fresh the answer must be.
- Known sources, target audiences, competitors, communities, or pages to inspect.
- What evidence threshold is needed: directional scan, proof-backed brief, or audit-grade review.

## Operating rules
- Buying decisions are multi-causal.
- Separate controllable factors from external timing or budget issues.
- Use the review to improve both product and messaging.

- Source quality matters more than source quantity. One verified primary source beats ten secondary blog posts.
- Separate findings from interpretations. Data first, conclusions second. Mixing them undermines credibility.
- Triangulate important claims across at least two independent sources. Single-source claims are hypotheses.
- Rate confidence on every finding: high (verified, replicable), medium (directionally sound, limited data), low (anecdotal, unverified).
- Name what you do not know. Unresearched questions are more valuable than poorly researched answers.
## Claude Code tool pattern
- Use current sources when claims, markets, rankings, or product details may have changed.
- Read enough of the source material to preserve nuance; do not summarize from snippets alone when the distinction matters.
- Capture evidence in a way that separates observation, inference, and recommendation.

## Expanded workflow
1. Inventory the relevant wins and losses.
2. Extract stated reasons, hidden signals, and timing context.
3. Group the patterns into themes.
4. Recommend concrete changes to improve future outcomes.
## Output contract
- Decision patterns
- Top win factors
- Top loss factors
- Recommended changes
- Evidence-backed findings tied to the decision at hand.
- Source quality notes, uncertainty, and next research gaps.

## Failure modes to avoid
- Answering from memory when freshness or direct evidence matters.
- Using anecdotal signals as if they were the whole market.
- Losing the decision context and returning an interesting but unusable scan.

## Handoff cues

- Win/loss review: outcomes, reasons, patterns, competitive dynamics, action items.
- Win/loss ratio trends over time.
- Recommended positioning and sales improvements.

## Example invocation
- Slash: `/res_win_loss_review <task>`
- Natural language: "Use win Loss Review to turn won and lost deals, pilots, or evaluations into patterns about value, objections, and timing."
- Example: "Research this market and tell me what is actually true right now."
- Example: "Audit the claims and prove what we can really say with confidence."
- Often paired with: `core_evidence_research`, `res_source_check`, `safe_external_claims`

## Quality bar
- A useful review explains what to change next, not just what happened.
- Every finding has a source citation and a confidence rating.
- Important claims are triangulated across independent sources.
- Findings and interpretations are clearly separated.
- Unanswered questions are explicitly named.
## Related workflows
- Research chain: `res_competitor_scan` → `res_market_map` → `res_interview_synthesis`

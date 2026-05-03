---
name: res_competitor_scan
description: "Map competing products, messages, wedges, and weak spots for strategy or attention work."
user-invocable: true
metadata: {"openclaw":{"emoji":"🔎"}}
---

## Purpose
- Map competing products, messages, wedges, and weak spots for strategy or attention work.
- This is a **research specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when the user needs a live view of the market, adjacent alternatives, or competitive positioning.

## Avoid when
- Do not use when the task only concerns internal implementation details.

## Inputs to gather
- The research question, decision to support, and how fresh the answer must be.
- Known sources, target audiences, competitors, communities, or pages to inspect.
- What evidence threshold is needed: directional scan, proof-backed brief, or audit-grade review.

## Operating rules
- Focus on the alternatives a user would truly compare, not just look-alike brands.
- Track product promise, proof, pricing posture, and distribution style.
- Prefer signal over exhaustive lists.

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
1. Define the market frame and target user.
2. Select the most relevant competitors and substitutes.
3. Compare message, product angle, proof, and go-to-market motion.
4. Return a wedge the project can own.
## Output contract
- Market frame
- Competitor table
- Observed patterns
- Recommended wedge
- Evidence-backed findings tied to the decision at hand.
- Source quality notes, uncertainty, and next research gaps.

## Failure modes to avoid
- Answering from memory when freshness or direct evidence matters.
- Using anecdotal signals as if they were the whole market.
- Losing the decision context and returning an interesting but unusable scan.

## Handoff cues
- Competitor scan: competitors, positioning, features, pricing, strengths, weaknesses.
- Competitive advantage assessment for your product.
- Monitoring plan for ongoing tracking.

## Example invocation
- Slash: `/res_competitor_scan <task>`
- Natural language: "Use competitor Scan to map competing products, messages, wedges, and weak spots for strategy or attention work."
- Example: "Research this market and tell me what is actually true right now."
- Example: "Audit the claims and prove what we can really say with confidence."
- Often paired with: `core_evidence_research`, `res_source_check`, `safe_external_claims`

## Quality bar

- Every competitor claim is sourced from public information, not hearsay.
- The scan covers direct, indirect, and adjacent competitors.
- Competitive advantages are specific and defensible, not generic superlatives.
- The scan is dated and has a refresh cadence — competitor landscapes change.
- Every finding has a source citation and a confidence rating.
- Important claims are triangulated across independent sources.
- Findings and interpretations are clearly separated.
- Unanswered questions are explicitly named.
## Related workflows
- Research chain: `res_competitor_scan` → `res_market_map` → `res_interview_synthesis`

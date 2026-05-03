---
name: res_partner_landscape
description: "Find plausible partners, integrations, and channel allies with fit, leverage, and mutual value."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udd0e","requires":{"config":["browser.enabled"]}}}
---

## Purpose
- Find plausible partners, integrations, and channel allies with fit, leverage, and mutual value.
- This is a **research specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when growth or product strategy could benefit from integrations, co-marketing, or ecosystem access.

## Avoid when
- Do not suggest partnerships that are famous but strategically empty.

## Inputs to gather
- The research question, decision to support, and how fresh the answer must be.
- Known sources, target audiences, competitors, communities, or pages to inspect.
- What evidence threshold is needed: directional scan, proof-backed brief, or audit-grade review.

## Operating rules
- Partner fit beats logo envy.
- Look for shared audience, adjacent workflows, or complementary proof.
- A credible partner list includes why both sides would care.

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
1. Clarify the job the partnership should do.
2. Map candidate categories and specific targets.
3. Score fit, leverage, and realism.
4. Recommend the best few next moves.
## Output contract
- Partnership goal
- Target list
- Fit rationale
- Outreach prerequisites
- Evidence-backed findings tied to the decision at hand.
- Source quality notes, uncertainty, and next research gaps.

## Failure modes to avoid
- Answering from memory when freshness or direct evidence matters.
- Using anecdotal signals as if they were the whole market.
- Losing the decision context and returning an interesting but unusable scan.

## Handoff cues

- Partner landscape: potential partners, overlap, partnership models, mutual value.
- Priority partners ranked by strategic fit.
- Outreach strategy for top 3-5 partners.

## Example invocation
- Slash: `/res_partner_landscape <task>`
- Natural language: "Use partner Landscape to find plausible partners, integrations, and channel allies with fit, leverage, and mutual value."
- Example: "Research this market and tell me what is actually true right now."
- Example: "Audit the claims and prove what we can really say with confidence."
- Often paired with: `core_evidence_research`, `res_source_check`, `safe_external_claims`

## Quality bar
- A partner landscape is good when it turns vague ecosystem thinking into a short list of winnable moves.
- Every finding has a source citation and a confidence rating.
- Important claims are triangulated across independent sources.
- Findings and interpretations are clearly separated.
- Unanswered questions are explicitly named.
## Related workflows
- Research chain: `res_competitor_scan` → `res_market_map` → `res_interview_synthesis`

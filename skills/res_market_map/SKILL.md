---
name: res_market_map
description: "Segment a market into audiences, jobs, triggers, channels, and buying alternatives."
user-invocable: true
metadata: {"openclaw":{"emoji":"🔎"}}
---

## Purpose
- Segment a market into audiences, jobs, triggers, channels, and buying alternatives.
- This is a **research specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when the user needs a strategic view of who the project is for and where attention can be won.

## Avoid when
- Do not use for narrow technical debugging or single-page copy tweaks.

## Inputs to gather
- The research question, decision to support, and how fresh the answer must be.
- Known sources, target audiences, competitors, communities, or pages to inspect.
- What evidence threshold is needed: directional scan, proof-backed brief, or audit-grade review.

## Operating rules
- Organize the market by user problem and trigger, not only by industry labels.
- Look for underserved segments and asymmetric entry points.
- Keep the map actionable for product or distribution decisions.

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
1. Define the core job to be done.
2. Break the market into meaningful segments.
3. Map triggers, alternatives, and reachable channels for each segment.
4. Highlight the best entry wedge.
## Output contract
- Market segments
- Job and trigger map
- Reach channels
- Best wedge and why
- Evidence-backed findings tied to the decision at hand.
- Source quality notes, uncertainty, and next research gaps.

## Failure modes to avoid
- Answering from memory when freshness or direct evidence matters.
- Using anecdotal signals as if they were the whole market.
- Losing the decision context and returning an interesting but unusable scan.

## Handoff cues

- Market map: segments, players, positioning, market size, growth trends.
- White space opportunities.
- Recommended positioning based on market gaps.

## Example invocation
- Slash: `/res_market_map <task>`
- Natural language: "Use market Map to segment a market into audiences, jobs, triggers, channels, and buying alternatives."
- Example: "Research this market and tell me what is actually true right now."
- Example: "Audit the claims and prove what we can really say with confidence."
- Often paired with: `core_evidence_research`, `res_source_check`, `safe_external_claims`

## Quality bar
- The map should tell the team where to aim first.
- Every finding has a source citation and a confidence rating.
- Important claims are triangulated across independent sources.
- Findings and interpretations are clearly separated.
- Unanswered questions are explicitly named.
## Related workflows
- Research chain: `res_competitor_scan` → `res_market_map` → `res_interview_synthesis`

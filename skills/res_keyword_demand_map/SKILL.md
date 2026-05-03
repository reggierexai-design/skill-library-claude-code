---
name: res_keyword_demand_map
description: "Map search intent, topic clusters, and likely demand signals for SEO and search-discovery work."
user-invocable: true
---

## Purpose
- Map search intent, topic clusters, and likely demand signals for SEO and search-discovery work.
- This is a **research specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when planning search-led content, comparison pages, documentation pages, or category capture.

## Avoid when
- Do not use when the project has no search-relevant audience or the goal is purely brand storytelling.

## Inputs to gather
- The research question, decision to support, and how fresh the answer must be.
- Known sources, target audiences, competitors, communities, or pages to inspect.
- What evidence threshold is needed: directional scan, proof-backed brief, or audit-grade review.

## Operating rules
- Search intent matters more than raw keyword volume alone.
- Cluster by problem and decision stage, not just word similarity.
- Separate navigational, educational, and commercial intent.

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
1. Identify the audience jobs and search intents.
2. Map topic clusters and query variants.
3. Assess what page types currently win and why.
4. Recommend priority pages and content angles.
## Output contract
- Intent clusters
- Priority topics
- Observed SERP patterns
- Recommended page plan
- Evidence-backed findings tied to the decision at hand.
- Source quality notes, uncertainty, and next research gaps.

## Failure modes to avoid
- Answering from memory when freshness or direct evidence matters.
- Using anecdotal signals as if they were the whole market.
- Losing the decision context and returning an interesting but unusable scan.

## Handoff cues

- Keyword demand map: keywords, volume, difficulty, intent, content opportunities.
- Priority keywords for content creation.
- Competitive gap analysis.

## Example invocation
- Slash: `/res_keyword_demand_map <task>`
- Natural language: "Use keyword Demand Map to map search intent, topic clusters, and likely demand signals for seo and search-discovery work."
- Example: "Research this market and tell me what is actually true right now."
- Example: "Audit the claims and prove what we can really say with confidence."
- Often paired with: `core_evidence_research`, `res_source_check`, `safe_external_claims`

## Quality bar
- A keyword map is useful when it reveals which searches are worth serving and how the project can win them.
- Every finding has a source citation and a confidence rating.
- Important claims are triangulated across independent sources.
- Findings and interpretations are clearly separated.
- Unanswered questions are explicitly named.
## Related workflows
- Research chain: `res_competitor_scan` → `res_market_map` → `res_interview_synthesis`

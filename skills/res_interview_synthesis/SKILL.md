---
name: res_interview_synthesis
description: "Turn user calls, notes, and transcripts into pains, language patterns, and decision inputs."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udd0e"}}
---

## Purpose
- Turn user calls, notes, and transcripts into pains, language patterns, and decision inputs.
- This is a **research specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when the user has qualitative research that needs to become product, messaging, or prioritization guidance.

## Avoid when
- Do not use when there is no real source material to synthesize.

## Inputs to gather
- The research question, decision to support, and how fresh the answer must be.
- Known sources, target audiences, competitors, communities, or pages to inspect.
- What evidence threshold is needed: directional scan, proof-backed brief, or audit-grade review.

## Operating rules
- Preserve user language where it carries signal.
- Separate repeated patterns from one-off anecdotes.
- Link findings to concrete decisions.

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
1. Inventory the source material.
2. Code the material into themes, phrases, pains, and motivators.
3. Rank what is frequent, intense, and decision-relevant.
4. Return insights tied to product or messaging actions.
## Output contract
- Top themes
- Important phrases
- Decision implications
- Open questions for more research
- Evidence-backed findings tied to the decision at hand.
- Source quality notes, uncertainty, and next research gaps.

## Failure modes to avoid
- Answering from memory when freshness or direct evidence matters.
- Using anecdotal signals as if they were the whole market.
- Losing the decision context and returning an interesting but unusable scan.

## Handoff cues

- Interview synthesis: themes, quotes, patterns, insights, confidence level.
- Sample size and demographic breakdown.
- Actionable recommendations ranked by evidence strength.

## Example invocation
- Slash: `/res_interview_synthesis <task>`
- Natural language: "Use interview Synthesis to turn user calls, notes, and transcripts into pains, language patterns, and decision inputs."
- Example: "Research this market and tell me what is actually true right now."
- Example: "Audit the claims and prove what we can really say with confidence."
- Often paired with: `core_evidence_research`, `res_source_check`, `safe_external_claims`

## Quality bar
- Synthesis should make the next product or messaging decision easier.
- Every finding has a source citation and a confidence rating.
- Important claims are triangulated across independent sources.
- Findings and interpretations are clearly separated.
- Unanswered questions are explicitly named.
## Related workflows
- Research chain: `res_competitor_scan` → `res_market_map` → `res_interview_synthesis`

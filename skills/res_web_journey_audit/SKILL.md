---
name: res_web_journey_audit
description: "Audit a live website or product flow for clarity, friction, and attention leakage."
user-invocable: true
---

## Purpose
- Audit a live website or product flow for clarity, friction, and attention leakage.
- This is a **research specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when the user wants a current review of a landing page, onboarding flow, pricing page, or signup journey.

## Avoid when
- Do not use when browser access is unavailable or when the page can be evaluated from static local files alone.

## Inputs to gather
- The research question, decision to support, and how fresh the answer must be.
- Known sources, target audiences, competitors, communities, or pages to inspect.
- What evidence threshold is needed: directional scan, proof-backed brief, or audit-grade review.

## Operating rules
- Audit the journey as a first-time user would.
- Focus on drop-off risks, trust gaps, and unclear next steps.
- Tie observations to visible evidence on page.

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
1. Define the desired user action.
2. Walk the journey step by step.
3. Log friction, confusion, proof gaps, and dead ends.
4. Recommend the highest-leverage fixes first.
## Output contract
- Journey summary
- Observed friction
- Conversion blockers
- Recommended fixes in priority order
- Evidence-backed findings tied to the decision at hand.
- Source quality notes, uncertainty, and next research gaps.

## Failure modes to avoid
- Answering from memory when freshness or direct evidence matters.
- Using anecdotal signals as if they were the whole market.
- Losing the decision context and returning an interesting but unusable scan.

## Handoff cues

- Web journey audit: pages, flows, friction points, drop-off data, improvement priorities.
- Competitor comparison for key journey steps.
- Recommended A/B tests for highest-impact friction.

## Example invocation
- Slash: `/res_web_journey_audit <task>`
- Natural language: "Use web Journey Audit to audit a live website or product flow for clarity, friction, and attention leakage."
- Example: "Research this market and tell me what is actually true right now."
- Example: "Audit the claims and prove what we can really say with confidence."
- Often paired with: `core_evidence_research`, `res_source_check`, `safe_external_claims`

## Quality bar
- The audit should help the team fix the actual page that exists today.
- Every finding has a source citation and a confidence rating.
- Important claims are triangulated across independent sources.
- Findings and interpretations are clearly separated.
- Unanswered questions are explicitly named.
## Related workflows
- Research chain: `res_competitor_scan` → `res_market_map` → `res_interview_synthesis`

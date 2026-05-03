---
name: res_message_board_scan
description: "Scan forums, communities, and comment threads for pains, objections, language, and attention hooks."
user-invocable: true
---

## Purpose
- Scan forums, communities, and comment threads for pains, objections, language, and attention hooks.
- This is a **research specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when you need raw audience language, repeated objections, or community context around a problem.

## Avoid when
- Do not treat a few loud comments as a full market picture.

## Inputs to gather
- The research question, decision to support, and how fresh the answer must be.
- Known sources, target audiences, competitors, communities, or pages to inspect.
- What evidence threshold is needed: directional scan, proof-backed brief, or audit-grade review.

## Operating rules
- Look for patterns across sources, not one memorable quote.
- Capture language in context instead of stripping it of meaning.
- Distinguish genuine pain from entertainment, trolling, or hype.

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
1. Choose communities close to the target audience.
2. Collect repeated pains, desires, and objections.
3. Group the findings into usable themes.
4. Translate themes into product, messaging, or content implications.
## Output contract
- Community surfaces reviewed
- Repeated themes
- Audience language
- Actionable implications
- Evidence-backed findings tied to the decision at hand.
- Source quality notes, uncertainty, and next research gaps.

## Failure modes to avoid
- Answering from memory when freshness or direct evidence matters.
- Using anecdotal signals as if they were the whole market.
- Losing the decision context and returning an interesting but unusable scan.

## Handoff cues

- Message board scan: communities, threads, sentiment, pain points, feature requests.
- Priority themes ranked by frequency and intensity.
- Opportunities for authentic engagement.

## Example invocation
- Slash: `/res_message_board_scan <task>`
- Natural language: "Use message Board Scan to scan forums, communities, and comment threads for pains, objections, language, and attention hooks."
- Example: "Research this market and tell me what is actually true right now."
- Example: "Audit the claims and prove what we can really say with confidence."
- Often paired with: `core_evidence_research`, `res_source_check`, `safe_external_claims`

## Quality bar
- A good scan gives the team sharper language and better instincts without pretending the sample is perfect.
- Every finding has a source citation and a confidence rating.
- Important claims are triangulated across independent sources.
- Findings and interpretations are clearly separated.
- Unanswered questions are explicitly named.
## Related workflows
- Research chain: `res_competitor_scan` → `res_market_map` → `res_interview_synthesis`

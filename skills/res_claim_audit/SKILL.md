---
name: res_claim_audit
description: "Audit landing page, pitch, or outbound claims for credibility, proof, and overreach."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udd0e"}}
---

## Purpose
- Audit landing page, pitch, or outbound claims for credibility, proof, and overreach.
- This is a **research specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when messaging may be too vague, too grand, or unsupported by the actual product.

## Avoid when
- Do not use on purely exploratory brainstorming that is not intended for publication.

## Inputs to gather
- The research question, decision to support, and how fresh the answer must be.
- Known sources, target audiences, competitors, communities, or pages to inspect.
- What evidence threshold is needed: directional scan, proof-backed brief, or audit-grade review.

## Operating rules
- Every strong claim needs corresponding proof, mechanism, or evidence.
- Cut hype before polishing style.
- Prefer precise, defensible language over inflated outcomes.

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
1. Extract all meaningful claims.
2. Score each for truth, clarity, specificity, and proof.
3. Rewrite or remove weak claims.
4. Return the strongest honest message set.
## Output contract
- Claim inventory
- Risky claims
- Rewrites
- Proof gaps to close
- Evidence-backed findings tied to the decision at hand.
- Source quality notes, uncertainty, and next research gaps.

## Failure modes to avoid
- Answering from memory when freshness or direct evidence matters.
- Using anecdotal signals as if they were the whole market.
- Losing the decision context and returning an interesting but unusable scan.

## Handoff cues

- Claim audit report: claims, evidence strength, gaps, recommended fixes.
- Priority claims needing immediate evidence or removal.
- Compliance implications if any claims are misleading.

## Example invocation
- Slash: `/res_claim_audit <task>`
- Natural language: "Use claim Audit to audit landing page, pitch, or outbound claims for credibility, proof, and overreach."
- Example: "Research this market and tell me what is actually true right now."
- Example: "Audit the claims and prove what we can really say with confidence."
- Often paired with: `core_evidence_research`, `res_source_check`, `safe_external_claims`

## Quality bar
- Better to sound smaller and true than larger and brittle.
- Every finding has a source citation and a confidence rating.
- Important claims are triangulated across independent sources.
- Findings and interpretations are clearly separated.
- Unanswered questions are explicitly named.
## Related workflows
- Research chain: `res_competitor_scan` → `res_market_map` → `res_interview_synthesis`

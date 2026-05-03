---
name: res_source_check
description: "Verify important claims against high-quality sources and mark what is still uncertain."
user-invocable: true
metadata: {"openclaw":{"emoji":"🔎"}}
---

## Purpose
- Verify important claims against high-quality sources and mark what is still uncertain.
- This is a **research specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when the output depends on current facts, numbers, policy details, or quotations.

## Avoid when
- Do not use for subjective taste judgments or clearly local project facts.

## Inputs to gather
- The research question, decision to support, and how fresh the answer must be.
- Known sources, target audiences, competitors, communities, or pages to inspect.
- What evidence threshold is needed: directional scan, proof-backed brief, or audit-grade review.

## Operating rules
- Verify the highest-impact claims first.
- Prefer primary or official sources when they exist.
- Mark uncertainty instead of smoothing it over.

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
1. List the claims that matter.
2. Check each against the best available sources.
3. Resolve conflicts or report them honestly.
4. Flag unsupported claims for removal or rewrite.
## Output contract
- Claim list
- Support status
- Best source per claim
- Rewrite or removal recommendations
- Evidence-backed findings tied to the decision at hand.
- Source quality notes, uncertainty, and next research gaps.

## Failure modes to avoid
- Answering from memory when freshness or direct evidence matters.
- Using anecdotal signals as if they were the whole market.
- Losing the decision context and returning an interesting but unusable scan.

## Handoff cues

- Source check: claims, sources, credibility ratings, verification status.
- Unverifiable claims flagged for removal or qualification.
- Recommended replacements for weak sources.

## Example invocation
- Slash: `/res_source_check <task>`
- Natural language: "Use source Check to verify important claims against high-quality sources and mark what is still uncertain."
- Example: "Research this market and tell me what is actually true right now."
- Example: "Audit the claims and prove what we can really say with confidence."
- Often paired with: `core_evidence_research`, `safe_external_claims`

## Quality bar
- Unsupported claims should leave the draft, not hide inside it.
- Every finding has a source citation and a confidence rating.
- Important claims are triangulated across independent sources.
- Findings and interpretations are clearly separated.
- Unanswered questions are explicitly named.
## Related workflows
- Research chain: `res_competitor_scan` → `res_market_map` → `res_interview_synthesis`

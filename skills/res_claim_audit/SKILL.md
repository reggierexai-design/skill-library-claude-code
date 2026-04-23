---
name: res_claim_audit
description: "Audit landing page, pitch, or outbound claims for credibility, proof, and overreach."
user-invocable: true
disable-model-invocation: true
---


# Claim Audit

## Purpose
- Audit landing page, pitch, or outbound claims for credibility, proof, and overreach.
- This is a **research specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use when messaging may be too vague, too grand, or unsupported by the actual product.
- The main bottleneck is best solved through research work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not use on purely exploratory brainstorming that is not intended for publication.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- The research question, decision to support, and how fresh the answer must be.
- Known sources, target audiences, competitors, communities, or pages to inspect.
- What evidence threshold is needed: directional scan, proof-backed brief, or audit-grade review.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- Every strong claim needs corresponding proof, mechanism, or evidence.
- Cut hype before polishing style.
- Prefer precise, defensible language over inflated outcomes.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Use current sources when claims, markets, rankings, or product details may have changed.
- Read enough of the source material to preserve nuance; do not summarize from snippets alone when the distinction matters.
- Capture evidence in a way that separates observation, inference, and recommendation.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Extract all meaningful claims.
2. Score each for truth, clarity, specificity, and proof.
3. Rewrite or remove weak claims.
4. Return the strongest honest message set.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

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
- Declaring success before the output is usable by the next operator, owner, or decision-maker.

## Handoff cues
- State current status, remaining blockers, and the smallest next move.
- Name the files, pages, systems, or source material that another operator should read first.
- Flag approvals, missing evidence, or live-system access that still require a human decision.

## Example invocation
- Slash: `/res_claim_audit <task>`
- Natural language: "Use claim Audit to audit landing page, pitch, or outbound claims for credibility, proof, and overreach."
- Example: "Research this market and tell me what is actually true right now."
- Example: "Audit the claims and prove what we can really say with confidence."
- Often paired with: `core_evidence_research`, `res_source_check`, `safe_external_claims`

## Quality bar
- Better to sound smaller and true than larger and brittle.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.

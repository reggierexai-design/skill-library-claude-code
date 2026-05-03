---
name: att_seo_page_brief
description: "Design search-driven pages with intent, proof, structure, and conversion paths."
user-invocable: true
metadata: {"openclaw":{"emoji":"📣"}}
---

## Purpose
- Design search-driven pages with intent, proof, structure, and conversion paths.

## Use when
- Use when the user wants an organic discovery page, comparison page, use-case page, or educational page that can rank and convert.

## Avoid when
- Do not use when the page has no real search intent or the task is purely paid acquisition copy.

## Inputs to gather
- Target keyword or topic: what does the audience search for?
- Search intent: informational, navigational, commercial, or transactional?
- Current ranking: where does the site rank for this term today?
- Competitor content: what currently ranks on page 1 and why?
- Existing page content: what's already published and what needs updating?

## Operating rules
- Search pages should satisfy intent first and persuade second.
- Build around a narrow query cluster, proof, and a clear conversion path.
- Avoid thin pages that only restate generic marketing claims.

## Claude Code tool pattern
- Use `WebFetch` to research competitor content and current platform conventions.
- Read existing site copy, product pages, and proof assets before drafting so output fits the real product truth.
- When external claims appear, verify before publishing with `safe_external_claims`.
- After drafting, run `att_proof_mining` to verify every claim has backing.

## Expanded workflow
1. Define target query intent and audience.
2. Choose the page promise, angle, and conversion goal.
3. Outline sections, proof, FAQs, and internal links.
4. Return a page brief with editorial and conversion notes.
## Output contract
- Target intent
- Page angle
- Section outline
- Proof and CTA plan
## Failure modes to avoid
- Writing content without studying what currently ranks — guessing at what satisfies the intent.
- Keyword stuffing — search engines penalize obvious manipulation.
- Ignoring search intent — a transactional page written like a guide won't convert.
- Thin content — 500 words on a topic page 1 covers in 3000 words won't rank.
- No internal link strategy — isolated pages don't build authority.

## Handoff cues
- Provide the SEO brief: keyword, intent, outline, content gap, word count, internal links, CTA.
- Flag any existing pages that should be updated instead of creating new content.
- Note expected timeline to rank based on domain authority and keyword difficulty.

## Example invocation
- Slash: `/att_seo_page_brief <task>`
- Natural language: "Use sEO Page Brief to design search-driven pages with intent, proof, structure, and conversion paths."
- Example: "Design an SEO brief for the keyword AI workforce for small business."
- Example: "Competitors rank for best AI agent platform. Create a brief to beat them."
- Often paired with: `att_message_house`, `att_launch_plan`, `att_proof_mining`

## Quality bar

- The brief matches content depth to search intent.
- Page 1 results analyzed and content gap identified.
- Title and H1 naturally include the primary keyword.
- Internal link plan connects to authoritative existing pages.
- Word count target matches or exceeds top-ranking content.

## Related workflows
- Content system: `att_message_house` → `att_content_calendar` → `att_content_repurposing`
- Launch sequence: `att_launch_plan` → `att_proof_mining` → `att_thread_writer`
- Proof deployment: `att_proof_mining` → `att_case_study_builder` → `att_social_proof_pack`

---
name: doc_glossary_builder
description: "Build a shared glossary for terms, metrics, entities, and overloaded language across a project."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udcda"}}
---

## Purpose
- Build a shared glossary for terms, metrics, entities, and overloaded language across a project.
- This is a **documentation specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when teams or docs keep using the same words to mean different things.

## Avoid when
- Do not use when terminology is already stable and well-documented.

## Inputs to gather
- Target reader, prerequisite knowledge, starting state, and desired success moment.
- Existing docs, product behavior, known support pain points, and terms that must stay consistent.
- Whether the output should optimize for fast start, troubleshooting, migration, or reference completeness.

## Operating rules
- Define in the audience's language, not the expert's. A glossary that defines terms using other jargon isn't a glossary â€” it's a puzzle.
- Include context-specific usage. A term that means one thing in marketing and another in engineering needs both definitions.
- Cross-reference related terms. Glossary entries should link to each other, creating a concept web not a flat list.
- Keep definitions to 2-3 sentences. If a definition needs a paragraph, it's an explainer, not a glossary entry.

- Write for the reader who is frustrated and in a hurry, not the reader who has time and patience. Docs are searched, not read cover-to-cover.
- Every doc needs a clear purpose statement: who is this for, what will they learn, what will they do after reading?
- Code examples should be copy-pasteable and runnable. Broken code examples destroy trust in the entire document.
- Structure for scanning: headers, bullets, short paragraphs. Wall-of-text documentation is unread documentation.
- Docs need maintenance like code needs maintenance. Stale docs are worse than no docs because they actively mislead.
## Claude Code tool pattern
- Read the source behavior, UI copy, API shape, or runbook reality before writing documentation.
- Keep the happy path tight; move depth into links, reference sections, or follow-on docs.
- Make docs observable: the reader should know what success, failure, and next steps look like.

## Expanded workflow
1. Collect terms from: docs, support tickets, product UI, sales conversations.
2. Write definitions in the audience's language (not jargon).
3. Add context-specific usage notes where terms vary by domain.
4. Cross-reference related terms.
5. Organize alphabetically with a category index.
6. Integrate: where does the glossary live and how is it maintained?

## Output contract
- Reader-specific doc draft or outline with clear structure and next links.
- Known gaps, stale-risk notes, and what should be validated against the product.

## Failure modes to avoid
- Writing docs from assumptions instead of the real behavior of the system.
- Trying to solve onboarding, troubleshooting, and reference use cases in one page.
- Hiding prerequisites, permissions, or environment assumptions until too late.

## Handoff cues
- Glossary: terms, definitions, context-specific usage, related terms.
- Cross-references between related concepts.
- Integration plan: where the glossary lives and how it's maintained.

## Example invocation
- Slash: `/doc_glossary_builder <task>`
- Natural language: "Use documentation Glossary Builder to build a shared glossary for terms, metrics, entities, and overloaded language across a project."
- Example: "Write the doc a real operator or user can follow on the first try."
- Example: "Turn support friction into a clearer quickstart, guide, or troubleshooting page."
- Often paired with: `doc_quickstart_guide`, `doc_troubleshooting_guide`, `eng_docs_for_change`

## Quality bar
## Related workflows
- Docs system: `doc_information_architecture` â†’ `doc_quickstart_guide` â†’ `doc_troubleshooting_guide` â†’ `doc_docs_feedback_loop`
- A frustrated user can find the answer they need within 60 seconds.
- Every code example is copy-pasteable and tested.
- The document states its audience, purpose, and prerequisites upfront.
- Content is structured for scanning, not sequential reading.
---
name: doc_concept_explainer
description: "Write a clear concept page that teaches how something works before diving into procedures."
user-invocable: true
---

## Purpose
- Write a clear concept page that teaches how something works before diving into procedures.
- This is a **documentation specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when users need a mental model before setup, usage, or troubleshooting will make sense.

## Avoid when
- Do not use when a task page alone is sufficient.

## Inputs to gather
- Target reader, prerequisite knowledge, starting state, and desired success moment.
- Existing docs, product behavior, known support pain points, and terms that must stay consistent.
- Whether the output should optimize for fast start, troubleshooting, migration, or reference completeness.

## Operating rules
- Start with the analogy, then add precision. Concepts are understood through comparison to known things. Technical precision without a mental model is just jargon.
- One concept, one explainer. Trying to explain 5 related concepts in one doc confuses instead of clarifying.
- Show, don't just tell. Code examples, diagrams, and concrete scenarios beat paragraphs of abstraction.
- Explain why, not just what. Understanding the motivation behind a concept makes the details stick.

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
1. Define the concept and the audience's starting knowledge.
2. Find the best analogy: what does the reader already know that's similar?
3. Explain the concept using the analogy first, then add technical precision.
4. Add concrete examples: code, diagrams, or scenarios.
5. Explain the motivation: why does this concept exist?
6. Link to related concepts and prerequisites.
7. Test with someone in the target audience â€” can they explain it back?

## Output contract
- Reader-specific doc draft or outline with clear structure and next links.
- Known gaps, stale-risk notes, and what should be validated against the product.

## Failure modes to avoid
- Writing docs from assumptions instead of the real behavior of the system.
- Trying to solve onboarding, troubleshooting, and reference use cases in one page.
- Hiding prerequisites, permissions, or environment assumptions until too late.

## Handoff cues
- Concept explainer: title, audience, analogy, technical details, examples, related concepts.
- Difficulty level and prerequisite concepts.
- Where this doc fits in the documentation hierarchy.

## Example invocation
- Slash: `/doc_concept_explainer <task>`
- Natural language: "Use documentation Concept Explainer to write a clear concept page that teaches how something works before diving into procedures."
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

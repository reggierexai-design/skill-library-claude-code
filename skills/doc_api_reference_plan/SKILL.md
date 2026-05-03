---
name: doc_api_reference_plan
description: "Plan API reference content so endpoints, parameters, errors, and examples stay coherent."
user-invocable: true
---

## Purpose
- Plan API reference content so endpoints, parameters, errors, and examples stay coherent.
- This is a **documentation specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when API docs need structure, consistency, or a migration from scattered notes.

## Avoid when
- Do not mix conceptual guides and raw reference in one undifferentiated page.

## Inputs to gather
- Target reader, prerequisite knowledge, starting state, and desired success moment.
- Existing docs, product behavior, known support pain points, and terms that must stay consistent.
- Whether the output should optimize for fast start, troubleshooting, migration, or reference completeness.

## Operating rules
- Reference content should be scannable and consistent.
- Show required fields, defaults, errors, and examples.
- Keep generated and hand-written content clearly separated.

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
1. Map the API surface and reader needs.
2. Define the page template and content rules.
3. List required examples and error coverage.
4. Return a reference plan with gaps and owners.
## Output contract
- Reference template
- Coverage map
- Example needs
- Gaps and owners
- Reader-specific doc draft or outline with clear structure and next links.
- Known gaps, stale-risk notes, and what should be validated against the product.

## Failure modes to avoid
- Writing docs from assumptions instead of the real behavior of the system.
- Trying to solve onboarding, troubleshooting, and reference use cases in one page.
- Hiding prerequisites, permissions, or environment assumptions until too late.

## Handoff cues
- API reference plan: endpoints, parameters, responses, examples per endpoint.
- Organization structure (by resource, feature, or workflow).
- Auto-generation vs manual documentation decisions.

## Example invocation
- Slash: `/doc_api_reference_plan <task>`
- Natural language: "Use aPI Reference Plan to plan api reference content so endpoints, parameters, errors, and examples stay coherent."
- Example: "Write the doc a real operator or user can follow on the first try."
- Example: "Turn support friction into a clearer quickstart, guide, or troubleshooting page."
- Often paired with: `doc_quickstart_guide`, `doc_troubleshooting_guide`, `eng_docs_for_change`

## Quality bar

- Every endpoint has parameters, response schema, and at least one working example.
- Error responses are documented as thoroughly as success responses.
- The organization matches how developers think: by resource or workflow, not by internal architecture.
- Auto-generated sections are verified; manual sections are tested.
- A frustrated user can find the answer they need within 60 seconds.
- Every code example is copy-pasteable and tested.
- The document states its audience, purpose, and prerequisites upfront.
- Content is structured for scanning, not sequential reading.
## Related workflows
- Docs system: `doc_information_architecture` → `doc_quickstart_guide` → `doc_troubleshooting_guide` → `doc_docs_feedback_loop`

---
name: doc_example_pack
description: "Create a small, coherent set of examples that makes a feature or API easier to understand."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83e\uddf0"}}
---

## Purpose
- Create a small, coherent set of examples that makes a feature or API easier to understand.
- This is a **documentation specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a feature is easier to learn by example than by prose alone.

## Avoid when
- Do not use when no stable examples can be kept accurate.

## Inputs to gather
- Target reader, prerequisite knowledge, starting state, and desired success moment.
- Existing docs, product behavior, known support pain points, and terms that must stay consistent.
- Whether the output should optimize for fast start, troubleshooting, migration, or reference completeness.

## Operating rules
- Examples should be runnable, not pseudo-code. If the user can't copy-paste and see it work, it's not an example â€” it's a snippet.
- Cover real use cases, not toy problems. A todo app example teaches the API; a real-world workflow example teaches the product.
- Progressive difficulty: start with hello world, end with production patterns. Each example should build on the previous one's knowledge.
- Include error handling in advanced examples. Real code catches errors; example code that doesn't sets users up for production failures.

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
1. List the top 5-10 use cases from support tickets and user interviews.
2. Write the hello-world example (simplest possible working code).
3. Write intermediate examples covering common use cases.
4. Write advanced examples with error handling, edge cases, and production patterns.
5. Test every example: copy, paste, run, verify output.
6. Add cross-references between examples and concept docs.

## Output contract
- Reader-specific doc draft or outline with clear structure and next links.
- Known gaps, stale-risk notes, and what should be validated against the product.

## Failure modes to avoid
- Writing docs from assumptions instead of the real behavior of the system.
- Trying to solve onboarding, troubleshooting, and reference use cases in one page.
- Hiding prerequisites, permissions, or environment assumptions until too late.

## Handoff cues
- Example pack: use cases, code samples, expected outputs, setup requirements.
- Difficulty progression from basic to advanced.
- Cross-references to related docs and examples.

## Example invocation
- Slash: `/doc_example_pack <task>`
- Natural language: "Use documentation Example Pack to create a small, coherent set of examples that makes a feature or api easier to understand."
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
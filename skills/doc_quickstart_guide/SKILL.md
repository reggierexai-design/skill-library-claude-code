---
name: doc_quickstart_guide
description: "Write a fast-start guide that gets a new user to first success with minimal friction."
user-invocable: true
---

## Purpose
- Write a fast-start guide that gets a new user to first success with minimal friction.
- This is a **documentation specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a product or tool needs a clean first-run experience in documentation.

## Avoid when
- Do not stuff a quickstart with every edge case or architecture detail.

## Inputs to gather
- Target reader, prerequisite knowledge, starting state, and desired success moment.
- Existing docs, product behavior, known support pain points, and terms that must stay consistent.
- Whether the output should optimize for fast start, troubleshooting, migration, or reference completeness.

## Operating rules
- Optimize for first success, not completeness.
- State prerequisites up front.
- Keep the happy path unbroken.

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
1. Define the target new user and the first success moment.
2. List prerequisites and the shortest path.
3. Write the steps, checks, and next links.
4. Return a quickstart draft or outline.
## Output contract
- Target reader
- Prerequisites
- Fast-start steps
- Success checks and next links
- Reader-specific doc draft or outline with clear structure and next links.
- Known gaps, stale-risk notes, and what should be validated against the product.

## Failure modes to avoid
- Writing docs from assumptions instead of the real behavior of the system.
- Trying to solve onboarding, troubleshooting, and reference use cases in one page.
- Hiding prerequisites, permissions, or environment assumptions until too late.

## Handoff cues
- Quickstart guide: prerequisites, setup steps, first success milestone, next steps.
- Time budget and difficulty level.
- Troubleshooting section for common setup issues.

## Example invocation
- Slash: `/doc_quickstart_guide <task>`
- Natural language: "Use quickstart Guide to write a fast-start guide that gets a new user to first success with minimal friction."
- Example: "Write the doc a real operator or user can follow on the first try."
- Example: "Turn support friction into a clearer quickstart, guide, or troubleshooting page."
- Often paired with: `doc_troubleshooting_guide`, `eng_docs_for_change`

## Quality bar

- A new user can go from zero to first success in under 15 minutes.
- Every step is verifiable: the user knows when they've done it right.
- Prerequisites are listed upfront, not discovered halfway through.
- The guide covers the happy path; troubleshooting handles the top 3 failure points.
- A frustrated user can find the answer they need within 60 seconds.
- Every code example is copy-pasteable and tested.
- The document states its audience, purpose, and prerequisites upfront.
- Content is structured for scanning, not sequential reading.
## Related workflows
- Docs system: `doc_information_architecture` → `doc_quickstart_guide` → `doc_troubleshooting_guide` → `doc_docs_feedback_loop`

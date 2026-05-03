---
name: doc_release_notes
description: "Turn raw changes into clear release notes grouped by user impact, risk, and next actions."
user-invocable: true
---

## Purpose
- Turn raw changes into clear release notes grouped by user impact, risk, and next actions.
- This is a **documentation specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a release, patch, or sprint delivered enough change to need customer-facing notes.

## Avoid when
- Do not paste commit logs at users and call it release notes.

## Inputs to gather
- Target reader, prerequisite knowledge, starting state, and desired success moment.
- Existing docs, product behavior, known support pain points, and terms that must stay consistent.
- Whether the output should optimize for fast start, troubleshooting, migration, or reference completeness.

## Operating rules
- Lead with user impact.
- Separate highlights, fixes, and breaking changes.
- Be honest about limits and follow-up work.

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
1. Collect the changes and affected users.
2. Group them by impact and urgency.
3. Write concise notes plus action items.
4. Return a release-notes draft ready for review.
## Output contract
- Highlights
- Fixes and changes
- Breaking changes or actions
- Known issues
- Reader-specific doc draft or outline with clear structure and next links.
- Known gaps, stale-risk notes, and what should be validated against the product.

## Failure modes to avoid
- Writing docs from assumptions instead of the real behavior of the system.
- Trying to solve onboarding, troubleshooting, and reference use cases in one page.
- Hiding prerequisites, permissions, or environment assumptions until too late.

## Handoff cues

- Release notes: version, date, changes by category, breaking changes, upgrade instructions.
- User-facing impact for each change.
- Link to migration guide if applicable.

## Example invocation
- Slash: `/doc_release_notes <task>`
- Natural language: "Use release Notes to turn raw changes into clear release notes grouped by user impact, risk, and next actions."
- Example: "Write the doc a real operator or user can follow on the first try."
- Example: "Turn support friction into a clearer quickstart, guide, or troubleshooting page."
- Often paired with: `doc_quickstart_guide`, `doc_troubleshooting_guide`, `eng_docs_for_change`

## Quality bar
- Release notes are good when users can tell what changed and what to do next.
- A frustrated user can find the answer they need within 60 seconds.
- Every code example is copy-pasteable and tested.
- The document states its audience, purpose, and prerequisites upfront.
- Content is structured for scanning, not sequential reading.
## Related workflows
- Docs system: `doc_information_architecture` → `doc_quickstart_guide` → `doc_troubleshooting_guide` → `doc_docs_feedback_loop`

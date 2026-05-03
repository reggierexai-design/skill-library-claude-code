---
name: doc_docs_feedback_loop
description: "Build a lightweight loop for finding missing, stale, or confusing documentation early."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udd01"}}
---

## Purpose
- Build a lightweight loop for finding missing, stale, or confusing documentation early.
- This is a **documentation specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when docs quality drifts because feedback is scattered or ignored.

## Avoid when
- Do not rely on gut feel when evidence about doc pain already exists.

## Inputs to gather
- Target reader, prerequisite knowledge, starting state, and desired success moment.
- Existing docs, product behavior, known support pain points, and terms that must stay consistent.
- Whether the output should optimize for fast start, troubleshooting, migration, or reference completeness.

## Operating rules
- Treat support pain and search misses as documentation signals.
- Close the loop with owners and review cadence.
- Fix the highest-friction pages first.

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
1. Define the main doc pain signals.
2. Set a capture, triage, and owner process.
3. Prioritize pages and fixes by user impact.
4. Return a docs feedback loop with cadence and owners.
## Output contract
- Signal sources
- Triage process
- Priority pages
- Cadence and owners
- Reader-specific doc draft or outline with clear structure and next links.
- Known gaps, stale-risk notes, and what should be validated against the product.

## Failure modes to avoid
- Writing docs from assumptions instead of the real behavior of the system.
- Trying to solve onboarding, troubleshooting, and reference use cases in one page.
- Hiding prerequisites, permissions, or environment assumptions until too late.

## Handoff cues

- Feedback loop report: sources, themes, priority fixes, content gaps.
- Recommended doc updates with priority.
- Process improvements for ongoing feedback collection.

## Example invocation
- Slash: `/doc_docs_feedback_loop <task>`
- Natural language: "Use docs Feedback Loop to build a lightweight loop for finding missing, stale, or confusing documentation early."
- Example: "Write the doc a real operator or user can follow on the first try."
- Example: "Turn support friction into a clearer quickstart, guide, or troubleshooting page."
- Often paired with: `doc_quickstart_guide`, `doc_troubleshooting_guide`, `eng_docs_for_change`

## Quality bar
- A useful feedback loop makes docs measurably easier to trust over time.
- A frustrated user can find the answer they need within 60 seconds.
- Every code example is copy-pasteable and tested.
- The document states its audience, purpose, and prerequisites upfront.
- Content is structured for scanning, not sequential reading.
## Related workflows
- Docs system: `doc_information_architecture` → `doc_quickstart_guide` → `doc_troubleshooting_guide` → `doc_docs_feedback_loop`

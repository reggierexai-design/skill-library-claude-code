---
name: doc_information_architecture
description: "Organize docs so users can find the right answer quickly by role, task, and depth."
user-invocable: true
---

## Purpose
- Organize docs so users can find the right answer quickly by role, task, and depth.
- This is a **documentation specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when documentation exists but readers cannot find what they need or keep asking the same questions.

## Avoid when
- Do not rearrange docs before understanding the real user journeys.

## Inputs to gather
- Target reader, prerequisite knowledge, starting state, and desired success moment.
- Existing docs, product behavior, known support pain points, and terms that must stay consistent.
- Whether the output should optimize for fast start, troubleshooting, migration, or reference completeness.

## Operating rules
- Organize around tasks and roles, not internal org charts.
- Keep tutorials, references, and troubleshooting distinct.
- Make the next click obvious.

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
1. Identify the core doc audiences and jobs.
2. Group content into a clearer structure.
3. Define navigation, page types, and cross-links.
4. Return a documentation IA with priority fixes.
## Output contract
- Audiences and jobs
- Content structure
- Navigation rules
- Priority fixes
- Reader-specific doc draft or outline with clear structure and next links.
- Known gaps, stale-risk notes, and what should be validated against the product.

## Failure modes to avoid
- Writing docs from assumptions instead of the real behavior of the system.
- Trying to solve onboarding, troubleshooting, and reference use cases in one page.
- Hiding prerequisites, permissions, or environment assumptions until too late.

## Handoff cues

- IA document: content inventory, taxonomy, navigation structure, cross-links.
- User journey mapping to content paths.
- Content gap analysis and prioritized creation plan.

## Example invocation
- Slash: `/doc_information_architecture <task>`
- Natural language: "Use documentation Information Architecture to organize docs so users can find the right answer quickly by role, task, and depth."
- Example: "Write the doc a real operator or user can follow on the first try."
- Example: "Turn support friction into a clearer quickstart, guide, or troubleshooting page."
- Often paired with: `doc_quickstart_guide`, `doc_troubleshooting_guide`, `eng_docs_for_change`

## Quality bar
- Good documentation architecture lowers support load and time-to-answer.
- A frustrated user can find the answer they need within 60 seconds.
- Every code example is copy-pasteable and tested.
- The document states its audience, purpose, and prerequisites upfront.
- Content is structured for scanning, not sequential reading.
## Related workflows
- Docs system: `doc_information_architecture` → `doc_quickstart_guide` → `doc_troubleshooting_guide` → `doc_docs_feedback_loop`

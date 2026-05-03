---
name: doc_migration_guide
description: "Write a migration path that explains what changed, who is affected, and how to upgrade safely."
user-invocable: true
---

## Purpose
- Write a migration path that explains what changed, who is affected, and how to upgrade safely.
- This is a **documentation specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a release changes APIs, workflows, pricing, permissions, or expectations.

## Avoid when
- Do not publish breaking changes without explicit upgrade guidance.

## Inputs to gather
- Target reader, prerequisite knowledge, starting state, and desired success moment.
- Existing docs, product behavior, known support pain points, and terms that must stay consistent.
- Whether the output should optimize for fast start, troubleshooting, migration, or reference completeness.

## Operating rules
- State the audience and impact clearly.
- Separate must-do steps from optional improvements.
- Call out rollback and compatibility windows.

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
1. Define the change set and affected users.
2. List required migration steps and checks.
3. Add compatibility, rollback, and FAQ sections.
4. Return a migration guide draft or outline.
## Output contract
- Affected audience
- Upgrade steps
- Compatibility and rollback notes
- FAQ topics
- Reader-specific doc draft or outline with clear structure and next links.
- Known gaps, stale-risk notes, and what should be validated against the product.

## Failure modes to avoid
- Writing docs from assumptions instead of the real behavior of the system.
- Trying to solve onboarding, troubleshooting, and reference use cases in one page.
- Hiding prerequisites, permissions, or environment assumptions until too late.

## Handoff cues
- Migration guide: current state, target state, step-by-step migration, breaking changes.
- Rollback instructions for each step.
- Timeline and support resources.

## Example invocation
- Slash: `/doc_migration_guide <task>`
- Natural language: "Use migration Guide to write a migration path that explains what changed, who is affected, and how to upgrade safely."
- Example: "Write the doc a real operator or user can follow on the first try."
- Example: "Turn support friction into a clearer quickstart, guide, or troubleshooting page."
- Often paired with: `doc_quickstart_guide`, `doc_troubleshooting_guide`, `eng_docs_for_change`

## Quality bar

- Every migration step is independently reversible — rollback at any point.
- Breaking changes are called out explicitly, not buried in prose.
- The guide is tested by someone who didn't write it.
- Timeline estimates account for the slowest reasonable scenario, not the fastest.
- A frustrated user can find the answer they need within 60 seconds.
- Every code example is copy-pasteable and tested.
- The document states its audience, purpose, and prerequisites upfront.
- Content is structured for scanning, not sequential reading.
## Related workflows
- Docs system: `doc_information_architecture` → `doc_quickstart_guide` → `doc_troubleshooting_guide` → `doc_docs_feedback_loop`

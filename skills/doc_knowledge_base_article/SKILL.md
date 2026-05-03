---
name: doc_knowledge_base_article
description: "Turn a recurring question into a support-ready article with clear steps and escalation cues."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udcd6"}}
---

## Purpose
- Turn a recurring question into a support-ready article with clear steps and escalation cues.
- This is a **documentation specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when support keeps answering the same question or workaround manually.

## Avoid when
- Do not write a KB article for issues that still need root-cause correction first.

## Inputs to gather
- Target reader, prerequisite knowledge, starting state, and desired success moment.
- Existing docs, product behavior, known support pain points, and terms that must stay consistent.
- Whether the output should optimize for fast start, troubleshooting, migration, or reference completeness.

## Operating rules
- Solve the reader problem fast.
- State symptoms, causes, steps, and escalation clearly.
- Write for scanning under pressure.

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
1. Define the user problem and symptom language.
2. List the known causes and the safest steps.
3. Add escalation cues and related links.
4. Return a publishable KB article or outline.
## Output contract
- Problem statement
- Symptoms and causes
- Resolution steps
- Escalation cues
- Reader-specific doc draft or outline with clear structure and next links.
- Known gaps, stale-risk notes, and what should be validated against the product.

## Failure modes to avoid
- Writing docs from assumptions instead of the real behavior of the system.
- Trying to solve onboarding, troubleshooting, and reference use cases in one page.
- Hiding prerequisites, permissions, or environment assumptions until too late.

## Handoff cues
- Article draft: title, problem statement, solution steps, screenshots, related articles.
- SEO metadata and target search terms.
- Review and freshness schedule.

## Example invocation
- Slash: `/doc_knowledge_base_article <task>`
- Natural language: "Use knowledge Base Article to turn a recurring question into a support-ready article with clear steps and escalation cues."
- Example: "Write the doc a real operator or user can follow on the first try."
- Example: "Turn support friction into a clearer quickstart, guide, or troubleshooting page."
- Often paired with: `doc_quickstart_guide`, `doc_troubleshooting_guide`, `eng_docs_for_change`

## Quality bar

- The article solves the user's problem without requiring them to read another article first.
- Steps are ordered and testable: the user can follow them and verify success at each step.
- Screenshots match the current UI version.
- The article is findable: title and metadata match how users search for this problem.
- A frustrated user can find the answer they need within 60 seconds.
- Every code example is copy-pasteable and tested.
- The document states its audience, purpose, and prerequisites upfront.
- Content is structured for scanning, not sequential reading.
## Related workflows
- Docs system: `doc_information_architecture` → `doc_quickstart_guide` → `doc_troubleshooting_guide` → `doc_docs_feedback_loop`

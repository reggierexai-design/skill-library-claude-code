---
name: doc_glossary_builder
description: "Build a shared glossary for terms, metrics, entities, and overloaded language across a project."
user-invocable: true
disable-model-invocation: true
---


# Documentation Glossary Builder

## Purpose
- Build a shared glossary for terms, metrics, entities, and overloaded language across a project.
- This is a **documentation specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use when teams or docs keep using the same words to mean different things.
- The main bottleneck is best solved through documentation work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not use when terminology is already stable and well-documented.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Target reader, prerequisite knowledge, starting state, and desired success moment.
- Existing docs, product behavior, known support pain points, and terms that must stay consistent.
- Whether the output should optimize for fast start, troubleshooting, migration, or reference completeness.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- Work from evidence in the workspace, the prompt, or verified sources.
- Keep the output decision-oriented rather than bloated.
- Name assumptions, risks, and unresolved questions explicitly.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Read the source behavior, UI copy, API shape, or runbook reality before writing documentation.
- Keep the happy path tight; move depth into links, reference sections, or follow-on docs.
- Make docs observable: the reader should know what success, failure, and next steps look like.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Define the exact slice of work in scope.
2. Gather the minimum evidence needed to reason safely.
3. Produce the plan, review, or artifact that best fits the task.
4. Check the output for gaps, regressions, or overclaiming.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

## Output contract
- Scope
- Key findings or plan
- Risks and assumptions
- Recommended next actions
- Reader-specific doc draft or outline with clear structure and next links.
- Known gaps, stale-risk notes, and what should be validated against the product.

## Failure modes to avoid
- Writing docs from assumptions instead of the real behavior of the system.
- Trying to solve onboarding, troubleshooting, and reference use cases in one page.
- Hiding prerequisites, permissions, or environment assumptions until too late.
- Declaring success before the output is usable by the next operator, owner, or decision-maker.

## Handoff cues
- State current status, remaining blockers, and the smallest next move.
- Name the files, pages, systems, or source material that another operator should read first.
- Flag approvals, missing evidence, or live-system access that still require a human decision.

## Example invocation
- Slash: `/doc_glossary_builder <task>`
- Natural language: "Use documentation Glossary Builder to build a shared glossary for terms, metrics, entities, and overloaded language across a project."
- Example: "Write the doc a real operator or user can follow on the first try."
- Example: "Turn support friction into a clearer quickstart, guide, or troubleshooting page."
- Often paired with: `doc_quickstart_guide`, `doc_troubleshooting_guide`, `eng_docs_for_change`

## Quality bar
- The result should be specific enough that another operator could act on it without guessing.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.

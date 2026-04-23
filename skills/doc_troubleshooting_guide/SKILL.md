---
name: doc_troubleshooting_guide
description: "Organize diagnosis by symptom, checks, and likely causes so users can recover methodically."
user-invocable: true
disable-model-invocation: true
---


# Troubleshooting Guide

## Purpose
- Organize diagnosis by symptom, checks, and likely causes so users can recover methodically.
- This is a **documentation specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use when users face repeated setup, runtime, or integration failures.
- The main bottleneck is best solved through documentation work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not dump raw logs without a diagnosis path.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Target reader, prerequisite knowledge, starting state, and desired success moment.
- Existing docs, product behavior, known support pain points, and terms that must stay consistent.
- Whether the output should optimize for fast start, troubleshooting, migration, or reference completeness.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- Troubleshooting should narrow uncertainty step by step.
- Order checks from common and safe to rare and invasive.
- Keep root-cause clues next to the relevant symptom.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Read the source behavior, UI copy, API shape, or runbook reality before writing documentation.
- Keep the happy path tight; move depth into links, reference sections, or follow-on docs.
- Make docs observable: the reader should know what success, failure, and next steps look like.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. List the recurring symptoms and environments.
2. Define the diagnostic checks and branch logic.
3. Map each branch to likely causes and fixes.
4. Return a troubleshooting guide structure or draft.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

## Output contract
- Symptoms
- Checks and branch logic
- Likely causes
- Escalation points
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
- Slash: `/doc_troubleshooting_guide <task>`
- Natural language: "Use troubleshooting Guide to organize diagnosis by symptom, checks, and likely causes so users can recover methodically."
- Example: "Write the doc a real operator or user can follow on the first try."
- Example: "Turn support friction into a clearer quickstart, guide, or troubleshooting page."
- Often paired with: `doc_quickstart_guide`, `eng_docs_for_change`

## Quality bar
- A good troubleshooting guide helps users prove what is wrong, not just try random fixes.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.

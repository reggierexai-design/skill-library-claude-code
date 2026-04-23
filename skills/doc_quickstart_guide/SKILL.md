---
name: doc_quickstart_guide
description: "Write a fast-start guide that gets a new user to first success with minimal friction."
user-invocable: true
disable-model-invocation: true
---


# Quickstart Guide

## Purpose
- Write a fast-start guide that gets a new user to first success with minimal friction.
- This is a **documentation specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use when a product or tool needs a clean first-run experience in documentation.
- The main bottleneck is best solved through documentation work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not stuff a quickstart with every edge case or architecture detail.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Target reader, prerequisite knowledge, starting state, and desired success moment.
- Existing docs, product behavior, known support pain points, and terms that must stay consistent.
- Whether the output should optimize for fast start, troubleshooting, migration, or reference completeness.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- Optimize for first success, not completeness.
- State prerequisites up front.
- Keep the happy path unbroken.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Read the source behavior, UI copy, API shape, or runbook reality before writing documentation.
- Keep the happy path tight; move depth into links, reference sections, or follow-on docs.
- Make docs observable: the reader should know what success, failure, and next steps look like.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Define the target new user and the first success moment.
2. List prerequisites and the shortest path.
3. Write the steps, checks, and next links.
4. Return a quickstart draft or outline.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

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
- Declaring success before the output is usable by the next operator, owner, or decision-maker.

## Handoff cues
- State current status, remaining blockers, and the smallest next move.
- Name the files, pages, systems, or source material that another operator should read first.
- Flag approvals, missing evidence, or live-system access that still require a human decision.

## Example invocation
- Slash: `/doc_quickstart_guide <task>`
- Natural language: "Use quickstart Guide to write a fast-start guide that gets a new user to first success with minimal friction."
- Example: "Write the doc a real operator or user can follow on the first try."
- Example: "Turn support friction into a clearer quickstart, guide, or troubleshooting page."
- Often paired with: `doc_troubleshooting_guide`, `eng_docs_for_change`

## Quality bar
- A good quickstart gets a motivated user from zero to proof quickly.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.

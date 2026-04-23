---
name: des_accessibility_review
description: "Review flows for accessibility risks in navigation, semantics, contrast, content, and feedback."
user-invocable: true
disable-model-invocation: false
---


# Accessibility Review

## Purpose
- Review flows for accessibility risks in navigation, semantics, contrast, content, and feedback.
- This is a **design specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use when a UI, document, or workflow may exclude users with different access needs.
- The main bottleneck is best solved through design work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not treat accessibility as a last-minute color check only.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Target user state, screen or flow, product goal, and any platform or brand constraints.
- Existing screens, components, copy, research, and accessibility or localization requirements.
- What decision is needed now: critique, brief, direction, spec, or usability plan.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- Accessibility includes navigation, meaning, timing, and feedback.
- Prefer structural fixes over labels on broken interactions.
- Call out blockers before nice-to-haves.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Read the product context and surrounding flow before critiquing or proposing a design change.
- Anchor design decisions in hierarchy, clarity, accessibility, and completion of the user task.
- Keep design outputs specific enough that product and engineering can act on them.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Map the flow and the interaction patterns.
2. Review high-risk accessibility areas and blockers.
3. Rank issues by severity and fixability.
4. Return a practical accessibility review.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

## Output contract
- Flow reviewed
- Accessibility issues
- Severity and fixes
- Follow-up checks
- Actionable critique, brief, spec, or copy direction tied to user outcomes.
- Priority issues, rationale, and the smallest next design move.

## Failure modes to avoid
- Confusing taste with user-centered rationale.
- Critiquing a single screen while ignoring the surrounding flow and state transitions.
- Producing abstract design language with no implementable next step.
- Declaring success before the output is usable by the next operator, owner, or decision-maker.

## Handoff cues
- State current status, remaining blockers, and the smallest next move.
- Name the files, pages, systems, or source material that another operator should read first.
- Flag approvals, missing evidence, or live-system access that still require a human decision.

## Example invocation
- Slash: `/des_accessibility_review <task>`
- Natural language: "Use accessibility Review to review flows for accessibility risks in navigation, semantics, contrast, content, and feedback."
- Example: "Review this flow for clarity, hierarchy, and completion risk."
- Example: "Translate the product problem into a buildable design brief or wireframe spec."
- Often paired with: `des_design_brief`, `des_design_critique`

## Quality bar
- A good accessibility review finds real barriers early enough to fix them.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.

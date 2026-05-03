---
name: des_accessibility_review
description: "Review flows for accessibility risks in navigation, semantics, contrast, content, and feedback."
user-invocable: true
---

## Purpose
- Review flows for accessibility risks in navigation, semantics, contrast, content, and feedback.
- This is a **design specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a UI, document, or workflow may exclude users with different access needs.

## Avoid when
- Do not treat accessibility as a last-minute color check only.

## Inputs to gather
- Target user state, screen or flow, product goal, and any platform or brand constraints.
- Existing screens, components, copy, research, and accessibility or localization requirements.
- What decision is needed now: critique, brief, direction, spec, or usability plan.

## Operating rules
- Accessibility includes navigation, meaning, timing, and feedback.
- Prefer structural fixes over labels on broken interactions.
- Call out blockers before nice-to-haves.

- Design for the most common path first, then handle edge cases. Optimizing for edge cases creates mediocre mainstream experiences.
- Every design decision should be traceable to a user need or a brand principle. Decorative decisions without rationale accumulate as design debt.
- Consistency reduces cognitive load. A consistent mediocre pattern beats an inconsistent brilliant one.
- Accessibility is not optional. If a design excludes users with disabilities, it fails regardless of its aesthetic quality.
- Test with real users, not stakeholders. Stakeholder preferences are not user needs.
## Claude Code tool pattern
- Read the product context and surrounding flow before critiquing or proposing a design change.
- Anchor design decisions in hierarchy, clarity, accessibility, and completion of the user task.
- Keep design outputs specific enough that product and engineering can act on them.

## Expanded workflow
1. Map the flow and the interaction patterns.
2. Review high-risk accessibility areas and blockers.
3. Rank issues by severity and fixability.
4. Return a practical accessibility review.
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

## Handoff cues
- Accessibility audit: WCAG criteria, pass/fail, severity, remediation steps.
- Priority-ordered fix list.
- Testing tool recommendations.

## Example invocation
- Slash: `/des_accessibility_review <task>`
- Natural language: "Use accessibility Review to review flows for accessibility risks in navigation, semantics, contrast, content, and feedback."
- Example: "Review this flow for clarity, hierarchy, and completion risk."
- Example: "Translate the product problem into a buildable design brief or wireframe spec."
- Often paired with: `des_design_brief`, `des_design_critique`

## Quality bar

- All WCAG 2.1 AA criteria are checked; AAA criteria are flagged as enhancements.
- Issues are prioritized by user impact: blocking, major, or minor.
- Every issue has a specific remediation step, not just a standards reference.
- Keyboard navigation and screen reader flow are tested, not just color contrast.
- Every design decision traces to a user need or brand principle.
- The most common user path is optimized first.
- Accessibility requirements are met (WCAG 2.1 AA minimum).
- The design has been tested or is ready to test with real users.
## Related workflows
- Design flow: `des_design_brief` → `des_wireframe_spec` → `des_design_critique` → `des_usability_test_plan`

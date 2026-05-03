---
name: des_design_critique
description: "Critique a design against goals, hierarchy, clarity, and flow instead of taste alone."
user-invocable: true
---

## Purpose
- Critique a design against goals, hierarchy, clarity, and flow instead of taste alone.
- This is a **design specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when reviewing a screen, flow, or concept that needs disciplined feedback.

## Avoid when
- Do not critique without a goal, audience, or use context.

## Inputs to gather
- Target user state, screen or flow, product goal, and any platform or brand constraints.
- Existing screens, components, copy, research, and accessibility or localization requirements.
- What decision is needed now: critique, brief, direction, spec, or usability plan.

## Operating rules
- Judge the design against the job it must do.
- Separate clarity issues from aesthetic preferences.
- Rank the issues that most affect outcomes.

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
1. State the design goal and audience.
2. Review the design against the task flow.
3. Identify the biggest clarity and interaction issues.
4. Return ranked critique with suggested improvements.
## Output contract
- Goal and context
- Top issues
- Why they matter
- Suggested improvements
- Actionable critique, brief, spec, or copy direction tied to user outcomes.
- Priority issues, rationale, and the smallest next design move.

## Failure modes to avoid
- Confusing taste with user-centered rationale.
- Critiquing a single screen while ignoring the surrounding flow and state transitions.
- Producing abstract design language with no implementable next step.

## Handoff cues
- Critique summary: strengths, issues, severity, specific recommendations.
- Priority-ordered improvement list.
- Any user research or data supporting critique points.

## Example invocation
- Slash: `/des_design_critique <task>`
- Natural language: "Use design Critique to critique a design against goals, hierarchy, clarity, and flow instead of taste alone."
- Example: "Review this flow for clarity, hierarchy, and completion risk."
- Example: "Translate the product problem into a buildable design brief or wireframe spec."
- Often paired with: `des_design_brief`, `des_accessibility_review`

## Quality bar

- Every critique point references a specific design element and a user or business outcome.
- Strengths and issues are both documented — critique is not just a bug list.
- Severity ratings separate must-fix from nice-to-have.
- Recommendations are actionable: what to change, not just what's wrong.
- Every design decision traces to a user need or brand principle.
- The most common user path is optimized first.
- Accessibility requirements are met (WCAG 2.1 AA minimum).
- The design has been tested or is ready to test with real users.
## Related workflows
- Design flow: `des_design_brief` → `des_wireframe_spec` → `des_design_critique` → `des_usability_test_plan`

---
name: des_visual_direction
description: "Set the visual tone, references, and constraints for a cohesive design direction."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\uddbc\ufe0f"}}
---

## Purpose
- Set the visual tone, references, and constraints for a cohesive design direction.
- This is a **design specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a product or campaign needs a clearer look and feel before detailed mockups.

## Avoid when
- Do not confuse inspiration hunting with a usable direction.

## Inputs to gather
- Target user state, screen or flow, product goal, and any platform or brand constraints.
- Existing screens, components, copy, research, and accessibility or localization requirements.
- What decision is needed now: critique, brief, direction, spec, or usability plan.

## Operating rules
- Visual direction should support the product promise.
- Use references to clarify decisions, not copy them.
- Name what to avoid as well as what to pursue.

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
1. Define the intended emotional and functional signal.
2. Select reference themes and anti-patterns.
3. Set typography, color, and motion directions at a high level.
4. Return a crisp visual direction brief.
## Output contract
- Desired signal
- Reference themes
- Core visual principles
- Anti-patterns and constraints
- Actionable critique, brief, spec, or copy direction tied to user outcomes.
- Priority issues, rationale, and the smallest next design move.

## Failure modes to avoid
- Confusing taste with user-centered rationale.
- Critiquing a single screen while ignoring the surrounding flow and state transitions.
- Producing abstract design language with no implementable next step.

## Handoff cues

- Visual direction document: mood, palette, typography, imagery, motion principles.
- Reference examples with annotations.
- Implementation notes for design system integration.

## Example invocation
- Slash: `/des_visual_direction <task>`
- Natural language: "Use visual Direction to set the visual tone, references, and constraints for a cohesive design direction."
- Example: "Review this flow for clarity, hierarchy, and completion risk."
- Example: "Translate the product problem into a buildable design brief or wireframe spec."
- Often paired with: `des_design_brief`, `des_design_critique`, `des_accessibility_review`

## Quality bar
- A useful visual direction gives teams a shared taste without handcuffing execution.
- Every design decision traces to a user need or brand principle.
- The most common user path is optimized first.
- Accessibility requirements are met (WCAG 2.1 AA minimum).
- The design has been tested or is ready to test with real users.
## Related workflows
- Design flow: `des_design_brief` → `des_wireframe_spec` → `des_design_critique` → `des_usability_test_plan`

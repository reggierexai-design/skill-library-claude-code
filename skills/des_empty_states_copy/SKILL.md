---
name: des_empty_states_copy
description: "Write empty-state copy that teaches the next step without sounding robotic or needy."
user-invocable: true
metadata: {"openclaw":{"emoji":"\u270d\ufe0f"}}
---

## Purpose
- Write empty-state copy that teaches the next step without sounding robotic or needy.
- This is a **design specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a product screen has no data, no projects, no results, or no activity yet.

## Avoid when
- Do not waste empty states on generic filler.

## Inputs to gather
- Target user state, screen or flow, product goal, and any platform or brand constraints.
- Existing screens, components, copy, research, and accessibility or localization requirements.
- What decision is needed now: critique, brief, direction, spec, or usability plan.

## Operating rules
- Explain the state and the best next action.
- Keep the tone confident and brief.
- Match the user context and product promise.

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
1. Identify the empty-state scenario and user mindset.
2. Draft concise copy and the best CTA.
3. Check the copy against the product tone and flow.
4. Return a small set of strong options.
## Output contract
- Scenario
- Primary copy
- CTA options
- Tone notes
- Actionable critique, brief, spec, or copy direction tied to user outcomes.
- Priority issues, rationale, and the smallest next design move.

## Failure modes to avoid
- Confusing taste with user-centered rationale.
- Critiquing a single screen while ignoring the surrounding flow and state transitions.
- Producing abstract design language with no implementable next step.

## Handoff cues

- Empty state inventory: screens, scenarios, copy, CTAs for each.
- Tone guidelines for empty vs error vs loading states.
- Implementation notes for developers.

## Example invocation
- Slash: `/des_empty_states_copy <task>`
- Natural language: "Use empty States Copy to write empty-state copy that teaches the next step without sounding robotic or needy."
- Example: "Review this flow for clarity, hierarchy, and completion risk."
- Example: "Translate the product problem into a buildable design brief or wireframe spec."
- Often paired with: `des_design_brief`, `des_design_critique`, `des_accessibility_review`

## Quality bar
- Good empty-state copy reduces hesitation and gets users moving again.
- Every design decision traces to a user need or brand principle.
- The most common user path is optimized first.
- Accessibility requirements are met (WCAG 2.1 AA minimum).
- The design has been tested or is ready to test with real users.
## Related workflows
- Design flow: `des_design_brief` → `des_wireframe_spec` → `des_design_critique` → `des_usability_test_plan`

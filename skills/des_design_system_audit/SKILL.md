---
name: des_design_system_audit
description: "Audit a design system for inconsistency, missing states, adoption friction, and maintenance burden."
user-invocable: true
---

## Purpose
- Audit a design system for inconsistency, missing states, adoption friction, and maintenance burden.
- This is a **design specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a product has a component library or emerging design system that feels inconsistent or costly.

## Avoid when
- Do not use when there is no reusable design surface to audit.

## Inputs to gather
- Target user state, screen or flow, product goal, and any platform or brand constraints.
- Existing screens, components, copy, research, and accessibility or localization requirements.
- What decision is needed now: critique, brief, direction, spec, or usability plan.

## Operating rules
- Audit what's actually used, not what's documented. The real design system is what ships, not what's in Figma.
- Gaps are as important as inconsistencies. Patterns that exist in production but not in the system create drift.
- Prioritize by adoption impact. Fixing the 3 most-used components helps more than adding 10 obscure ones.
- Include documentation gaps. An undocumented component is an unadoptable component.

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
1. Inventory all components: design system vs production.
2. Audit consistency: are components used correctly across products?
3. Identify gaps: production patterns not in the system.
4. Assess documentation: which components lack specs?
5. Measure adoption: which teams use the system and which build custom?
6. Prioritize fixes: consistency > gaps > documentation > new components.

## Output contract
- Actionable critique, brief, spec, or copy direction tied to user outcomes.
- Priority issues, rationale, and the smallest next design move.

## Failure modes to avoid
- Confusing taste with user-centered rationale.
- Critiquing a single screen while ignoring the surrounding flow and state transitions.
- Producing abstract design language with no implementable next step.

## Handoff cues
- Audit report: components inventoried, inconsistencies found, gaps identified.
- Recommended additions and deprecations.
- Naming and documentation standardization plan.

## Example invocation
- Slash: `/des_design_system_audit <task>`
- Natural language: "Use design System Audit to audit a design system for inconsistency, missing states, adoption friction, and maintenance burden."
- Example: "Review this flow for clarity, hierarchy, and completion risk."
- Example: "Translate the product problem into a buildable design brief or wireframe spec."
- Often paired with: `des_design_brief`, `des_design_critique`, `des_accessibility_review`

## Quality bar
## Related workflows
- Design flow: `des_design_brief` â†’ `des_wireframe_spec` â†’ `des_design_critique` â†’ `des_usability_test_plan`
- Every design decision traces to a user need or brand principle.
- The most common user path is optimized first.
- Accessibility requirements are met (WCAG 2.1 AA minimum).
- The design has been tested or is ready to test with real users.

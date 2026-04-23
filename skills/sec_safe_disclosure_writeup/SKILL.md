---
name: sec_safe_disclosure_writeup
description: "Write a precise security issue report with impact, evidence, and safe remediation guidance."
user-invocable: true
disable-model-invocation: true
---


# Security Safe Disclosure Writeup

## Purpose
- Write a precise security issue report with impact, evidence, and safe remediation guidance.
- This is a **security specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use when documenting a security issue for maintainers, internal teams, or responsible disclosure.
- The main bottleneck is best solved through security work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not use to write exploitation instructions or public proof-of-concept detail.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Asset surface, trust boundaries, auth paths, data sensitivity, and exposure assumptions.
- Relevant architecture, permissions, logging behavior, third-party dependencies, and recent changes.
- Whether the task is a review, audit, threat model, disclosure note, or remediation prioritization.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- Work from evidence in the workspace, the prompt, or verified sources.
- Keep the output decision-oriented rather than bloated.
- Name assumptions, risks, and unresolved questions explicitly.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Read the real data flow, auth model, config, and dependency surface before naming security posture.
- Prioritize exploitability, impact, and exposure over abstract checklist compliance.
- Return remediation advice that fits the actual system and ownership model.
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
- Security review or model with risk ranking, exposure logic, and remediation direction.
- Assumptions, open questions, and where human security review is still required.

## Failure modes to avoid
- Calling something secure because the right buzzwords are present.
- Treating every finding as equally urgent or equally exploitable.
- Writing findings with no threat story, impact path, or remediation owner.
- Declaring success before the output is usable by the next operator, owner, or decision-maker.

## Handoff cues
- State current status, remaining blockers, and the smallest next move.
- Name the files, pages, systems, or source material that another operator should read first.
- Flag approvals, missing evidence, or live-system access that still require a human decision.

## Example invocation
- Slash: `/sec_safe_disclosure_writeup <task>`
- Natural language: "Use security Safe Disclosure Writeup to write a precise security issue report with impact, evidence, and safe remediation guidance."
- Example: "Review this surface like a real security operator, not a checklist generator."
- Example: "Tell me the plausible threats, likely exposures, and highest-value mitigations."
- Often paired with: `sec_threat_model`, `sec_appsec_review`, `safe_high_impact_changes`

## Quality bar
- The result should be specific enough that another operator could act on it without guessing.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.

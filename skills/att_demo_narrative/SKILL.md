---
name: att_demo_narrative
description: "Turn a product demo into a story with stakes, payoff, and memorable product proof."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udce3"}}
---

## Purpose
- Turn a product demo into a story with stakes, payoff, and memorable product proof.

## Use when
- Use for launch demos, sales demos, recorded walkthroughs, or homepage product storytelling.

## Avoid when
- Do not use when the product flow itself is still too broken to demonstrate credibly.

## Inputs to gather
- The demo flow: what product capability to show, in what order, toward what conclusion.
- Audience context: technical buyers, business buyers, or mixed? What do they already believe?
- The hook: what tension or problem does the demo resolve?
- The proof moment: where in the demo does the product prove its value?
- Objection context: what are buyers skeptical about before seeing the demo?

## Operating rules
- A demo is a story, not a screen recording.
- Show the pain, the turning point, and the payoff.
- Pick the smallest path that proves the product's value.

## Claude Code tool pattern
- Use `WebFetch` to research competitor content and current platform conventions.
- Read existing site copy, product pages, and proof assets before drafting so output fits the real product truth.
- When external claims appear, verify before publishing with `safe_external_claims`.
- After drafting, run `att_proof_mining` to verify every claim has backing.

## Expanded workflow
1. Choose the audience and demo objective.
2. Select the core flow and proof moments.
3. Write the narrative beats and transitions.
4. Return a demo script or storyboard.
## Output contract
- Audience and objective
- Narrative beats
- Proof moments
- Close and next step
## Failure modes to avoid
- Feature tours disguised as demos — showing everything, telling nothing.
- No before state — jumping to the solution without establishing the problem.
- Over-rehearsed to the point of feeling scripted; under-rehearsed to the point of breaking.
- No failure recovery — when the demo breaks, the narrative dies too.

## Handoff cues
- Provide the demo script and flow with timing per section.
- Name the failure recovery plan and the backup narrative.
- Flag any product capabilities that need to be working reliably before the demo can be given live.

## Example invocation
- Slash: `/att_demo_narrative <task>`
- Natural language: "Use demo Narrative to turn a product demo into a story with stakes, payoff, and memorable product proof."
- Example: "Turn this product walkthrough into a 5-minute demo with a story arc."
- Example: "I am demoing at a conference. Script a narrative that handles the top 3 objections live."
- Often paired with: `att_message_house`, `att_launch_plan`, `att_proof_mining`

## Quality bar

- The demo tells one clear story with problem, mechanism, and result.
- A viewer can summarize the demo in one sentence afterward.
- The demo has a failure recovery plan.
- Both full (5-8 min) and short (2-3 min) versions available.

## Related workflows
- Content system: `att_message_house` → `att_content_calendar` → `att_content_repurposing`
- Launch sequence: `att_launch_plan` → `att_proof_mining` → `att_thread_writer`
- Proof deployment: `att_proof_mining` → `att_case_study_builder` → `att_social_proof_pack`

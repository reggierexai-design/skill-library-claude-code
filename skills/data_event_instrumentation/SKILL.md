---
name: data_event_instrumentation
description: "Plan events, properties, and naming so analytics data stays trustworthy and useful."
user-invocable: true
disable-model-invocation: true
---


# Data Event Instrumentation

## Purpose
- Plan events, properties, and naming so analytics data stays trustworthy and useful.
- This is a **data specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use when a product needs better event tracking or the current taxonomy is messy.
- The main bottleneck is best solved through data work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not add events without naming rules, ownership, and data consumers in mind.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Business question, metric definitions, time windows, segments, and source systems involved.
- Known anomalies, dashboard complaints, experiment context, or instrumentation limits.
- What level of confidence is needed before a decision is made from the analysis.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- Track decisions, not every click.
- Name events consistently and define properties precisely.
- Avoid collecting sensitive data without a clear reason.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Lock definitions before comparing numbers; many data disagreements are really definition disagreements.
- Inspect lineage, joins, filters, and freshness assumptions before trusting a chart or query output.
- Return the smallest analysis or instrumentation change that increases confidence in the decision.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Define the product questions and funnel points.
2. Name the events and required properties.
3. Set implementation and QA rules.
4. Return an instrumentation plan with examples.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

## Output contract
- Event list
- Properties
- Naming rules
- QA checklist
- Decision-oriented analysis plan, readout, or instrumentation recommendation.
- Definition notes, caveats, and the next check needed to trust the result.

## Failure modes to avoid
- Analyzing a metric whose definition is still moving.
- Explaining a number shift without ruling out pipeline or instrumentation breakage.
- Returning dashboards or queries that look busy but do not answer the actual question.
- Declaring success before the output is usable by the next operator, owner, or decision-maker.

## Handoff cues
- State current status, remaining blockers, and the smallest next move.
- Name the files, pages, systems, or source material that another operator should read first.
- Flag approvals, missing evidence, or live-system access that still require a human decision.

## Example invocation
- Slash: `/data_event_instrumentation <task>`
- Natural language: "Use data Event Instrumentation to plan events, properties, and naming so analytics data stays trustworthy and useful."
- Example: "Turn this vague data question into a trustworthy analysis path."
- Example: "Tell me whether the problem is real behavior, bad instrumentation, or a reporting artifact."
- Often paired with: `data_analysis_plan`, `data_metric_definition`, `data_anomaly_triage`

## Quality bar
- Good instrumentation creates dependable analysis instead of a noisy event graveyard.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.

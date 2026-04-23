---
name: data_analysis_plan
description: "Turn a vague data question into a scoped analysis plan with metrics, cuts, and checks."
user-invocable: true
disable-model-invocation: false
---


# Data Analysis Plan

## Purpose
- Turn a vague data question into a scoped analysis plan with metrics, cuts, and checks.
- This is a **data specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use when someone wants insight from data but the question, metric, or slice is still fuzzy.
- The main bottleneck is best solved through data work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not jump into charts or SQL before defining the decision the analysis should support.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Business question, metric definitions, time windows, segments, and source systems involved.
- Known anomalies, dashboard complaints, experiment context, or instrumentation limits.
- What level of confidence is needed before a decision is made from the analysis.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- Start from a decision, not a dashboard.
- Define grain, segments, and time windows early.
- Include checks for bias, missingness, and bad joins.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Lock definitions before comparing numbers; many data disagreements are really definition disagreements.
- Inspect lineage, joins, filters, and freshness assumptions before trusting a chart or query output.
- Return the smallest analysis or instrumentation change that increases confidence in the decision.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Define the decision and target metric.
2. List the required data, cuts, and comparisons.
3. Add data quality and interpretation checks.
4. Return a scoped analysis plan with next steps.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

## Output contract
- Decision and question
- Metrics and cuts
- Checks and caveats
- Execution plan
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
- Slash: `/data_analysis_plan <task>`
- Natural language: "Use data Analysis Plan to turn a vague data question into a scoped analysis plan with metrics, cuts, and checks."
- Example: "Turn this vague data question into a trustworthy analysis path."
- Example: "Tell me whether the problem is real behavior, bad instrumentation, or a reporting artifact."
- Often paired with: `data_metric_definition`, `data_anomaly_triage`

## Quality bar
- A good analysis plan prevents wasted queries and misleading conclusions.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.

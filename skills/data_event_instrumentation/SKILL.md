---
name: data_event_instrumentation
description: "Plan events, properties, and naming so analytics data stays trustworthy and useful."
user-invocable: true
---

## Purpose
- Plan events, properties, and naming so analytics data stays trustworthy and useful.
- This is a **data specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a product needs better event tracking or the current taxonomy is messy.

## Avoid when
- Do not add events without naming rules, ownership, and data consumers in mind.

## Inputs to gather
- Business question, metric definitions, time windows, segments, and source systems involved.
- Known anomalies, dashboard complaints, experiment context, or instrumentation limits.
- What level of confidence is needed before a decision is made from the analysis.

## Operating rules
- Track decisions, not every click.
- Name events consistently and define properties precisely.
- Avoid collecting sensitive data without a clear reason.

- Check data quality before analyzing. Dirty data produces dirty insights. Verify null counts, outlier ranges, and schema drift first.
- Distinguish between correlation and causation in every finding. A spike that coincides with a launch is not caused by the launch without a controlled comparison.
- Present confidence intervals, not just point estimates. An average without variance is a single number pretending to be information.
- Every metric needs a clear definition, a data source, and a known limitation.
- Prefer simple analyses that answer the question over complex analyses that impress but confuse.
## Claude Code tool pattern
- Lock definitions before comparing numbers; many data disagreements are really definition disagreements.
- Inspect lineage, joins, filters, and freshness assumptions before trusting a chart or query output.
- Return the smallest analysis or instrumentation change that increases confidence in the decision.

## Expanded workflow
1. Define the product questions and funnel points.
2. Name the events and required properties.
3. Set implementation and QA rules.
4. Return an instrumentation plan with examples.
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

## Handoff cues

- Instrumentation plan: events, properties, triggers, validation rules.
- Implementation checklist for each event.
- QA verification steps.

## Example invocation
- Slash: `/data_event_instrumentation <task>`
- Natural language: "Use data Event Instrumentation to plan events, properties, and naming so analytics data stays trustworthy and useful."
- Example: "Turn this vague data question into a trustworthy analysis path."
- Example: "Tell me whether the problem is real behavior, bad instrumentation, or a reporting artifact."
- Often paired with: `data_analysis_plan`, `data_metric_definition`, `data_anomaly_triage`

## Quality bar
- Good instrumentation creates dependable analysis instead of a noisy event graveyard.
- Data quality checks are run before any analysis is presented.
- Findings distinguish correlation from causation.
- Confidence intervals or variance measures accompany all point estimates.
- Every metric has a definition, source, and known limitation.
## Related workflows
- Analytics build: `data_analysis_plan` → `data_metric_definition` → `data_dashboard_brief`
- Data quality: `data_quality_checks` → `data_pipeline_triage` → `data_anomaly_triage`

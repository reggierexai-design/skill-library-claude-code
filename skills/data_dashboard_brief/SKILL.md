---
name: data_dashboard_brief
description: "Design a dashboard that supports action, ownership, and review cadence instead of vanity views."
user-invocable: true
---

## Purpose
- Design a dashboard that supports action, ownership, and review cadence instead of vanity views.
- This is a **data specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when building or fixing a dashboard for operators, leaders, or product teams.

## Avoid when
- Do not add widgets before defining who will act on the signals.

## Inputs to gather
- Business question, metric definitions, time windows, segments, and source systems involved.
- Known anomalies, dashboard complaints, experiment context, or instrumentation limits.
- What level of confidence is needed before a decision is made from the analysis.

## Operating rules
- Every chart should answer a real question.
- Separate overview, diagnosis, and drill-down.
- Show targets, comparisons, and freshness where they matter.

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
1. Define the dashboard audience and review ritual.
2. Pick the core metrics and supporting diagnostics.
3. Specify layout, filters, and annotations.
4. Return a dashboard brief ready for implementation.
## Output contract
- Audience and cadence
- Metrics and visuals
- Layout and filters
- Instrumentation gaps
- Decision-oriented analysis plan, readout, or instrumentation recommendation.
- Definition notes, caveats, and the next check needed to trust the result.

## Failure modes to avoid
- Analyzing a metric whose definition is still moving.
- Explaining a number shift without ruling out pipeline or instrumentation breakage.
- Returning dashboards or queries that look busy but do not answer the actual question.

## Handoff cues

- Dashboard brief: audience, key metrics, layout, filters, update cadence.
- Data source mapping for each widget.
- Any data pipeline dependencies.

## Example invocation
- Slash: `/data_dashboard_brief <task>`
- Natural language: "Use data Dashboard Brief to design a dashboard that supports action, ownership, and review cadence instead of vanity views."
- Example: "Turn this vague data question into a trustworthy analysis path."
- Example: "Tell me whether the problem is real behavior, bad instrumentation, or a reporting artifact."
- Often paired with: `data_analysis_plan`, `data_metric_definition`, `data_anomaly_triage`

## Quality bar
- A useful dashboard changes weekly behavior instead of decorating a screen.
- Data quality checks are run before any analysis is presented.
- Findings distinguish correlation from causation.
- Confidence intervals or variance measures accompany all point estimates.
- Every metric has a definition, source, and known limitation.
## Related workflows
- Analytics build: `data_analysis_plan` → `data_metric_definition` → `data_dashboard_brief`
- Data quality: `data_quality_checks` → `data_pipeline_triage` → `data_anomaly_triage`

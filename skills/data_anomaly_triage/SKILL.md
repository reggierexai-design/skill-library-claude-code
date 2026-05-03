---
name: data_anomaly_triage
description: "Triage a surprising metric change by checking definitions, pipelines, seasonality, and real behavior."
user-invocable: true
---

## Purpose
- Triage a surprising metric change by checking definitions, pipelines, seasonality, and real behavior.
- This is a **data specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a dashboard spike or drop could be either a real signal or a data problem.

## Avoid when
- Do not send teams chasing ghosts before checking instrumentation and freshness.

## Inputs to gather
- Business question, metric definitions, time windows, segments, and source systems involved.
- Known anomalies, dashboard complaints, experiment context, or instrumentation limits.
- What level of confidence is needed before a decision is made from the analysis.

## Operating rules
- Assume neither bug nor business change until tested.
- Check the boring explanations first.
- Preserve an audit trail of what was ruled out.

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
1. Define the anomaly window and affected metrics.
2. Check freshness, definitions, and pipeline health.
3. Compare neighboring metrics and segments.
4. Return the likely cause and recommended next checks.
## Output contract
- Anomaly summary
- Checks performed
- Likely causes
- Next actions
- Decision-oriented analysis plan, readout, or instrumentation recommendation.
- Definition notes, caveats, and the next check needed to trust the result.

## Failure modes to avoid
- Analyzing a metric whose definition is still moving.
- Explaining a number shift without ruling out pipeline or instrumentation breakage.
- Returning dashboards or queries that look busy but do not answer the actual question.

## Handoff cues

- Anomaly report: what's anomalous, likely cause, severity.
- Recommended investigation steps.
- Monitoring adjustments to catch recurrence.

## Example invocation
- Slash: `/data_anomaly_triage <task>`
- Natural language: "Use data Anomaly Triage to triage a surprising metric change by checking definitions, pipelines, seasonality, and real behavior."
- Example: "Turn this vague data question into a trustworthy analysis path."
- Example: "Tell me whether the problem is real behavior, bad instrumentation, or a reporting artifact."
- Often paired with: `data_analysis_plan`, `data_metric_definition`

## Quality bar
- Good anomaly triage gets to credible causes before narratives harden.
- Data quality checks are run before any analysis is presented.
- Findings distinguish correlation from causation.
- Confidence intervals or variance measures accompany all point estimates.
- Every metric has a definition, source, and known limitation.
## Related workflows
- Analytics build: `data_analysis_plan` → `data_metric_definition` → `data_dashboard_brief`
- Data quality: `data_quality_checks` → `data_pipeline_triage` → `data_anomaly_triage`

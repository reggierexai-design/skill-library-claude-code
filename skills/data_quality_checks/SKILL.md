---
name: data_quality_checks
description: "Design recurring checks for freshness, completeness, consistency, and metric integrity."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udccf"}}
---

## Purpose
- Design recurring checks for freshness, completeness, consistency, and metric integrity.
- This is a **data specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a pipeline, dashboard, or experiment needs trustable data over time.

## Avoid when
- Do not use when no recurring data asset or metric needs monitoring.

## Inputs to gather
- Business question, metric definitions, time windows, segments, and source systems involved.
- Known anomalies, dashboard complaints, experiment context, or instrumentation limits.
- What level of confidence is needed before a decision is made from the analysis.

## Operating rules
- Check data quality at ingestion, not just at query time. Bad data that enters the system corrupts everything downstream.
- Automate repetitive checks. If you're manually validating the same schema every day, write a script.
- Distinguish between data quality (is the data correct?) and data completeness (is the data all there?). They need different checks.
- Quality thresholds should be explicit and measured, not vibes.

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
1. Define the data sources and their expected schemas.
2. Identify quality dimensions: completeness, accuracy, consistency, timeliness, uniqueness.
3. Write checks for each dimension: null counts, value ranges, cross-field consistency, freshness.
4. Set thresholds: what level of quality is acceptable vs what triggers an alert?
5. Automate the checks to run on ingestion or on a schedule.
6. Create a dashboard or alert system for quality failures.

## Output contract
- Decision-oriented analysis plan, readout, or instrumentation recommendation.
- Definition notes, caveats, and the next check needed to trust the result.

## Failure modes to avoid
- Analyzing a metric whose definition is still moving.
- Explaining a number shift without ruling out pipeline or instrumentation breakage.
- Returning dashboards or queries that look busy but do not answer the actual question.

## Handoff cues
- Data quality report: checks run, pass/fail, anomalies found.
- Recommended fixes for any quality issues.
- Ongoing monitoring plan for data quality.

## Example invocation
- Slash: `/data_quality_checks <task>`
- Natural language: "Use data Quality Checks to design recurring checks for freshness, completeness, consistency, and metric integrity."
- Example: "Turn this vague data question into a trustworthy analysis path."
- Example: "Tell me whether the problem is real behavior, bad instrumentation, or a reporting artifact."
- Often paired with: `data_analysis_plan`, `data_metric_definition`, `data_anomaly_triage`

## Quality bar
## Related workflows
- Analytics build: `data_analysis_plan` â†’ `data_metric_definition` â†’ `data_dashboard_brief`
- Data quality: `data_quality_checks` â†’ `data_pipeline_triage` â†’ `data_anomaly_triage`
- Data quality checks are run before any analysis is presented.
- Findings distinguish correlation from causation.
- Confidence intervals or variance measures accompany all point estimates.
- Every metric has a definition, source, and known limitation.
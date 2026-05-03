---
name: data_analysis_plan
description: "Turn a vague data question into a scoped analysis plan with metrics, cuts, and checks."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udcca"}}
---

## Purpose
- Turn a vague data question into a scoped analysis plan with metrics, cuts, and checks.
- This is a **data specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when someone wants insight from data but the question, metric, or slice is still fuzzy.

## Avoid when
- Do not jump into charts or SQL before defining the decision the analysis should support.

## Inputs to gather
- Business question, metric definitions, time windows, segments, and source systems involved.
- Known anomalies, dashboard complaints, experiment context, or instrumentation limits.
- What level of confidence is needed before a decision is made from the analysis.

## Operating rules
- Start from a decision, not a dashboard.
- Define grain, segments, and time windows early.
- Include checks for bias, missingness, and bad joins.

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
1. Define the decision and target metric.
2. List the required data, cuts, and comparisons.
3. Add data quality and interpretation checks.
4. Return a scoped analysis plan with next steps.
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

## Handoff cues
- Analysis plan: questions, data sources, methods, expected outputs.
- Data quality assessment.
- Timeline and priority of analyses.

## Example invocation
- Slash: `/data_analysis_plan <task>`
- Natural language: "Use data Analysis Plan to turn a vague data question into a scoped analysis plan with metrics, cuts, and checks."
- Example: "Turn this vague data question into a trustworthy analysis path."
- Example: "Tell me whether the problem is real behavior, bad instrumentation, or a reporting artifact."
- Often paired with: `data_metric_definition`, `data_anomaly_triage`

## Quality bar

- Every analysis question maps to a specific data source and metric.
- The plan distinguishes between exploratory and confirmatory analysis.
- Sample size and statistical power are addressed before analysis begins.
- Results can be reproduced from the documented steps.
- Data quality checks are run before any analysis is presented.
- Findings distinguish correlation from causation.
- Confidence intervals or variance measures accompany all point estimates.
- Every metric has a definition, source, and known limitation.
## Related workflows
- Analytics build: `data_analysis_plan` → `data_metric_definition` → `data_dashboard_brief`
- Data quality: `data_quality_checks` → `data_pipeline_triage` → `data_anomaly_triage`

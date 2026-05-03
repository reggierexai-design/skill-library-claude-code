---
name: data_sql_query_plan
description: "Turn an analysis question into a query plan with tables, joins, filters, and validation checks."
user-invocable: true
---

## Purpose
- Turn an analysis question into a query plan with tables, joins, filters, and validation checks.
- This is a **data specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when the user needs SQL help but the real data shape is not yet mapped.

## Avoid when
- Do not write complex SQL from memory before confirming the schema and grain.

## Inputs to gather
- Business question, metric definitions, time windows, segments, and source systems involved.
- Known anomalies, dashboard complaints, experiment context, or instrumentation limits.
- What level of confidence is needed before a decision is made from the analysis.

## Operating rules
- Start from the row grain.
- Make joins explicit and testable.
- Plan validation queries before the final query.

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
1. Define the target output and grain.
2. Map the tables, joins, and filters.
3. Add validation checks and edge cases.
4. Return a query plan or staged query outline.
## Output contract
- Target output
- Table and join map
- Validation checks
- Query outline
- Decision-oriented analysis plan, readout, or instrumentation recommendation.
- Definition notes, caveats, and the next check needed to trust the result.

## Failure modes to avoid
- Analyzing a metric whose definition is still moving.
- Explaining a number shift without ruling out pipeline or instrumentation breakage.
- Returning dashboards or queries that look busy but do not answer the actual question.

## Handoff cues
- SQL query plan: question, query structure, tables, joins, filters.
- Performance considerations for large tables.
- Validation approach for query correctness.

## Example invocation
- Slash: `/data_sql_query_plan <task>`
- Natural language: "Use data SQL Query Plan to turn an analysis question into a query plan with tables, joins, filters, and validation checks."
- Example: "Turn this vague data question into a trustworthy analysis path."
- Example: "Tell me whether the problem is real behavior, bad instrumentation, or a reporting artifact."
- Often paired with: `data_analysis_plan`, `data_metric_definition`, `data_anomaly_triage`

## Quality bar

- The query plan addresses performance before it becomes a production issue.
- JOINs are explicit and indexed; no cross-joins or Cartesian products.
- Results are validated against a known sample or manual calculation.
- The query is readable and maintainable by another analyst.
- Data quality checks are run before any analysis is presented.
- Findings distinguish correlation from causation.
- Confidence intervals or variance measures accompany all point estimates.
- Every metric has a definition, source, and known limitation.
## Related workflows
- Analytics build: `data_analysis_plan` → `data_metric_definition` → `data_dashboard_brief`
- Data quality: `data_quality_checks` → `data_pipeline_triage` → `data_anomaly_triage`

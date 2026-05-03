---
name: data_metric_definition
description: "Write a metric definition that is consistent across teams, tools, and review meetings."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83d\udcd0"}}
---

## Purpose
- Write a metric definition that is consistent across teams, tools, and review meetings.
- This is a **data specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a metric is disputed, overloaded, or implemented differently across reports.

## Avoid when
- Do not treat a label like a definition.

## Inputs to gather
- Business question, metric definitions, time windows, segments, and source systems involved.
- Known anomalies, dashboard complaints, experiment context, or instrumentation limits.
- What level of confidence is needed before a decision is made from the analysis.

## Operating rules
- Define the numerator, denominator, grain, and exclusions.
- State the owner, cadence, and source of truth.
- Call out how the metric can be gamed.

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
1. Name the metric and the question it answers.
2. Write the calculation, scope, and exclusions.
3. Add ownership, cadence, and caveats.
4. Return a clean metric definition ready for adoption.
## Output contract
- Metric purpose
- Calculation
- Scope and exclusions
- Owner and caveats
- Decision-oriented analysis plan, readout, or instrumentation recommendation.
- Definition notes, caveats, and the next check needed to trust the result.

## Failure modes to avoid
- Analyzing a metric whose definition is still moving.
- Explaining a number shift without ruling out pipeline or instrumentation breakage.
- Returning dashboards or queries that look busy but do not answer the actual question.

## Handoff cues
- Metric definition document: name, formula, data source, calculation, thresholds.
- Responsible owner and review cadence.
- Known caveats and limitations.

## Example invocation
- Slash: `/data_metric_definition <task>`
- Natural language: "Use data Metric Definition to write a metric definition that is consistent across teams, tools, and review meetings."
- Example: "Turn this vague data question into a trustworthy analysis path."
- Example: "Tell me whether the problem is real behavior, bad instrumentation, or a reporting artifact."
- Often paired with: `data_analysis_plan`, `data_anomaly_triage`

## Quality bar

- Every metric has a formula, data source, and owner.
- Edge cases are documented: how are nulls, duplicates, and time boundaries handled?
- The metric is calculable from available data — no aspirational metrics that can't be measured.
- A change in the metric can be traced to a specific business action.
- Data quality checks are run before any analysis is presented.
- Findings distinguish correlation from causation.
- Confidence intervals or variance measures accompany all point estimates.
- Every metric has a definition, source, and known limitation.
## Related workflows
- Analytics build: `data_analysis_plan` → `data_metric_definition` → `data_dashboard_brief`
- Data quality: `data_quality_checks` → `data_pipeline_triage` → `data_anomaly_triage`

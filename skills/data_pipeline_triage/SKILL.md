---
name: data_pipeline_triage
description: "Triage broken or delayed data flows by isolating the failing stage and recovery options."
user-invocable: true
---

## Purpose
- Triage broken or delayed data flows by isolating the failing stage and recovery options.
- This is a **data specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when scheduled data jobs, transformations, or reports are failing or late.

## Avoid when
- Do not rewrite the whole pipeline during active triage.

## Inputs to gather
- Business question, metric definitions, time windows, segments, and source systems involved.
- Known anomalies, dashboard complaints, experiment context, or instrumentation limits.
- What level of confidence is needed before a decision is made from the analysis.

## Operating rules
- Contain impact before optimizing architecture.
- Identify the first failing stage, not every downstream symptom.
- Separate data correctness from freshness.

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
1. Map the pipeline stages and the current failure.
2. Locate the first broken handoff or dependency.
3. Propose the safest recovery path.
4. Return recovery steps plus hardening ideas.
## Output contract
- Affected pipeline stage
- Likely cause
- Recovery plan
- Hardening ideas
- Decision-oriented analysis plan, readout, or instrumentation recommendation.
- Definition notes, caveats, and the next check needed to trust the result.

## Failure modes to avoid
- Analyzing a metric whose definition is still moving.
- Explaining a number shift without ruling out pipeline or instrumentation breakage.
- Returning dashboards or queries that look busy but do not answer the actual question.

## Handoff cues
- Pipeline triage: what's broken, root cause hypothesis, severity.
- Recommended fix and verification steps.
- Monitoring improvements to catch future issues earlier.

## Example invocation
- Slash: `/data_pipeline_triage <task>`
- Natural language: "Use data Pipeline Triage to triage broken or delayed data flows by isolating the failing stage and recovery options."
- Example: "Turn this vague data question into a trustworthy analysis path."
- Example: "Tell me whether the problem is real behavior, bad instrumentation, or a reporting artifact."
- Often paired with: `data_analysis_plan`, `data_metric_definition`, `data_anomaly_triage`

## Quality bar

- The root cause is identified before any fix is attempted.
- Data freshness SLA is known and the triage measures time to recovery against it.
- Downstream consumers are notified before they discover the issue themselves.
- The fix addresses the root cause, not just the symptom.
- Data quality checks are run before any analysis is presented.
- Findings distinguish correlation from causation.
- Confidence intervals or variance measures accompany all point estimates.
- Every metric has a definition, source, and known limitation.
## Related workflows
- Analytics build: `data_analysis_plan` → `data_metric_definition` → `data_dashboard_brief`
- Data quality: `data_quality_checks` → `data_pipeline_triage` → `data_anomaly_triage`

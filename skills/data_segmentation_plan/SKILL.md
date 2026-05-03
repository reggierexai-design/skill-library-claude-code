---
name: data_segmentation_plan
description: "Plan how to segment users, accounts, or events so analysis reveals actionable differences."
user-invocable: true
---

## Purpose
- Plan how to segment users, accounts, or events so analysis reveals actionable differences.
- This is a **data specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when aggregate metrics hide differences across audience, plan, cohort, or behavior.

## Avoid when
- Do not use when the question is already answered by a single obvious slice.

## Inputs to gather
- Business question, metric definitions, time windows, segments, and source systems involved.
- Known anomalies, dashboard complaints, experiment context, or instrumentation limits.
- What level of confidence is needed before a decision is made from the analysis.

## Operating rules
- Segments must be actionable. If you can't treat a segment differently, it's not a segment â€” it's a label.
- Start with behavioral segments, not demographic ones. What people do is more predictive than who they are.
- Segment size matters. Segments too small to analyze or too small to target aren't useful.
- Validate segments with holdout tests. Do segmented campaigns actually outperform unsegmented ones?

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
1. Define the segmentation goal: what decision will segments inform?
2. Choose segmentation approach: behavioral, demographic, psychographic, or value-based.
3. Identify the data signals available for segmentation.
4. Build initial segments and measure their distinctiveness.
5. Validate: do segments differ meaningfully in behavior or outcomes?
6. Size each segment: are they large enough to act on?
7. Document segment profiles with actionable characteristics.

## Output contract
- Decision-oriented analysis plan, readout, or instrumentation recommendation.
- Definition notes, caveats, and the next check needed to trust the result.

## Failure modes to avoid
- Analyzing a metric whose definition is still moving.
- Explaining a number shift without ruling out pipeline or instrumentation breakage.
- Returning dashboards or queries that look busy but do not answer the actual question.

## Handoff cues
- Segmentation plan: segments defined, criteria, data sources, analysis methods.
- Validation approach for segment quality.
- Recommended actions per segment.

## Example invocation
- Slash: `/data_segmentation_plan <task>`
- Natural language: "Use data Segmentation Plan to plan how to segment users, accounts, or events so analysis reveals actionable differences."
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

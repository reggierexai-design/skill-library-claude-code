---
name: data_experiment_readout
description: "Read an experiment with effect size, uncertainty, caveats, and next actions instead of hype."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83e\uddea"}}
---

## Purpose
- Read an experiment with effect size, uncertainty, caveats, and next actions instead of hype.
- This is a **data specialist** for OpenClaw operators who need a result that can survive review, handoff, or execution.

## Use when
- Use when a test has ended and the team needs a disciplined readout.

## Avoid when
- Do not declare victory from noise or partial rollout data.

## Inputs to gather
- Business question, metric definitions, time windows, segments, and source systems involved.
- Known anomalies, dashboard complaints, experiment context, or instrumentation limits.
- What level of confidence is needed before a decision is made from the analysis.

## Operating rules
- Effect size matters more than p-value theater.
- State exposure, duration, and contamination risks.
- Tie conclusions to concrete next actions.

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
1. Summarize the test setup and exposure.
2. Interpret the primary and secondary results.
3. Note caveats, risks, and confidence level.
4. Return a decision-ready readout with next steps.
## Output contract
- Test summary
- Results and effect size
- Caveats
- Recommended action
- Decision-oriented analysis plan, readout, or instrumentation recommendation.
- Definition notes, caveats, and the next check needed to trust the result.

## Failure modes to avoid
- Analyzing a metric whose definition is still moving.
- Explaining a number shift without ruling out pipeline or instrumentation breakage.
- Returning dashboards or queries that look busy but do not answer the actual question.

## Handoff cues
- Experiment readout: hypothesis, results, statistical significance, recommendation.
- Segment analysis if applicable.
- Follow-up experiment suggestions.

## Example invocation
- Slash: `/data_experiment_readout <task>`
- Natural language: "Use data Experiment Readout to read an experiment with effect size, uncertainty, caveats, and next actions instead of hype."
- Example: "Turn this vague data question into a trustworthy analysis path."
- Example: "Tell me whether the problem is real behavior, bad instrumentation, or a reporting artifact."
- Often paired with: `data_analysis_plan`, `data_metric_definition`, `data_anomaly_triage`

## Quality bar

- Statistical significance is reported with confidence intervals, not just p-values.
- The readout separates signal from noise: primary metric first, supporting metrics second.
- Segment analysis is included but doesn't override the primary result.
- The recommendation is clear: ship, iterate, or kill — no hedging.
- Data quality checks are run before any analysis is presented.
- Findings distinguish correlation from causation.
- Confidence intervals or variance measures accompany all point estimates.
- Every metric has a definition, source, and known limitation.
## Related workflows
- Analytics build: `data_analysis_plan` → `data_metric_definition` → `data_dashboard_brief`
- Data quality: `data_quality_checks` → `data_pipeline_triage` → `data_anomaly_triage`

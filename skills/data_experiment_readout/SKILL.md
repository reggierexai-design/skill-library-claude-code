---
name: data_experiment_readout
description: "Read an experiment with effect size, uncertainty, caveats, and next actions instead of hype."
user-invocable: true
disable-model-invocation: false
---


# Data Experiment Readout

## Purpose
- Read an experiment with effect size, uncertainty, caveats, and next actions instead of hype.
- This is a **data specialist** for Claude Code users who need a result that can survive review, handoff, or execution.
- Prefer this skill when a structured operating pass will outperform a generic answer.

## Use when
- Use when a test has ended and the team needs a disciplined readout.
- The main bottleneck is best solved through data work rather than generic brainstorming.
- There is enough context to act, or the first useful move is to identify what is missing.

## Avoid when
- Do not declare victory from noise or partial rollout data.
- Do not use it to add ceremony when a short direct answer would solve the task.
- Stop and re-route if the task crosses into a higher-risk domain than this skill is meant to handle alone.

## Inputs to gather
- Business question, metric definitions, time windows, segments, and source systems involved.
- Known anomalies, dashboard complaints, experiment context, or instrumentation limits.
- What level of confidence is needed before a decision is made from the analysis.
- Acceptance threshold: what would make the output ready for use, review, or handoff.

## Operating rules
- Effect size matters more than p-value theater.
- State exposure, duration, and contamination risks.
- Tie conclusions to concrete next actions.
- Separate facts, assumptions, and recommendations so the operator can see what is proven versus inferred.
- Prefer the smallest sufficient move that improves clarity, decision quality, or execution momentum.
- When context is stale or incomplete, name the gap instead of hiding it inside confident language.

## Claude Code tool pattern
- Lock definitions before comparing numbers; many data disagreements are really definition disagreements.
- Inspect lineage, joins, filters, and freshness assumptions before trusting a chart or query output.
- Return the smallest analysis or instrumentation change that increases confidence in the decision.
- Keep the workspace state legible: summarize touched files, consulted sources, and checks performed when they materially affect trust.

## Expanded workflow
1. Summarize the test setup and exposure.
2. Interpret the primary and secondary results.
3. Note caveats, risks, and confidence level.
4. Return a decision-ready readout with next steps.
5. Check the draft against the original request and remove anything that does not change the outcome.
6. End with the exact next action, follow-up check, or approval path.

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
- Declaring success before the output is usable by the next operator, owner, or decision-maker.

## Handoff cues
- State current status, remaining blockers, and the smallest next move.
- Name the files, pages, systems, or source material that another operator should read first.
- Flag approvals, missing evidence, or live-system access that still require a human decision.

## Example invocation
- Slash: `/data_experiment_readout <task>`
- Natural language: "Use data Experiment Readout to read an experiment with effect size, uncertainty, caveats, and next actions instead of hype."
- Example: "Turn this vague data question into a trustworthy analysis path."
- Example: "Tell me whether the problem is real behavior, bad instrumentation, or a reporting artifact."
- Often paired with: `data_analysis_plan`, `data_metric_definition`, `data_anomaly_triage`

## Quality bar
- A good experiment readout makes overconfidence difficult.
- The result should reduce ambiguity or risk, not merely add more words.
- A good pass leaves a clear next action, owner, or verification step.

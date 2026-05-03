---
name: eng_performance_probe
description: "Find the dominant performance bottleneck before suggesting optimization work."
user-invocable: true
---

## Purpose
- Find the dominant performance bottleneck before suggesting optimization work.

## Use when
- Use when the user reports slowness, expensive queries, laggy rendering, or poor throughput.

## Avoid when
- Do not use when the problem is correctness, not performance.

## Inputs to gather

- Performance symptom: slow endpoint, high CPU, memory growth, or latency spike.
- Baseline metrics: what are normal performance numbers for this system?
- Load profile: what's the traffic pattern when the issue appears?
- Recent changes: deployments, config changes, data volume shifts.
- Available profiling tools: APM, profiler, flame graphs, tracing.

## Operating rules
- Measure first. Guess second.
- Optimize the main bottleneck, not the most visible code.
- Keep the cost model explicit: CPU, network, memory, IO, or rendering.

- Read the code and the error before proposing a fix. Diagnose first, treat second.
- Prefer the minimal change that solves the problem. Every line added is a line that can break.
- Test the fix, test the surrounding area, test the edge cases. A fix that works for the happy path only is not a fix.
- Document why, not just what. Future engineers need to understand the reasoning, not just see the change.
- If the fix takes longer than 30 minutes, stop and reconsider the approach. Complex fixes usually indicate the wrong diagnosis.
## Claude Code tool pattern
- Use `Bash` to run diagnostic commands, read logs, and check system state.
- Use `Read` to inspect source files, configs, and error output directly.
- Use `Edit` for targeted code changes. Prefer `eng_minimal_patch` scope discipline.
- After changes, use `eng_test_strategy` to verify the fix works and nothing else broke.

## Expanded workflow
1. Define the performance symptom and target path.
2. Measure or inspect the hot path.
3. Identify the dominant bottleneck.
4. Recommend the smallest effective optimization sequence.
## Output contract
- Symptom
- Hot path
- Dominant bottleneck
- Optimization plan
- Implementation note, review note, or fix plan tied to specific files and checks.
- Verification evidence, remaining risks, and rollback or next-step notes when relevant.

## Failure modes to avoid

- Optimizing without measuring — guessing at bottlenecks leads to wasted effort.
- Micro-optimizing code that's not the bottleneck — fix the biggest consumer first.
- Testing performance without realistic load — synthetic benchmarks lie.
- Ignoring N+1 queries — the most common performance killer in web apps.
- No baseline — without before measurements, you can't prove the fix worked.

## Handoff cues

- Performance report: bottleneck identified, data supporting it.
- Fix applied with before/after measurements.
- Any secondary bottlenecks noted for future work.
- Performance regression test or monitoring added.

## Example invocation
- Slash: `/eng_performance_probe <task>`
- Natural language: "Use performance Probe to find the dominant performance bottleneck before suggesting optimization work."
- Example: "Use this before editing code so we touch the minimum safe surface."
- Example: "Review the change and tell me what could break, not just what looks nice."
- Often paired with: `eng_repo_onboarding`, `eng_minimal_patch`, `eng_test_strategy`

## Quality bar
- A performance answer is useful only when the bottleneck is real.
- The fix is the smallest change that resolves the issue without introducing new problems.
- Root cause is identified and documented, not just the symptom.
- Tests cover the fix, the regression, and at least one edge case.
- The change is reviewable in under 10 minutes.
## Related workflows
- Debug chain: `eng_bug_triage` → `eng_debug_systematically` → `eng_minimal_patch` → `eng_test_strategy`
- Release safety: `eng_release_readiness` → `eng_code_review_pass` → `eng_feature_flag_rollout`

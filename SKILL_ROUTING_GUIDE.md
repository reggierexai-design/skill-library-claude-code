# Skill Routing Guide

## Use an internal/core skill when
- you need planning, handoff, review, recovery, or bounded execution
- the request is broad and needs decomposition first
- the next action is not yet obvious

## Use a slash-first specialist when
- the user is asking for a specific workflow
- the work has side effects
- the workflow benefits from deliberate invocation
- you want a narrow method rather than broad ambient guidance

## Good routing examples

- vague bug -> `eng_bug_triage` then `eng_debug_systematically`
- upcoming launch -> `att_launch_plan` + `doc_release_notes` + `ops_launch_retrospective`
- risky change -> `safe_high_impact_changes` + `sec_threat_model` + `qa_release_smoke_test`

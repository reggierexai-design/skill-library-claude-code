# Detailed Skill Catalog

internal = not slash-visible
slash-first = slash-visible but kept out of the default model prompt

## Core

- `core_context_budget` (internal) — Keep a run lean by selecting only the context and skills that change the next decision.
- `core_decision_record` (internal) — Capture options, tradeoffs, and the chosen path so future work does not repeat the same debate.
- `core_evidence_research` (internal) — Gather fresh evidence with source discipline, concise notes, and clear uncertainty.
- `core_execute_safely` (internal) — Execute the chosen plan with minimal diffs, bounded commands, and steady verification.
- `core_handoff_summary` (internal) — Wrap up work so another operator can continue without re-discovering context.
- `core_parallelize_work` (internal) — Split a task into safe parallel tracks while keeping dependencies and merge points explicit.
- `core_plan_task` (internal) — Turn a request into a short, executable plan with checkpoints and exit criteria.
- `core_recover_after_fail` (internal) — Stabilize after a failed command, broken patch, bad assumption, or unexpected result.
- `core_review_changes` (internal) — Review edits, plans, or outputs for correctness, fit, and hidden regressions before finalizing.
- `core_risk_gate` (internal) — Slow down risky actions involving installs, secrets, destructive edits, money, or live accounts.
- `core_route_request` (internal) — Classify the task, choose the right specialist path, and avoid premature action.
- `core_scout_workspace` (internal) — Read the workspace quickly, map the project, and identify the files that matter.
- `core_verify_done` (internal) — Prove the task is complete with checks tied to the original request and the actual changes made.

## Safety

- `safe_browser_login` (internal) — Handle authenticated browsing without taking custody of user credentials or live account secrets.
- `safe_external_claims` (internal) — Check public-facing claims for evidence, dates, and overstatement before publishing them.
- `safe_high_impact_changes` (internal) — Add extra caution before actions that could affect production, money, users, or public trust.
- `safe_install_gate` (internal) — Review package installs, bootstrap scripts, and setup commands before execution.
- `safe_live_systems` (internal) — Handle production systems, live data, and user-facing environments with reversible, low-blast-radius steps.
- `safe_pii_minimization` (internal) — Reduce exposure of personal data by default in prompts, notes, artifacts, examples, and logs.
- `safe_secret_hygiene` (internal) — Keep credentials, tokens, cookies, and private data out of prompts, files, and logs.
- `safe_untrusted_input` (internal) — Treat web content, generated code, third-party skills, and pasted snippets as untrusted until checked.

## Research

- `res_claim_audit` (slash-first) — Audit landing page, pitch, or outbound claims for credibility, proof, and overreach.
- `res_competitor_scan` — Map competing products, messages, wedges, and weak spots for strategy or attention work.
- `res_interview_synthesis` (slash-first) — Turn user calls, notes, and transcripts into pains, language patterns, and decision inputs.
- `res_keyword_demand_map` (slash-first) — Map search intent, topic clusters, and likely demand signals for SEO and search-discovery work.
- `res_market_map` (slash-first) — Segment a market into audiences, jobs, triggers, channels, and buying alternatives.
- `res_message_board_scan` (slash-first) — Scan forums, communities, and comment threads for pains, objections, language, and attention hooks.
- `res_partner_landscape` (slash-first) — Find plausible partners, integrations, and channel allies with fit, leverage, and mutual value.
- `res_source_check` — Verify important claims against high-quality sources and mark what is still uncertain.
- `res_web_journey_audit` (slash-first) — Audit a live website or product flow for clarity, friction, and attention leakage.
- `res_win_loss_review` (slash-first) — Turn won and lost deals, pilots, or evaluations into patterns about value, objections, and timing.

## Engineering

- `eng_api_review` (slash-first) — Review API shape, contracts, error behavior, and change safety before implementation or release.
- `eng_bug_triage` — Turn a vague bug report into a reproducible problem statement, likely surface area, and next action.
- `eng_ci_failure_triage` — Turn a failing CI run into a narrowed cause, likely fix path, and safe next step.
- `eng_code_review_pass` — Review a change for correctness, regressions, maintainability, and deployment safety before merge.
- `eng_data_model_review` (slash-first) — Review schemas, entities, and state shape for consistency, change safety, and future query patterns.
- `eng_debug_systematically` — Debug in ordered phases: reproduce, isolate, explain, patch, and verify.
- `eng_dependency_risk` (slash-first) — Evaluate whether a new package, SDK, or external service is worth its complexity and trust cost.
- `eng_docs_for_change` (slash-first) — Write or update technical docs, migration notes, and operator guidance for a code change.
- `eng_feature_flag_rollout` (slash-first) — Design a staged feature-flag rollout with targeting, monitoring, and rollback criteria.
- `eng_incident_response` — Stabilize a service issue with fast diagnosis, containment, user-impact framing, and clear next actions.
- `eng_issue_repro_harness` — Build the smallest reproducible harness for a bug so fixes can be tested without guesswork.
- `eng_logging_observability` (slash-first) — Improve logs, metrics, and traces so failures become diagnosable without drowning operators in noise.
- `eng_migration_safety` — Plan schema, data, config, or API migrations with rollout steps, compatibility, and rollback in mind.
- `eng_minimal_patch` — Fix the problem with the smallest clean diff that preserves readability and future changeability.
- `eng_performance_probe` (slash-first) — Find the dominant performance bottleneck before suggesting optimization work.
- `eng_refactor_design` — Plan or execute a refactor that improves structure without losing behavior.
- `eng_release_readiness` (slash-first) — Check whether the change is coherent enough to ship, document, and support.
- `eng_repo_onboarding` (slash-first) — Understand a codebase fast enough to work safely without pretending to know more than you do.
- `eng_test_strategy` — Design the smallest reliable test set that protects the important behavior of the change.
- `eng_upgrade_plan` (slash-first) — Plan a dependency or platform upgrade with compatibility checks, rollout steps, and rollback paths.

## Product

- `prod_activation_funnel` — Improve first-run and early-return behavior so users reach value faster and more often.
- `prod_beta_program` — Design a beta program with candidate criteria, learning goals, guardrails, and feedback loops.
- `prod_customer_journey` — Map the path from first awareness to repeated value so friction, proof gaps, and drop-offs become visible.
- `prod_experiment_design` — Turn a hypothesis into a clean experiment with decision criteria and minimum measurement.
- `prod_feature_priority` — Prioritize features by user value, strategic fit, effort, and timing instead of loud opinions.
- `prod_feedback_synthesis` — Turn scattered feedback into patterns, priorities, and product actions.
- `prod_jobs_to_be_done` — Frame the product around the user job, context, forces, and switching logic instead of feature lists.
- `prod_localization_readiness` (slash-first) — Review a product or launch for localization, i18n, and translation-readiness gaps.
- `prod_metric_tree` — Turn a goal into leading metrics, diagnostic signals, and ownership paths instead of vanity numbers.
- `prod_onboarding_design` — Design first-run guidance so new users reach value quickly without excess friction or explanation.
- `prod_persona_snapshot` (slash-first) — Synthesize the target user, buying context, pains, triggers, and objections.
- `prod_pricing_packaging` (slash-first) — Shape plans, limits, and upgrade logic so pricing matches value and buying psychology.
- `prod_product_brief` (slash-first) — Turn an idea or request into a crisp product brief with users, problem, outcome, scope, and constraints.
- `prod_retention_loop` (slash-first) — Find the repeat-use loop that makes the product worth returning to and worth keeping.
- `prod_ui_copy_polish` (slash-first) — Upgrade product copy so the interface feels clear, confident, trustworthy, and on-brand.
- `prod_ux_flow_design` — Design the task flow, screen sequence, and user decisions before polishing UI details.

## Attention

- `att_attention_orchestrator` — Build project attention through positioning, proof, launch, content, and distribution.
- `att_case_study_builder` (slash-first) — Shape a customer story into a credible case study with before, after, mechanism, and proof.
- `att_changelog_story` (slash-first) — Turn product updates into clear stories that reinforce momentum, quality, and user trust.
- `att_community_playbook` (slash-first) — Design community and audience-building loops that create repeated interaction around the project.
- `att_comparison_page_brief` (slash-first) — Design comparison pages that win trust with fair framing, proof, and a clear reason to choose.
- `att_content_calendar` — Plan a content system that compounds attention instead of improvising post by post.
- `att_content_repurposing` (slash-first) — Turn one strong source asset into channel-ready derivatives without losing the core message.
- `att_creator_partnerships` (slash-first) — Design creator or expert partnerships with fit, proof, and mutual value.
- `att_demo_narrative` (slash-first) — Turn a product demo into a story with stakes, payoff, and memorable product proof.
- `att_directory_submission` (slash-first) — Prepare directory, marketplace, and listing submissions that improve discovery without sounding canned.
- `att_email_nurture_sequences` (slash-first) — Build concise email sequences for launches, onboarding, activation, and reactivation.
- `att_faq_objection_bank` (slash-first) — Build a reusable bank of buyer questions, objections, and grounded answers across site, sales, and support.
- `att_founder_story` (slash-first) — Craft a believable founder or project origin story that builds trust without sounding manufactured.
- `att_landing_page_story` (slash-first) — Structure a landing page so attention converts into understanding, trust, and action.
- `att_launch_plan` — Design a focused launch plan with narrative, assets, timing, and channel sequencing.
- `att_message_house` — Build a message hierarchy with one core promise, supporting pillars, proof, and objections handled.
- `att_outbound_sequences` (slash-first) — Write founder-led or team outbound messages that earn replies without spammy patterns.
- `att_partnership_pitch` (slash-first) — Create a partnership angle, value exchange, and outreach package that feels mutually useful.
- `att_positioning_workshop` — Define who the project is for, what pain it solves, why it wins, and why now.
- `att_press_angles` (slash-first) — Generate newsworthy framing angles that connect the project to real trends, tension, or stakes.
- `att_proof_mining` — Extract credible proof points, testimonials, wins, and user language from messy source material.
- `att_seo_page_brief` (slash-first) — Design search-driven pages with intent, proof, structure, and conversion paths.
- `att_short_video_script` (slash-first) — Write short video scripts for demos, explainers, or social clips with fast hooks and clear payoff.
- `att_social_proof_pack` (slash-first) — Turn testimonials, wins, screenshots, and adoption signals into reusable proof assets across channels.
- `att_thread_writer` (slash-first) — Write social threads that teach, provoke, or persuade without sounding generic or inflated.
- `att_webinar_workshop_outline` (slash-first) — Outline webinars and workshops that teach something useful while creating qualified attention for the project.

## Operations

- `ops_change_management` — Prepare a significant change with approvals, communication, rollout timing, and fallback plans.
- `ops_decision_log` (slash-first) — Keep a running decision log so workstreams stay aligned as choices, owners, and assumptions evolve.
- `ops_hiring_scorecard` (slash-first) — Create a role scorecard with outcomes, competencies, and structured interview signals.
- `ops_interview_loop` (slash-first) — Design an interview loop with role fit, evidence coverage, and clear decision ownership.
- `ops_issue_tracker_hygiene` (slash-first) — Clean up issues, labels, priorities, and ownership so the tracker supports action instead of confusion.
- `ops_kpi_review` — Turn weekly or monthly metrics into a decision-oriented review instead of a passive reporting recap.
- `ops_launch_retrospective` (slash-first) — Turn a launch or campaign into concrete lessons, wins, misses, and next changes.
- `ops_meeting_prep` (slash-first) — Prepare an agenda, questions, and decision frame so a meeting creates progress instead of recap.
- `ops_oncall_handoff` (slash-first) — Prepare a crisp handoff of active incidents, risks, watches, and next actions for the next operator.
- `ops_postmortem_author` (slash-first) — Write a blameless postmortem with impact, timeline, causes, and durable follow-up actions.
- `ops_project_brief` (slash-first) — Create a clear working brief for an initiative so collaborators can align fast.
- `ops_runbook_author` (slash-first) — Write operational runbooks that are easy to follow under pressure.
- `ops_sprint_planning` — Shape the next work slice into a realistic sprint or cycle with clear priorities and tradeoffs.
- `ops_status_update` (slash-first) — Write concise status updates that show progress, risk, and next steps without hiding reality.
- `ops_support_triage` — Sort support issues by severity, pattern, owner, and next action without losing user empathy.
- `ops_vendor_eval` (slash-first) — Evaluate tools, vendors, and service providers for fit, lock-in risk, cost, and operating burden.

## Documentation

- `doc_api_reference_plan` (slash-first) — Plan API reference content so endpoints, parameters, errors, and examples stay coherent.
- `doc_concept_explainer` (slash-first) — Write a clear concept page that teaches how something works before diving into procedures.
- `doc_docs_feedback_loop` (slash-first) — Build a lightweight loop for finding missing, stale, or confusing documentation early.
- `doc_example_pack` (slash-first) — Create a small, coherent set of examples that makes a feature or API easier to understand.
- `doc_glossary_builder` (slash-first) — Build a shared glossary for terms, metrics, entities, and overloaded language across a project.
- `doc_information_architecture` (slash-first) — Organize docs so users can find the right answer quickly by role, task, and depth.
- `doc_knowledge_base_article` (slash-first) — Turn a recurring question into a support-ready article with clear steps and escalation cues.
- `doc_migration_guide` (slash-first) — Write a migration path that explains what changed, who is affected, and how to upgrade safely.
- `doc_quickstart_guide` (slash-first) — Write a fast-start guide that gets a new user to first success with minimal friction.
- `doc_release_notes` (slash-first) — Turn raw changes into clear release notes grouped by user impact, risk, and next actions.
- `doc_troubleshooting_guide` (slash-first) — Organize diagnosis by symptom, checks, and likely causes so users can recover methodically.

## Data

- `data_analysis_plan` — Turn a vague data question into a scoped analysis plan with metrics, cuts, and checks.
- `data_anomaly_triage` — Triage a surprising metric change by checking definitions, pipelines, seasonality, and real behavior.
- `data_dashboard_brief` (slash-first) — Design a dashboard that supports action, ownership, and review cadence instead of vanity views.
- `data_event_instrumentation` (slash-first) — Plan events, properties, and naming so analytics data stays trustworthy and useful.
- `data_experiment_readout` — Read an experiment with effect size, uncertainty, caveats, and next actions instead of hype.
- `data_metric_definition` (slash-first) — Write a metric definition that is consistent across teams, tools, and review meetings.
- `data_pipeline_triage` (slash-first) — Triage broken or delayed data flows by isolating the failing stage and recovery options.
- `data_quality_checks` — Design recurring checks for freshness, completeness, consistency, and metric integrity.
- `data_segmentation_plan` — Plan how to segment users, accounts, or events so analysis reveals actionable differences.
- `data_sql_query_plan` (slash-first) — Turn an analysis question into a query plan with tables, joins, filters, and validation checks.

## Design

- `des_accessibility_review` — Review flows for accessibility risks in navigation, semantics, contrast, content, and feedback.
- `des_component_contract` (slash-first) — Define a UI component by purpose, variants, states, and constraints so teams use it consistently.
- `des_design_brief` — Translate a product problem into a design brief with users, constraints, and success criteria.
- `des_design_critique` (slash-first) — Critique a design against goals, hierarchy, clarity, and flow instead of taste alone.
- `des_design_system_audit` (slash-first) — Audit a design system for inconsistency, missing states, adoption friction, and maintenance burden.
- `des_empty_states_copy` (slash-first) — Write empty-state copy that teaches the next step without sounding robotic or needy.
- `des_usability_test_plan` (slash-first) — Plan lightweight usability sessions that reveal friction, confusion, and unmet expectations.
- `des_visual_direction` (slash-first) — Set the visual tone, references, and constraints for a cohesive design direction.
- `des_wireframe_spec` (slash-first) — Describe screens, states, and interactions clearly enough to build or critique without mockups.

## Program

- `pm_backlog_refinement` (slash-first) — Clean a backlog into better-shaped work with priority signals, dependencies, and next actions.
- `pm_decision_meeting` (slash-first) — Prepare a meeting so it actually resolves a decision instead of circling the issue again.
- `pm_dependency_map` (slash-first) — Map the teams, systems, approvals, and sequencing that could block delivery.
- `pm_governance_model` (slash-first) — Define decision rights, review cadence, escalation paths, and operating rules for a program.
- `pm_milestone_plan` — Break a project into milestones, exit criteria, and dependencies that can actually be tracked.
- `pm_risk_register` — Build a practical risk register with triggers, owners, mitigations, and review cadence.
- `pm_roadmap_scenarios` (slash-first) — Turn competing ideas into roadmap scenarios with tradeoffs, dependencies, and downside risks.
- `pm_scope_tradeoffs` — Clarify what to cut, defer, or simplify when time, quality, and capacity are in tension.
- `pm_stakeholder_update` (slash-first) — Write a crisp update that explains progress, risk, decisions, and asks without noise.

## AI

- `ai_agent_spec` — Specify an agent workflow, boundaries, tools, and outputs before implementation.
- `ai_context_budget` — Shape prompts, memory, and retrieved context to fit the smallest useful budget.
- `ai_eval_harness` — Design test cases and score rules that catch regressions in agent quality and safety.
- `ai_failure_taxonomy` — Classify agent failures so fixes target the real weakness instead of symptoms.
- `ai_guardrail_review` (slash-first) — Review an agent for risky behaviors, abuse paths, and missing refusals before wider use.
- `ai_memory_policy` — Define what an agent should remember, forget, summarize, or ask again over time.
- `ai_model_routing` (slash-first) — Choose which model handles which work based on quality, speed, cost, and risk.
- `ai_prompt_regression_review` (slash-first) — Review prompt changes for behavior regressions, instruction conflicts, and hidden tradeoffs.
- `ai_prompt_system` — Turn scattered instructions into a stable prompt architecture with clear sections and duties.
- `ai_rag_design` (slash-first) — Design retrieval, chunking, freshness, and citation behavior for grounded question answering.
- `ai_subagent_decomposition` — Split a complex job into safe subagent tracks with bounded scope, interfaces, and merge points.
- `ai_tool_schema_review` (slash-first) — Review tool names, arguments, and failure contracts so agents can use them reliably.

## Sales

- `sales_account_plan` (slash-first) — Build an account plan covering stakeholders, pain, timing, deal strategy, and expansion paths.
- `sales_account_research` (slash-first) — Summarize an account in terms of likely pain, stakeholders, timing, and approach angles.
- `sales_demo_flow` (slash-first) — Shape a demo around the buyer problem, proof points, and next commitment instead of a product tour.
- `sales_discovery_call_plan` (slash-first) — Prepare a discovery call that surfaces pain, urgency, fit, and buying constraints.
- `sales_followup_sequence` (slash-first) — Write a short follow-up sequence that moves a deal forward without sounding automated.
- `sales_mutual_action_plan` (slash-first) — Create a buyer-facing action plan with milestones, dependencies, and next commitments.
- `sales_objection_map` (slash-first) — Turn recurring objections into clearer responses, proof paths, and qualification cues.
- `sales_pipeline_review` (slash-first) — Review a pipeline for deal quality, bottlenecks, forecast risk, and next actions.
- `sales_proposal_outline` (slash-first) — Outline a proposal around goals, scope, proof, pricing, and mutual next steps.

## Quality

- `qa_acceptance_test_plan` — Turn requirements into a lean acceptance plan that proves the change works for real users.
- `qa_bug_report_refine` (slash-first) — Turn a messy bug note into a clear report with environment, repro steps, and expected behavior.
- `qa_regression_sweep` (slash-first) — Define a fast regression sweep around a change so adjacent breakage is caught before release.
- `qa_release_smoke_test` — Create a minimal post-build smoke test that catches obvious breakage before wider rollout.
- `qa_repro_steps_author` (slash-first) — Write exact reproduction steps for a bug, edge case, or flaky failure without guesswork.
- `qa_risk_based_testing` — Prioritize testing by user impact, change risk, and failure cost instead of equal treatment.
- `qa_test_case_matrix` (slash-first) — Build a compact matrix of states, roles, inputs, and environments that must be tested.
- `qa_ui_state_check` (slash-first) — Review UI states so loading, empty, error, success, and permission cases all behave coherently.

## Security

- `sec_appsec_review` — Review code or design for common application-security weaknesses and realistic exploit paths.
- `sec_auth_session_review` (slash-first) — Review authentication, session handling, and account-recovery flows for takeover risk.
- `sec_data_flow_review` — Trace sensitive data through a system and find storage, exposure, retention, and permission risks.
- `sec_dependency_audit` (slash-first) — Review dependency trust, maintenance posture, and supply-chain risk before adoption or upgrade.
- `sec_logging_exposure_check` (slash-first) — Check logs, traces, and telemetry for secrets, personal data, and unsafe diagnostic leakage.
- `sec_permission_audit` (slash-first) — Audit roles, scopes, and permissions for least-privilege gaps and over-broad access.
- `sec_safe_disclosure_writeup` (slash-first) — Write a precise security issue report with impact, evidence, and safe remediation guidance.
- `sec_threat_model` — Model assets, threats, trust boundaries, and mitigations before building or changing a system.

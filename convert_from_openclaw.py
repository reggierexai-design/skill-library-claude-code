#!/usr/bin/env python3
"""
Convert upgraded OpenClaw v1.0 skills to Claude Code format.
Key differences:
- "OpenClaw tool pattern" → "Claude Code tool pattern" 
- Tool references adapted for Claude Code (edit, read, exec → Claude Code equivalents)
- Remove "disable-model-invocation" from frontmatter
- Add Claude Code specific context where needed
- Add new solo/comm/legal/finance/vibe skills
"""

import os, re, shutil

SRC_DIR = r"E:\rexhub-repos\skill-library-openclaw\skills"
DEST_DIR = r"E:\rexhub-repos\skill-library-claude-code\skills"

# Tool pattern replacements for Claude Code
CLAUDE_TOOL_PATTERNS = {
    "att": [
        "- Use `WebFetch` to research competitor content and current platform conventions.",
        "- Read existing site copy, product pages, and proof assets before drafting so output fits the real product truth.",
        "- When external claims appear, verify before publishing with `safe_external_claims`.",
        "- After drafting, run `att_proof_mining` to verify every claim has backing.",
    ],
    "core": [
        "- Use `Read` to load relevant files and context before planning.",
        "- Use `Bash` to check workspace state (git status, file structure) before and after actions.",
        "- After execution, use `core_verify_done` to confirm the result meets the stated objective.",
    ],
    "eng": [
        "- Use `Bash` to run diagnostic commands, read logs, and check system state.",
        "- Use `Read` to inspect source files, configs, and error output directly.",
        "- Use `Write` or `Edit` for targeted code changes. Prefer `eng_minimal_patch` scope discipline.",
        "- After changes, use `eng_test_strategy` to verify the fix works and nothing else broke.",
    ],
    "prod": [
        "- Use `WebFetch` to review competitor products and user feedback on review sites.",
        "- Use `Read` to load analytics data, user research files, and product specs.",
        "- After design work, run `core_review_changes` to check for scope creep.",
    ],
    "data": [
        "- Use `Bash` to run data queries and analysis scripts.",
        "- Use `Read` to load data exports, schema files, and query results.",
        "- After analysis, use `data_quality_checks` to validate findings before presenting.",
    ],
    "ops": [
        "- Use `Bash` to check system status, run deployments, and verify infrastructure state.",
        "- Use `Read` to load runbooks, config files, and incident history.",
        "- After operational changes, use `ops_change_management` to document what changed and why.",
    ],
    "pm": [
        "- Use `Read` to load project plans, roadmaps, and stakeholder communications.",
        "- Use `Bash` to check project status (git logs, CI results, milestone tracking).",
        "- After planning, use `pm_scope_tradeoffs` to pressure-test scope decisions.",
    ],
    "qa": [
        "- Use `Bash` to run test suites, check CI results, and verify deployment state.",
        "- Use `Read` to load test plans, bug reports, and acceptance criteria.",
        "- After testing, use `qa_release_smoke_test` to confirm release readiness.",
    ],
    "sec": [
        "- Use `Bash` to run security scanning tools, check dependency vulnerabilities, and audit configs.",
        "- Use `Read` to load security policies, auth configurations, and access control files.",
        "- After security review, use `sec_threat_model` to assess residual risk.",
    ],
    "sales": [
        "- Use `WebFetch` to research prospect companies, news, and relevant context before outreach.",
        "- Use `Read` to load CRM data, call notes, and deal history.",
        "- After sales planning, use `att_proof_mining` to ensure every claim in materials is backed.",
    ],
    "res": [
        "- Use `WebFetch` to gather competitor data, market reports, and source material.",
        "- Use `Read` to load interview transcripts, survey data, and research notes.",
        "- After research, use `core_evidence_research` to rate source quality and confidence.",
    ],
    "safe": [
        "- Use `Read` to load configs, credentials, and access control files for auditing.",
        "- Use `Bash` to verify system state, check permissions, and test security controls.",
        "- After safety review, use `core_risk_gate` to assess whether the change can proceed.",
    ],
    "doc": [
        "- Use `Read` to load existing docs, code comments, and API definitions.",
        "- Use `Bash` to check code structure and generate API schemas when needed.",
        "- After writing docs, use `doc_docs_feedback_loop` to plan for ongoing accuracy.",
    ],
    "des": [
        "- Use `Read` to load design specs, component libraries, and existing UI copy.",
        "- Use `WebFetch` to review competitor designs and accessibility standards.",
        "- After design work, use `des_accessibility_review` to verify compliance.",
    ],
    "solo": [
        "- Use `Bash` to check current project status, deadlines, and shipping readiness.",
        "- Use `Read` to load personal productivity notes, goals, and rhythm files.",
        "- Pair with `solo_scope_guard` to prevent scope expansion during execution.",
    ],
    "vibe": [
        "- Use `Bash` to run AI-assisted code generation, debugging, and deployment commands.",
        "- Use `Read` to load prompts, code templates, and AI tool configurations.",
        "- After building, use `vibe_debug_no_code` to test without deep technical knowledge.",
    ],
    "comm": [
        "- Use community platform tools to check channels, respond to members, and manage discussions.",
        "- Use `Read` to load community guidelines, feedback data, and engagement metrics.",
        "- After community actions, use `comm_retention_audit` to check member retention trends.",
    ],
    "legal": [
        "- Use `WebFetch` to look up regulation references and compliance requirements.",
        "- Use `Read` to load existing legal documents, terms, and privacy policies.",
        "- After legal review, flag anything that needs actual attorney review. This skill assists, not replaces counsel.",
    ],
    "finance": [
        "- Use `Read` to load financial data, pricing spreadsheets, and revenue reports.",
        "- Use `Bash` to run calculations and financial models.",
        "- After financial analysis, use `finance_burn_rate` to cross-check sustainability.",
    ],
    "ai": [
        "- Use `Bash` to run model evaluations, prompt tests, and benchmarking scripts.",
        "- Use `Read` to load prompt templates, eval datasets, and model configurations.",
        "- After AI system design, use `ai_eval_harness` to validate performance claims.",
    ],
}

DEFAULT_TOOL_PATTERN = [
    "- Use `Read` to load relevant context files before starting.",
    "- Use `Bash` to verify current state before and after changes.",
    "- After completing, verify the result meets the stated objective.",
]

converted = 0
errors = 0

# Get list of all OpenClaw v1.0 skill directories
openclaw_skills = set(os.listdir(SRC_DIR))

# Get list of existing Claude Code skill directories
claude_skills = set()
if os.path.exists(DEST_DIR):
    claude_skills = set(os.listdir(DEST_DIR))

# Process all OpenClaw skills (includes the new 30)
for skill_name in sorted(openclaw_skills):
    src_path = os.path.join(SRC_DIR, skill_name, "SKILL.md")
    if not os.path.exists(src_path):
        continue
    
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Replace "OpenClaw tool pattern" section header
    content = content.replace("## OpenClaw tool pattern", "## Claude Code tool pattern")
    
    # 2. Replace tool references in the tool pattern section
    # Find the Claude Code tool pattern section
    cat = skill_name.split("_")[0] if "_" in skill_name else "other"
    tool_pattern = CLAUDE_TOOL_PATTERNS.get(cat, DEFAULT_TOOL_PATTERN)
    
    # Replace the entire tool pattern section content
    pattern = r'(## Claude Code tool pattern\s*\n)((?:- .*\n)+)'
    match = re.search(pattern, content)
    if match:
        # Check if the content still has OpenClaw tool names
        section_content = match.group(2)
        if any(t in section_content for t in ["`exec`", "`read`", "`write`", "`edit`", "`web_fetch`"]):
            # Replace with Claude Code equivalents
            section_content = section_content.replace("`exec`", "`Bash`")
            section_content = section_content.replace("`read`", "`Read`")
            section_content = section_content.replace("`write`", "`Write`")
            section_content = section_content.replace("`edit`", "`Edit`")
            section_content = section_content.replace("`web_fetch`", "`WebFetch`")
            content = content[:match.start(2)] + section_content + content[match.end(2):]
    
    # 3. Remove "disable-model-invocation" from frontmatter
    content = re.sub(r'\ndisable-model-invocation: [^\n]+', '', content)
    
    # 4. Replace platform_target reference if present
    content = content.replace("platform_target: OpenClaw", "platform_target: Claude Code")
    
    # Write to Claude Code skill directory
    dest_skill_dir = os.path.join(DEST_DIR, skill_name)
    os.makedirs(dest_skill_dir, exist_ok=True)
    dest_path = os.path.join(dest_skill_dir, "SKILL.md")
    
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    converted += 1

print(f"Converted: {converted} skills from OpenClaw v1.0 to Claude Code format")
print(f"Skills that are new (not in original Claude Code v0.6): {len(openclaw_skills - claude_skills)}")

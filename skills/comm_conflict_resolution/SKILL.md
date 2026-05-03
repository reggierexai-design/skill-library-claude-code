---
name: comm_conflict_resolution
description: "Resolve community conflicts constructively before they damage the community culture."
user-invocable: true
---

# Conflict Resolution

## Purpose
Resolve community conflicts constructively before they damage the community culture. Unresolved conflict doesn't go away — it metastasizes. A disagreement that could have been handled in a 10-minute conversation becomes a faction war that splits the community.

## Use when
Use when two community members are in a heated disagreement. Use when a member is consistently disrupting others. Use when the community climate feels tense or divided. Use when you need to enforce community guidelines.

## Avoid when
Don't use for simple disagreements that resolve naturally. Don't intervene too early — let adults work it out first. Don't take sides publicly — your role is facilitation, not judgment.

## Inputs to gather
- Conflict description: who's involved, what happened, what's the disagreement?
- Community guidelines: what rules apply to this situation?
- History: is this a pattern or a one-time incident?
- Impact: who else is affected? Is the conflict spilling into public channels?
- Each party's perspective: what does each person think happened?

## Operating rules
- Address conflict early. The longer it festers, the harder it is to resolve and the more collateral damage it causes.
- Listen to both sides privately before acting publicly. What looks like bad behavior from one angle might be a misunderstanding from another.
- Focus on behavior, not character. "Your comment was dismissive" not "you're a jerk."
- Enforce guidelines consistently. If you let one person slide, you lose credibility with everyone else.
- Protect the community culture, not individual feelings. Sometimes the right answer is asking someone to leave.

## Claude Code tool pattern
- Use `comm_feedback_system` to gather community sentiment before and after resolution.
- Use `comm_ritual_design` to create constructive spaces that prevent conflict.
- Use `ops_support_triage` for prioritizing which conflicts need immediate attention.

## Expanded workflow
1. **Identify the conflict.** Who's involved? What happened? How long has it been going on?
2. **Assess the impact.** Is this contained between two people or spreading to the community? Is anyone being harmed?
3. **Review the guidelines.** What rules apply? Were they broken? Be clear before you act.
4. **Talk to each party privately.** Listen without interrupting. Each person needs to feel heard.
5. **Identify the root cause.** Is this a values disagreement? A misunderstanding? A personality clash? A rule violation?
6. **Propose a resolution.** Mediation, guideline enforcement, behavior agreement, or in rare cases, removal.
7. **Follow up.** Check in with both parties after a week. Did the resolution hold?
8. **Document and learn.** What caused this? How can similar conflicts be prevented? Update guidelines if needed.

## Output contract
- Conflict summary: who, what, impact level
- Resolution approach: mediation, enforcement, agreement, or removal
- Follow-up plan: check-in timing and method
- Guideline updates needed (if any)
- Prevention measures for similar conflicts

## Failure modes to avoid
- Ignoring conflict hoping it goes away — it won't.
- Taking sides publicly before understanding both perspectives.
- Being too lenient with repeat offenders — it signals that guidelines don't matter.
- Being too harsh with first-time mistakes — it signals that the community isn't safe.
- Not following up after resolution — unresolved feelings resurface.
- No documentation — you'll face the same situation again without a reference.

## Handoff cues
- Conflict status: identified, in resolution, resolved, or escalating.
- Resolution approach and timeline.
- Follow-up check-in date.
- Any guideline updates needed.

## Example invocation
- Slash: `/comm_conflict_resolution <task>`
- Natural language: "Use comm_conflict_resolution to resolve community conflicts constructively before they damage the community culture."

## Quality bar
Conflict is addressed within 48 hours of identification. Both parties are heard privately before any public action. Resolution focuses on behavior, not character. Guidelines are enforced consistently. Follow-up happens within one week.

## Related workflows
- **Community health:** `comm_conflict_resolution` → `comm_feedback_system` → `comm_retention_audit`
- **Prevention system:** `comm_ritual_design` → `comm_onboarding_flow` (set norms early) → `comm_conflict_resolution`
- **Guideline enforcement:** `comm_conflict_resolution` → guideline update → `comm_onboarding_flow` (update new member guidance)

---
name: att_creator_partnerships
description: "Design creator or expert partnerships with fit, proof, and mutual value."
user-invocable: true
metadata: {"openclaw":{"emoji":"\ud83c\udfa5"}}
---

## Purpose
- Design creator or expert partnerships with fit, proof, and mutual value.

## Use when
- Use when outside voices could credibly expand reach, trust, or category education.

## Avoid when
- Do not use when the product has no fit for external voices or no support for follow-through.

## Inputs to gather
- Target creators: who in the niche has audience overlap with your buyers?
- Your offer to the creator: what value do you bring (affiliate revenue, early access, co-creation, exposure)?
- Creator constraints: platform, audience size, content style, brand safety rules.
- Your goals: awareness, conversions, content co-creation, or social proof.
- Budget: any financial commitment (affiliate rates, sponsorships, product gifts).

## Operating rules
- Partnership value must flow both ways. If you're only asking for promotion, you're buying ads.
- Match creator size to your stage. Micro-creators (1K-10K engaged followers) often convert better.
- Design the collaboration, not just the ask. Co-created content outperforms sponsored mentions.
- Start with 2-3 pilots before scaling. Test the format, measure conversion, then expand.

## Claude Code tool pattern
- Use `WebFetch` to research competitor content and current platform conventions.
- Read existing site copy, product pages, and proof assets before drafting so output fits the real product truth.
- When external claims appear, verify before publishing with `safe_external_claims`.
- After drafting, run `att_proof_mining` to verify every claim has backing.

## Expanded workflow
1. Define what you need: awareness, conversions, or content.
2. Research creators: audience overlap, engagement rate (not follower count), content quality, past partnerships.
3. Design the value exchange: what the creator gets, what you get, what the audience gets.
4. Draft the partnership brief: deliverables, timeline, creative freedom, measurement plan.
5. Launch 2-3 pilots, measure results, then decide whether to scale.

## Output contract
## Failure modes to avoid
- Paying for mentions without creative involvement â€” audiences detect inauthentic sponsorships.
- Choosing creators by follower count instead of engagement rate and audience overlap.
- Over-constraining the creative brief â€” the creator knows their audience better than you do.
- No measurement plan â€” can't attribute results means can't improve.

## Handoff cues
- State the partnership brief: creator, deliverables, timeline, measurement plan.
- Flag any legal considerations (FTC disclosure, contracts) that need `legal_terms_privacy_basics`.
- Note the measurement schedule: when to check results and whether to continue.

## Example invocation
- Slash: `/att_creator_partnerships <task>`
- Natural language: "Use attention Creator Partnerships to design creator or expert partnerships with fit, proof, and mutual value."
- Example: "Find 5 micro-creators in the maker studio niche and design a partnership brief for each."
- Example: "I have no budget but early access to give. Design a creator partnership that works."
- Often paired with: `att_message_house`, `att_launch_plan`, `att_proof_mining`

## Quality bar
## Related workflows
- Content system: `att_message_house` â†’ `att_content_calendar` â†’ `att_content_repurposing`
- Launch sequence: `att_launch_plan` â†’ `att_proof_mining` â†’ `att_thread_writer`
- Proof deployment: `att_proof_mining` â†’ `att_case_study_builder` â†’ `att_social_proof_pack`

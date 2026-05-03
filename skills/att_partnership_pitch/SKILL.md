--- name: att_partnership_pitch description: "Create a partnership angle, value exchange, and outreach package that feels mutually useful." user-invocable: true disable-model-invocation: true metadata: {"openclaw":{"emoji":"🤝"}} ---
# Partnership Pitch

## Purpose
- Create a partnership angle, value exchange, and outreach package that feels mutually useful.
- This is an **attention specialist** for structuring partnership proposals where both sides benefit — not just one side asking for a favor.

## Use when
- Use when pitching integrations, co-marketing, co-launches, or ecosystem relationships.
- Use when you have a product and want to expand reach through partners who serve the same audience.
- Use when cold-reaching to potential partners and needing a compelling reason for them to engage.

## Avoid when
- Do not use when the partnership idea only benefits one side — that's an ad buy, not a partnership.
- Do not use when your product has no proof of value yet — partners need evidence that collaborating with you helps their audience.
- Do not use when you haven't researched the partner's business model, audience, and constraints.

## Inputs to gather
- Target partner: who they are, what they offer, who their audience is, what their business model depends on.
- The mutual value: what does the partner get? What do you get? What does the joint audience get? (All three must be concrete.)
- Partnership structure: co-marketing, integration, reseller, affiliate, co-creation, or distribution?
- Partner constraints: brand guidelines, technical requirements, deal structures, timeline preferences.
- Your proof: what evidence demonstrates that your product delivers value and that the partnership is worth their time?
- Audience overlap: how many of their users would genuinely benefit from your product?

## Operating rules
- **Mutual value must be concrete, not implied.** "Exposure to our audience" is not concrete. "Access to 2,000 active users who match your ICP" is concrete. Name the specific value on each side.
- **Pitch the smallest viable collaboration first.** Don't propose a deep integration on the first call. Start with something low-risk: a co-post, a joint webinar, a reciprocal mention. Prove the value, then expand.
- **Respect the partner's audience and incentives.** Their audience trusts them. A partnership that undermines that trust (irrelevant product, poor fit, hard sell) damages the partner, which kills the partnership.
- **Lead with what they get, not what you want.** The pitch that starts with "we'd love to..." is about you. The pitch that starts with "your audience has been asking for X, and we can help you deliver it" is about them.
- **Include proof that you deliver.** A partner is staking their credibility on you. Show them that your product works, that users value it, and that you follow through. No proof = no partnership.
- **Design the collaboration, not just the ask.** Co-created content, joint tutorials, and shared workflows outperform one-sided "please promote us" asks. Make the partner a participant, not a channel.

## Claude Code tool pattern
- Use `WebFetch` to research the partner's website, recent content, and audience before drafting the pitch.
- Use `att_proof_mining` to inventory what proof you have that demonstrates value to the partner's audience.
- After drafting, use `legal_terms_review` or `legal_terms_privacy_basics` if the partnership involves data sharing, affiliate terms, or co-branding.

## Expanded workflow
1. **Research the partner.** What do they sell? Who are their users? What have they partnered on before? What do they care about protecting? This research shapes the pitch — generic outreach gets ignored.
2. **Define the mutual value.** Write it down: "Partner gets X. We get Y. Joint audience gets Z." If any of these are vague, the partnership pitch is not ready.
3. **Choose the smallest viable collaboration.** Not a deep integration — a pilot. A co-post, a reciprocal discount, a joint tutorial. Something that takes 1-2 weeks to test, not 3 months to build.
4. **Write the pitch.** Structure: (1) context — you know their audience, (2) value — what their users need that you provide, (3) the ask — a specific, small collaboration, (4) proof — evidence you deliver, (5) next step — a low-commitment response.
5. **Write the follow-up.** If they don't respond in 5 days, a follow-up that adds value (a relevant insight, a new proof point, a smaller ask). Never just "bumping this."
6. **Return the pitch, follow-up, and internal brief.** The brief documents: what you're offering, what you expect in return, success metrics, and how to measure whether the partnership is working.

## Output contract
- Partner research summary: who they are, what they care about, audience overlap
- Mutual value statement: concrete value for partner, for you, for the joint audience
- Pitch email or message (ready to send)
- Follow-up email (value-add, not just a bump)
- Likely objections and responses
- Partnership brief: scope, success metrics, timeline, and exit criteria

## Failure modes to avoid
- Pitching your benefit, not theirs — partners don't care about your growth, they care about their audience.
- Proposing complex structures before proving value with a pilot — deep integrations need trust first.
- No proof that your side delivers value — "our product is great" is not proof. User outcomes are proof.
- Ignoring the partner's brand and audience norms — a mismatched partnership damages both brands.
- One-sided asks disguised as partnerships — "please promote us" with nothing in return is an ad request.
- Vague value propositions — "we'll cross-promote" without specifics is empty.

## Handoff cues
- Full pitch document with research, value exchange, and email copy.
- Follow-up email drafted and ready.
- Likely objections with prepared responses.
- Flag any legal or brand review needed before the partnership goes live.
- Note the follow-up timing: when to check in and what to say.

## Example invocation
- Slash: `/att_partnership_pitch <task>`
- Natural language: "Build a partnership pitch for this company."
- Example: "Design a co-marketing pitch for a complementary SaaS product."
- Example: "I want to partner with this tool. Build the mutual value case and outreach email."
- Often paired with: `att_message_house`, `att_launch_plan`, `att_proof_mining`

## Quality bar
- The partner sees concrete upside in the first 2 sentences of the pitch.
- Mutual value is stated in specific terms, not vague promises.
- The initial ask is small enough to say yes to in one email.
- Proof of your value is included in the pitch.
- The follow-up adds value, not just pressure.

## Related workflows
- Partnership pipeline: `att_partnership_pitch` → `att_creator_partnerships` → `att_outbound_sequences`
- Launch support: `att_launch_plan` → `att_partnership_pitch` → `att_email_nurture_sequences`
- Proof backing: `att_proof_mining` → `att_partnership_pitch`

--- name: att_proof_mining description: "Extract credible proof points, testimonials, wins, and user language from messy source material." user-invocable: true disable-model-invocation: false metadata: {"openclaw":{"emoji":"📣"}} ---
# Proof Mining

## Purpose
- Extract credible proof points, testimonials, wins, and user language from messy source material.
- This is an **attention specialist** for building a proof inventory that makes claims credible and copy persuasive.

## Use when
- Use when the user has reviews, chat logs, support tickets, notes, case studies, or customer messages that may contain reusable proof.
- Use when preparing for a launch, sales page, or investor update and the proof is scattered across tools and inboxes.
- Use when claims need backing before they go public — "safe_external_claims" before publication.

## Avoid when
- Do not invent proof or overstate weak signals as validation.
- Do not use when there's genuinely no proof yet — instead, advise building proof first (run a pilot, collect a testimonial, ship a measurable improvement).
- Do not use for competitive intelligence — that's `res_competitor_scan`.

## Inputs to gather
- Customer results: any measurable outcomes, before/after comparisons, or time savings.
- User feedback: support tickets, emails, social mentions, app store reviews, DMs.
- Usage data: activation rates, retention curves, feature adoption, time-to-value.
- Competitor gaps: what can competitors NOT prove that you can?
- Current proof inventory: what proof assets already exist and what's missing?
- Source material: paste or attach the raw text (chat logs, emails, review screenshots, notes).

## Operating rules
- **Proof hierarchy (strongest to weakest):** Measured outcome with control ("43% increase vs baseline") > Measured outcome without control ("cut onboarding time from 20 min to 8 min") > Specific testimonial with context ("I used to spend 3 hours on X, now it takes 20 min") > Vague testimonial ("this is great!") > Expert opinion > Social proof count ("10K users"). Always label which tier each proof point sits at.
- **Separate direct proof, implied proof, and unsupported claims.** Direct proof = verifiable outcome. Implied proof = directional signal that needs caveats. Unsupported = assertion without evidence — flag it, don't deploy it.
- **Capture the user's own language.** Customer words beat marketing polish. "I was drowning in spreadsheets" is stronger copy than "streamlined workflow management." Transcribe exactly, then annotate.
- **Tag every proof point by claim it supports.** A proof point without a claim it backs is an orphan. Map: proof → claim → channel where it deploys.
- **Rate confidence on each point:** high (verifiable, specific, recent), medium (directional but missing specificity or recency), low (anecdotal, old, or unverified). Only deploy high and medium with appropriate caveats.

## Claude Code tool pattern
- When source material is in files (support exports, chat logs, review CSVs), use `Read` to load them directly.
- When proof references external claims (stats, benchmarks), use `WebFetch` to verify before including.
- After mining, feed the proof bank into `att_thread_writer`, `att_message_house`, or `att_social_proof_pack` for deployment.
- When proof is thin, recommend `prod_experiment_design` or `data_experiment_readout` to generate measured outcomes.

## Expanded workflow
1. **Define the proof need.** What claims are being made? What proof is required to back each one? Start from the claims, not the sources.
2. **Ingest and scan source material.** Read through reviews, tickets, messages, data exports. Highlight anything that could serve as proof — even weak signals.
3. **Extract candidate proof points.** For each: the exact quote or data point, the source (who/where/when), the claim it supports, and the confidence level.
4. **Classify by proof hierarchy.** Label each point: measured outcome, specific testimonial, vague testimonial, expert opinion, or social count. Note which tier.
5. **Map proof to claims and channels.** Which proof backs which claim? Where will it deploy (landing page, sales deck, social, docs)? Find gaps: claims without proof, and proof without claims.
6. **Capture user language separately.** Pull the strongest verbatim phrases — these become copy assets independent of the proof points.
7. **Return the proof bank with safe usage notes.** Include confidence ratings, provenance, and recommended deployment. Flag what NOT to say (anything that overstates the proof).

## Output contract
- Proof bank: each point with source, tier, confidence rating, claim it supports, and deployment channel
- User language bank: strongest verbatim quotes, annotated with context
- Proof gap analysis: claims that lack backing, proof that lacks claims
- Priority proof to generate: what measurement or testimonial would unlock the most value if obtained
- Safe usage notes: what can be said, what needs caveats, what can't be said yet

## Failure modes to avoid
- Publishing vague proof as if it's specific — "improved efficiency" is not proof. "Cut processing time from 4 hours to 22 minutes" is.
- Cherry-picking outliers — one amazing result is not typical. Note whether results are representative.
- Fabricating specificity — rounding up ("almost 50%") when the real number is 43% destroys trust when someone checks.
- Hoarding proof instead of deploying it — mined proof that sits in a spreadsheet helps no one.
- Ignoring weak proof signals — if testimonials are your strongest proof, that tells you to invest in generating measured outcomes.
- Deploying low-confidence proof without caveats — implied proof stated as direct proof is a credibility trap.

## Handoff cues
- Proof inventory: each point rated, mapped to claims, with deployment recommendations.
- User language bank: verbatim phrases ready for copy use.
- Gap map: claims without proof, ranked by urgency.
- Next proof to generate: the single measurement or testimonial that would unlock the most value.
- Channel deployment plan: where each proof point should appear.

## Example invocation
- Slash: `/att_proof_mining <task>`
- Natural language: "Mine proof from these support tickets and reviews."
- Example: "I have 200 support emails — find the proof points I can use on my landing page."
- Example: "Extract the strongest testimonials and user language from this chat log."
- Often paired with: `att_message_house`, `att_launch_plan`, `att_thread_writer`

## Quality bar
- Every proof claim is traceable to a specific source: customer name, data point, or verifiable event.
- At least 3 proof tiers represented (measured outcome, testimonial, social proof).
- No proof claim is fabricated or exaggerated — if you cannot verify it, label it "unverified" and don't deploy it.
- The strongest proof maps to the biggest objection in the positioning.
- User language captures real phrasing, not marketing-speak paraphrasing.
- Gaps are explicitly named: "We claim X but have no proof for it."

## Related workflows
- Content system: `att_message_house` → `att_content_calendar` → `att_proof_mining` → `att_thread_writer`
- Launch sequence: `att_launch_plan` → `att_proof_mining` → `att_social_proof_pack`
- Proof deployment: `att_proof_mining` → `att_case_study_builder` → `att_social_proof_pack`
- Proof generation: `prod_experiment_design` → `data_experiment_readout` → `att_proof_mining`

--- name: att_landing_page_story description: "Structure a landing page so attention converts into understanding, trust, and action." user-invocable: true disable-model-invocation: true metadata: {"openclaw":{"emoji":"📄"}} ---
# Landing Page Story

## Purpose
- Structure a landing page so attention converts into understanding, trust, and action.
- This is an **attention specialist** for building pages where every section moves the visitor closer to the CTA — not just fills space.

## Use when
- Use when a homepage, waitlist page, feature page, or launch page needs a stronger narrative arc.
- Use when conversion rate is low and the page feels like a feature list rather than a story.
- Use when building a page for a specific traffic source (cold social, warm email, paid ad) and the page needs to match arrival context.

## Avoid when
- Do not use when the page only needs local copy edits and the structure already works.
- Do not use when the product's core value proposition is still unclear — run `att_positioning_workshop` first.

## Inputs to gather
- The page's single job: what action should the visitor take? (Sign up, buy, book a demo, download, join waitlist)
- The visitor's arrival context: where did they come from and what do they already believe? Cold social traffic needs different treatment than warm email clicks.
- The proof hierarchy: what's the most compelling evidence for this audience? (Testimonials, data, demo, comparisons)
- Competitive alternatives: what else is the visitor considering? Why should they choose this?
- Existing page copy and conversion data (if optimizing — what's the current conversion rate? Where do visitors drop off?)

## Operating rules
- **Lead with the problem, promise, and next step — fast.** The hero section must convey what this is, who it's for, and what to do next within 5 seconds of page load. If a visitor has to scroll to understand the value, you've already lost most of them.
- **Sequence: problem → promise → proof → differentiation → action.** Don't jump to features before establishing why they matter. Don't ask for commitment before building trust.
- **Cut sections that do not move belief or action.** Every section should pass the deletion test: if you removed it, would conversion drop? If not, cut it.
- **One primary CTA.** Multiple competing CTAs mean the visitor does nothing. Every section can reinforce the primary CTA; none should introduce a different one.
- **Match the page to the arrival context.** A page for cold social traffic should restate the hook that got them to click. A page for warm email traffic can skip the introduction and lead with proof.

## Claude Code tool pattern
- Use `Read` to load existing page copy and analytics data before restructuring.
- Use `att_proof_mining` to inventory the strongest proof points for the page.
- Use `att_message_house` output to ensure the page aligns with the core messaging.
- Use `WebFetch` to review competitor landing pages and find structural gaps.

## Expanded workflow
1. **Define the conversion goal.** One primary action. Name it: "visitor signs up for free trial." Everything on the page serves this goal.
2. **Audit the current page (if optimizing).** Map every section. Which ones move belief? Which are filler? What's the drop-off point in the scroll depth data?
3. **Write the hero section.** Headline = core promise. Subheadline = who it's for + why it's different. CTA = the single action. This section does 80% of the work.
4. **Structure the proof sequence.** After the hero: (1) social proof that validates the promise, (2) mechanism explanation that makes the promise credible, (3) differentiation that makes switching worthwhile, (4) objection handling that removes remaining doubt.
5. **Write section-by-section copy.** Each section has one job: move the visitor from where they are to one step closer to the CTA. No section exists just to fill space.
6. **Add the CTA reinforcement.** The primary CTA should appear at least 3 times: hero, middle, and bottom. Each appearance can use slightly different language matched to the proof context above it.
7. **Return the page blueprint or draft.** Section order, copy points, proof placement, CTA locations, and notes for A/B testing.

## Output contract
- Hero section: headline, subheadline, CTA
- Section-by-section structure: what each section does and why it exists
- Proof placement: which proof goes where
- Objection handling: where and how concerns are addressed
- CTA strategy: where CTAs appear and what language they use
- A/B test priorities: headline and CTA first, proof order second
- Arrival context notes: how the page should vary for different traffic sources

## Failure modes to avoid
- Multiple competing CTAs — the visitor gets paralyzed and does nothing.
- Feature lists instead of outcomes — "real-time analytics" is a feature. "Know what's happening before it becomes a problem" is an outcome.
- Social proof disconnected from claims — testimonials that don't relate to the headline promise create doubt, not trust.
- No deletion test — sections that grew organically and no one questions anymore.
- Ignoring arrival context — the same page for cold traffic (needs explanation) and warm traffic (needs proof) underserves both.

## Handoff cues
- Full page copy with section annotations explaining why each section exists.
- Proof gap flags: claims that lack supporting evidence on the page.
- A/B test plan: what to test first (headline, CTA, proof order).
- Arrival context variations: what changes for different traffic sources.

## Example invocation
- Slash: `/att_landing_page_story <task>`
- Natural language: "Restructure this landing page to convert better."
- Example: "Rewrite this homepage to have a clear narrative arc instead of feature soup."
- Example: "Design a waitlist page that makes zero-audience visitors want to sign up."
- Often paired with: `att_message_house`, `att_proof_mining`, `att_positioning_workshop`

## Quality bar
- The hero section conveys the value, audience, and next step in under 5 seconds.
- Every section passes the deletion test — removing it would reduce conversion.
- The primary CTA appears at least 3 times with context-matched language.
- Proof is placed where it addresses the concern it resolves.
- A visitor from any traffic source knows what to do next without scrolling back up.

## Related workflows
- Positioning first: `att_positioning_workshop` → `att_message_house` → `att_landing_page_story`
- Proof backing: `att_proof_mining` → `att_landing_page_story`
- SEO version: `att_seo_page_brief` → `att_landing_page_story`

--- name: att_message_house description: "Build a message hierarchy with one core promise, supporting pillars, proof, and objections handled." user-invocable: true disable-model-invocation: false metadata: {"openclaw":{"emoji":"\ud83c\udfe0"}} ---
# Message House

## Purpose
- Build a message hierarchy with one core promise, supporting pillars, proof, and objections handled.
- This is an **attention specialist** for creating the single source of truth that keeps all messaging consistent — across site, content, demos, sales, and outreach.

## Use when
- Use when the team needs consistent messaging across site, content, demos, and outreach.
- Use when launching a new product, entering a new market, or repositioning an existing product.
- Use when sales, marketing, and product are saying different things about the same product.
- Use when the current messaging is a laundry list — everything is "core" so nothing stands out.

## Avoid when
- Do not use when the underlying positioning is still unresolved — run `att_positioning_workshop` first.
- Do not use when you only need a single piece of copy — that's `att_thread_writer` or `att_landing_page_story`.
- Do not use when the product truth isn't settled — a message house built on aspirational claims is a fiction document.

## Inputs to gather
- The core value: what's the single most important thing this product does for its users?
- Target audiences: 2-4 distinct segments, what each cares about most.
- Proof per segment: what evidence supports the value claim for each audience?
- Competitive landscape: what alternatives exist, what's the genuine differentiation?
- Tone boundaries: how bold or conservative can the messaging be?
- Existing messaging: what's currently on the site, in the deck, in sales emails? (to find inconsistencies)

## Operating rules
- **One core promise.** Not two. Not "and also." One thing the product is about. If you can't say it in one sentence, you don't have a core promise — you have a list.
- **3-5 support pillars max.** Each pillar is a reason to believe the core promise. Each pillar needs proof or mechanism — not just a claim. "Easy to use" is a claim. "Set up in 3 clicks with no config file" is a pillar.
- **Handle the top 3 objections inside the house.** The audience will raise them anyway. Pre-handle them with proof, reframing, or honest acknowledgment. Objections ignored become objections believed.
- **Translate, don't transform.** Each audience segment gets the same core promise expressed in their language and concerns — not a different promise. A message house with 4 audiences and 4 different core promises is 4 message houses.
- **Off-limits section.** Explicitly name what the team should NOT say — claims that overreach, comparisons that are unprovable, language that regulators would flag. This is as important as what to say.

## Claude Code tool pattern
- Read the current site copy, landing pages, and sales materials first to find existing message inconsistencies.
- Use `att_proof_mining` to verify that every pillar has backing before finalizing the house.
- After building the house, feed it into `att_content_calendar` for systematic content deployment.
- Use `res_competitor_scan` output to sharpen differentiation pillars.

## Expanded workflow
1. **Audit existing messaging.** Collect what's currently being said across channels. Find the contradictions, overclaims, and gaps before building the new house.
2. **Write the core promise.** One sentence. Test it: can a stranger repeat it back? If not, it's too complex. "We help X do Y" format works. "We empower synergistic paradigm shifts" does not.
3. **Define 3-5 support pillars.** Each one answers "why should I believe the core promise?" Each one needs a proof type: measured outcome, mechanism explanation, testimonial, or authority.
4. **Map proof to each pillar.** High-confidence proof gets deployed directly. Medium-confidence gets caveats. Missing proof becomes a priority to generate.
5. **List top 3-5 objections and responses.** Price, complexity, switching cost, trust, "we already use X." For each: acknowledge the concern, reframe or prove against it.
6. **Translate for each audience segment.** Same core promise, different emphasis and language. Write 2-3 sentences per segment: what they care about, which pillars to lead with, what objection to pre-handle.
7. **Define off-limits.** What should never be said, what claims need legal review, what comparisons are unprovable.
8. **Return the message house document** with core promise, pillars, proof map, objection handling, audience translations, and off-limits.

## Output contract
- Core promise (one sentence)
- Support pillars (3-5, each with proof)
- Objection handling (top 3-5, with responses)
- Audience translations (per-segment phrasing)
- Off-limits section (what not to say)
- Proof map: which pillars have backing, which need generation
- Channel deployment notes: where each element appears

## Failure modes to avoid
- Multiple core promises — if everything is core, nothing is. The audience remembers one thing.
- Proof pillars without evidence — those are claims, not pillars. "Fast" without a measurement is a wish.
- Audience messages that change the promise instead of translating it — each audience gets the same house, different emphasis.
- Generic promises that apply to any competitor — "we save you time" is not a promise, it's a category.
- No off-limits section — without it, the team will overclaim. The off-limits list prevents the biggest messaging failures.
- Building the house without auditing current messaging first — you'll repeat the same contradictions.

## Handoff cues
- Full message house document ready to share with team.
- Proof pillars flagged: which are backed, which need generation.
- Asset update list: which existing materials need rewriting to align.
- Quick-reference card: core promise + top 3 pillars in 50 words for internal use.

## Example invocation
- Slash: `/att_message_house <task>`
- Natural language: "Build a message house for this product."
- Example: "Our messaging is a mess — sales says one thing, the site says another. Build the single source of truth."
- Example: "We're launching next month and need everyone on the same page about what we say."
- Often paired with: `att_positioning_workshop`, `att_proof_mining`, `att_launch_plan`

## Quality bar
- The core promise can be repeated back by a stranger after one reading.
- Every pillar has proof or mechanism — no bare claims.
- The top 3 objections are handled explicitly, not ignored.
- Each audience segment gets translation, not a different promise.
- The off-limits section is non-empty — every product has claims it shouldn't make.
- Using the message house should shorten every future writing task by 30%+.

## Related workflows
- Positioning first: `att_positioning_workshop` → `att_message_house`
- Content system: `att_message_house` → `att_content_calendar` → `att_content_repurposing`
- Launch sequence: `att_message_house` → `att_launch_plan` → `att_proof_mining` → `att_thread_writer`
- Proof backing: `att_proof_mining` → `att_message_house` (iterate until pillars are backed)

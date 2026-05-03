--- name: att_positioning_workshop description: "Define who the project is for, what pain it solves, why it wins, and why now." user-invocable: true disable-model-invocation: false metadata: {"openclaw":{"emoji":"\ud83c\udfdb\ufe0f"}} ---
# Positioning Workshop

## Purpose
- Define who the product is for, what pain it solves, why it wins, and why now.
- This is an **attention specialist** for finding the sharp edge of a product's identity — the thing that makes the right people say "that's exactly for me" and the wrong people self-select out.

## Use when
- Use when the message is generic, confused, or easy to confuse with adjacent products.
- Use when entering a crowded category and needing to find a defensible wedge.
- Use when the product serves multiple audiences and the positioning tries to serve all of them equally (serving none).
- Use before building a message house — positioning comes first.

## Avoid when
- Do not use when the user only needs copy from an already-solid positioning strategy.
- Do not use when the product itself is undefined — positioning can't fix a product that doesn't do something specific.
- Do not use for competitive analysis alone — that's `res_competitor_scan`.

## Inputs to gather
- The product's real capability today (not roadmap promises — only what ships now).
- The market alternatives: competitors, workarounds, spreadsheets, and status quo.
- The wedge: what specific tension or unmet need does the product address that alternatives don't?
- Audience beliefs: what does the target user already believe about this category? What do they think they need vs what they actually need?
- Constraints: how bold or conservative can the positioning be? (Regulatory, brand, competitive sensitivity.)
- Competitor messaging: what are they claiming? Where are the gaps in their story?

## Operating rules
- **Positioning is about exclusion as much as inclusion.** The best positioning makes some people say "not for me" — and that's the point. "For everyone" means "for no one."
- **The substitution test:** Replace your product name with a competitor's name in the positioning statement. If it still reads true, the positioning isn't differentiated. Keep sharpening until it breaks.
- **Frame the enemy, the wedge, and the proof.** Enemy = the status quo or competitor approach. Wedge = the specific tension your product resolves. Proof = why the wedge is real and your product delivers on it.
- **Category matters more than features.** "We're a project management tool" puts you in a crowded category. "We're the operating system for solo founders" creates a new one. Choose the category frame intentionally.
- **"Why now" is non-negotiable.** If the product could have existed 5 years ago, the positioning lacks urgency. What changed — in the market, in technology, in user behavior — that makes this the right time?
- **Avoid category clichés.** "AI-powered," "all-in-one," "seamless," "next-gen" — these are noise words. Every competitor says them. Say the specific thing instead.

## Claude Code tool pattern
- Use `res_competitor_scan` to map the competitive landscape before the workshop.
- Use `WebFetch` to read competitor landing pages and find their positioning gaps.
- After the workshop, feed the output into `att_message_house` to build the messaging system.
- Use `att_proof_mining` to verify that the chosen wedge has real proof behind it.

## Expanded workflow
1. **Map the market context.** Who are the competitors? What do they claim? Where are the gaps in their story? What's the status quo the user is currently tolerating?
2. **Define the audience precisely.** Not "developers" — "solo founders building SaaS products without a team." The more specific, the sharper the positioning. Name the archetype.
3. **Name the enemy.** What approach, belief, or system does the product replace? The enemy isn't always a competitor — it's the way things are done now.
4. **Find the wedge.** What tension does the audience feel that the enemy creates? What specific relief does the product provide? The wedge is the gap between current reality and desired state.
5. **Choose the category frame.** Existing category (compete within it), sub-category (carve out a niche), or new category (create one). Each has tradeoffs: existing = recognized but crowded, new = distinctive but requires education.
6. **Write the positioning statement.** Format: "For [specific audience] who [experience specific pain], [product name] is a [category frame] that [delivers specific value] because [proof/mechanism]." Test it with the substitution test.
7. **Stress-test against confusion.** What would a skeptic say? What would a competitor claim? Where would the positioning fall apart under scrutiny? Fix the weak spots.
8. **Define the "why now."** What recent change makes this positioning timely? Technology shift, market shift, behavioral shift, regulatory shift.
9. **Return the full positioning output** with category frame, audience definition, wedge, enemy, proof, and "why now."

## Output contract
- Audience definition (specific archetype, not generic segment)
- Enemy (what approach/belief the product replaces)
- Wedge (the specific tension the product resolves)
- Category frame (existing, sub-, or new category with rationale)
- Positioning statement (one sentence, substitution-tested)
- "Why now" justification
- Proof requirements: what evidence is needed to make the positioning credible
- Anti-confusion notes: how to avoid being mistaken for competitors

## Failure modes to avoid
- Positioning that passes the substitution test — if a competitor could say the same thing, it's not positioning.
- Feature lists instead of positions — "fast, easy, affordable" is not a position, it's a feature checklist anyone can claim.
- Ignoring the category — if you don't choose your category, the market will choose it for you, and they'll put you in the most crowded one.
- Too broad — positioned for everyone means resonant with no one.
- "Best" without "because" — "the best project management tool" is a claim. "The only PM tool built for solo founders who ship weekly" is a position.
- No "why now" — without urgency, the positioning feels like it could have launched any time, which means it's not compelling now.

## Handoff cues
- Positioning statement ready for team review.
- Category frame with rationale for the choice.
- Audience definition specific enough to test against real people.
- Proof requirements: what to generate before going public with the positioning.
- Message house update needed: flag that `att_message_house` should be built or rebuilt from this output.

## Example invocation
- Slash: `/att_positioning_workshop <task>`
- Natural language: "Run a positioning workshop for this product."
- Example: "Our product could be described 5 different ways — help us find the sharp edge."
- Example: "We keep getting compared to [competitor] but we're genuinely different — find the positioning that makes that clear."
- Often paired with: `att_message_house`, `att_proof_mining`, `att_launch_plan`

## Quality bar
- The right people immediately feel seen when they read the positioning.
- The wrong people self-select out — and that's intentional.
- The substitution test fails (competitor names can't be swapped in).
- "Why now" is specific and current, not generic.
- The category frame is a deliberate choice, not an accident.

## Related workflows
- Positioning first: `att_positioning_workshop` → `att_message_house` → `att_content_calendar`
- Launch sequence: `att_positioning_workshop` → `att_launch_plan` → `att_proof_mining`
- Competitive grounding: `res_competitor_scan` → `att_positioning_workshop`

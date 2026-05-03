---
name: att_press_angles
description: "Generate newsworthy framing angles that connect the project to real trends, tension, or stakes."
---

# Press Angles

## Purpose
- Generate newsworthy framing angles that connect the project to real trends, tension, or stakes.
- This is an **attention specialist** for finding the story within the product that journalists would actually cover — not just repackaging marketing copy as a press release.

## Use when
- Use when preparing outreach to media, newsletters, podcasts, or influential curators.
- Use when launching something genuinely new and needing the story to be bigger than "we shipped a feature."
- Use when the product connects to a trend, conflict, or shift that gives it broader relevance.

## Avoid when
- Do not use when there is no genuine news hook or broader relevance — journalists can smell a product pitch dressed as news.
- Do not use for routine updates, minor feature releases, or non-events.
- Do not use when you plan to mass-pitch the same generic email to 20 journalists.

## Inputs to gather
- The news: what's actually new and noteworthy? (Launch, funding, major customer win, data reveal, category shift.)
- Target publications: which outlets cover this space? Which specific journalists write about this category?
- The journalist's audience: what do their readers care about? What stories have they covered recently?
- Proof: data, customer stories, or trend evidence that makes the angle credible.
- The broader trend: what macro shift does this product connect to? (AI adoption, solo founder movement, creator economy, remote work, etc.)

## Operating rules
- **The angle must be bigger than the product itself.** "We launched a tool" is not news. "The solo founder movement is creating a new class of software that replaces entire teams" is news that happens to feature your product.
- **Tie the story to a real shift, conflict, or surprising data point.** Trend = "X is happening and here's proof." Conflict = "Y approach is failing and here's why." Data = "Z% of [group] are doing [surprising thing]."
- **Avoid fake-news framing for ordinary updates.** Not every feature drop is newsworthy. Overselling routine updates trains journalists to ignore you.
- **One angle per pitch.** Don't give a journalist three story options. Pick the strongest one, make it irresistible, and pitch that.
- **Include proof in the pitch, not promises of proof.** "We have data showing X" in the pitch gets interest. "We can provide data upon request" gets skipped.
- **Personalize every pitch.** Reference the journalist's recent work. Show you read them. Mass-pitched emails go to spam; personalized ones get replies.

## Claude Code tool pattern
- Use `WebFetch` to read the journalist's recent articles and understand their beat and interests.
- Use `att_proof_mining` to find the data points and proof that make the angle credible.
- Use `res_competitor_scan` to find the market context that gives the story tension.

## Expanded workflow
1. **Identify the underlying newsworthiness.** What happened? Why does it matter beyond the product? What trend does it ride? What conflict does it resolve? What surprise does it reveal?
2. **Draft 3-5 framing angles.** Each angle connects the product to a bigger story: a trend, a conflict, a data point, a shift in behavior, or an underdog narrative.
3. **Match each angle to outlet and journalist fit.** A data angle goes to a data journalist. A founder story angle goes to a profiles writer. A trend angle goes to a category expert. Don't pitch a trend story to a product reviewer.
4. **Select the strongest angle for each target.** Not the same angle for everyone — the one most likely to resonate with that specific journalist's audience and recent coverage.
5. **Write the pitch.** Structure: (1) hook — the bigger story, (2) why them — reference their work, (3) the angle — how your product fits, (4) proof — data, customer, or evidence, (5) the ask — a specific next step (brief call, try the product, review data).
6. **Include a ready-to-use quote.** Journalists often need a quote they can drop in. Write one that's punchy, specific, and attributed. This removes friction.
7. **Return the angles, pitches, and tracking plan.**

## Output contract
- 3-5 framing angles with trend/conflict/data connection
- Angle-journalist match: which angle for which outlet
- Pitch emails: personalized per journalist
- Ready-to-use quote
- Press assets: what to prepare (screenshots, data, customer references)
- Tracking plan: who was pitched, when, and follow-up timing

## Failure modes to avoid
- Product pitches disguised as stories — journalists don't write ads, and they can spot them instantly.
- Multiple angles in one pitch — pick one. Confused pitches get deleted.
- No news hook — "we exist" is not news. "X% of [group] are doing [surprising thing]" is.
- Promises of proof instead of proof in the pitch — "we can share data" gets skipped; "here's the data" gets read.
- Mass-pitching the same email to 20 journalists — personalization is the minimum bar.

## Handoff cues
- All pitches sent: journalist, outlet, angle, date.
- Follow-up timing for each pitch.
- Press assets prepared and ready to share.
- Any journalists who responded and what they need next.

## Example invocation
- Slash: `/att_press_angles <task>`
- Natural language: "Find press angles for this launch."
- Example: "Find 3 newsworthy angles for a solo founder launching an AI product in a crowded space."
- Example: "We have usage data showing X. Turn it into a press pitch journalists would cover."
- Often paired with: `att_launch_plan`, `att_proof_mining`, `att_founder_story`

## Quality bar
- Each pitch has one clear angle tailored to the journalist's beat and audience.
- The news hook is timely and specific — not "we launched a product."
- Proof is included in the pitch itself, not promised upon request.
- A ready-to-use quote is provided.
- Every pitch references the journalist's recent work.

## Related workflows
- Launch PR: `att_launch_plan` → `att_press_angles` → `att_outbound_sequences`
- Story building: `att_founder_story` → `att_press_angles`
- Proof backing: `att_proof_mining` → `att_press_angles`

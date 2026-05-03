--- name: att_directory_submission description: "Prepare directory, marketplace, and listing submissions that improve discovery without sounding canned." user-invocable: true disable-model-invocation: true metadata: {"openclaw":{"emoji":"📋"}} ---
# Directory Submission

## Purpose
- Prepare directory, marketplace, and listing submissions that improve discovery without sounding canned.
- This is an **attention specialist** for turning product listings into conversion assets on directory sites — not just filling out forms.

## Use when
- Use when submitting the project to startup directories, app marketplaces, catalogs, or review sites.
- Use when launching with zero audience and needing organic discovery channels that don't require followers.
- Use when updating existing listings that have gone stale or are underperforming.

## Avoid when
- Do not spray the same generic description into every directory — each has its own audience, format, and evaluation criteria.
- Do not submit before the product has enough proof, screenshots, and a working demo to make a compelling listing.
- Do not use for paid advertising placement — that's a different strategy.

## Inputs to gather
- Product name, URL, tagline, and one-line description (tailored per directory).
- Category and subcategory for each directory — miscategorization kills discovery.
- Logo assets in required sizes (usually 128x128, 256x256, 512x512, plus any banner/og:image).
- Pricing model: free, freemium, paid, or open source. Many directories filter by this.
- Unique differentiator: what makes this listing stand out from similar entries? Why should someone click yours over the 50 others in the same category?
- Proof points: reviews, testimonials, usage numbers, or awards that directories display.

## Operating rules
- **Each directory has its own intent, audience, and space limits.** Product Hunt favors novel launches with community engagement. AlternativeTo favors "X alternative to Y" positioning. G2 favors verified reviews. Tailor the listing, not just the logo.
- **Discovery improves when category choice and proof are specific.** Picking the right category matters more than the description. A product in the wrong category is invisible to the people searching for it.
- **Listings should lead to the next action, not just look complete.** A listing without a clear CTA (try free, see demo, read review) is a dead end. The listing's job is to move the visitor to the product.
- **For zero-audience launches, directories are your best friend.** Product Hunt, Hacker News, dev.to, Indie Hackers, Reddit, AlternativeTo — these are channels where strangers discover products they didn't know they needed. Prioritize them.
- **Track every submission.** Create a spreadsheet: directory name, date submitted, status, follow-up date, listing URL, and referral traffic. Without tracking, you waste effort on directories that don't perform and neglect ones that do.

## Claude Code tool pattern
- Use `WebFetch` to review the directory's format, top-performing listings, and submission guidelines before preparing your listing.
- Use `att_proof_mining` to pull the strongest proof points for each directory's audience.
- After submission, track referral traffic via UTM parameters to measure which directories drive actual signups.

## Expanded workflow
1. **Prioritize directories by audience fit.** Not all directories matter equally. Rank by: (a) does your target user search here? (b) does the directory rank in Google for your category? (c) can you get featured or highlighted?
2. **Review top-performing listings in each directory.** What makes them work? What proof do they show? What categories are they in? Learn from what's already winning.
3. **Prepare the listing copy per directory.** Same core truth, different expression. Product Hunt: novel + community angle. AlternativeTo: "alternative to X" framing. App stores: feature-led + review-heavy.
4. **Prepare all required assets.** Screenshots, demo video, logo variants, pricing, support links. Incomplete listings get skipped.
5. **Submit with timing in mind.** Product Hunt: launch at 12:01 AM PST for max visibility. Hacker News: post mid-morning US time on weekdays. Reddit: check the specific subreddit's active hours.
6. **Engage with comments and reviews post-submission.** Directory listings that get engagement rank higher. Respond to every comment, answer every question.
7. **Track results and iterate.** Which directories drive traffic? Which convert? Double down on what works, drop what doesn't.

## Output contract
- Directory priority list: ranked by audience fit and potential impact
- Per-directory listing copy: description, tagline, category selection, proof points
- Asset checklist: screenshots, logos, demo links, pricing info
- Submission tracker: directory, status, follow-up dates
- Referral tracking plan: UTM params for measuring conversion per directory

## Failure modes to avoid
- Copy-pasting the same description across all directories without tailoring.
- Targeting only high-DA directories that aren't relevant to the niche — a niche directory with 500 targeted visitors beats a general directory with 50,000 untargeted ones.
- Submitting before the product has enough proof or screenshots to make a compelling listing.
- No tracking — losing track of what's submitted and what needs follow-up.
- Ignoring post-submission engagement — listings that get community responses rank higher.

## Handoff cues
- Submission tracker with all directories, statuses, and follow-up dates.
- Per-directory listing copy ready to paste.
- Flag any directories that require payment and the expected ROI.
- Note which directories need ongoing maintenance (updating versions, responding to reviews).

## Example invocation
- Slash: `/att_directory_submission <task>`
- Natural language: "Prepare directory submissions for this product launch."
- Example: "I am launching with zero audience. Which directories matter most and what do I submit?"
- Example: "Prepare Product Hunt and AlternativeTo listings for this SaaS launch."
- Often paired with: `att_launch_plan`, `att_proof_mining`, `att_zero_audience_distribution`

## Quality bar
- Each listing is tailored to its directory, not copy-pasted.
- Category selection is deliberate and based on where target users search.
- Proof points are included in every listing.
- Submission tracking is set up before the first submission.
- Post-submission engagement plan exists for the first 48 hours.

## Related workflows
- Launch sequence: `att_launch_plan` → `att_directory_submission` → `att_thread_writer`
- Zero-audience distribution: `att_directory_submission` → `att_content_repurposing` → `att_community_playbook`
- Proof backing: `att_proof_mining` → `att_directory_submission`

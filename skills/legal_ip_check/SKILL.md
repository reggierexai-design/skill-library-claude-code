---
name: legal_ip_check
description: "Audit intellectual property ownership, licensing, and infringement risks before launch."
user-invocable: true
metadata: {"openclaw":{"emoji":"©️"}}
---

# IP Check

## Purpose
Audit intellectual property ownership, licensing, and infringement risks. IP issues discovered after launch are exponentially more expensive to fix than ones caught before. A trademark dispute after you've built brand awareness means starting over. A GPL violation after distribution means legal exposure.

## Use when
Use before launching a product publicly. Use when incorporating third-party code, assets, or APIs. Use when rebranding or renaming. Use when hiring contractors to write code.

## Avoid when
Don't use as a substitute for an IP attorney — this identifies risks; a lawyer should review anything material. Don't skip this because you're "too small to be noticed" — that's when you're most vulnerable.

## Inputs to gather
- Product name and branding: trademark search results?
- Code and dependencies: what's original, what's forked, what's licensed?
- Third-party assets: images, fonts, icons — are licenses compatible with your use?
- API terms of service: do the APIs you depend on allow your use case?
- Open source licenses: are all dependency licenses compatible with your distribution model?

## Operating rules
- Search before you name. A name you can't trademark is a name you can't protect. Use USPTO and local trademark databases.
- Audit every dependency's license. GPL in a proprietary product is a time bomb. MIT/Apache is usually safe. When unsure, check.
- Third-party assets need explicit license verification. "I found it on Google Images" is not a license.
- API terms of service can restrict your use. Some APIs prohibit commercial use, reselling, or certain industries.
- Document everything. If you verified a license, write down when, where, and what you found. This is your defense if challenged.

## Claude Code tool pattern
- Use `eng_dependency_risk` for dependency license auditing.
- Use `legal_terms_review` for API terms of service review.
- Use `safe_install_gate` for package safety checks.

## Expanded workflow
1. **Search your product name.** USPTO database, state databases, common law trademark search. Is the name available and protectable?
2. **Audit all dependency licenses.** Every package in your dependency tree — are licenses compatible with your distribution model?
3. **Verify third-party asset licenses.** Images, fonts, icons — do they allow commercial use and your distribution method?
4. **Review API terms of service.** Do the APIs you use allow your commercial use case? Any restrictions?
5. **Check for patent risks.** Are you implementing any patented algorithms or methods? This is rare for most indie products but worth checking.
6. **Document ownership.** Who owns the code? Contractors? Co-founders? Any IP assignment gaps? If a contractor wrote code without an IP assignment clause, they may own it.
7. **Create an IP risk register.** Item, risk level, mitigation, owner. Track until all items are resolved.

## Output contract
- Trademark search results for product name and branding
- Dependency license audit: compatible, incompatible, needs-review
- Third-party asset license verification
- API terms of service compliance notes
- IP risk register with mitigations

## Failure modes to avoid
- Skipping trademark search — you can't protect a name you don't own.
- GPL in a proprietary product — license violation with legal consequences.
- Using images without license verification — "found on Google" is not a license.
- Ignoring API terms of service — they can revoke access or sue for breach.
- No IP assignment from contractors — you may not own code you paid for.

## Handoff cues
- Trademark search results and name protectability assessment.
- Dependency license audit with compatibility findings.
- IP risk register with top risks and mitigations.
- Any IP assignment gaps that need closing.

## Example invocation
- Slash: `/legal_ip_check <task>`
- Natural language: "Use legal_ip_check to audit intellectual property ownership, licensing, and infringement risks before launch."

## Quality bar
Product name has been searched in relevant trademark databases. All dependency licenses are verified and compatible. Third-party asset licenses are documented. API terms of service are reviewed for compliance. IP risk register is created and reviewed.

## Related workflows
- **IP audit before launch:** `legal_ip_check` → `eng_dependency_risk` → `legal_terms_review` → `eng_release_readiness`
- **License compliance:** `eng_dependency_risk` → `legal_ip_check` → `safe_install_gate`
- **Branding safety:** `legal_ip_check` → `att_positioning_workshop` (ensure name is defensible)

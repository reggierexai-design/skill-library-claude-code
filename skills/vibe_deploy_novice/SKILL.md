---
name: vibe_deploy_novice
description: "Deploy your first app to the internet even if you've never used a terminal before."
user-invocable: true
metadata: {"openclaw":{"emoji":"🌐"}}
---

# Deploy Novice

## Purpose
Deploy your first app to the internet even if you've never used a terminal before. Deployment is the most intimidating step for vibe coders — but it's also the most important. An app that only runs on your laptop isn't a product. It's a hobby.

## Use when
Use when your app works locally and you want it live on the internet. Use when you need to share your app with users. Use when you're ready to go from prototype to product.

## Avoid when
Don't deploy code you haven't tested locally. Don't deploy without understanding the basics of what's being exposed. Don't use for production-grade deployments that need scaling, monitoring, and security hardening.

## Inputs to gather
- App type: static site, web app with backend, mobile app?
- Framework: what did you build with? (React, Next.js, Flask, etc.)
- Hosting preference: Vercel, Netlify, Railway, Render, or need a recommendation?
- Custom domain: do you have one or use the default?
- Environment variables: API keys, database URLs, secrets?

## Operating rules
- Start with the easiest platform for your stack. Next.js → Vercel. Static → Netlify. Backend → Railway or Render. Don't fight the defaults.
- Never hardcode secrets. Use environment variables. If you pushed an API key to GitHub, rotate it immediately.
- Deploy early and often. The first deploy is the hardest. After that, it gets easier.
- Use the platform's defaults. Don't customize build settings, regions, or caching until you need to.
- Test the deployed version, not just local. Things behave differently on the internet.

## Claude Code tool pattern
- Use `vibe_prompt_to_app` to get the app ready for deployment.
- Use `vibe_debug_no_code` if deployment fails.
- Use `safe_secret_hygiene` to check for exposed secrets before deploying.

## Expanded workflow
1. **Choose your hosting platform.** Match your stack to the easiest platform. Don't overthink it.
2. **Prepare your project.** Make sure it runs locally. Check for hardcoded secrets. Add a .gitignore.
3. **Connect to the platform.** Usually: sign up → connect GitHub repo → or use CLI. Follow the platform's guide.
4. **Set environment variables.** Add any API keys or config in the platform dashboard. Never in the code.
5. **Deploy.** Hit the deploy button or push to the connected branch. Wait for the build.
6. **Test the deployed version.** Open the live URL. Test the core flow. Check for differences from local.
7. **Set up a custom domain (optional).** Point your domain's DNS to the platform. Most platforms have guides.
8. **Document the deployment process.** Write down what you did. You'll need it again.

## Output contract
- Live app URL accessible on the internet
- Deployment steps documented
- Environment variables configured (not in code)
- Custom domain connected (if applicable)
- Known differences between local and deployed behavior

## Failure modes to avoid
- Hardcoded secrets pushed to GitHub — rotate immediately if this happens.
- Choosing a complex platform when a simple one works — use the easiest option.
- Not testing the deployed version — local and production can behave differently.
- One big deploy instead of iterative deploys — deploy early, deploy often.
- No documentation of the process — you'll forget what you did next time.

## Handoff cues
- Live URL and deployment platform.
- Deployment steps documentation.
- Any issues encountered and their fixes.
- Next deployment steps (CI/CD, custom domain, monitoring).

## Example invocation
- Slash: `/vibe_deploy_novice <task>`
- Natural language: "Use vibe_deploy_novice to deploy your first app to the internet even if you've never used a terminal before."

## Quality bar
App is accessible at a live URL. No secrets are in the code. Environment variables are configured in the platform. Core flow works on the deployed version. Deployment steps are documented.

## Related workflows
- **First deployment:** `vibe_prompt_to_app` → `vibe_debug_no_code` → `vibe_deploy_novice` → live
- **Secret safety:** `safe_secret_hygiene` → `vibe_deploy_novice` → `eng_release_readiness`
- **Ship cycle:** `vibe_deploy_novice` → `solo_rapid_ship` → `att_changelog_story`

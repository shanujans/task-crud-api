# Retrospective — General AI Fluency Track

*Written for the person I was in Week 1.*

---

## What I Set Out to Do

In Week 1, I had a vague goal: "get better at AI-assisted building and ship a portfolio that proves it." I'd built things before — a loan-risk ML package on PyPI, a Telegram file uploader, a C# desktop app for coursework — but they were scattered. No through-line. No claim. No habit of documenting *how* I built them so the next one would be faster.

The track promised a structure: weekly assignments that stack, a portfolio that compounds, and a capstone that proves the whole thing. I took that literally.

---

## What Changed

**Week 3 (Consistency, Not Talent) was the pivot.** I wrote the one-line claim: *"I build the AI layer and the backend it runs on."* That sentence forced every subsequent decision. The portfolio isn't a gallery — it's evidence for that claim. The capstone isn't a project — it's the strongest proof point. The weekly review agent (FL-07) isn't a toy — it's the system that keeps the compounding going.

**The portfolio stopped being a design exercise and became a delivery vehicle.** I removed Lottie animations (they killed mobile performance), replaced the CDN Tailwind with a local build, added real form validation, wired Supabase persistence, and deployed to a custom domain (`shanujan.is-a.dev`). The "Open It on Your Phone" assignment (Week 6) wasn't polish — it was the moment I treated the site like a product real people use.

**AI went from "write code for me" to "think with me."** The FL-07 Claude Project is the clearest example: I didn't ask it to generate a weekly review. I designed a 7-step conversation flow, wrote the system prompt, defined the output format, and *then* used it. The AI runs the interview; I own the answers. That pattern — human structures, AI executes, human verifies — is now how I approach everything.

---

## What I'd Build Next

**BE-10: Multi-Tenant AI Agent Gateway.** (Already scoped in the FL Capstone deliverable.)

A production-grade gateway between clients (web, mobile, Slack, WhatsApp) and LLM providers (OpenAI, Anthropic, Gemini, local models). Handles auth, rate limiting, routing, observability, cost control per tenant. Stack: Cloudflare Workers + Hono + D1 + Inngest.

Why this one: it directly extends BE-09 (decision flow), BE-03 (auth/triage), and the capstone (widget platform). It proves the claim at infrastructure level — every AI product needs this layer; most engineers haven't built it. Three-week sprint, verifiable weekly deliverables, $0 infra on Workers free tier.

---

## Three Most Transferable Things I Learned

### 1. Structure the conversation, don't just prompt.
The difference between "write me a README" and "here's a 7-step interview flow, run it and emit this exact Markdown format" is the difference between a draft you rewrite and an artifact you ship. The FL-07 system prompt taught me: **define the contract first, then hand it to AI.** Every assignment since has followed that pattern.

### 2. Honest limitations beat fake perfection.
The capstone's `README_FL09.md` lists five limitations — in-memory rate limiting, minimal auth, mocked geo, plain widget UI, console-log email. Each has a *reason* (brief scope, grade focus, deterministic tests). On camera (demo script), I explain one design decision and one limitation without hedging. Reviewers trust the work more because I'm not pretending it's production-hardened. **Credibility comes from naming the edges, not hiding them.**

### 3. The portfolio is a product, not a poster.
The "Open It on Your Phone" fixes weren't cosmetic: Hero without Lottie (readable terminal), Projects with local icons (no external deps), Footer with 48px touch targets and autocomplete, Navbar with 44px hamburger, `font-display: swap`, reduced-motion support, vendor chunk splitting. The build is 113KB gzipped. It works on a 3G connection on a 5-year-old Android. That discipline — **treat the portfolio like the thing you're proving you can build** — is the habit that compounds.

---

## Closing Note to Week 1 Me

You thought this track was about learning AI tools. It's not. It's about building a *system* where AI is a reliable component — one you can verify, one that compounds across weeks, one that leaves a trail of honest artifacts. The claim ("I build the AI layer and the backend it runs on") isn't marketing. It's the constraint that makes every decision obvious.

The capstone is done. The portfolio is live. The next case (BE-10) is scoped and calendared. The weekly review agent is waiting for Monday's commit data.

Keep going. The compounding is real.
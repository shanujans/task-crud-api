# FL Capstone — Next Case Study Protocol

## How to Add the Next Case Study (Three-Beat Shape)

**Beat 1 — Problem**  
What was the real constraint or pain point? One sentence. No fluff.  
*Example: "Kapruka.lk shoppers dropped off at checkout because language switching took 4 clicks and 7 minutes."*

**Beat 2 — What You Did**  
What did you build, and what was the key technical decision? Two bullets max.  
*Example: "Built TARA — a multilingual AI agent on Cloudflare Workers + Gemini. Key decision: stream tool calls to cut perceived latency from 7 min → 2 min."*

**Beat 3 — What Came of It**  
One measurable outcome + one live proof link.  
*Example: "Checkout time 7 min → 2 min. Live: tara-green.vercel.app | Code: github.com/shanujans/tara-agent"*

---

**Template for each new case** (copy-paste into `portfolio-source/components/Work.tsx` → add to `cases` array):

```tsx
{
  id: "short-slug",                    // e.g. "be09-decision-flow"
  title: "Human-Readable Title",       // e.g. "AI Decision Flow Builder"
  problem: "One-sentence problem statement",
  action: [
    "Key technical decision / what you built",
    "Stack: Next.js + Inngest + React Flow + OpenAI"
  ],
  result: "Measurable outcome + live URL + repo URL",
  tags: ["AI", "Backend", "Full-Stack"], // pick from your tag taxonomy
  featured: false,                      // true only for the lead case (TARA)
  links: {
    live: "https://...",
    repo: "https://github.com/shanujans/...",
    demo: "https://..."                 // optional: Loom / video walkthrough
  },
  screenshot: "/screenshots/short-slug.png" // add real capture to public/screenshots/
}
```

**Where it lives in the portfolio:**
1. Add entry to `cases` array in `components/Work.tsx`
2. Drop real screenshot in `public/screenshots/short-slug.png`
3. Update `Work` page renders automatically (no other files to touch)
4. Commit → push → GitHub Pages auto-deploys (gh-pages branch)

**Time to add one case:** ~15 minutes (write 3 beats, drop screenshot, push).

---

## Next Real Piece of Work (Named + Scoped)

**Name:** **BE-10: "Multi-Tenant AI Agent Gateway"**  
A production-grade gateway that sits between clients (web, mobile, Slack, WhatsApp) and LLM providers (OpenAI, Anthropic, Gemini, local models). Handles auth, rate limiting, routing, observability, and cost control per tenant.

**Why this one:**  
- Directly extends BE-09 (decision flow) + BE-03 (auth/triage) + capstone (widget platform)
- Proves the "AI layer + backend" claim at infrastructure level
- Real portfolio value: every AI product needs this; most engineers haven't built it

**Scope (verifiable, 3-week sprint):**
| Week | Deliverable | Verifiable Link |
|------|-------------|-----------------|
| 1 | Core gateway: Cloudflare Worker + Hono + D1 (tenant config, API keys, routing) | `github.com/shanujans/ai-agent-gateway` + Workers deploy URL |
| 2 | Provider abstraction: OpenAI / Anthropic / Gemini / Ollama unified interface + streaming | Same repo, `/providers` directory |
| 3 | Observability: request logs, latency p95, token spend per tenant, alerting via Inngest | Live dashboard URL + Grafana Cloud free tier |

**Success metric:** Serve 100 req/day across 3 test tenants with <200ms p95 overhead, $0 infra cost (Workers free tier).

---

## Concrete Reminder Set

**Calendar Event (Google Calendar / Outlook):**  
- **Title:** `🚀 Start BE-10: Multi-Tenant AI Agent Gateway`  
- **Date:** **Monday, September 21, 2026** (first working day after capstone submit)  
- **Time:** 09:00–11:00 (deep-work block)  
- **Recurrence:** Weekly, Monday 09:00–11:00 for 3 weeks (Sept 21, Sept 28, Oct 5)  
- **Description:**  
  ```
  Week 1: Scaffold Cloudflare Worker + Hono + D1 schema. Push to github.com/shanujans/ai-agent-gateway
  Week 2: Implement provider abstraction layer (OpenAI, Anthropic, Gemini, Ollama). Streaming support.
  Week 3: Add observability (request logs, token spend, p95 latency). Deploy to Workers + Grafana Cloud.
  Success: 100 req/day across 3 tenants, <200ms p95 overhead.
  ```

**Backup nudge (GitHub Issues):**  
- Created issue `shanujans/portfolio-source#1` titled "Add BE-10 case study after launch" — auto-assigns to me, triggers notification on Sept 21.

**Claude Project Context (Preserved):**  
- Weekly Review Agent (this project) already knows: voice, stack (Cloudflare Workers, React, Inngest, D1, OpenAI), identity kit (purple/amber, Manrope/Inter), claim ("I build the AI layer and the backend it runs on").  
- Next case conversation = 5 minutes: "Add BE-10 case using the three-beat template. Here's the problem/action/result. Generate the Work.tsx entry."  
- No rebuild needed. The project *is* the context.

---

## Submission Evidence

| Item | Evidence |
|------|----------|
| How-to note | This file (`fl_capstone_next_case.md`) — three-beat template + exact file locations |
| Named next piece | **BE-10: Multi-Tenant AI Agent Gateway** — scoped, 3-week plan, verifiable links |
| Reminder set | Google Calendar recurring event (Mon 09:00, 3 weeks) + GitHub Issue `shanujans/portfolio-source#1` |
| Claude Project preserved | Weekly Review Agent prompt at `fl07_system_prompt.md` — voice, stack, identity kit all encoded |

---

**Deliverable Link:**  
`https://github.com/shanujans/flyrank/blob/main/fl_capstone_next_case.md`

**Portal Submission:**  
Submit this file URL to `https://aifluency.flyrank.ai/week-10.html#send-the-link`
# Build-in-Public Post — "I Build the AI Layer and the Backend It Runs On"

*Draft for LinkedIn / Dev.to / FlyRank showcase thread*

---

## The Hook

Six months ago, my portfolio was a graveyard of half-finished projects. Today, `shanujan.is-a.dev` is a live, mobile-first site with a custom domain, GA4 analytics, a FlyRank graduate badge, and a capstone project that passes 17/17 automated tests — including cross-origin widget rendering, geo fallback chains, and honeypot spam prevention.

The difference wasn't talent. It was a habit.

---

## The Real Decision: In-Memory Rate Limiting (And Why I Kept It)

The capstone brief explicitly said: *"Distributed rate limiting is out of scope."* I could have reached for Redis anyway — it would've looked more "production-ready" on paper. But the brief was right: the grade lives in the backend hardening, not the infra.

So `app/rate_limit.py` is a Python dict with a sliding window. Single-process. Resets on restart. Doesn't share state across workers.

**Here's the honest part:** If this went to prod tomorrow, this is the *first* thing I'd swap. But for the capstone, keeping it simple meant I could spend that complexity budget on the things that actually mattered: the geo fallback chain (provider A → provider B → store anyway), the safe side effect (notification failure never blocks the 201), the honeypot that returns a fake 201 to bots while storing nothing.

**Lesson:** Constraints aren't limitations — they're focus. The brief gave me permission to say "not this," so I could say "yes, this" to the hardening that actually proves the claim.

---

## The Real Limitation: Mocked Geo by Default

Flip `MOCK_GEO=true` in `.env` and the geo enrichment returns deterministic Sri Lanka data (Provider A: Colombo, Provider B: Negombo). Flip it `false` and it hits ip-api.com and ipapi.co — free tiers, 45 req/min and ~1,000/day.

The fallback chain logic is real. I proved both providers down → submission still succeeds without geo (`test_probe4_both_providers_down_still_succeeds_without_geo`). But the *data* is mocked by default.

**Why:** Deterministic tests. The brief said "mock the geo providers when you prove the fallback." So I did. But it means the enrichment you see in the dashboard isn't real visitor location — it's a controlled test double.

**Lesson:** Every mock is a trade-off. Deterministic CI vs. real-world data. I chose the former for the capstone. The code supports both — flip the flag — but the default honors the brief's grading reality.

---

## What This Proves

> **I build the AI layer and the backend it runs on.**

- **BE-09:** AI Decision Flow Builder — React Flow + Inngest + OpenAI, deployed on Vercel
- **BE-08:** PDF Report Generator — FastAPI + Playwright, 200 seeded orders, 4 aggregations, clean page breaks
- **BE-06:** Background Job Framework — FastAPI + threading, Redis-ready, idempotent
- **BE-03:** Auth API + Triage — Supabase Auth, Swagger, `/triage` endpoint with OpenRouter LLM
- **Capstone:** Embeddable Widget Platform — FastAPI + SQLite, 17 tests, cross-origin proven, $0 stack
- **Portfolio:** React + Vite + Tailwind, custom domain, mobile-first, real contact form → Supabase

---

## The System That Keeps It Going

The FL-07 Weekly Review Agent (a Claude Project) runs a 7-step interview every week:
1. Fetch commits across 5 repos
2. Label the week
3. What shipped (links + SHAs)
4. One thing genuinely understood
5. What blocked (specific)
6. Metrics (commits, LOC, latency, hours)
7. Top 3 verifiable next-week goals

It emits a Markdown file to my Obsidian vault. No "great job!" — just accountability. The AI runs the interview; I own the answers.

---

## What's Next

**BE-10: Multi-Tenant AI Agent Gateway.** Starts Monday, Sept 21. Three weeks. Cloudflare Workers + Hono + D1 + Inngest. Gateway between any client and any LLM provider. Auth, routing, rate limiting, observability, cost control per tenant. $0 infra.

Calendar event set. GitHub issue created. Weekly review agent will track it.

---

## The Ask

If you're hiring for AI integration / full-stack / backend roles — or know someone who is — the proof is in the repos above. Not a resume bullet. Running code. Honest limitations. Verifiable tests.

**Portfolio:** https://shanujan.is-a.dev/  
**Capstone:** https://github.com/shanujans/flyrank-capstone-widgetplatform  
**All BE projects:** https://github.com/shanujans?tab=repositories

---

*Built during the FlyRank General AI Fluency track. The certificate is nice. The habit is the asset.*
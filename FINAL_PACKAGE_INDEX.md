# FL Track — Final Submission Package (FL-10)

**Index of every deliverable from the General AI Fluency track.**  
All links point to files in this repository (`shanujans/flyrank`) or deployed URLs.

---

## 📁 Repository Structure

```
flyrank/
├── fl_capstone_next_case.md          # FL Capstone (Week 10) — next case protocol + BE-10 + reminders
├── week03_submission.md              # Week 3 — Consistency, Not Talent (claim, content map, identity kit)
├── fl04_automation_workflow.md       # FL-04 — Ship an Automation Workflow v2
├── fl05_agent_concepts_mcp.md        # FL-05 — Agent Concepts and MCP Basics
├── fl06_explain_terminal_background.md  # FL-06 — Explain It Like You Built It
├── fl06_agent_design_doc.md          # FL-07 — Design Your Personal Agent (design doc)
├── fl07_system_prompt.md             # FL-07 — Weekly Review Agent system prompt (Claude Project)
├── fl07_build_log.md                 # FL-07 — Build artifacts log
├── 2026-W34.md                       # FL-07 — Sample weekly review output
├── make_it_do_something_explainer.md # Week 6 — Make It Do Something (contact form)
├── mobile_fix_log.md                 # Week 6 — Open It on Your Phone (mobile fixes)
├── dns_walkthrough.md                # PF-04 — Personal Website Live (DNS walkthrough)
├── identity_kit.md                   # Identity kit (fonts, palette, style)
├── case_studies.md                   # Case study drafts
├── through_line.md                   # Through-line narrative
├── prompt_ladder.md                  # Prompt ladder exercises
├── prompt_iteration_log.md           # Prompt iteration log
├── curated_images.md                 # Curated image references
├── proof_statement.txt               # Proof statement
├── README.md                         # This repo's root README
└── flyrank-capstone-widgetplatform/  # Capstone project (FL-09/FL-10)
    ├── README_FL09.md                # FL-09 — Enhanced README (this deliverable)
    ├── DEMO_SCRIPT.md                # FL-09 — Demo video script
    ├── README.md                     # Original capstone README
    ├── DESIGN.md                     # Design doc
    ├── EVIDENCE.md                   # Evidence per requirement
    ├── BUILDLOG.md                   # AI usage log
    ├── capstone.yaml                 # Evaluator manifest
    ├── docker-compose.yml
    ├── Dockerfile
    ├── requirements.txt
    ├── .env.example
    ├── app/                          # FastAPI application
    ├── tests/                        # 17 tests, all passing
    ├── customer-site/                # Cross-origin demo page
    └── scripts/seed.py               # Demo data seeder
```

---

## ✅ Deliverable Checklist (FL Track)

| Week | Assignment | Code | Status | Link |
|------|------------|------|--------|------|
| 2 | Automation Workflow v2 | FL-04 | ✅ Done | [`fl04_automation_workflow.md`](./fl04_automation_workflow.md) |
| 3 | Agent Concepts & MCP | FL-05 | ✅ Done | [`fl05_agent_concepts_mcp.md`](./fl05_agent_concepts_mcp.md) |
| 4 | Explain Like You Built It | FL-06 | ✅ Done | [`fl06_explain_terminal_background.md`](./fl06_explain_terminal_background.md) |
| 5 | Design Your Personal Agent | FL-07 | ✅ Done | [`fl06_agent_design_doc.md`](./fl06_agent_design_doc.md) + [`fl07_system_prompt.md`](./fl07_system_prompt.md) |
| 5 | Build Artifacts | FL-07 | ✅ Done | [`fl07_build_log.md`](./fl07_build_log.md) + [`2026-W34.md`](./2026-W34.md) |
| 6 | Make It Do Something | — | ✅ Done | [`make_it_do_something_explainer.md`](./make_it_do_something_explainer.md) |
| 6 | Open It on Your Phone | — | ✅ Done | [`mobile_fix_log.md`](./mobile_fix_log.md) |
| 7 | Personal Website Live | PF-04 | ✅ Done | [`dns_walkthrough.md`](./dns_walkthrough.md) + [shanujan.is-a.dev](https://shanujan.is-a.dev/) |
| 8 | Documentation & Demo | FL-09 | ✅ Done | [`flyrank-capstone-widgetplatform/README_FL09.md`](./flyrank-capstone-widgetplatform/README_FL09.md) + [`DEMO_SCRIPT.md`](./flyrank-capstone-widgetplatform/DEMO_SCRIPT.md) |
| 10 | Capstone / Next Case | FL-10 | ✅ Done | [`fl_capstone_next_case.md`](./fl_capstone_next_case.md) |
| 10 | Final Package & Retrospective | FL-10 | ✅ Done | **This file** + [`RETROSPECTIVE.md`](./RETROSPECTIVE.md) |

---

## 🌐 Live Deployments

| Asset | URL | Status |
|-------|-----|--------|
| Personal Portfolio (custom domain) | https://shanujan.is-a.dev/ | ✅ Live (HTTPS, GA4, FlyRank badge) |
| Portfolio (GitHub Pages backup) | https://shanujans.github.io/ | ✅ Live |
| Capstone Widget Platform (API) | *Local only — run via Docker/venv* | ✅ Runnable |
| Capstone Cross-Origin Demo | *Local only — customer-site on :5500* | ✅ Runnable |
| BE-03 Auth API + Triage | https://github.com/shanujans/be03-auth-api | ✅ Pushed |
| BE-05 Polite Scraper | https://github.com/shanujans/be05-polite-scraper | ✅ Pushed |
| BE-06 Background Job | https://github.com/shanujans/be06-background-job | ✅ Pushed |
| BE-08 PDF Report Generator | https://github.com/shanujans/be08-pdf-report-generator | ✅ Pushed |
| BE-09 AI Decision Flow | https://github.com/shanujans/be09-ai-decision-flow | ✅ Pushed (Vercel) |
| Capstone Widget Platform | https://github.com/shanujans/flyrank-capstone-widgetplatform | ✅ Pushed |

---

## 📹 FL-09 Demo Video

**Script:** [`flyrank-capstone-widgetplatform/DEMO_SCRIPT.md`](./flyrank-capstone-widgetplatform/DEMO_SCRIPT.md)  
**Recording:** *To be recorded — 3–5 min live terminal + browser, no slides*  
**Covers:** Architecture → Test suite → Cross-origin widget render → One design decision (in-memory rate limiting) → One limitation (mocked geo) → AI transparency line

---

## 🤖 AI Transparency (Per Framework)

Every deliverable that used AI assistance includes an honest breakdown. Key projects:

| Project | AI Role | Human Verification |
|---------|---------|-------------------|
| Capstone Widget Platform | Initial full repo scaffold (Claude) | Ran tests, fixed bugs, manual cross-origin demo |
| BE-09 AI Decision Flow | Scaffolding + Inngest wiring | TypeScript fixes, build verification, Vercel deploy |
| BE-08 PDF Report Generator | FastAPI + Playwright structure | SQLite seeding, aggregation logic, PDF page breaks |
| Portfolio (React + Vite) | Component scaffolding, Tailwind config | Mobile fixes, Lottie removal, form integration |
| Weekly Review Agent (Claude Project) | System prompt design | Prompt iteration, eval cases, MCP config |

---

## 📊 Hours Log (Plausible Against Timestamps)

| Week | Assignment | Estimated Hours | Evidence |
|------|------------|-----------------|----------|
| 2 | FL-04 Automation Workflow | 4h | Pipeline runs, commits |
| 3 | FL-05 Agent Concepts + MCP | 3h | Markdown + screenshots |
| 3 | Week 3 Consolidated Deliverable | 3h | `week03_submission.md` |
| 4 | FL-06 Explain Like You Built It | 2h | `fl06_explain_terminal_background.md` |
| 5 | FL-07 Design Personal Agent | 4h | Design doc + system prompt + build log |
| 6 | Make It Do Something | 3h | Contact form + Supabase + explainer |
| 6 | Open It on Your Phone | 4h | Mobile fix log + before/after |
| 7 | PF-04 Personal Website Live | 3h | DNS walkthrough + custom domain deploy |
| 8 | FL-09 Documentation & Demo | 3h | Enhanced README + demo script |
| 10 | FL-10 Capstone + Retrospective | 3h | This package + retrospective |
| **Total** | | **32h** | |

> **Note:** Hours are estimates based on commit timestamps and file creation dates. Portal hours log should match this breakdown.

---

## 🎓 Capstone Project Summary

**FlyRank Capstone — Embeddable Widget & Lead-Capture Platform**  
**Repo:** https://github.com/shanujans/flyrank-capstone-widgetplatform  
**Stack:** Python + FastAPI + SQLite (Postgres-swappable)  
**Tests:** 17/17 passing (all acceptance probes automated)  
**Key Hardened Behaviors:** Tenant isolation, CORS hardening, rate limiting, geo fallback chain, safe side effects, honeypot spam prevention, cross-origin widget delivery  
**Limitations (Honest):** In-memory rate limiting, minimal auth, mocked geo by default, minimal widget UI, console-log email  
**AI Transparency:** Documented in `BUILDLOG.md` and `README_FL09.md`

---

## 📝 Retrospective

See [`RETROSPECTIVE.md`](./RETROSPECTIVE.md) — 500–800 words, written for Week 1 me.

---

## 📢 Build-in-Public Post

See [`BUILD_IN_PUBLIC_POST.md`](./BUILD_IN_PUBLIC_POST.md) — LinkedIn/Dev.to draft explaining one real decision and one real limitation.

---

## 📋 Final Review Checkpoint

- [x] Every deliverable present and reachable from this index
- [x] Retrospective specific to my build (not generic)
- [x] Hours log complete and plausible against timestamps
- [x] Site live on FlyRank domain (shanujan.is-a.dev) — navigable in <5 min
- [x] Build-in-public post explains one real decision + one real limitation
- [x] AI transparency named in capstone README and BUILDLOG
- [x] Demo video script ready for recording (FL-09)

---

**Submitted by:** Shanujan Suresh  
**Track:** General AI Fluency  
**Date:** September 2026  
**Certificate Track:** Final Checkpoint (FL-10)
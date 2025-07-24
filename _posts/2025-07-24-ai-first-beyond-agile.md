---
layout: post
title: "AI-First ≠ Agile-Plus: What Using AI-First Actually Means"
date: 2025-07-24
tags: [AI-literacy]
description: "'AI-first' is everywhere lately. But beyond Agile buzzwords and Bezos' pizza teams, what does AI-first actually mean for engineers in practice?"
last_updated: 2025-07-24
author: "Nils Durner"
categories: [journal]
---

Today, Armand Ruiz (VP of AI Platform at IBM) posted [his thoughts](https://www.linkedin.com/posts/armand-ruiz_thoughts-on-how-to-build-an-ai-first-company-activity-7354103116046196737-7kq8) on building an "AI-first company." Among his points: culture beats models, small teams have outsized impact, and "Slack is the new org chart."

These ideas aren't particularly new. Agile methodology emphasized similar values decades ago, and Jeff Bezos' "two‑pizza" rule for team size is well-known. Ruiz’s list, while useful, feels closer to classic Silicon Valley wisdom than something uniquely "AI-first."

I want to suggest a more precise meaning of "AI-first" at two distinct levels:

## 1. Personal AI-first: "Try AI Before Doing it Manually"

An "AI-first" mindset personally means explicitly considering AI tools first - before reaching for traditional manual methods. It's a simple, practical rule you learn by doing until it becomes muscle memory.

Three concrete examples from my own recent experience:

### 1.1 Process Visualization (Heise Article)

In my recent [Heise article](https://www.heise.de/ratgeber/Prozessvisualisierung-mit-generativer-KI-im-Praxistest-10266093.html), I describe practical visualization use-cases: turning document piles and abstract ideas into shareable diagrams with generative AI.

### 1.2 Personalized Daily News Agent (OpenAI Demo)

Inspired by [OpenAI’s recent o3/o4‑mini demo (timestamp 8:05)](https://www.youtube.com/watch?v=sq8GBPUb3rk&t=486s), you can have an AI agent scan news daily, filter by personal interests, surface one surprising fact, plot data, and hand you a blog‑ready snippet. That’s AI-first as discovery - hard to match manually.

### 1.3 Lost Luggage and Rapid Form-Filling

An airline delayed my luggage; I had to submit a reimbursement form. Instead of retyping everything, I:

1. Captured a full-page screenshot of the form (Safari DevTools).
2. Uploaded it plus my e-ticket, delay confirmation, and an Apple Music receipt (for personal details) into ChatGPT (o3).
3. Prompted: _"Give me the form field inputs in order for quick copy/paste."_  

Result: nearly all field values ready to paste as I progressed. A few were missing, so I switched to o4‑mini and asked follow-up questions (“Ticket number?”).

**Pattern:** Unstructured data → AI structuring → Human verification.

## 2. Organizational AI-first: Practical Perspective (Short & Sweet)

For organizations, "AI-first" goes beyond Agile-style recommendations around teams and culture. It means using AI explicitly as the default first step when designing processes, products, and decision-making.

Rather than turning this post into a management handbook, here are two solid meta-sources if you want the broad picture without hype:

- [Stanford’s AI Index Report](https://aiindex.stanford.edu/report/)
- [State of AI Report](https://www.stateof.ai)

Both show that "AI-first" in organizations is now measurable, not hypothetical.

## 3. Customer/Consumer AI-first: Enable Others

Adjacent to “me” and “the company” sit **your users**. If AI-first for an individual means *I try AI first*, the customer-facing version is: **we make it easy for *them* to try AI first with our product**.

A concrete example: Deutsche Telekom’s upcoming "AI phone" (Magenta AI) bakes an assistant into the device so ordinary users can act through AI—booking tables, answering questions with sources, acting across apps. That’s AI-first UX shipped outward, not just used internally.

For software teams, that translates to **AI-readable affordances**, not just nice prose docs:

- OpenAPI specs that are actually LLM-friendly:
    - clear field names, edge-case examples, calling sequences spelled out
    - pretty-printed to avoid overly long names that may trip up AI coding CLIs like [OpenAI Codex](openai-codex-web) in particular
- Expose your data/tools via a standard interface (e.g. an MCP server) so users’ agents can query and act
- **`/llms.txt` file**: a plain-text/markdown hub that tells models where the high‑value docs, schemas, and policies live
- Mini "prompt packs" or task templates to jump-start common agent workflows.

---

## Takeaways for Engineers

- **Personal AI-first:** Start asking: "Can AI do this quicker or better?" Begin with small, annoying tasks; graduate to the bigger sufferings
- **Customer AI-first:** If you ship software, expose it so *your users’* agents can consume (and perhaps automate) it.
- **Organizational AI-first:** If you just need signal, skim one of the reports above. Plenty of hard numbers, little consultant-speak.

Finally, adopting an "AI-first" mindset doesn't imply AI is always superior or necessary. It simply means giving AI the first chance — thoughtfully, critically, and practically.

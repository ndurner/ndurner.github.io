---
title: "Citation handling with LLM Search"
date: 2025-10-03
last_updated: 2025-10-03T00:00:00+00:00
author: "Nils Durner"
redirect_to:
  - https://ndurner.substack.com/p/llm-search-citation-handling
tags: [Substack]
excerpt: "An Australian lawyer was stripped of his ability to practice after he had submitted a list of hallucinated list of citations to court on July 19, 2024. “The list had been prepared using legal software that utilised AI”, according to reporting by The Guardian. Now, a little over a year later, LLM-powered web search in combination with an Agentic AI frontend allowed me to manage my list of citations"
substack_url: "https://ndurner.substack.com/p/llm-search-citation-handling"
canonical_url: "https://ndurner.substack.com/p/llm-search-citation-handling"
sitemap: false
---

An Australian lawyer was stripped of his ability to practice after he had submitted a list of hallucinated list of citations to court on July 19, 2024. “The list had been prepared using legal software that utilised AI”, according to [reporting by The Guardian](https://www.theguardian.com/law/2025/sep/03/lawyer-caught-using-ai-generated-false-citations-in-court-case-penalised-in-australian-first).

Now, a little over a year later, [LLM-powered web search](web-search-o3) in combination with an [Agentic AI frontend](codex-cli-native) allowed me to manage my list of citations for a technical report rather effortlessly: because the list was in plaintext BibTeX format, the Codex Agent had immediate read and write access to it. While writing the report (in LaTeX, so also accessible to the Codex), I could prompt Codex through the Visual Studio Code IDE to add citations I vaguely remembered (“at … add a reference to the GPT-5 Model Card or System Card”) or already had a pointer for and just needed the citation details fleshed out and/or implemented (e.g. from arXiv or retrieved via ChatGPT Web Search). I checked the citations after Codex had added them, and found only two minor issues:

- f...

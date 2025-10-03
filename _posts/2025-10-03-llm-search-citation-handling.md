---
layout: post
title: "Citation handling with LLM Search"
date: 2025-10-03
tags: [llm, openai, codex, web search, agents, chatgpt]
last_updated: 2025-10-03T12:53:00+02:00
author: "Nils Durner"
categories: [journal]
---

An Australian lawyer was stripped of his ability to practice after he had submitted a list of hallucinated list of citations to court on July 19, 2024. "The list had been prepared using legal software that utilised AI", according to [reporting by The Guardian](https://www.theguardian.com/law/2025/sep/03/lawyer-caught-using-ai-generated-false-citations-in-court-case-penalised-in-australian-first).

Now, a little over a year later, [LLM-powered web search](web-search-o3) in combination with an [Agentic AI frontend](codex-cli-native) allowed me to manage my list of citations for a technical report rather effortlessly: because the list was in plaintext BibTeX format, the Codex Agent had immediate read and write access to it. While writing the report (in LaTeX, so also accessible to the Codex), I could prompt Codex through the Visual Studio Code IDE to add citations I vaguely remembered ("at ... add a reference to the GPT-5 Model Card or System Card") or already had a pointer for and just needed the citation details fleshed out and/or implemented (e.g. from arXiv or retrieved via ChatGPT Web Search). I checked the citations after Codex had added them, and found only two minor issues:
1. for the OpenAI resources, Codex preferred to use the URLs of the respective landing pages, rather than:
    1. a direct link to the PDF
    2. an arXiv link and specifier
2. for older publications, it just put the DOI number in, and not the (open access) web URL
Otherwise, they were flawless.

Likewise, Ethan Mollick [reports](https://www.linkedin.com/posts/emollick_my-co-author-lennart-meincke-had-gpt-5-pro-activity-7379645792879353856-X8Mr?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAGX2jIBd6RDsNRYv13Bvu3x4nnCNu96SEw):
> [GPT-5 Pro] caught a tiny error in the citations [of a new journal submission] that we had missed (apparently by estimating the right volume, rather than looking it up!) (This does not mean that the models never hallucinate citations, however, and models weaker than GPT-5 Pro do it more often, but a lot of progress). I have seen hallucinations from the weaker versions of GPT-5. I have not yet seen one from GPT-5 Pro (which doesn’t mean they aren’t ever there, of course)

He's using ChatGPT rather than Codex. In Codex, I switched between the "gpt-5" and "gpt-5-codex" models and found "gpt-5" to be more reliable/useful for writing overall. 
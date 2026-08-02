---
title: "Conversion problems in AI web search"
date: 2026-08-01
last_updated: 2026-08-01T19:33:12+00:00
author: "Nils Durner"
redirect_to:
  - https://ndurner.substack.com/p/conversion-problems-in-ai-web-search
tags: [Substack]
excerpt: "While testing new UI responsiveness changes in MyChatty, I ran a prompt that I know will trigger web search and for which I know the answer: “Who is Nils Durner?” Kimi K3 returned that I hold a patent related to bootstrapping peer-to-peer networks, which I do not. The ingredients for this error come from my ORCID record, a public profile for linking researchers to their publications and other prof"
substack_url: "https://ndurner.substack.com/p/conversion-problems-in-ai-web-search"
canonical_url: "https://ndurner.substack.com/p/conversion-problems-in-ai-web-search"
sitemap: false
---

While testing new UI responsiveness changes in [MyChatty](https://open.substack.com/pub/ndurner/p/mychatty-frontier-genai-at-little), I ran a prompt that I know will trigger web search and for which I know the answer: “Who is Nils Durner?” Kimi K3 returned that I hold a patent related to bootstrapping peer-to-peer networks, which I do not.

The ingredients for this error come from my [ORCID record](https://orcid.org/my-orcid?orcid=0009-0005-4071-0765), a public profile for linking researchers to their publications and other professional work. Among other entries it lists a withdrawn patent application and an academic paper, both from 2008. OpenRouter’s web search tool turned these two entries into one compressed mash-up before presenting it to the Kimi K3 LLM, which led to this erroneous chatbot response.

## **AI distortion**

MyChatty had asked OpenRouter to use its server-side web search tool. A direct replay of the API interaction showed that OpenRouter had accessed ORCID, but the `url_citation` annotation shows that not the full ORCID profile was used. Instead, the web-search tool seems to heavily compress the page - and also mixes up table content ([an old problem coined “AI ...

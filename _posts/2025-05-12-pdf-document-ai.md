---
layout: post
title: "PDFs, LLMs, and 'The Bitter Lesson' in Document AI"
author: "Nils Durner"
categories: [journal]
tags: ["chatgpt", "o3", "pdf", "docling", "openai", "document AI", "operator"]
date: 2025-05-12
last_updated: 2025-05-12
description: "Compares PDF AI tool reviews: Docling vs ChatGPT with config tweaks, applies 'The Bitter Lesson' on compute-centric methods, and highlights LLM extraction inconsistencies."
---

In a recent [LinkedIn discussion](https://www.linkedin.com/feed/update/urn:li:activity:7326127846207217664?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7326127846207217664%2C7326330982683340800%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287326330982683340800%2Curn%3Ali%3Aactivity%3A7326127846207217664%29) around a review of PDF-focused KI-Assistants ([ComputerBase article](https://www.computerbase.de/artikel/apps/pdfs-ki-auswerten-adobe-assistent-notebooklm-chatgpt.92276/)), I touched on limitations, workarounds, and the ongoing tension between domain-specific tooling and general-purpose, ever-evolving AI platforms.

## The Article in Brief

The ComputerBase article put Adobe's new KI-Assistant, Google’s NotebookLM, and ChatGPT through a series of document-related tasks: extracting facts from text, interpreting figures and charts, comparing legal documents, translating and summarizing policy papers, and extracting values from academic studies. The verdict: while all tools are useful for basic text search and summarisation, they reliably fail or hallucinate when it comes to graphical data, tables, or chart-driven values—especially when the answer is not plainly stated in text.

Michael Welsch on LinkedIn summarized the current state as one where enterprise users seeking reliability still need to build their own solutions, citing the lack of acutely engineered parsing, table extraction, and robust source-tracing in out-of-the-box KI-Assistants. He points out that while the required techniques exist, they’re not systematically deployed—presumably because the economics of SaaS AI don't allow for it at consumer price-points (yet).

## On ChatGPT, API-Frontends, and the Limits of Prompting

The article notes ChatGPT's tendency to pull in external information, sometimes to the frustration of those seeking pure document analysis. [As I wrote earlier](chatgpt-copilot-search), there are workarounds - and this is important: the apparent “unreliability” of ChatGPT in document QA scenarios is, at least partly, configurable. For enterprise use, API-based frontends like the ones I have reviewed in [my article on process visualization](ai-assisted-process-visualiaztion-collaboration) offer more stable, repeatable behavior compared to the consumer ChatGPT UI.

## Docling and the Domain-Specific Approach

Christian Bennefeld, another commenter in the LinkedIn thread, brought up [Docling](markitdown-docling-document-parsing) — as a more robust parsing backend for PDF (and other formats). In the thread, Christian volunteered to benchmark Docling against the scenarios tested in the ComputerBase article. This will be valuable: while AI systems with "integrated" PDF capabilities (like ChatGPT or the OpenAI Responses API) are improving, it's unclear to me where we currently stand. As I noted on the LinkedIn thread, it’s worth remembering the lesson of scalability and generalization: quoting Sutton’s ["The Bitter Lesson"](http://www.incompleteideas.net/IncIdeas/BitterLesson.html):

> "General methods that leverage computation are ultimately the most effective, and by a large margin... The only thing that matters in the long run is the leveraging of computation."

My own [Aileen 2 project](aileen), a labor-intensive hackathon agent, is illustrative here. What required painstaking integration of OCR, layout analysis, and model orchestration is now, only months later, available as a single package ([OpenAI's Operator product and CUA model](opernai-computer-use)).

## "Jagged Frontier" and the Reality of LLM Performance

Ethan Mollick’s ["Jagged Frontier"](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged) metaphor is apt: LLMs/VLMs have surprising strengths and unpredictable blind spots. The ComputerBase article’s test of extracting fiber rollout rates from the [BREKO Marktanalyse 2024](https://brekoverband.de/wp-content/uploads/2025/03/breko_marktanalyse_2024.pdf) is a case in point. The article found that also ChatGPT could not determine the market share (in absolute numbers) of Deutsche Telekom. According to my test however, a slightly modified prompt fixed this - at least with o3 and o4-mini via the API. Then again, the o-Series showed unstable performance with a map of German states with percentages assigned (slide 14): the correct result for Berlin was most of the time given wrong (the number presented was the percentage for Bavaria) and only sometimes correct ([see gist](https://gist.github.com/ndurner/7661f2df5d807e48a6b6ef6eb9e0bdad)).

## The Use(lessness) of Human Knowledge Engineering

From the perspective of "The Bitter Lesson", investing in specialized pipelines — be it Docling, custom layout parsers, or hand-crafted extraction rules — may be satisfying and valuable in the short term. I experienced this first-hand with Aileen 2, and the same could be true for Docling-based deployments: as LLMs/VLMs and their tool-use capabilities (see OpenAI Operator, CUA model) scale, their native, integrated approaches may surpass domain-specific systems for mainstream applications. The effort required to keep custom pipelines ahead of the general models may thus quickly become unsustainable, unless there are unique, high-value data or compliance requirements.
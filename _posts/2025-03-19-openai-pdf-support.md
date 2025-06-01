---
layout: post
title: "OpenAI PDF support"
date: 2025-03-19
tags: ["llm", "openai", "pdf"]
last_updated: 2025-03-19
description: "Announces ChatGPT Prompts Playground and API PDF ingestion (100-page/32MB limit), highlighting improved direct support yet reinforcing advanced pre-processing advice."
author: "Nils Durner"
categories: [journal]
---

In the LLM frontend comparison for my [article on process visualization](ai-assisted-process-visualiaztion-collaboration), I have included whether or not the particular frontend includes support for PDF files. Some of the frontends considered do so only poorly: either they only use the text portion, or the PDF gets pre-processed through RAG.  
OpenAI have now added the capability to process PDF files to the Prompts Playground and the API. At first glance, this seems better than what some of the aforementioned frontends deliver. However, there are still limits: as their [guide](https://platform.openai.com/docs/guides/pdf-files?api-mode=chat) details, it's just 100 pages and 32 MB. The recommendations from the deep-dive on PDF (pre-)processing is thus still solid advice.
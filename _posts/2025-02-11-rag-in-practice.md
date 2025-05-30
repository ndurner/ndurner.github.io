---
layout: post
title: "RAG in practice"
author: "Nils Durner"
categories: [journal]
tags: [ai, rag]
date: 2025-02-11
last_updated: 2025-02-11
description: "Details RAG-based PDF chatbot failures: embeddings proximity errors, chunking undermining coherence, and recommends direct large-context ingestion (e.g., 200K+ tokens)."
---

Studies by Salesforce Research and [Google Deepmind](https://arxiv.org/abs/2409.12941), as well as own experiments, have previously cast fundamental doubt on RAG. Now, Richard Meng came forward and [shared practical confirmation](https://www.linkedin.com/posts/berkeleymeng_weve-spoken-with-30-companies-who-developed-activity-7294883636653314049-sjTb?utm_source=share&utm_medium=member_desktop):
> We've spoken with 30 companies who developed RAG-based chatbots on PDF documents. Every single one has failed

The problems he shares are familiar:
> 1) In vector space, "non-dairy products" is often closer to "milk" than "meat," this is a fundamental flaw of vector embedding search because they're very lossy.
> 2) Splitting documents into smaller chunks disrupts coherence, breaking cross-references and context.
[...]

And he concludes:
> If your documents are small: just load them directly into the LLM context. [...] Chatting on documents must be redesigned.

Documents don't have to be small, actually: Anthropic have long [supported 200K contexts](tokenizer-inefficiency-needle-haystack-anthropic-claude) ([less on AWS](chatbots-update) and Google LLM context lengths are specc'ed at 2M.
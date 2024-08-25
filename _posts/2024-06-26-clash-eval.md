---
layout: post
title: "ClashEval: When LLM Safeguards Clash with RAG"
date: 2024-05-20
tags: [llm, rag, misinformation, ai-safety, aleph alpha]
---

A recent paper titled "ClashEval: Quantifying the tug-of-war between an LLM's internal prior and external evidence" (arXiv:2404.10198) reveals that measures implemented to combat misinformation might inadvertently hinder the effectiveness of Retrieval-Augmented Generation (RAG) systems in certain industry applications.

The researchers introduce ClashEval, a framework designed to measure the tension between an LLM's pre-trained knowledge and external information provided during inference. This tension becomes particularly apparent in RAG systems, where the model must integrate its internal knowledge with retrieved external data.

Key findings from the paper suggest that anti-misinformation provisions, while crucial for general-purpose AI safety, can sometimes work against specialized industry use-cases. For instance, in scenarios where domain-specific knowledge is critical, the LLM's tendency to rely on its pre-trained information (which may be outdated or generalized) could override more current or specialized data provided through RAG.

This aligns with talking points previously raised by Aleph Alpha, a German AI company: they defended the lack of guardrails with their Luminous models through "industry use-cases".
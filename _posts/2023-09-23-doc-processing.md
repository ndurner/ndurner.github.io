---
layout: post
title: "Document Processing"
date: 2023-09-21
last_updated: 2023-09-21
description: "Recaps advances in document processing: extended-context LLaMA 2, PDFTriage for PDF QA, Claude summary of books, density prompting, and compression-theory insights."
tags: [Llama 2, Claude, Document-processing, PDF, AI, LLM]
---

Quick recap on recent advancements in Document-processing below.

1. Following up on the huge context size of the **Llama 2** code model (> 100K), contributors of non-profits EleutherAI and Nous-Research have expanded stock Llama 2 attention windows to 128K tokens
    1. Note that this size is only very comparable to OpenAI GPT, Claude etc. because the Tokenizers are different. I have seen 1/4 size variations with a quick check (Llama 2 vs. Aleph Alpha, IIRC).
    2. No real analysis done wrt. to actual accuracy. The paper only reports Perplexity, meaning how confident the model is.
    3. (this should be enough to directly load dozens of pages into the LLM; "stuffing method";)
2. In [PDFTriage: Question Answering over Long, Structured Documents](https://arxiv.org/pdf/2309.08872.pdf) researchers from Stanford + Adobe Research describe LLM Tool-use to **analyze PDF** documents. ("Structured" not in the sense of "unstructured" vs "structured data", but more in the "Tagged PDF" sense).
3. Comp.Sec. luminary Bruce Schneier prompted Claude about one of his books: [LLM Summary of My Book Beyond Fear](https://www.schneier.com/blog/archives/2023/09/llm-summary-of-my-book-beyond-fear.html). Verdict: "The summary is pretty accurate, and so are the criticisms.". He doesn't seem to have uploaded the whole book, though: "Of course, this only works with older books that the LLM has ingested" -- so this is likely not a testament of Claude 2's document summarization abilities.
4. [Chain of Density Prompting](https://arxiv.org/abs/2309.04269) is making waves for **summarization** tasks. The idea has been ported to Claude, but the method needed adaptation.
5. [Language Modeling Is **Compression**](https://arxiv.org/pdf/2309.10668.pdf). Reception on Twitter is controversial.
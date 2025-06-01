---
layout: post
title: "Document-to-Markdown Converters for LLM Use"
author: "Nils Durner"
categories: [journal]
tags: [docling, markitdown, pdf, document AI, pymupdf4llm, jina, llm]
date: 2024-12-14
last_updated: 2024-12-14
description: "Compares MarkItDown, Docling, PyMuPDF4LLM, and Jina AI Reader for converting documents to Markdown, highlighting installation, fidelity, OCR, API integration, and enterprise options."
---

Recently, a few open-source tools for converting PDFs, Office documents, and other formats into Markdown have drawn attention. Among these are [MarkItDown](https://github.com/microsoft/markitdown) from Microsoft, [Docling](https://github.com/DS4SD/docling) from IBM Research, [PyMuPDF4LLM](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/), and the [Jina AI Reader API](http://jina.ai/reader/). They aim to provide text suitable for downstream tasks, including LLM-driven analysis, without requiring manual formatting.

## MarkItDown: Minimal and Straightforward

[MarkItDown surfaced on HackerNews](https://news.ycombinator.com/item?id=42410803) within the last 24 hours, where one user called it “pretty decent” for HTML and PDF input. However, its implementation relies on external tools (e.g. [spawning](https://github.com/microsoft/markitdown/blob/main/src/markitdown/_markitdown.py#L626) unrestricted native-code `exiftool` or `ffmpeg` processes from the Python code base), which raises security concerns if you’re handling arbitrary, unchecked files. It also uses simplistic assumptions for tables (e.g. treating the [first row as header](https://github.com/microsoft/markitdown/blob/main/src/markitdown/_markitdown.py#L574)), without regard to relational structure. The trade-off is clear: MarkItDown is easy to run but provides only a basic text extraction, with limited attention to layout or complex document features.

MarkItDown can be tried here: [matt palmer's msftmd](https://msftmd.replit.app).

## Docling: Detailed Parsing and Emerging Commercialization

Docling, [highlighted by IBM’s VP of Product for AI Platform Armand Ruiz on LinkedIn](https://www.linkedin.com/posts/armand-ruiz_this-project-got-more-than-11000-stars-on-activity-7273668186598785024-f0ji?utm_source=share&utm_medium=member_desktop), aims to preserve layout, reading order, and tables, even offering OCR for scanned (or otherwise inaccessible) PDFs. In my tests, it converted a ~100-page PDF into Markdown while maintaining much of the document’s structural integrity. On the downside, I encountered repetitive extraction of identical header images. This suggests room for improvement, but [since Docling values community contributions](https://www.linkedin.com/feed/update/urn:li:activity:7273668186598785024?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7273668186598785024%2C7273675877664669696%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287273675877664669696%2Curn%3Ali%3Aactivity%3A7273668186598785024%29), this may be fixed soon.

Armand mentioned on LinkedIn that commercial versions of Docling are “becoming available on IBM software”, which could refer to IBM watsonx.ai Text Extract in particular. For organizations that need advanced parsing and prefer solutions backed by a large vendor, such more polished, enterprise-focused distributions could be relevant. Meanwhile, the open-source version already supports a wide range of file formats at no additional cost.

## PyMuPDF4LLM: Robust PDF Handling and Optional Office Support

Before Docling’s release, I relied on PyMuPDF4LLM for text extraction. PyMuPDF4LLM produces structured Markdown from PDFs and can be extended with a commercial PyMuPDF Pro license to handle Office documents as well. While I have not pushed it to the limit with complex layouts in a broad test, my experience has been that it offers robust, rather reliable PDF to Markdown conversion for downstream LLM use.

## Jina AI Reader: API-Based Extraction with Some Gaps

Jina AI’s Reader API allows supplying URLs or documents and receiving Markdown-friendly output. In principle, this can streamline integration — just call the API and get results. When I tested it, however, I noticed some content omissions, such as missing code snippets, and unexpected escaping of certain characters. This suggests that while the convenience of an API-driven approach is appealing, it’s worth verifying the completeness and accuracy of the extracted text.

Jina, being Berlin-based, might resonate with organizations influenced by local buying preference as [indicated by a recent survey](germany-surveys).

## Concluding the Differences

- **MarkItDown:** Simple setup and minimal overhead, but limited structural fidelity and reliance on external utilities.
- **Docling:** More faithful representation of complex documents, OCR support, and free multi-format handling. Some rough edges remain, but improvements can come from its open-source community, dedicated staff, or the emerging commercial variants IBM mentioned.
- **PyMuPDF4LLM:** Strong base for PDF extraction, and can handle Office documents with PyMuPDF Pro. A solid option if you’re comfortable with PyMuPDF already and are open to licensing for extended features.
- **Jina AI Reader:** Convenient API approach, but my tests showed occasional missing elements. Suitable if you prefer a service-based solution and, for some users, the local (German) presence might be a plus.

Each tool targets a similar problem - turning various document types into Markdown - but their approaches differ in complexity, accuracy, cost, and support structure. Depending on your priorities, one of these tools may better fit your needs.
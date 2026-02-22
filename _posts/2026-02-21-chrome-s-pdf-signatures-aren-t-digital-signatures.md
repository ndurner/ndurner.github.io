---
title: "Chrome’s “PDF Signatures” Aren’t Digital Signatures"
date: 2026-02-21
last_updated: 2026-02-21T13:43:22+00:00
author: "Nils Durner"
redirect_to:
  - https://ndurner.substack.com/p/chromes-pdf-signatures-arent-digital
tags: [Substack]
excerpt: "Heise reports that Chrome added “digital signatures” and annotations. Google’s own release wording (“annotate, highlight and draw a signature on a PDF”) conveys the same, but is only accurate for UX, not for standards semantics: this is proprietary scribbling, not digital signing. Worse, it breaks real digital signatures that are already in a document. To someone familiar with PDF internals, Googl"
substack_url: "https://ndurner.substack.com/p/chromes-pdf-signatures-arent-digital"
canonical_url: "https://ndurner.substack.com/p/chromes-pdf-signatures-arent-digital"
sitemap: false
---

Heise [reports](https://www.heise.de/en/news/Google-Chrome-gets-three-useful-productivity-features-11184117.html) that Chrome added “digital signatures” and annotations. Google’s own release wording (“annotate, highlight and draw a signature on a PDF”) conveys the same, but is only accurate for UX, not for standards semantics: this is proprietary scribbling, not digital signing. Worse, it breaks real digital signatures that are already in a document.

To someone familiar with PDF internals, Google‘s alleged „productivity feature“ is a disappointment: different than stated, it does **not** use Ink Annotation objects (/Subtype /Ink, /InkList), and it does **not** create PDF signature objects (/Sig, /ByteRange). The latter means no cryptographic signer binding, no tamper-evident document integrity, no non-repudiation, and no PAdES-/eIDAS-style trust semantics („Electronic Signatures“). As the PDF Association [puts it](https://pdfa.org/huggingface-echoes-safedocs/#chrome-does-not-sign-or-annotate-your-pdf):

> [Instead,] Chrome “bakes” the drawn content into each PDF page’s content stream, using a marked-content sequence with the custom tag “`GOOG:INKIsInker`” ([as defined here](https:...

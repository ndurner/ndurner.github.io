---
layout: post
title: "2024 Quantum Computing Review"
author: "Nils Durner"
categories: [journal]
tags: [pqc, quantum computing]
date: 2024-12-26
last_updated: 2024-12-26
description: "Reviews 2024 quantum computing gaps: no real-world Shor’s algorithm decryption, pending post-quantum algorithm integration in EU standards, and limited real-world advantage beyond niche simulations."
---

With end-of-year roundups and predictions being in season, it's also worthwhile to consider what hasn't, despite ceaseless cheerling, been achieved or announced:

1. Quantum advantage in breaking real-world encryption. While classical computing has cracked very weak RSA (trivially small key size of perhaps 1/10^535 the strength of today's digital signatures), quantum computers still can't maintain coherence long enough to run Shor's algorithm - the still theoretical quantum threat to current encryption.

2. Finalized standards for quantum-resistant signatures. US-NIST has proposed post-quantum algorithms like ML-DSA, but it's up to the EU's ENISA to integrate these into our signature standards (e.g., PAdES). Concerns over e.g. ML-DSA's complex security assumptions and non-deterministic signing process warrant careful consideration. Fortunately, there's no need to rush, as original timelines for quantum threats remain valid.

3. Real-world quantum advantage beyond foundational simulations. Recent experiments focus on specific physics problems, serving mainly as proof-of-concept. A wide gap remains between these simulations and the claimed transformative impacts on medicine, finance, and energy.
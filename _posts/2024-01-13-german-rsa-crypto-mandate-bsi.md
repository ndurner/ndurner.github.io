---
layout: post
title: "RSA-3000 cryptography recommendation in Germany"
date: 2024-01-13
last_updated: 2024-01-13
description: "Summarizes Germany's BSI mandate on implementing RSA cryptography standards, compliance deadlines, and technical requirements for federal IT systems."
tags: [Cryptography, encryption, signature, RSA]
---

The perceived RSA-3000 crypto mandate by the German Federal Office for Information Security (BSI) has been reported by Heise Medien GmbH & Co. KG, highlighting that: \
💡 a BSI speaker confirmed that this is a recommendation, not a mandate \
💡 the TLS certificate of the BSI website still uses RSA-2048 as well \
💡 the wording, especially across BSI publications, is confusing and could be misleading

[This reporting](https://www.heise.de/news/BSI-Verwirrung-um-Anforderungen-an-Schluessellaengen-fuer-TLS-Verbindungen-9596072.html) is in the context of TLS (publications TR-02102-2, TR-03116-4), but the same issues are present with the general "Technische Richtlinien" document on cryptographic algorithms and key lengths (TR-02102 part 1), which is cited by sources like keylength.org, often without the nuance from the preamble, such as:
👩🏻‍⚖️ the recommendations do not preempt regulatory approval processes
🧑🏻‍💻 they target developers planning new systems
💫 they may exceed the stated goal of achieving 120 bits of security

The Heise article concludes that "A signature algorithm for TLS needs to be secure for only as long as the certificate is valid, which is typically one year." It also notes that the US National Institute of Standards and Technology (NIST) "considers RSA with a key length of 2048 bits to be sufficiently secure for signatures until the year 2030".

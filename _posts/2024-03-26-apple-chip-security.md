---
layout: post
title: "Apple Chip Flaw"
date: 2024-03-26
last_updated: 2024-03-26
description: "Analyzes Apple’s M-series security architecture, detailing Secure Enclave, hardware encryption, and implications for secure AI on-device workloads."
tags: [apple, security, cryptography]
---

The tech press is busy reporting on an alleged "[Apple Chip Flaw Leaks Secret Encryption Keys](https://www.wired.com/story/apple-m-chip-flaw-leak-encryption-keys/)".

This is not a real concern. Rather, it's junk science.
 
The researchers used a third-party cryptography tool/library, called "OpenSSL". Apple's own cryptography library is called "CryptoKit", and this is commonly used by Apps and macOS/iOS/iPadOS itself. The difference is that CryptoKit uses the so-called "Secure Enclave" (also sometimes described as "Trusted Execution Environment") instead of the regular Apple Silicon CPU (as OpenSSL does by default). Of course, the TEE is designed to whitstand the type of "side-channel attacks" the researchers have exploited.
 
There can be situations where you might want to run OpenSSL on fruit , but if you intend to do risky encryption or signing, you would use an OpenSSL backend that is either based on CryptoKit or any other Secure Element or HSM. Anything else is either very bad practice or a laboratory setup divorced from the real world.
 
At any rate, it's not an "Apple Chip Flaw", and it helps to consider that Apple engineers, especially those working on their security features, are world-class. The researcher's mistake, on the other hand, is beginner-level.
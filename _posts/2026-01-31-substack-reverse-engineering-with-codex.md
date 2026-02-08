---
title: "Reverse Engineering with Codex"
date: 2026-01-31
last_updated: 2026-01-31T16:28:56+00:00
author: "Nils Durner"
redirect_to:
  - https://ndurner.substack.com/p/reverse-engineering-with-codex
tags: [Substack]
excerpt: "Sparks of AGI, revisited Back in 2023, Sparks of AGI implemented reverse engineering through reverse prompting: GPT-4 instructed the user to run Unix tools like file , strings , a debugger, and a disassembler, and then reasoned from the outputs. The paper’s reverse engineering example is essentially a supervised, tool-mediated process where the model explains each step and the human executes it: t"
substack_url: "https://ndurner.substack.com/p/reverse-engineering-with-codex"
canonical_url: "https://ndurner.substack.com/p/reverse-engineering-with-codex"
sitemap: false
---

## Sparks of AGI, revisited

Back in 2023, *[Sparks of AGI](https://arxiv.org/abs/2303.12712)* implemented reverse engineering through reverse prompting: GPT-4 instructed the user to run Unix tools like *file*, *strings*, a debugger, and a disassembler, and then reasoned from the outputs. The paper’s reverse engineering example is essentially a supervised, tool-mediated process where the model explains each step and the human executes it: the model moves from file format and strings to assembly, then uses a debugger to inspect execution and derive the password logic. The workflow is explicit and careful, and the human remains the hands.

In my own GPT-4 experiments at that time, I compiled and then de-compiled small C snippets with “*gcc -S*” and found it could recover plausible function names from assembly, implying semantic understanding. One frustrating hold-back at the time was the missing search engine integration, which meant added manual labor caused by hallucination errors in tool invocations.

For a recent interoperability project, I revisited the idea of using a coding agent as an **agentic execution environment**, moving from GPT-4 era reverse prompting toward autonomous...

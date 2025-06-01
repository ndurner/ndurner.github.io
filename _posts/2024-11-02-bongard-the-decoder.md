---
layout: post
title: "Visual Bongard Puzzles & VLMs: Technical Review"
author: "Nils Durner"
categories: [journal]
tags: [vlm, mllm, llm, ai research, benchmarks, the decoder]
date: 2024-11-02
last_updated: 2024-11-02
description: "Critiques 'Bongard in Wonderland' VLM paper: outdated model versions, system prompt errors, poor statistical design, and reproduction showing major performance gains in updated Claude releases."
---

A recent paper titled "Bongard in Wonderland: Visual Puzzles that Still Make AI Go Mad?" has garnered some attention through German tech media. The study claims to demonstrate fundamental limitations in visual language models' (VLMs) reasoning capabilities. However, upon closer examination of their methodology and code implementation, several issues emerge that question the validity of these sweeping conclusions.

## Model Selection and Versioning

While the paper doesn't explicitly specify which model revisions were used, references suggest data collection around September 2024. This timing means the study missed significant improvements in model capabilities, particularly with Claude 3.5 Sonnet's latest release featuring enhanced pixel-counting abilities - a capability directly relevant to visual reasoning tasks. This outdated model choice is confirmed by the source code the principal study author has published on Github.

## Implementation Issues

Reviewing the published code revealed several concerning issues:

1. The system prompt confusion is particularly noteworthy. The code used a descriptive prompt intended for image analysis (`bongard/system_prompt.txt`) instead of the evaluative prompt (`llm_judge/system_prompt.txt`) meant for result assessment. This fundamentally changes what the LLM judge was instructed to do.

2. The experimental design shows questionable statistical rigor. For instance, the researchers used consecutive seeds (1,2,3) rather than well-distributed ones for reproducibility, while mixing different sampling approaches (temperature-based for some models, seed-based for others) without justification.

3. The evaluation methodology relies purely on textual descriptions judged by an LLM, rather than direct assessment of visual understanding. Furthermore, the ground truth used for evaluation wasn't included in the repository, raising reproducibility concerns.

My reproduction attempts with Claude demonstrate both the impact of these issues and the rapid progress in the field:

```
GENEROUS evaluation (v1):
Correctly solved: 6 out of 100 BPs
Success rate: 6.0%

GENEROUS evaluation (v2):
Correctly solved: 43 out of 100 BPs
Success rate: 43.0%
```

This dramatic improvement between versions challenges the paper's conclusions about fundamental limitations.

## Abstract vs. Real-World Reasoning

The study's focus on abstract Bongard problems seems misaligned with current AI applications. While VLMs might struggle with artificial black-and-white shapes, Claude's new ability to count pixels accurately for computer interface interaction demonstrates practical visual reasoning capabilities that are directly relevant.

## Media Representation

The coverage of this workshop paper exemplifies a pattern in AI reporting where limitations get amplified while context gets lost. German tech outlet The Decoder, for instance, presented the findings without crucial caveats about methodology or model versions. This creates a potentially misleading narrative about AI capabilities.

## Conclusion

While the study raises interesting questions about visual reasoning in AI systems, its methodological issues and rapidly outdated model selection limit its conclusions. The significant improvement in model performance over just a few months suggests claims regarding fundamental limitations are ill-advised.
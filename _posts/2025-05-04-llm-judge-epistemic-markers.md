---
layout: post
title: "EMBER: Epistemic Markers as a Stress‑Test for LLM‑based Evaluation"
date: 2025-05-04
last_updated: 2025-05-04
tags: [evaluation, llm, ai research, evals]
---

In my note on [LLM as a judge](https://ndurner.github.io/llm-as-judge), I pointed out a study where **GPT‑4 (0613)** aligned well with human ratings.  
A new paper – “[Are LLM‑Judges Robust to Expressions of Uncertainty?](https://arxiv.org/pdf/2410.20774)” – asks what happens once those answers include explicit markers of certainty or doubt. The authors provide "EMBER", a benchmark that patches existing QA and instruction‑following outputs with:

* *Strengtheners* (e.g. “I’m absolutely certain …”),  
* *Weakeners* (e.g. “I’m not sure, but …”), or  
* no marker (neutral baseline).

The semantic content stays unchanged, so any shift in verdict must be due to phrasing.

## Benchmark structure

| Split | Task | Instances | Models whose outputs were patched |
|-------|------|-----------|-----------------------------------|
| **EMBER‑QA** | single‑answer correctness (Natural Questions, TriviaQA) | 2 000 | GPT‑4, NewBing |
| **EMBER‑IF** | pairwise instruction following (MIXINSTRUCT) | 823 | GPT‑4o‑generated variants |

For evaluation the authors used five commonly deployed judge models:

* GPT‑3.5‑turbo  
* GPT‑4‑turbo  
* GPT‑4o  
* Llama‑3‑8B‑Instruct  
* Llama‑3‑70B‑Instruct  

## Key findings

### Question answering (EMBER‑QA)

| Judge model | Accuracy drop on **correct** answers (strengthener → weakeners) | Verdict switch rate (weakeners) |
|-------------|---------------------------------------------------------------|---------------------------------|
| Llama‑3‑8B | ‑4.9 pp → **‑47.2 pp** | **47 %** |
| Llama‑3‑70B | ‑0.4 pp → ‑3.0 pp | 4 % |
| GPT‑3.5‑turbo | ‑4.7 pp → ‑5.2 pp | 9 % |
| GPT‑4‑turbo | ±0 pp → +2.0 pp | 3 % |
| GPT‑4o | ‑1.5 pp → **‑19.0 pp** | 20 % |

*Numbers taken from Table 2 of the paper. Verdict switch rate (VSR) is the share of samples whose verdict flips relative to the neutral baseline.*

Observations:

* All judges show a bias pattern: neutral > strengthener > weakener.  
* Larger models are less sensitive, yet even GPT‑4o changes its mind on one in five QA cases when a weakener is added.

### Instruction following (EMBER‑IF)

The pairwise setting amplifies the effect. When a correct answer carries a weakener and an incorrect answer is neutral, verdicts flipped in **30 %–35 %** of cases for Llama‑3‑8B and still **~5 %** for GPT‑4o (Table 3). The direction is systematic: judges penalise uncertainty expressions regardless of factual correctness.

### Human baseline

Crowd workers, presented with the same material, ignored the markers and evaluated solely on substance. This undermines the assumption that LLM‑only evaluation is an inexpensive but equivalent proxy for human judgement once epistemic wording is encouraged.

## Relation to earlier notes

In *LLM as a judge* I cautiously endorsed GPT‑4 as a stand‑in for human raters under **neutral phrasing**.  
In *[Visual Bongard Puzzles & VLMs](https://ndurner.github.io/bongard-the-decoder)* I argued that prompt details can dominate results. EMBER confirms both points: evaluation reliability drops as soon as uncertainty wording – arguably desirable for honest models (Askell et al., 2021) – enters the mix.

## Outlook

* **GPT‑4 retirement.** OpenAI’s April 10 2025 changelog states that GPT‑4 will be withdrawn from ChatGPT by 30 Apr 2025 and that legacy GPT‑4 (0613) endpoints will retire in the Azure OpenAI Service on 6 Jun 2025. With its deprecation, the judge model that previously served as a de‑facto reference is disappearing.  
* **No clear successor.** GPT‑4o performs best on EMBER but still shows significant bias (≈ 5–20 % VSR, depending on task). At the time of writing there is **no model whose verdicts are both robust and reproducible enough to be a gold standard**.  
* **Data availability.** Code and data are [hosted on GitHub](https://github.com/DongryeolLee96/EMBER) with the dataset [mirrored on Hugging Face](https://huggingface.co/datasets/Dongryeol/EMBER). However, the release only comprises of 1000 dataset entries in EMBER-QA, while the paper states that there should be 2000 "instances" ([HuggingFace Discussion](https://huggingface.co/datasets/Dongryeol/EMBER/discussions/1#68174d0747c573f3c66eb691)).
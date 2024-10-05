---
layout: post
title: "Synthetic Data in AI: Hype, Concerns, and Reality"
date: 2024-07-28
last_updated: 2024-07-28
tags: [ai, llm, synthetic-data, model-collapse]
---

A recent paper in Nature, "AI models collapse when trained on recursively generated data" by Shumailov et al., has sparked a heated debate in the AI community about the potential risks of using synthetic data for training language models. The paper suggests that indiscriminate use of model-generated content in training can cause irreversible defects in the resulting models, a phenomenon they term "model collapse."

This study has gained significant traction, with some, like Alexandr Wang, CEO of Scale AI, [viewing it as a cautionary tale](https://x.com/alexandr_wang/status/1816491442069782925) against overreliance on synthetic data. Wang argues that "Synthetic data can create a short-term boost in eval results, but you will pay for it later with model collapse!"

However, the reality might be more nuanced. Rylan Schaeffer, [in response to the controversy](https://x.com/RylanSchaeffer/status/1816535790534701304), points interested readers to their [COLM 2024 paper](https://t.co/uCSQPhLGMA) and says that model collapse appears primarily when researchers intentionally induce it in ways that don't match actual practices.

Interestingly, major AI labs seem to be finding ways to make synthetic data work effectively. For instance, Meta's recent technical report on Llama 3.1 indicates that synthetic data can improve, not hurt, performance when used correctly.

This aligns with my own experiences. In October 2023, [I experimented with training GPT-3.5 using synthetic data](https://ndurner.github.io/training-own-model-finetuning), finding that adding new knowledge through this method was indeed viable. The process, while not perfect, showed promise in expanding the model's knowledge base.

More recently, we've seen significant developments in this area:

1. Nvidia introduced Nemotron-4-340B-Instruct, a large language model explicitly designed for synthetic data generation to train other LLMs. Their approach relies heavily on synthetic data, with over 98% of their alignment data being synthetically generated.

2. Amazon has showcased the use of Llama 3.1 405B for synthetic data generation and distillation to fine-tune smaller models. They demonstrate how this can improve the performance of models like Llama 3 8B.

These developments suggest that the use of synthetic data, far from being a path to model collapse, is becoming a key strategy in advancing AI capabilities. The key seems to lie in how this data is generated and used.

For those interested in diving deeper into this topic, I recommend checking out the following resources:

- The original Nature paper: [AI models collapse when trained on recursively generated data](https://www.nature.com/articles/s41586-024-07566-y)
- Nvidia's Nemotron-4-340B-Instruct: [Model Card](https://build.nvidia.com/nvidia/nemotron-4-340b-instruct/modelcard)
- Amazon's blog post on using Llama 3.1 405B: [Use Llama 3.1 405B for synthetic data generation](https://aws.amazon.com/blogs/machine-learning/use-llama-3-1-405b-to-generate-synthetic-data-for-fine-tuning-tasks/)
- My earlier experiment with GPT-3.5 and synthetic data: [Training an Own OpenAI Model (Fine-Tuning 2.0)](https://ndurner.github.io/training-own-model-finetuning)

[Update 2024-08-26]
Aleph Alpha, a German AI company that emphasizes on "Compliant, Transparent, Capable", released their new model family Pharia-1, noting in the model card that synthetic data was used in training. On the fact that, in comparison to the "control" model, the "aligned" model got weaker in instruction-following:
> We believe this is due to the increased use of synthetic data in the datasets and the tendency of LLM-based evaluation methods to favor verbosity.

Reference: [Pharia-1-LLM](https://aleph-alpha.com/de/introducing-pharia-1-llm-transparent-and-compliant/)
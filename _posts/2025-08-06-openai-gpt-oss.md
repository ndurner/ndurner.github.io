---
layout: post
title: "OpenAI GPT-OSS open weights model released"
date: 2025-08-06
tags: [llm, openai, gpt-oss, ollama]
last_updated: 2025-08-06
author: "Nils Durner"
categories: [journal]
---

## Intro
OpenAI has released the open-weights model that was announced end of March. It is a reasoning model that comes in two sizes: 20B and 120B, in a Mixture-of-Experts configuration. [Model Card](https://openai.com/index/gpt-oss-model-card/). Commenters call it "similar to o3" in performance, but that's seems untrue - it's about o3-mini grade, but lags behind o4-mini.

## Providers
* for quick testing, there's [gpt-oss.com](http://gpt-oss.com). This does not allow one to specify a System/Developer prompt, though
* Third party "Inference Providers"
    * beware: accuracy can be inconsistent! Romain Huet, Head of Developer Experience 
at OpenAI: "Heads-up for developers trying gpt-oss: performance and correctness [can vary a bit across providers and runtimes](https://x.com/romainhuet/status/1952916530792153093) right now due to implementation differences. We’re working with inference providers to make sure gpt-oss performs at its best everywhere, and we’d love your feedback!". [He adds](https://x.com/DKundel/status/1952917845760950475): "We've verified the vLLM implementation so there should be no issues with that. If you run into issues let us know."
    * [OpenRouter](https://openrouter.ai) has support
    * [Awesome GPT-OSS](https://github.com/openai/gpt-oss/blob/main/awesome-gpt-oss.md) lists Cloudflare and Groq
    * Support on Azure AI Foundry and AWS Bedrock announcements make it appear it would be available as of now, but neither actually does.
* Local: the [Github repo](https://github.com/openai/gpt-oss/) lists several options - including vLLM, HuggingFace Transformers and Ollama.
    * Transformers doesn't seem viable on Apple Silicon as of now, though (see below)

### Gotchas on macOS
For reference, running the Transformers `serve` command as given in the [Inference examples](https://github.com/openai/gpt-oss/tree/main?tab=readme-ov-file#inference-examples) straight fails on macOS:
```
% transformers serve

ImportError: Missing dependencies for the serving CLI. Please install with `pip install transformers[serving]`
```
... which in turn fails with:
```
% pip install transformers[serving]

zsh: no matches found: transformers[serving]
```
The trick here is to quote the package name:
```
% pip install "transformers[serving]"
```

Ultimately though, the MPS backend for Apple Silicon doesn't seem to be supported: `transformers serve` will start up fine and `transformers chat` will make a connection, but the server will fail at runtime in the background:
```
  File "/Users/ndurner/gpt-oss/.venv/lib/python3.13/site-packages/transformers/quantizers/quantizer_mxfp4.py", line 60, in validate_environment
    raise RuntimeError("Using MXFP4 quantized models requires a GPU")
RuntimeError: Using MXFP4 quantized models requires a GPU
```

As the [OpenAI Cookbook on gpt-oss with Ollama](https://cookbook.openai.com/articles/gpt-oss/run-locally-ollama) explicitely notes:
> *Perfect for* higher-end consumer GPUs or *Apple Silicon Macs*
... this seems to be the way.

## Insights
The open-sourced stack released along with the models gives some additional insights. I have noticed before that the o1 model likes to be addressed as "ChatGPT" in prompts, not "o1". This is confirmed by the "You are ChatGPT" identity prompt published as part of the Harmony Prompt template harness ([Cookbook](https://cookbook.openai.com/articles/openai-harmony), [Github repo](https://github.com/openai/harmony)).
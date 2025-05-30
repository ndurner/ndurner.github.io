---
layout: post
title: "Anthropic Claude 4, o3 improvements"
author: "Nils Durner"
categories: [journal]
tags: ["anthropic", "claude", "o1", "amazon bedrock", "openai"]
date: 2025-05-27
last_updated: 2025-05-27
description: "Covers Claude 4 Opus/Sonnet vs o3/o4-mini benchmarks, new extended reasoning with tool-use, AWS Bedrock model and API quirks, and o3/o4-mini Code Interpreter plus encrypted reasoning."
---

Anthropic released Claude 4 Opus and Sonnet last week. Per the benchmark results they have [published](https://www.anthropic.com/news/claude-4), Claude 4 Opus is roughly comparable to OpenAI o3. However, the updated [Aider LLM Leaderboard](https://aider.chat/docs/leaderboards/) places Claude 4 Opus on par with o4-mini, at a substantially higher cost. While Anthropic claims that "Claude Sonnet 4 is a significant upgrade to Claude Sonnet 3.7", the Aider Leaderboard actually places Sonnet 4 behind Sonnet 3.7.

One eye-catching novelty is Claude 4's reasoning capabilites that allow tool-use while Reasoning ("Extended thinking with tool use"). Reasoning can be switched on an off ("hybrid models" vs "extended thinking").

## Amazon Bedrock
Claude 4 is available on Amazon Bedrock, model names: "anthropic.claude-opus-4-20250514-v1:0" and "anthropic.claude-sonnet-4-20250514-v1:0". Gotchas I have identified so far:
* using the model names straight results in the error message "An error occurred (ValidationException) when calling the ConverseStream operation: Invocation of model ID anthropic.claude-sonnet-4-20250514-v1:0 with on-demand throughput isn’t supported. Retry your request with the ID or ARN of an inference profile that contains this model.". Prepending the region, e.g. "us.", to the model name fixes this.
* Reasoning does not seem to be available through the Converse API. Adding the "thinking" parameter to the inferenceConfig results in: "Error: Parameter validation failed:\nUnknown parameter in inferenceConfig: "thinking", must be one of: maxTokens, temperature, topP, stopSequences". Code samples seem only available for the InvokeModel API.
* the playground on the AWS console caps the maximum output length at 32K, while the limit on the thinking token budget is 63999. Trying to run the model with this full reasoning budget thus yields this error: "The model returned the following errors: `max_tokens` must be greater than `thinking.budget_tokens`."

## o3/o4-mini Improvements
Improvements of o3 and o4-mini and their API may appear to be more incremental, but are powerful nontheless:
* Code Interpreter (including "deep image understanding" aka "thinking with images") and File Search now available for use [during the Reasoning process](https://x.com/OpenAIDevs/status/1925214117214011510).
* Reasoning traces can now be retained without storing them at OpenAI through a new stateless usage option: ["Encrypted reasoning items"](https://platform.openai.com/docs/guides/reasoning#encrypted-reasoning-items).
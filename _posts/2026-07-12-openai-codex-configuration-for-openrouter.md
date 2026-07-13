---
title: "OpenAI Codex configuration for OpenRouter"
date: 2026-07-12
last_updated: 2026-07-12T11:07:18+00:00
author: "Nils Durner"
redirect_to:
  - https://ndurner.substack.com/p/openai-codex-configuration-for-openrouter
tags: [Substack]
excerpt: "OpenAI’s coding & work tool Codex is not tied to OpenAI as a first-party model provider. In particular, it allows OpenRouter to be used - a hub to currently 480 models offered by independent inference providers. These inference providers offer models not found in the OpenAI like OpenAI’s own open-weights models gpt-oss-20b or gpt-oss-120b, or third party models including Gemini, Claude, Grok or GL"
substack_url: "https://ndurner.substack.com/p/openai-codex-configuration-for-openrouter"
canonical_url: "https://ndurner.substack.com/p/openai-codex-configuration-for-openrouter"
sitemap: false
---

OpenAI’s coding & work tool Codex is not tied to OpenAI as a first-party model provider. In particular, it allows OpenRouter to be used - a hub to currently 480 models offered by independent inference providers. These inference providers offer models not found in the OpenAI like OpenAI’s own open-weights models gpt-oss-20b or gpt-oss-120b, or third party models including Gemini, Claude, Grok or GLM. (There is a bug that prevents these third party models from actually being used, see below).

Codex configuration is in ~/.codex/config.toml on Mac. The first thing to change is the OpenAI centric model specifier from:

to perhaps:

and tell Codex to the OpenRouter provider:

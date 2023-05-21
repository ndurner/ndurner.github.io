---
layout: post
title: "AI Security Concerns"
author: "Nils Durner"
categories: [journal]
tags: [openai, gpt, security]
date: 2023-04-21
---

Following up on the publication of ["AI security concerns in a nutshell - Practical AI-Security guide"](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/KI/Practical_Al-Security_Guide_2023.html) by the German BSI (Federal Office of Information Security), I highlighted that another, more specific security concern to generative AI is prompt injection, a throwback to the SQL injection attacks of the… 2000s? 2010s? Anyway, OpenAI's proposed mitigation is the „System Prompt“ that API users can use. This is a light-hearted showcase of this, [shared today by @gdb on Twitter](https://twitter.com/gdb/status/1649441972732694528):
![System prompt to GPT: "use only emoji". User asks for executable Python code, GPT signals that it cannot comply - using Emoji](https://pbs.twimg.com/media/FuK-ubQaEAEM0yG?format=jpg&name=small)
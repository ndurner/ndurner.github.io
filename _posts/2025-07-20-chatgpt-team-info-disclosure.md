---
layout: post
title: "ChatGPT Team adds users' name & organization to prompts"
date: 2025-07-20
tags: [llm, ChatGPT, OpenAI, ai-literacy]
last_updated: 2025-07-20T12:09:17+02:00
author: "Nils Durner"
categories: [journal]
---

Even with "Memory" and style preferences turned off in the ChatGPT personalization settings, the paid "Team" subscription tier causes personal data to be disclosed to the underlaying Language Model. This includes:
* Full name used for registration
* Corporate E-Mail address
* "Handle": corporate user name
* Organization name

![GPT 4.1 langauge model returns user's data in ChatGPT](assets/img/chatgpt-team-whoami.png)

(a November 2024 report by Prof. Florian Gallwitz showed that [the LLM was also passed the IP address](https://x.com/FlorianGallwitz/status/1853358400576356684))

This background information can induce certain biases, scew or even ellicit confabulation/hallucination as shown here: when inquiring about an old patent filing of mine, ChatGPT claimed that the technology from the patent, developed at my former employer, was used in the tech stack of my new employer (something I don't know but highly doubt). I suppose the connection to my new employer was made based on the Organization Name as disclosed via the model context.
![OpenAI o3 in ChatGPT mixes up information from a patent filing and the context it got disclosed](assets/img/chatgpt-team-confabulation.png)

The free version of ChatGPT does not seem to have this problem:
```
Prompt: Who am I and what entity is my account associated with?

Response: I can’t see your identity or the entity associated with your account. For privacy and security, I don’t have access to personal account information unless you choose to share it with me. [...]
```

I wonder what it is like elsewhere - ChatGPT Enterprise, Claude, ...
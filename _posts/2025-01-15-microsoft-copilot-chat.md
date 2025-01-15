---
layout: post
title: "Microsoft Copilot Chat"
author: "Nils Durner"
categories: [journal]
tags: [ai, llm, microsoft, gpt4]
date: 2024-01-15
last_updated: 2024-01-15
---

Microsoft has launched Copilot Chat, an offering similar to ChatGPT:
* Blog post: https://aka.ms/CopilotChat
    * LinkedIn: [Microsoft](https://www.linkedin.com/posts/microsoft_copilot-for-all-introducing-microsoft-365-activity-7285333478001324033-JL_E?utm_source=share&utm_medium=member_desktop), [CMO](https://www.linkedin.com/posts/jaredspa_ai-copilot-activity-7285362157456707584-Pktc?utm_source=share&utm_medium=member_desktop)
* Web version: https://copilot.cloud.microsoft/
* WhatsApp, Telegram: [Copilot for Social Apps](https://support.microsoft.com/en-us/topic/copilot-for-social-apps-43eb625d-eb25-4c72-a458-19842bf42212#:~:text=You%20can%20communicate%20with%20Copilot%20on%20WhatsApp%20in,Copilot%20by%20entering%20the%20phone%20number%20%2B1%20877-224-1042.)

It seems generally free to use. There are some advanced features¹ on a pay-per-use basis, and a $30 subscription model with even more advanced integrations.

(¹ "Agents"; which are based on OpenAI Assistants?)

Notes:

* The blog post mentions "web grounding", but that doesn't seem to be actually available (in the EU)?
* When used via corporate SSO login, Enterprise Data Protection is enabled
* As I wrote elsewhere: "Confusingly, manufacturers also offer AI assistants that lure with the same AI model names but create different conditions for the underlying language model through their orientation, fine-tuning, and product design. These AI assistants include products like Claude from Anthropic, ChatGPT from OpenAI, Gemini from Google, and Bing Copilot from Microsoft.". Copilot Chat falls in the same category. Example: when used for the SVG (kind-of a programming language, like HTML, but for vector graphics) of a pelican riding a bike, it won't oblige like the original GPT-4o model does, but displays a pixel image inline:

![Microsoft Copilot Chat screenshot: pelican on a bike](assets/img/microsoft-copilot-chat-pelican.png)

Despite this being dressed up for business, Gen. AI remains perilous and should be handled with care. Also, don't rely on it for last-minute work as the usage limits are unclear. Again, as I wrote elsewhere: "Within the respective usage plans of these AI assistants, one must also expect non-transparent usage restrictions that may unexpectedly deny users further use or suddenly downgrade them to a particularly low-performance language model within the same model family."
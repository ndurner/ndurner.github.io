---
layout: post
title: "Anthropic's Claude 2: Initial Impressions"
date: 2023-07-12
last_updated: 2023-07-12
tags: [Claude, Anthropic, GPT-4]
---

Anthropic have released Claude 2, touting "two times better at giving harmless answers". Initial reactions on the web seem favorable, particularly regarding the support of larger documents that ChatGPT. What I have seen so far with the regular end-user chat UI:

- A book of 1027 pages didn't load: "Text extraction failed". Loading a 62-pages legislative document, as well as a short contract in German did work ![Claude 2 #1](assets/img/claude-2-1.png)
- Answers from the chatbot are not fully grounded in the document by default, it adds prior and outside knowledge. When asked, it admits to this (screenshot #2: the data protection URL was not in the document) ![Claude 2 #2](assets/img/claude-2-2.png)
- When referring to a specific part within the document, it gives the page and section ![Claude 2 #3](assets/img/claude-2-3.png)
- It did not catch editor's notes in the 62 pages document, despite saying otherwise when asked to check if the document may be draft ![Claude 2 #4](assets/img/claude-2-4.png)

So certainly not bad, but still not the entirely harmless AI you're looking for.

[Ethan Mollick](https://www.linkedin.com/posts/emollick_there-was-a-big-new-ai-release-today-claude-activity-7084733526662623232-1XDb?utm_source=share&utm_medium=member_desktop):

> In my early testing, it is really good. Not quite GPT-4, but much closer than any other model [...] On the downside, don't use Claude for data, even though it accepts CSV files. It hallucinates answers, while Code Interpreter is right.

Officially not available outside the US and UK, but "more globally available in the coming months".
---
layout: post
title: "LLM Chat Conversion Tool"
date: 2025-05-10
tags: ["llm", "gpt", "chatgpt", "playground"]
last_updated: 2025-05-10
description: "Introduces Chatbot Conversation Converter CLI: convert chat logs between Playground JSON, Workbench, HTML, and Markdown; file upload/download support pending."
author: "Nils Durner"
categories: [journal]
---

With ChatGPT offering features not found in the API, like o1-pro previously or o3 with integrated web search, users may want to switch back and forth between ChatGPT, the Prompts Playground, and perhaps archive to Markdown. Enter [Chatbot Conversation Converter](https://github.com/ndurner/chatbot_conversation_converter):
> A Python utility that converts chat conversations between different formats, including OpenAI Playground JSON, [Nils' Workbench](genai-workbenches) format and Markdown.

Also, ChatGPT HTML is supported as an input format. This can obtained through the Safari or Chrome developer console and saved to an intermediate file, to be used like so:
```
% python ./chatbot_convert.py --format markdown chatgpt.html
```
This will create a "transcript" Markdown file, which can then be used with the Prompts Playground for follow-up conversation.

Areas in need of improvement:
* images and other file uploads likely don't work
* file downloads from ChatGPT Code Interpreter are not included
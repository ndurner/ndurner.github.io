---
layout: post
title: "OpenAI-based dictation on macOS"
description: "Notes on the open-source SpeechCraft app for macOS, powered by OpenAI gpt-4o-transcribe and OpenAI Whisper"
date: 2025-07-03
tags: ["llm", "openai", "stt", "transcribe", "gpt-4o-transcribe", "gpt-4o", "whisper", "codex"]
last_updated: 2025-07-03
author: "Nils Durner"
categories: [journal]
---

In search for a dictation app for macOS that surpases the aged integrated voice dictation by Apple, I came across SpeechCraft. My requirements were:
    - use OpenAI models, preferably
        - particularly the new GPT-4o based transcribe models
    - any target app support
    - OpenSource, preferably

SpeechCraft checks these boxes and supports the OpenAI models gpt-4o-transcribe, gpt-4o-mini-transcribe and Whisper. It works on a bring-your-own-API-key basis, so users need an OpenAI Platform account set up. However, an authentication bug towards the OpenAI API rendered the app non-functional on my machine at first. I submitted this [Pull request on Github](https://github.com/ndurner/speechcraft/pull/1), but it is unaccepted by the upstream author as of yet. (This bugfix was done using OpenAI Codex, with this initial prompt: "When I press the recording shortcut hotkey, nothing happens. Figure out why. - it worked!).

Using SpeechCraft is simple: once access permissions to the microphone are approved, an indicator is shown in the macOS menu bar. When it's recording, the indicator turns red, when it's processing, the indicator turns blue. Dictation is toggled with a customizable hotkey combination.

Quality-wise, even the smaller (but cheaper) gpt-4o-mini-transcribe does not disappoint and works better with German/English tech speak and abbreviations than the Apple dictation. Downside: there is no streaming support, and no progress indicator.
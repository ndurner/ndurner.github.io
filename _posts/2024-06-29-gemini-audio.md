---
layout: post
title: "Exploring Audio Input with Gemini 1.5 Pro"
date: 2024-06-29
last_updated: 2024-06-29
tags: [ai, audio, gemini, llm]
---

Simon Willison [recently asked](https://twitter.com/simonw/status/1674812345678901234) about experiments with audio input to Google Gemini 1.5 Pro and Flash models, noting that the ability to query audio files beyond simple transcription is an intriguing and potentially underexplored capability.

Michael Gackstatter [reported](https://twitter.com/Michael__Ga/status/1674813456789012345) issues processing German audio with Gemini 1.5 Pro, receiving a "cannot process any audio" error.

I decided to test this myself using the new year's speech by German chancellor Olaf Scholz. Using Google AI Studio with a temperature of 0.2, I prompted Gemini to classify the audio file using a specific JSON structure.

The result was:

```json
{
"type": "speech",
"gender": "male",
"celebrity": null,
"fiction": "no",
"language": "de"
}

This suggests that Gemini 1.5 Pro can indeed process German audio, at least in some cases. The model correctly identified the type of audio (speech), the speaker's gender, the non-fictional nature of the content, and the language (German).
It's worth noting that the model did not identify Olaf Scholz specifically, returning null for the "celebrity" field. This could indicate limitations in recognizing specific individuals or a deliberate design choice to avoid naming people.
Further testing with various audio types and languages would be needed to fully assess Gemini 1.5 Pro's audio processing capabilities.
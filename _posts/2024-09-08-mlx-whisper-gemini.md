---
layout: post
title: "Podcast transcription: MLX Whisper vs. Gemini"
author: "Nils Durner"
categories: [journal]
tags: [mlx, whisper, gemini]
date: 2024-09-08
---

(TLDR; I tried device-local Whisper and ended up using Google Gemini instead.)

Several pain points with Apple Podcasts in particular got me interested in using Frontier Models to create a more personalized experience:
* Rather low audio quality for some episodes: poor (if any) post-processing without noise cancelling, lack of gain normalization, bad microphones, ...
* Thick speaker accents
* Apple Podcast Transcripts inadequate
    * Spelling errors in (with mainly German podcasts): "ChatGPT" becomes "Chachipiti", "Fließtext" becomes "Fleece-Text"
    * Only limited copy & paste length, no good to paste into summarizer
* Only superficial interest in a topic, but interested nonetheless

Idea: use device-local transcription and perhaps summarization using the MLX toolkit - with the OpenAI Whisper model and Llama 3.1 in particular.

Because the podcast episode was slightly too long, I decided to compress it to the Whisper-native fidelity of 20kHz Mono. Because I didn't want to install homebrew and run ffmpeg natively, this is a wrapper script that will use a docker instance for transcoding: [Gist](https://gist.github.com/ndurner/636d37fd83aed4b875cdb66653017ae7). On the first try running the result through Whisper, it misrecognized the language, so I specified it explicitely:
```
% mlx_whisper --model "mlx-community/whisper-large-v3-mlx" --language German test.mp3
```

This resulted in just periods however:
```
[00:00.000 --> 00:02.000]  .
[00:30.000 --> 00:32.000]  .
[01:00.000 --> 01:02.000]  .
````

As it turns out: Whisper does not seem to handle background music, which the podcast episode used during the introduction. Further, this threw the model off without automatic recovery. How-tos on the web use Whisper in larger processing pipelines, e.g. to provide speaker diarization? Perhaps the use of Whisper is limited when used on its own?

To get the transcript done, I turned to the Google Gemini - which is said to support audio natively. After several prompting tries to get the format right (polished interview with introduction, rather than faithful transcript with all filler words, ahems, etc.), Gemini delivered - very well.
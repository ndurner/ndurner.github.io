---
layout: post
title: "Podcast transcription: MLX Whisper vs. Gemini"
author: "Nils Durner"
categories: [journal]
tags: [mlx, whisper, gemini]
date: 2024-09-08
last_updated: 2024-10-05
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

mlx_whisper, the port to Apple Silicon, has a runtime dependency on ffmpeg. Because I didn't want to install homebrew and run ffmpeg natively, this is a wrapper script that will use a docker instance for transcoding: [Gist](https://gist.github.com/ndurner/636d37fd83aed4b875cdb66653017ae7). On the first try running the result through Whisper, it misrecognized the language, so I specified it explicitely:
```
% mlx_whisper --model "mlx-community/whisper-large-v3-mlx" --language German test.mp3
```

This resulted in just periods however:
```
[00:00.000 --> 00:02.000]  .
[00:30.000 --> 00:32.000]  .
[01:00.000 --> 01:02.000]  .
````

As it turns out: Whisper does not seem to handle background music, which the podcast episode used during the introduction. Further, this threw the model off without automatic recovery. How-tos on the web use Whisper in larger processing pipelines, e.g. to provide speaker diarization. Perhaps the use of Whisper is limited when used on its own?

To get the transcript done, I turned to the Google Gemini - which is said to support audio natively. After several prompting tries to get the format right (polished interview with introduction, rather than faithful transcript with all filler words, ahems, etc.), Gemini delivered - very well.

[Update 2024-09-15] \
User krageon on HackerNews [elaborates](https://news.ycombinator.com/item?id=41489152) on their processing pipeline:
> I use a noise filter pass (really just [arnndn-models/bd.rnnn](https://github.com/richardpl/arnndn-models/blob/master/bd.rnnn). and some speech band filtering after) before doing any processing in whisper. It's worked well for me when using dirty audio (music in the background, environmental noise, etc). When there is music, you either almost can't hear it at all or you'll only hear particularly clear parts featuring singing.

[Update 2024-10-05] \
Updated the transcoding script slightly: it now copies all outputs to the target directory. This helps with segmented audio files to meet the 25 MB file limit when using Whisper via the OpenAI API. This invocation of the script produces reasonably small files for use with Whisper:
```bash
./ffmpeg -i file.mp4 -vn -c:a libopus -b:a 32k -vbr on -ac 1 -ar 16000 -f segment -segment_time 3600 output_%03d.ogg
```
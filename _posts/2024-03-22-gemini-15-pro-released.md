---
layout: post
title: "Gemini 1.5 Pro released"
date: 2024-03-22
last_updated: 2024-03-22
description: "Covers Google's Gemini 1.5 Pro launch: improved factuality tuning, larger context windows, benchmark comparisons, and early user access details."
tags: [google, gemini]
---

Google Gemini 1.5 Pro, including its great capacity of 1 million tokens, is currently available for free at https://aistudio.google.com/. It's officially not available in the EU, and its Terms of Service, among others things, mandate that:
> You may only access the Services (or make API Clients available to users) within an available region.
(In pratice, it's enough to route your traffic via EC2 in North Virginia, just as always)
 
Surprisingly, videos are handled really well: from their paper, I got the impression that the foundation model would only handle individual frames (meaning: just several "photos" extracted from the video) and that's pretty much it. Through this interface however, there's more to it: you can talk about the audio track, and it works for song identification!
 
Other notes, from my one-evening test drive:
* the kind of "amnesia" that occurs with long GPT sessions als happens here, but seems less pronounced
* multi-modality reveals training deficiencies easily, the perception seems rather "rough" or "blurry" at times, e.g. getting a full transcript fails. "Make a list of..." also fails/resolves in hallucination. Spatiality is challenging. (This is basically the same for GPT-4V and Claude 3)
* Hallucination with multimodality is common, depending on the subject. A diving video of mine yielded a "giant clam" and a "boxfish" under a dome when asked for "the animal", and only got it right when asked "which species of shark" (=> white-tip reef shark). Coincidence? Anyway, the same is basically also true for GPT-4V and Claude 3: all three fail at making a list of all seashell species in a beach photo I have tried.
* A chat session there is called "a prompt". Consequently, when you want to save a session, you need to save "a prompt". This is done to GDrive, but accessing "the prompt" requires access from a supported region. Workaround: click the "Preview" button (on the bottom; see screenshot), and select the text for copy & paste there.

Nota bene: API access is still not generally available, and I suppose that this 👆🏻 is also just a product preview.
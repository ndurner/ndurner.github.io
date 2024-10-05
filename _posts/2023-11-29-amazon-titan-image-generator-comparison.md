---
layout: post
title: "Amazon's Titan Image Generator: A Comparison with DALL-E"
date: 2023-11-29
last_updated: 2023-11-29
tags: [Amazon, Titan Image Generator, DALL-E, AI, ML, Adobe Firefly]
filename: 2023-11-29-amazon-titan-image-generator-comparison.md
---

Amazon have launched a preview of Titan Image Generator - three screencaps from the AI/ML keynote attached below. This is very similar to the DALL-E that is available through [labs.openai.com](http://labs.openai.com) (DALL-E 2?):

- only very limited resolutions available, both for Generation and Editing (screenshot #4).
- result is always PNG

Unlike DALL-E:

- I haven't been able to gotten the Edit to really work (screenshot #5 -> #6, #7 -> #8 face changed even though I had only defined the editing rectangle around the shirt and asked for a blue one)
- You cannot work on a full resolution photo (DALL-E just restricts the editing area)

I couldn't find any watermarks (screencap #3) in the finished result. Either they are not part of the Preview, or they are at least in a different format & style from the ones applied by Adobe Firefly.

Speaking of **Adobe Firefly**: I had success with one photo by using it on iPad: [the brush bug](/adobe-firefly-case-study) didn't show, and neither did the image noise in the result download. Either there was a major bugfix release or it's simply a "Mobile First" app. 😉

![Screenshot #1](assets/img/Screenshot%202023-11-29%20175139.png) \
![Screenshot #7](assets/img/Screenshot%202023-11-29%20175337.png) \
![Screenshot #7](assets/img/Screenshot%202023-11-29%20175234.png) \
![Screenshot #6](assets/img/image%20(20).png) \
![Screenshot #5](assets/img/Screenshot%202023-11-29%20194413.png) \
![Screenshot #4](assets/img/Screenshot%202023-11-29%20194537.png) \
![Screenshot #2](assets/img/generatedImage%20(1).png) \
![Screenshot #3](assets/img/Screenshot%202023-11-29%20191046.png)

The Verge on the watermark:
> The catch, though, comes with how the invisible watermark is detected. Amazon created an API that people can connect to and then feed the image to check the image’s provenance. Philomin said this is by design; after all, Titan is not an end product but a model, so developers building with Titan Image Generator will choose how to provide that information to users.
([Source](https://www.theverge.com/2023/11/29/23980697/amazon-ai-image-model-watermark-copyright))
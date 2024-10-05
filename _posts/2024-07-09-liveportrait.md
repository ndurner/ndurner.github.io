---
layout: post
title: "LivePortrait: Animating the Static"
date: 2024-07-09
last_updated: 2024-07-09
tags: [ai, animation, deepfake]
---

A video that's currently captivating my social media timeline demonstrates a fascinating leap in AI-driven animation. Developed by Chinese research groups, this demo represents a significant milestone in what I'd love to see in a "Generative AI" product or service.
![Driver video animating still image](assets/img/liveportrait.mp4)

The technology, called LivePortrait, animates static images based on a driver video. In the demo, we see a woman on the left animating a static image of a man in the middle, resulting in a lifelike animation on the right. Intriguingly, it's not limited to photographs - it works with artworks too: Mona Lisa or Vermeer's Girl with a Pearl Earring coming to life!

For the technically inclined, the source code and AI weights are publicly available: [HuggingFace](https://huggingface.co/spaces/KwaiVGI/LivePortrait/tree/main). You can even try the demo yourself in the "App" tab, similar to how my chatbots are set up.

While the current implementation uses pre-recorded video to drive the animation, the potential for real-time streaming applications is tantalizing. This opens up a world of possibilities, but also raises concerns about potential misuse, particularly in the realm of deepfakes and identity fraud.

As Ethan Mollick [aptly put it](https://x.com/emollick/status/1809387705656086653), "If your security depends on a visual signal, start thinking about your options.".
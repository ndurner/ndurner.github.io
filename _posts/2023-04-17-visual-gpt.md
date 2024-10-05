---
layout: post
title: "Visual GPT"
author: "Nils Durner"
categories: [journal]
tags: [multi-modal, chatgpt, visual gpt, llava]
date: 2023-04-17
last_updated: 2023-04-17
---

Visual GPT, the multi-modal interface that a German Microsoft manager likely referred to in their earlier hints, has been released as source code: [Github](https://github.com/microsoft/visual-chatgpt). And it's a bit disappointing... at least when running on CPUs only, rather than GPUs.

Details:
Early reports are light on details, so here's what to expect with the "Advice for CPU users":
* the entire thing will occupy 47 GB on your hard disk
* "python visual_chatgpt.py" will run a web server, providing a web UI
* you can upload images, which seem to be turned into a textual description that is then fed to OpenAI GPT to be queried on
* image descriptions are basic, recognition quality is mixed. Examples:
  * ["a woman holding a baby fox in her arms"](https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/%27Snoop%27_and_Laura_%285605073271%29.jpg/1095px-%27Snoop%27_and_Laura_%285605073271%29.jpg?20180703075112)
  * ["a laptop with a waffle on the keyboard"](https://i.imgur.com/cqbWazr.jpg)
  * ["a table with a driller and a driller on it"](assets/img/llava-example-desk.jpeg)
* no trace of OCR

Example dialog with GPT, managed by Visual GPT (output to the console, among other background info):
> Human: provide a figure named image/a17d1dd2.png. The description is: a woman holding a baby fox in her arms. This information helps you to understand this image, but you should use tools to finish following tasks, rather than directly imagine from my description. If you understand, say "Received".\
> \
> AI: Received.\
> \
> Human: image/a17d1dd2.png What's her shirt color? \
> \
> AI: The woman in the image is wearing a white shirt.

Screenshot:
![Visual GPT with the above dialog](assets/img/visual-gpt.png)

Better results with LLaVA-13B [Heise newsticker](https://www.heise.de/news/LLaVA-Multimodales-offenes-KI-Modell-auf-LLaMA-Basis-liest-Bilder-und-Sprache-8974975.html): with the fox lady:
> ? describe the image in great detail \
> ! The image features a woman holding a small, yawning fox in her arms as she stands outside. The adorable fox appears to be sleepy and is likely being taken care of by the lady. In the background, there is a truck parked, and a couple of smaller figures are visible further back in the scene. The lady and the fox are the main focus of the image, with the woman providing a nurturing and protective environment for the little animal. \
> ? what's the color of her shirt? \
> ! The woman holding the fox is wearing a blue shirt.

Also, it seems to work with cropped objects, which Visual GPT does not. (see screenshot, but also hallucination becomes obvious in this one).
![Picture of two buses, one cropped](assets/img/llava-buses.png)

Not useful for slide processing, though.
![Slide with an architecture diagram, in German language](assets/img/llava-slide.png)

When giving a photo of opening hours, it reveals:
> As a visual AI assistant, I am unable to provide specific times or details about the sign's content, but I can confirm that the sign contains a list of times arranged in a row, written in German.

(Image credits:
 * ["'Snoop' and Laura" by Peter G Trimming is licensed under CC BY 2.0.](https://commons.wikimedia.org/wiki/File:%27Snoop%27_and_Laura_%285605073271%29.jpg)
 * [Stroopwafel by Triszz](https://www.reddit.com/r/cirkeltrek/comments/46ki4v/hulp_gezocht_ik_probeer_mijn_stroopwafel_te/)
 * [Desk by Flüpke](https://chaos.social/@fluepke)
)
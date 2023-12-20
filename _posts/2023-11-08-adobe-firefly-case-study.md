---
layout: post
title: "Adobe Firefly: A Case Study"
date: 2023-11-08
tags: [Adobe Firefly, AI, Image Editing, Generative AI, Inpainting]
filename: 2023-11-08-adobe-firefly-case-study.md
---

Quick case study of **Adobe Firefly** ("creative generative AI models with an initial focus on image and text effect generation"):

With picture #1 below, I wanted to emphasize on the model in the center, thus clean up the distractions on the left side, and also move the laptop on the right upwards. The "Inpainting" function in Affinity Photo.app works well to remove small to medium distractions in an image, but is no good for such large areas as in this picture. Relevant to my use-case, Firefly offers two Gen.AI. inpainting functions called "Removal" and "Addition". Removal allows the user to mark parts of the image with a brush tool, and these parts can then be replaced by one of the several AI-generated alternatives. Similarly, the Addition function also allows parts of the image to be marked, which are then replaced by what's generated as the result of the user's text prompt. The result is picture #2:

- left side replaced by a continuation of the window (Removal)
- right side replaced by "A modern laptop with the screen facing the viewer" (Addition)

The image download was a PNG file (even though I had uploaded a JPG), with even the untouched parts showing increased pixel noise (which I fixed back in Affinity Photo by stacking the original and AI processed image in layers and selectively retaining the best parts from either).

The paid edition removes the "Adobe Firefly" watermark at the bottom left - which I had hoped it would retain to clearly mark the image as Fake. What's more, this widely reported Content Credentials icon is nowhere to be seen. Quick inspection of the PNG with Notepad++ hints at some kind of digital signature having been applied ("DigiCert Trusted G4 RSA4096 SHA256 TimeStamping CA", "http://pki-ocsp.symauth.com"). If someone's interested in further analysis, let me know - maybe there is some kind of Namirial business interest there? (/attn @Libero Rignanese)

The Firefly product itself also appears rather unfinished and rushed-to-market:

- no file history or cloud storage. Users are encouraged to save often.
- selecting with said brush tool with multiple steps with releasing the mouse button in between tends to mess up the previously selected region mask. You absolutely have to select in one go.

End result: [LinkedIn](https://www.linkedin.com/posts/nilsdurner_ai-namirial-generativeai-activity-7128121543137628160-xL2M) 😉

![IMG_5858-brighter.jpg](assets/img/IMG_5858-brighter.jpg)\
![Firefly 20231106182829.png](assets/img/Firefly%2020231106182829.png)

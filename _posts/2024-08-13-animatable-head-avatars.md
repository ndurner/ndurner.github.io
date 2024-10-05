---
layout: post
title: "3D Animatable Head Avatars"
date: 2024-08-13
last_updated: 2024-08-13
tags: [deepfake]
---
A commenter shared previously that deep-fake methods struggle with forging faces from the side (cheeks, ears). Not anymore:
> In this paper, we present a novel 3D head avatar creation approach capable of generalizing from few-shot in-the-wild data with high-fidelity and animatable robustness. [...] we propose a framework comprising prior learning and avatar creation phases. [...] Extensive experiments demonstrate that our model effectively exploits head priors and successfully generalizes them to few-shot personalization, achieving photo-realistic rendering quality, multi-view consistency, and stable animation.

Resources:
* Project page with demo videos (slow): https://headgap.github.io/#
* Paper: https://arxiv.org/pdf/2408.06019
* X (faster loading demo video): https://x.com/_akhaliq/status/1823195465292324965

The numbers from the appendix suggest that the raw compute for training this may be had for less than $300.
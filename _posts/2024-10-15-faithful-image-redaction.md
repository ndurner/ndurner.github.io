---
layout: post
title: "Redaction without recompression"
author: "Nils Durner"
categories: [journal]
tags: [forensics, vlm, mllm, llm]
date: 2024-10-15
last_updated: 2024-10-15
---

As I was compiling bug reports for a Vision Language Model vendor, I found the need to redact images without JPEG recompression: simply re-saving a particular sample image that had originally triggered a repitition loop with the MLLM changed the image in such a way that I could not reproduce the problem. Solution: [asenior/Jpeg-Redaction-Library](https://github.com/asenior/Jpeg-Redaction-Library). From the project description:
> The main distinguishing feature of the library is the ability to erase regions of an image (for privacy protection) in the compressed domain.

The repository builds on macOS with (just) the Xcode developers tools installed (so Homebrew not required), but one has to make bin/ and lib/ individually:
```
% git clone --depth=1 https://github.com/asenior/Jpeg-Redaction-Library.git
% cd Jpeg-Redaction-Library
% cd lib
% make
% cd ../bin
% make
```

Usage: to black out one region:
```
% /tmp/Jpeg-Redaction-Library/bin/redact stitched_003.jpeg output.jpg "195,320,195,205:s"
```

To black out two regions:
```
% /tmp/Jpeg-Redaction-Library/bin/redact stitched_003.jpeg output.jpg "0,700,195,205:s;0,700,450,470:s;0,700,840,1610:s"
```

This type of redaction left the sample image in a shape that would still trigger the repitition loop, so created an as-faithful-as-possible redacted version when the Apple Preview app failed to do so. As I do not know if the JPEGs produced are still standards compliant or might appear damaged in some way, I pointed that out to my contact at the vendor.
---
layout: post
title: "xz Backdoor"
date: 2024-03-30
last_updated: 2024-03-30
description: "Reports discovery of backdoor in xz compression code via malicious patch, details vulnerability analysis and mitigation recommendations."
tags: [security, oss]
---

A lot has been (and continues to be) written about the [xz Backdoor](https://www.openwall.com/lists/oss-security/2024/03/29/4).

What is, however, even more troubling is that this yet another demonstrated open-source supply chain attack, perhaps with years of preparation in advance. It could have hit(*) any downstream maintainer, just like with the faker.js incident, but there were two possible evasion factors:
1. as with faker.js, there was only one active maintainer, as per https://lcamtuf.substack.com/p/technologist-vs-spy-the-xz-backdoor . I treat such as a major red flag. (granted, mainly because I doubt sustained development)
2. the Github source packages were not compromised, perhaps because they were directly built from the git repo, which was also not compromised
… which works when you follow the old-school style of manual dependency management or, to some extend, do rigoros version pinning, but fails if you let loose your unpinned Rust cargo, Python pip… or whatever your Linux distro uses. 

Not good at all.

Reminds of XKCD 2347.


(* in the sense of at least running code on the build host that doesn‘t belong)
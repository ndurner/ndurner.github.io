---
layout: post
title: "OBS Stream Recording"
date: 2024-04-21
last_updated: 2024-09-25
description: "Learn how to set up and troubleshoot remote stream recording on AWS EC2 instances, including fixing audio, RDP disconnection, and resolution issues with OBS and Windows Server."
tags: [obs, aws, rdp, microsoft teams]
---

How does one record a live stream in absence, perhaps using AWS EC2? A discussion on Reddit lead me to base everything on a g5.xlarge instance.


Problems:
⚒️ On the Windows Server, there initially was no soundcard. ~~Fixed by simply installing [Virtual Audio Cable (VAC)](https://vac.muzychenko.net/en/)?~~ Fixed by running Microsoft Teams in an OBS Source of type "Browser": this will include video and audio in the recording.

⚒️ On RDP disconnect, the OBS recording froze. Fixed with disconnecting using this command:
> tscon %sessionname% /dest:console

⚒️ The resolution of this fallback screen was pretty low, resulting in blurryness in the OBS recording result. GPT-4 Turbo provided helpful guidance on fixing this one:

The resolution issue you're experiencing after running tscon is likely because when you're disconnecting the RDP session using tscon, the session is being switched to the console (or physical) session. If no physical monitor is attached (which is the case with virtual machines like EC2), then Windows defaults to a lower resolution.

One way to get around this is to "trick" Windows into thinking a monitor with a specific resolution is attached. This is possible using a method called "Headless Ghost" or "dummy" plug. This method involves setting specific registry keys to make Windows think a monitor is connected and set its resolution.

Here's how to do it:

1. Open Registry Editor (regedit.exe).
2. Navigate to HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Configuration.
3. Under this key, there might be several subkeys. You'll need to apply the following steps to each of these subkeys:
4. Find the subkey 00 under each. This represents the first (and often only) monitor.
5. Change the PrimSurfSize.cx and PrimSurfSize.cy values to your desired resolution (for example, 1920 and 1080).
6. In addition, the Stride value needs to be recomputed. In most cases, the color depth is 32 bits. Formula: ((Horizontal Resolution * Color Depth + 7) / 8). For a 1920x1080 resolution with a color depth of 32 bits, you would calculate the Stride value as ((1920 * 32 + 7) / 8) = 7680. 
7. Change the ActiveSize.cx and ActiveSize.cy values to the same resolution.
8. Reboot the machine for the changes to take effect.

[Update 2024-09-25] \
clarified in the text that the Browser source is being used
---
title: "Browser-based Time Retrieval"
date: 2025-10-16
last_updated: 2025-10-16T00:00:00+00:00
author: "Nils Durner"
redirect_to:
  - https://ndurner.substack.com/p/browser-time-retrieval
tags: [Substack]
excerpt: "Clock skew - the phenomenon where computer clocks diverge from real time - remains a challenge even in the modern age of computing. A common solution is to periodically synchronize clocks with Internet time sources (“NTP”), but heavily firewalled servers may not benefit and can still drift. In scenarios where matching timestamps in log files is essential, a different solution is useful: something "
substack_url: "https://ndurner.substack.com/p/browser-time-retrieval"
canonical_url: "https://ndurner.substack.com/p/browser-time-retrieval"
sitemap: false
---

Clock skew - the phenomenon where computer clocks diverge from real time - remains a challenge even in the modern age of computing. A common solution is to periodically synchronize clocks with Internet time sources (“NTP”), but heavily firewalled servers may not benefit and can still drift. In scenarios where matching timestamps in log files is essential, a different solution is useful: something akin to icanhazip.com for IP addresses—but for time.

While previous providers like WorldTimeAPI and icanhazepoch.com have been discontinued, several options remain. Here are three:

### gettimeapi.dev

The request `https://gettimeapi.dev/v1/time?timezone=UTC` returns a JSON like this:

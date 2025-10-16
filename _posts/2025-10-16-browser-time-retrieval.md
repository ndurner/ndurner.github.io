---
layout: post
title: "Browser-based Time Retrieval"
date: 2025-10-16
tags: [tools, networking, time]
last_updated: 2025-10-16T17:58:00+02:00
author: "Nils Durner"
categories: [journal]
---

Clock skew - the phenomenon where computer clocks diverge from real time - remains a challenge even in the modern age of computing. A common solution is to periodically synchronize clocks with Internet time sources ("NTP"), but heavily firewalled servers may not benefit and can still drift. In scenarios where matching timestamps in log files is essential, a different solution is useful: something akin to icanhazip.com for IP addresses—but for time.

While previous providers like WorldTimeAPI and icanhazepoch.com have been discontinued, several options remain. Here are three:
### gettimeapi.dev
The request `https://gettimeapi.dev/v1/time?timezone=UTC` returns a JSON like this:
```
{"timestamp":1760627718,"time":"15:15:18.939251","date":"2025-10-16","timezone":"UTC","abbr":"UTC","offset":"+00:00","iso8601":"2025-10-16T15:15:18Z"}
```

Several time-zone abbreviations like "MST" are supported, but not all. Specifying "PT", "PDT", or "CEST" fails with:
```
{"error":"Invalid timezone"}
```

Instead, use an IANA time-zone identifier. For example, `https://gettimeapi.dev/v1/time?timezone=Europe/Berlin` returns:
```
{"timestamp":1760628040,"time":"17:20:40.568777","date":"2025-10-16","timezone":"Europe/Berlin","abbr":"CET","offset":"+01:00","iso8601":"2025-10-16T17:20:40+02:00"}
```
Here, the fields "abbr" and "offset" are not correct: at the time of writing, Berlin is still on daylight saving time—so "CEST" and "+02:00" would be correct.

### TimeAPI.io
Usage: `https://www.timeapi.io/api/Time/current/zone?timeZone=UTC`. This service responds relatively slowly and doesn’t accept the CEST abbreviation either. For the simple case of UTC:
```
{"year":2025,"month":10,"day":16,"hour":15,"minute":28,"seconds":36,"milliSeconds":386,"dateTime":"2025-10-16T15:28:36.3869071","date":"10/16/2025","time":"15:28","timeZone":"UTC","dayOfWeek":"Thursday","dstActive":false}
```

`Europe/Berlin` is valid here as well, and daylight saving time is correctly indicated via `dstActive`:
```
{"year":2025,"month":10,"day":16,"hour":17,"minute":34,"seconds":53,"milliSeconds":148,"dateTime":"2025-10-16T17:34:53.1486218","date":"10/16/2025","time":"17:34","timeZone":"Europe/Berlin","dayOfWeek":"Thursday","dstActive":true}
```

### Cloudflare Trace
Unlike the other two services, `https://1.1.1.1/cdn-cgi/trace` does not return a human-readable local time. Instead, it includes the number of seconds since 1970-01-01 (Unix epoch) in UTC:
```
...
ts=1760629515.434
```

You can quickly fetch and convert this to readable time using PowerShell or zsh.

#### PowerShell 7
```
# Fetch Cloudflare trace and extract the epoch timestamp
$trace = (Invoke-WebRequest -Uri 'https://1.1.1.1/cdn-cgi/trace' -UseBasicParsing).Content
$ts    = ($trace -split "`n" | Where-Object { $_ -like 'ts=*' }) -replace '^ts=',''

# Convert to UTC DateTime (preserve milliseconds)
$dtUtc = [DateTimeOffset]::FromUnixTimeMilliseconds([long]([double]$ts * 1000)).UtcDateTime
"UTC:            $($dtUtc.ToString('yyyy-MM-ddTHH:mm:ss.fffZ'))"

# Convert to local time zone
$dtLocal = [System.TimeZoneInfo]::ConvertTimeFromUtc($dtUtc, [System.TimeZoneInfo]::Local)
"Local:          $($dtLocal.ToString('yyyy-MM-ddTHH:mm:ss.fff zzz'))"

# Convert to a specific time zone (Windows ID example)
$tzBerlin = [System.TimeZoneInfo]::FindSystemTimeZoneById('Europe/Berlin')
$dtBerlin = [System.TimeZoneInfo]::ConvertTimeFromUtc($dtUtc, $tzBerlin)
"Europe/Berlin:  $($dtBerlin.ToString('yyyy-MM-ddTHH:mm:ss.fff zzz'))"
```

#### zsh macOS
```
ts=$(curl -s https://1.1.1.1/cdn-cgi/trace | sed -n 's/^ts=//p')
sec=${ts%.*}

echo "UTC:           $(date -u -r "$sec" '+%Y-%m-%dT%H:%M:%SZ')"
echo "Europe/Berlin: $(TZ=Europe/Berlin date -r "$sec" '+%Y-%m-%dT%H:%M:%S%z')"
```

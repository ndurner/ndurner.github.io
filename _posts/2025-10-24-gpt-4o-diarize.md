---
layout: post
title: "Transcription and Diarization with new GPT-4o"
date: 2025-10-24
tags: [llm, openai, gpt-4o, transcribe]
last_updated: 2025-10-24T23:12:00+02:00
author: "Nils Durner"
categories: [journal]
---

OpenAI have released a new speech-to-text model that also supports diarization (speaker separation and attribution): [GPT-4o Transcribe Diarize (aka "gpt-4o-transcribe-diarize")](https://platform.openai.com/docs/models/gpt-4o-transcribe-diarize). It's priced the same (estimated) cost of regular gpt-o4-transcribe and Whisper.
Immediate findings:
* chunk limit of 1400 seconds
* not available over the Realtime API
* `prompt`ing, e.g. to establish abbreviations or prior chunks, is not supported
* asked for the Word-Error-Rate WER compared to other models, [Peter Bakkum @OpenAI clarified](https://x.com/itsonolo/status/1981457377850511588): "Would consider it roughly comparable but would default to the other models if you don’t need diarization". Artificial Intelligence [reports a WER of 21%](https://artificialanalysis.ai/speech-to-text) for GPT-4o Transcribe, but notes that "Compared to Whisper, GPT-4o Transcribe smooths transcripts, which results in lower word-for-word accuracy, especially on less structured speech (e.g., meetings, earnings calls)."
* speaker attribution works by specifying references into the audio file. If no references were given, speaker labels are returned as "A:", "B: ", etc. - so the model doesn't learn and assign automatically from the audio. This is different from Google Gemini.
* a quick check at the office shows hallucination and omissions with a short chat in German language (see below)

## Implementations
An implementation with streaming support (but limited to 23 minutes) is part of my [OAI Chat](https://github.com/ndurner/oai_chat). A simplistic stand-alone implementation looks like this (sample output below):
```
import argparse
import base64
import mimetypes
from pathlib import Path
from typing import Dict, List, Optional

from openai import OpenAI


def to_data_url(path: Path) -> str:
    """
    Convert an audio file to a base64 data URL using the best-effort MIME type.
    """
    mime_type, _ = mimetypes.guess_type(path.name)
    mime_type = mime_type or "application/octet-stream"
    with path.open("rb") as handle:
        encoded = base64.b64encode(handle.read()).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Transcribe an audio file with diarization using OpenAI Realtime."
    )
    parser.add_argument(
        "audio_path",
        type=Path,
        help="Path to the audio file (e.g., an .m4a recording).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    audio_path: Path = args.audio_path.expanduser().resolve()
    if not audio_path.exists():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    client = OpenAI()

    with audio_path.open("rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="gpt-4o-transcribe-diarize",
            file=audio_file,
            response_format="diarized_json",
        )

    for segment in transcript.segments:
        print(segment.speaker, segment.text, segment.start, segment.end)


if __name__ == "__main__":
    main()
```

Sample output with two speakers, showing erroneous additions with ~~strikethrough~~ and erroneous omissions in **bold**:
> A  Hallo, 0.95 1.5000000000000002  
> ~~A  ich 1.6000000000000003 2.0500000000000007~~  
> B  Hallo, 2.0500000000000007 2.7  
> A  ich bin Nils. 2.8 4.2  
> B  **ich** bin Mascha. 5.25 5.95  
> A  Tschüss, Mascha. 7.1000000000000005 8.200000000000001  
> **B  Tschüss**
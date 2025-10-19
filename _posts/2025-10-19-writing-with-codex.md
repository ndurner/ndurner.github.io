---
layout: post
title: "Writing with OpenAI Codex"
date: 2025-10-19
tags: [llm, openai, codex, vscode]
last_updated: 2025-10-19T12:11:00+02:00
author: "Nils Durner"
categories: [journal]
---

## Motivation

For a recent writing project that built on an earlier piece I had written in a hurry, I wanted to see if #GenAI could help the way it already does for programming. Because my ideal venue was arXiv (an open‑access preprint library), I wanted a LaTeX‑based workflow for typesetting and citations, rather than the—on these fronts limited—ChatGPT Canvas ("CanMore"). To assist, I turned to OpenAI Codex: both the CLI and the VS Code extension.

## Where Codex Struggled on Longer Documents

Progress was swift at first, but became tedious and error‑prone as the document grew. Two behaviors seemed to drive this:

1. It reads files in ~250‑line chunks.
2. It tends to scan selectively rather than reading end‑to‑end.

I added a custom CLI logger to trace client–server interactions. The logs showed a handful of 250‑line reads followed by keyword‑driven `ripgrep` fetches. As a result, broad or cross‑cutting instructions often missed earlier or later occurrences.

Examples of misses:
- Switched the document style (`\usepackage`) and fetched the new `.sty`, but left comments referring to the old style elsewhere in the file.
- Added citations without checking for duplicates in `references.bib`, producing a duplicate that surfaced in the PDF.
- Assessed whether a draft LinkedIn post represented the article by searching for post‑derived keywords, which ensured some faithfulness but missed content present in the article and absent in the post.

In short, changes became more punctual and less comprehensive than desired as size increased.

## Techniques That Worked

- Anchor edits by pasting the key passage into the VS Code Codex sidebar before asking for changes.
    - (it may work to select text in the editor and prompt Codex straight, but I haven't tried this)
- Start a new thread with “Confirm that you have web access through icanhazip.com.” This reminded Codex it could use the network and discouraged hallucinated facts when it assumed no access.

## Web Search, Citations, and Preferences

- The Codex CLI `--search` flag is very useful: vague references ("that … paper by …") can become concrete citations, with entries added to BibTeX and in‑place `\cite{}` insertions.
- Personalization from ChatGPT does not carry over: Codex does not use ChatGPT’s tone or style settings. Instead, maintain an `Agents.md` to prime behavior. I reproduced mine below. In practice, adherence was uneven—especially American vs. British English. Switching spellings produced punctual fixes for a few common words but not a whole‑document pass.

## Models and Reasoning Effort

I switched models and reasoning levels frequently. GPT‑5 Codex handled multi‑step, programming‑style tasks better, while GPT‑5 suited prose. For example, the stylized “pills” on the first slide of this [deck](https://www.linkedin.com/posts/nilsdurner_red-teaming-challenge-presentation-openai-activity-7382320254225391616-7G0N?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAGX2jIBd6RDsNRYv13Bvu3x4nnCNu96SEw) and the circled numbers on subsequent slides were rendered by GPT‑5 Codex. I used Medium reasoning by default and Minimal for simple tasks that a non‑reasoning model such as GPT‑4.1 could do, which sped things up.

## Road Ahead: The /read Command
To overcome the problem of Codex considering parts but not the whole, I [filed an enhancement request](https://github.com/openai/codex/issues/4719#issuecomment-3368061864) for a slash command that reads an entire file into a conversation thread, avoiding unreliable chunked ingestion. I already have an experimental implementation that improves quality and speed.

## Appendix: Agents.md for LaTeX Project
```
Agent Notes

 - project organization
  - `main.tex`: Technical Report of a Kaggle Red-Teaming Challenge project submission
  - `references.bib`: bibliography database used by BibTeX.
  - `Makefile`: LaTeX build targets (`pdf`, `watch`, `clean`, `clobber`, `fast`, `draft`).
  - `slides.tex`: presentation slide deck
- LaTeX percent escaping: In LaTeX, `%` starts a comment. Use `\%` for literal percent symbols in prose, titles, captions, tables, and bibliography fields. Unescaped `%` in text truncates the line at that point.
- Example: write `97.5\% (Wilson 95\% CI)` not `97.5% (Wilson 95% CI)`.
- When editing `.tex` files, only leave `%` unescaped when you intend to start a comment.
- You do have web access, but HTML files could overwhelm you. The best strategy is to retrieve web content and convert it for yourself to Markdown. Create and maintain a scratch/ folder for that if you must. Be sure to always get the full content of a page (avoid reading partials with sed without scrolling to the end)
- Avoid using Em-Dashes (—)
- LaTeX hyphens: `\-` is a discretionary hyphen and only appears at a line break; it will vanish in the middle of a line. For visible hyphens in compounds use `-` (e.g., `gpt-oss`, `gpt-5-mini`, `queer-coded`, `Gen-Z`). Keep `\-` only when you want optional break points without showing a hyphen otherwise.
- "the Kaggle submission" refers to the project repository in $NILS_DOCS/gpt-oss-data/cook-gptoss-validation. There is an Obsidian vault with notes in $NILS_ICLOUD\~md\~obsidian/Documents/gpt-oss
- after making changes, ensure main.tex still compiles
- Style: Prefer American English spelling (e.g., behavior, organize, center, gray) in prose and comments; do not alter spellings in bibliographic titles.
```

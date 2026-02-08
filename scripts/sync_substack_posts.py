#!/usr/bin/env python3
"""Sync Substack RSS items into Jekyll posts.

This script is designed for GitHub Actions:
- fetch a Substack RSS feed
- create new markdown posts in _posts/
- skip items already imported (based on substack_url front matter)
"""

from __future__ import annotations

import argparse
import datetime as dt
import email.utils
import html
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

DEFAULT_FEED_URL = "https://ndurner.substack.com/feed"
DEFAULT_MAX_POSTS = 10


def parse_feed_urls(raw: str) -> list[str]:
    normalized = raw.replace("\n", ",")
    urls = [item.strip() for item in normalized.split(",")]
    return [item for item in urls if item]


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "post"


def yaml_quote(text: str) -> str:
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def strip_html(raw: str) -> str:
    no_tags = re.sub(r"<[^>]+>", " ", raw)
    no_space = re.sub(r"\s+", " ", no_tags).strip()
    return html.unescape(no_space)


def parse_date(raw: str) -> dt.datetime:
    parsed = email.utils.parsedate_to_datetime(raw)
    if parsed is None:
        raise ValueError(f"Could not parse date: {raw}")
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed.astimezone(dt.timezone.utc)


def text_from_item(item: ET.Element) -> str:
    content_encoded = item.find("{http://purl.org/rss/1.0/modules/content/}encoded")
    if content_encoded is not None and content_encoded.text:
        return strip_html(content_encoded.text)

    description = item.find("description")
    if description is not None and description.text:
        return strip_html(description.text)

    return ""


def read_existing_substack_urls(posts_dir: Path) -> set[str]:
    existing: set[str] = set()
    fm_substack_pattern = re.compile(r"^substack_url:\s*(.+?)\s*$")
    any_url_pattern = re.compile(r"https?://[^\s\"']+")
    for post_path in posts_dir.glob("*.md"):
        try:
            with post_path.open("r", encoding="utf-8") as handle:
                in_front_matter = False
                for idx, line in enumerate(handle):
                    if idx > 120:
                        break
                    stripped = line.strip()
                    if idx == 0 and stripped == "---":
                        in_front_matter = True
                        continue
                    if in_front_matter and stripped == "---":
                        break
                    if not in_front_matter:
                        continue

                    match = fm_substack_pattern.match(stripped)
                    if match:
                        value = match.group(1).strip()
                        if (value.startswith('"') and value.endswith('"')) or (
                            value.startswith("'") and value.endswith("'")
                        ):
                            value = value[1:-1]
                        if "substack.com/" in value:
                            existing.add(value)

                    for candidate in any_url_pattern.findall(stripped):
                        if "substack.com/" in candidate:
                            existing.add(candidate)
        except OSError:
            continue
    return existing


def fetch_feed(feed_url: str, feed_file: str | None = None) -> ET.Element:
    if feed_file:
        payload = Path(feed_file).read_bytes()
    else:
        headers = {
            # Substack/Cloudflare may reject urllib's default Python user-agent.
            "User-Agent": "Mozilla/5.0 (compatible; ndurner-gh-pages-sync/1.0)",
            "Accept": "application/rss+xml, application/xml;q=0.9, */*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
        }
        request = urllib.request.Request(feed_url, headers=headers)

        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                payload = response.read()
        except urllib.error.HTTPError as exc:
            if exc.code not in (403, 429):
                raise
            # Retry with curl for Cloudflare-sensitive endpoints.
            curl_cmd = [
                "curl",
                "--fail",
                "--silent",
                "--show-error",
                "--location",
                "--max-time",
                "45",
                "--retry",
                "2",
                "--retry-all-errors",
                "-H",
                f"User-Agent: {headers['User-Agent']}",
                "-H",
                f"Accept: {headers['Accept']}",
                "-H",
                f"Accept-Language: {headers['Accept-Language']}",
                feed_url,
            ]
            payload = subprocess.check_output(curl_cmd)
    return ET.fromstring(payload)


def next_available_filename(posts_dir: Path, date_prefix: str, slug: str) -> Path:
    candidate = posts_dir / f"{date_prefix}-substack-{slug}.md"
    index = 2
    while candidate.exists():
        candidate = posts_dir / f"{date_prefix}-substack-{slug}-{index}.md"
        index += 1
    return candidate


def build_post(title: str, published: dt.datetime, url: str, excerpt: str) -> str:
    published_iso = published.isoformat(timespec="seconds")
    published_date = published.date().isoformat()
    lines = [
        "---",
        f"title: {yaml_quote(title)}",
        f"date: {published_date}",
        f"last_updated: {published_iso}",
        'author: "Nils Durner"',
        "redirect_to:",
        f"  - {url}",
        "tags: [Substack]",
        f"substack_url: {yaml_quote(url)}",
        f"canonical_url: {yaml_quote(url)}",
        "sitemap: false",
        "---",
        "",
        "Published on Substack.",
        "",
    ]

    if excerpt:
        lines.extend(
            [
                excerpt[:500] + ("..." if len(excerpt) > 500 else ""),
                "",
            ]
        )

    lines.append(f"[Read on Substack]({url}).")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync Substack feed into Jekyll _posts")
    parser.add_argument(
        "--feed-url",
        default=os.getenv("SUBSTACK_FEED_URL", DEFAULT_FEED_URL),
        help="Substack RSS feed URL",
    )
    parser.add_argument(
        "--feed-urls",
        default=os.getenv("SUBSTACK_FEED_URLS", ""),
        help="Comma-separated fallback RSS feed URLs (tried after --feed-url)",
    )
    parser.add_argument(
        "--posts-dir",
        default="_posts",
        help="Path to Jekyll posts directory",
    )
    parser.add_argument(
        "--max-posts",
        type=int,
        default=int(os.getenv("SUBSTACK_MAX_POSTS", str(DEFAULT_MAX_POSTS))),
        help="Maximum number of feed items to inspect",
    )
    parser.add_argument(
        "--feed-file",
        default=None,
        help="Optional local RSS file path (for testing)",
    )
    parser.add_argument("--dry-run", action="store_true", help="Do not write files")
    args = parser.parse_args()

    if not args.feed_url or not args.feed_url.strip():
        args.feed_url = DEFAULT_FEED_URL

    candidate_urls = [args.feed_url]
    for url in parse_feed_urls(args.feed_urls):
        if url not in candidate_urls:
            candidate_urls.append(url)

    posts_dir = Path(args.posts_dir)
    if not posts_dir.exists():
        print(f"Posts directory does not exist: {posts_dir}", file=sys.stderr)
        return 1

    root = None
    if args.feed_file:
        try:
            root = fetch_feed(args.feed_url, args.feed_file)
        except OSError as exc:
            print(f"Failed to read RSS file: {exc}", file=sys.stderr)
            return 1
        except ET.ParseError as exc:
            print(f"Failed to parse RSS XML: {exc}", file=sys.stderr)
            return 1
    else:
        last_error: str | None = None
        for idx, feed_url in enumerate(candidate_urls, start=1):
            try:
                print(f"Fetch attempt {idx}/{len(candidate_urls)}: {feed_url}")
                root = fetch_feed(feed_url)
                break
            except (urllib.error.URLError, TimeoutError, OSError, subprocess.CalledProcessError) as exc:
                last_error = f"{type(exc).__name__}: {exc}"
                print(f"Fetch failed for {feed_url}: {last_error}", file=sys.stderr)
            except ET.ParseError as exc:
                last_error = f"XML parse error: {exc}"
                print(f"Fetch failed for {feed_url}: {last_error}", file=sys.stderr)

        if root is None:
            print(f"Failed to fetch feed from all candidates. Last error: {last_error}", file=sys.stderr)
            return 1

    channel = root.find("channel")
    if channel is None:
        print("Invalid RSS feed: missing channel", file=sys.stderr)
        return 1

    items = channel.findall("item")
    if not items:
        print("No feed items found")
        return 0

    existing_urls = read_existing_substack_urls(posts_dir)
    created = 0

    for item in items[: args.max_posts]:
        title_el = item.find("title")
        link_el = item.find("link")
        date_el = item.find("pubDate")
        if title_el is None or link_el is None or date_el is None:
            continue
        if not title_el.text or not link_el.text or not date_el.text:
            continue

        title = title_el.text.strip()
        url = link_el.text.strip()
        if not title or not url or url in existing_urls:
            continue

        try:
            published = parse_date(date_el.text.strip())
        except ValueError:
            continue
        date_prefix = published.date().isoformat()
        slug = slugify(title)
        target_file = next_available_filename(posts_dir, date_prefix, slug)
        excerpt = text_from_item(item)

        content = build_post(title, published, url, excerpt)
        print(f"Create: {target_file}")
        if not args.dry_run:
            target_file.write_text(content, encoding="utf-8")

        existing_urls.add(url)
        created += 1

    print(f"Created {created} new post(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

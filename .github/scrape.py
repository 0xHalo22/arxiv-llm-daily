#!/usr/bin/env python3
"""
arxiv-llm-daily: snapshot new LLM-adjacent arxiv papers once a day.

queries the public arxiv API (no auth, ATOM feed, rate-limited to 1 req/day)
for papers in cs.CL and cs.AI submitted in the last 24 hours, and writes
them to a dated markdown file.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

API_URL = "https://export.arxiv.org/api/query"
# cs.CL = computation and language (the big LLM category)
# cs.AI = artificial intelligence
CATEGORIES = ["cs.CL", "cs.AI"]
MAX_RESULTS = 50
# how many of the latest papers to actually include in each snapshot.
# we keep the api call large so we have headroom, but trim the output.
KEEP_N = 30
USER_AGENT = "arxiv-llm-daily-bot (+https://github.com/0xHalo22/arxiv-llm-daily)"

ROOT = Path(__file__).resolve().parents[1]
PAPERS_DIR = ROOT / "papers"
LATEST_FILE = ROOT / "latest.md"

ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}


def build_query_url() -> str:
    # OR the categories: (cat:cs.CL OR cat:cs.AI)
    cat_clause = " OR ".join(f"cat:{c}" for c in CATEGORIES)
    params = {
        "search_query": cat_clause,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": str(MAX_RESULTS),
    }
    return API_URL + "?" + urllib.parse.urlencode(params)


def fetch_feed() -> str:
    url = build_query_url()
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8")


def parse_entries(feed_xml: str) -> list[dict]:
    root = ET.fromstring(feed_xml)
    out = []
    for entry in root.findall("atom:entry", ATOM_NS):
        eid = entry.findtext("atom:id", default="", namespaces=ATOM_NS).strip()
        title = (entry.findtext("atom:title", default="", namespaces=ATOM_NS) or "").strip()
        summary = (entry.findtext("atom:summary", default="", namespaces=ATOM_NS) or "").strip()
        published = entry.findtext("atom:published", default="", namespaces=ATOM_NS).strip()
        authors = [
            (a.findtext("atom:name", default="", namespaces=ATOM_NS) or "").strip()
            for a in entry.findall("atom:author", ATOM_NS)
        ]
        # clean up whitespace in title and summary
        title = re.sub(r"\s+", " ", title)
        summary = re.sub(r"\s+", " ", summary)
        out.append(
            {
                "id": eid,
                "title": title,
                "summary": summary,
                "published": published,
                "authors": authors,
            }
        )
    return out


def take_latest(entries: list[dict], n: int = KEEP_N) -> list[dict]:
    """take the N most recent papers. arxiv doesn't publish on weekends,
    so a strict 'last 24h' filter can return zero on saturdays/sundays.
    taking the top-N regardless of exact age is more robust and arguably
    more useful — we always show the freshest papers available."""
    return entries[:n]


def fmt_entry(e: dict) -> str:
    authors = ", ".join(e["authors"][:5])
    if len(e["authors"]) > 5:
        authors += f", +{len(e['authors']) - 5} more"
    # trim summary to ~300 chars so the file stays readable
    summary = e["summary"]
    if len(summary) > 320:
        summary = summary[:317].rstrip() + "..."
    return (
        f"### [{e['title']}]({e['id']})\n"
        f"_{authors}_ • {e['published'][:10]}\n\n"
        f"{summary}\n"
    )


def render(entries: list[dict], today: str) -> str:
    lines = [
        f"# arxiv LLM daily — {today}",
        "",
        f"the {len(entries)} most recent papers from cs.CL and cs.AI.",
        "",
    ]
    for e in entries:
        lines.append(fmt_entry(e))
    lines.append(
        f"_snapshot taken at {datetime.now(timezone.utc).isoformat(timespec='seconds')}_"
    )
    lines.append("")
    return "\n".join(lines)


def run_git(*args: str) -> None:
    subprocess.run(["git", *args], check=True, cwd=ROOT)


def main() -> int:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    print(f"[arxiv-llm-daily] fetching arxiv feed for {today}")

    feed = fetch_feed()
    entries = parse_entries(feed)
    print(f"  got {len(entries)} entries from API")

    recent = take_latest(entries)
    print(f"  keeping top {len(recent)}")

    body = render(recent, today)
    PAPERS_DIR.mkdir(exist_ok=True)
    snapshot_path = PAPERS_DIR / f"{today}.md"
    snapshot_path.write_text(body, encoding="utf-8")
    LATEST_FILE.write_text(body, encoding="utf-8")
    print(f"[arxiv-llm-daily] wrote {snapshot_path} and latest.md")

    if os.environ.get("GITHUB_ACTIONS"):
        run_git("add", str(snapshot_path), str(LATEST_FILE))
        status = subprocess.run(
            ["git", "status", "--porcelain"], cwd=ROOT, capture_output=True, text=True
        )
        if not status.stdout.strip():
            print("[arxiv-llm-daily] no changes to commit")
            return 0
        msg = f"snapshot {today}: top {len(recent)} papers"
        run_git("commit", "-m", msg)
        print(f"[arxiv-llm-daily] committed: {msg}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

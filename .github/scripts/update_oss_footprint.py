#!/usr/bin/env python3
"""Regenerate the open-source footprint table in README.md.

Queries the public GitHub Search API for every PR authored by the profile
owner against external repositories, aggregates per-project totals, and
rewrites the block between START/END markers. Stdlib only; GH_TOKEN env var
required (the workflow passes GITHUB_TOKEN).
"""
import datetime
import json
import os
import re
import sys
import urllib.request

USER = "dvd233"
README = "README.md"
START = "<!--START_SECTION:oss-footprint-->"
END = "<!--END_SECTION:oss-footprint-->"
TOKEN = os.environ["GH_TOKEN"]


def api(url):
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "oss-footprint-workflow",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def collect_prs():
    items = []
    page = 1
    while True:
        data = api(
            "https://api.github.com/search/issues"
            f"?q=type:pr+author:{USER}&per_page=100&page={page}"
        )
        batch = data.get("items", [])
        items.extend(batch)
        if len(items) >= data.get("total_count", 0) or not batch:
            return items
        page += 1


def aggregate(items):
    stats = {}
    for item in items:
        repo = item["repository_url"].split("/repos/")[-1]
        if repo.split("/")[0].lower() == USER.lower():
            continue  # external upstream repositories only
        entry = stats.setdefault(repo, {"total": 0, "merged": 0, "open": 0})
        entry["total"] += 1
        if item.get("pull_request", {}).get("merged_at"):
            entry["merged"] += 1
        elif item.get("state") == "open":
            entry["open"] += 1
    return stats


def build_block(stats):
    rows = sorted(
        stats.items(),
        key=lambda kv: (-kv[1]["merged"], -kv[1]["total"], kv[0].lower()),
    )
    lines = [
        "| Project | ⭐ | PRs | ✅ Merged | 🚀 Open |",
        "|---|---:|---:|---:|---:|",
    ]
    for repo, s in rows:
        stars = api(f"https://api.github.com/repos/{repo}")["stargazers_count"]
        lines.append(
            f"| [`{repo}`](https://github.com/{repo}) "
            f"| {stars} | {s['total']} | {s['merged']} | {s['open']} |"
        )
    total = sum(s["total"] for s in stats.values())
    merged = sum(s["merged"] for s in stats.values())
    opened = sum(s["open"] for s in stats.values())
    lines.append(
        f"| **Total across {len(stats)} upstream projects** "
        f"|  | **{total}** | **{merged}** | **{opened}** |"
    )
    today = datetime.date.today().isoformat()
    lines.append(
        f"\n<sub>Snapshot {today} (UTC) — PRs minus merged minus open are"
        " closed without merge and are not counted as adopted work.</sub>"
    )
    return "\n".join(lines)


def main():
    with open(README, encoding="utf-8", newline="") as fh:
        content = fh.read()
    pattern = re.compile(f"{re.escape(START)}.*?{re.escape(END)}", re.S)
    if not pattern.search(content):
        sys.exit("footprint markers not found in README.md")
    block = build_block(aggregate(collect_prs()))
    updated = pattern.sub(f"{START}\n{block}\n{END}", content)
    if updated == content:
        print("footprint unchanged")
    else:
        with open(README, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(updated)
        print("footprint updated")


if __name__ == "__main__":
    main()

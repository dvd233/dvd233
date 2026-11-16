#!/usr/bin/env python3
"""Regenerate the open-source footprint table in README.md.

Queries the public GitHub Search API for every PR authored by the profile
owner against external repositories, aggregates per-project totals, and
rewrites the block between START/END markers. Stdlib only; GH_TOKEN env var
required (the workflow passes GITHUB_TOKEN).
"""
import json
import os
import re
import sys
import urllib.request

USER = "dvd233"
README = "README.md"
CASE_ASSETS = ("assets/case-qwen.svg", "assets/case-weknora.svg", "assets/case-openviking.svg")
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


def project_stars(stats):
    return {
        repo: api(f"https://api.github.com/repos/{repo}")["stargazers_count"]
        for repo in stats
    }


STAR_SLOT = re.compile(r"(<!--stars:([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)-->)(?:\d+(?:\.\d+)?[km]?)(<!--/stars-->)")


def update_star_slots(text, stars):
    by_repo = {repo.casefold(): count for repo, count in stars.items()}

    def replace(match):
        count = by_repo.get(match[2].casefold())
        if count is None:
            return match[0]
        if count >= 1_000_000:
            value = f"{count / 1_000_000:.1f}m"
        elif count >= 1_000:
            value = f"{count / 1_000:.1f}k"
        else:
            value = str(count)
        return match[1] + value + match[3]

    return STAR_SLOT.sub(replace, text)


def build_block(stats, stars=None):
    if stars is None:
        stars = project_stars(stats)
    header = [
        "| Project | ⭐ | PRs | ✅ Merged | 🚀 Open |",
        "|:---|:---:|:---:|:---:|:---:|",
    ]

    def row(repo, s):
        return (
            f"| [`{repo}`](https://github.com/{repo}) "
            f"| {stars[repo]} | {s['total']} | {s['merged']} | {s['open']} |"
        )

    # Keep totals visible and both project groups collapsed. Preserve the
    # existing merged/open and star ordering inside each disclosure.
    adopted = sorted(
        (kv for kv in stats.items() if kv[1]["merged"] > 0),
        key=lambda kv: (-kv[1]["merged"], -stars[kv[0]], kv[0].lower()),
    )
    pending = sorted(
        (kv for kv in stats.items() if kv[1]["merged"] == 0),
        key=lambda kv: (-kv[1]["open"], -stars[kv[0]], kv[0].lower()),
    )
    lines = header.copy()
    total = sum(s["total"] for s in stats.values())
    merged = sum(s["merged"] for s in stats.values())
    opened = sum(s["open"] for s in stats.values())
    lines.append(
        f"| **Total across {len(stats)} upstream projects** "
        f"|  | **{total}** | **{merged}** | **{opened}** |"
    )
    if adopted:
        lines += [
            "",
            "<details>",
            f"<summary><strong>✅ {len(adopted)} projects with merged PRs</strong></summary>",
            "",
            *header,
            *(row(repo, s) for repo, s in adopted),
            "",
            "</details>",
        ]
    if pending:
        lines += [
            "",
            "<details>",
            f"<summary><strong>🧾 {len(pending)} projects with open PRs"
            " or PRs closed without merge</strong></summary>",
            "",
            *header,
            *(row(repo, s) for repo, s in pending),
            "",
            "</details>",
        ]
    return "\n".join(lines)


def main():
    with open(README, encoding="utf-8", newline="") as fh:
        content = fh.read()
    pattern = re.compile(f"{re.escape(START)}.*?{re.escape(END)}", re.S)
    if not pattern.search(content):
        sys.exit("footprint markers not found in README.md")
    stats = aggregate(collect_prs())
    stars = project_stars(stats)
    block = build_block(stats, stars)
    updated = pattern.sub(lambda _: f"{START}\n{block}\n{END}", content)
    outputs = [(README, content, update_star_slots(updated, stars))]
    for path in CASE_ASSETS:
        if path not in content:
            continue
        with open(path, encoding="utf-8", newline="") as fh:
            art = fh.read()
        outputs.append((path, art, update_star_slots(art, stars)))
    for path, before, after in outputs:
        if before != after:
            with open(path, "w", encoding="utf-8", newline="") as fh:
                fh.write(after)
            print(f"updated {path}")


if __name__ == "__main__":
    main()

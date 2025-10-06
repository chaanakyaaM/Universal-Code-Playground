#!/usr/bin/env python3
"""
tools/update_contributors.py

Generate CONTRIBUTORS.md using GitHub API contributors endpoint.
Requires: GITHUB_TOKEN, GITHUB_REPO
"""
import os
from github import Github

TOKEN = os.getenv("GITHUB_TOKEN")
REPO = os.getenv("GITHUB_REPO")
if not TOKEN or not REPO:
    raise SystemExit("Set GITHUB_TOKEN and GITHUB_REPO environment variables.")

g = Github(TOKEN)
repo = g.get_repo(REPO)

def main():
    contributors = repo.get_contributors()
    lines = ["# Contributors\n", "Thanks to everyone who contributed!\n"]
    for c in contributors:
        lines.append(f"- [{c.login}]({c.html_url}) — contributions: {c.contributions}")
    open("CONTRIBUTORS.md", "w", encoding="utf-8").write("\n".join(lines))
    print("Wrote CONTRIBUTORS.md")

if __name__ == "__main__":
    main()

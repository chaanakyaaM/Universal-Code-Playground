#!/usr/bin/env python3
"""
tools/create_gfi_issues.py

Create good-first-issue issues for combinations of topics and languages.

Requires environment variables:
  GITHUB_TOKEN (your PAT)
  GITHUB_REPO  (owner/repo)
Run: python tools/create_gfi_issues.py
"""
import os
from github import Github
from pathlib import Path

TOKEN = os.getenv("GITHUB_TOKEN")
REPO = os.getenv("GITHUB_REPO")

if not TOKEN or not REPO:
    raise SystemExit("Set GITHUB_TOKEN and GITHUB_REPO environment variables.")

g = Github(TOKEN)
repo = g.get_repo(REPO)

ROOT = Path("snippets")
default_langs = ["python","java","c","cpp","javascript"]

def main():
    topics = [d.name for d in ROOT.iterdir() if d.is_dir()]
    for topic in topics:
        for lang in default_langs:
            title = f"Add {topic} snippet in {lang} — e.g. fibonacci"
            body = (
                f"**Language:** {lang}\n"
                f"**Topic:** {topic}\n\n"
                "Add a single file to `snippets/{topic}/{lang}/` implementing one small problem\n"
                "(e.g. fibonacci). Acceptance: header comment, example usage, single file, no external libs.\n"
            ).format(topic=topic)
            # Avoid duplicates: check existing issues with same title
            existing = list(repo.get_issues(state="open", labels=["good first issue"]))
            if any(i.title == title for i in existing):
                print("Issue exists:", title)
                continue
            issue = repo.create_issue(title=title, body=body, labels=["good first issue", "help wanted"])
            print("Created issue:", issue.number, title)

if __name__ == "__main__":
    main()

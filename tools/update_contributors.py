#!/usr/bin/env python3
"""
tools/update_contributors.py

Generate CONTRIBUTORS.md using the GitHub API contributors endpoint.
Requires: GITHUB_TOKEN (must have 'repo' scope) and GITHUB_REPO (e.g., 'user/repo-name').
"""
import os
import sys
from github import Github
from github import GithubException

# --- Configuration and Initialization ---
TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("GITHUB_REPO")

# Check for mandatory environment variables
if not TOKEN or not REPO_NAME:
    print("FATAL: Set GITHUB_TOKEN and GITHUB_REPO environment variables.", file=sys.stderr)
    sys.exit(1)

# Initialize GitHub connection
try:
    g = Github(TOKEN)
    repo = g.get_repo(REPO_NAME)
except GithubException as e:
    print(f"ERROR: Failed to connect to GitHub or repository: {e.status} {e.data}", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"ERROR: An unknown error occurred during GitHub connection: {e}", file=sys.stderr)
    sys.exit(1)


def main():
    """
    Fetches the contributor list and writes it to CONTRIBUTORS.md.
    """
    try:
        # Fetch all contributors
        print(f"Fetching contributors for {REPO_NAME}...")
        contributors = repo.get_contributors()
        
        lines = ["# Contributors\n", "Thanks to everyone who contributed!\n"]

        for c in contributors:
            # Check if login is valid before appending
            if c.login:
                lines.append(f"- [{c.login}]({c.html_url}) — contributions: {c.contributions}")
            else:
                print(f"Warning: Skipping contributor with no login (ID: {c.id})")

        # Write the file
        with open("CONTRIBUTORS.md", "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
            
        print("Successfully wrote CONTRIBUTORS.md")

    except GithubException as e:
        print(f"ERROR: GitHub API call failed during fetch: {e.status} {e.data}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

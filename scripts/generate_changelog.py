#!/usr/bin/env python3
"""
Generate AI-powered release notes using GitHub Models API.
Reads commit messages and generates structured, meaningful changelog.
"""

import os
import sys
import json
import urllib.request
import urllib.error

def generate_changelog(commits: str, version: str) -> str:
    """Generate changelog using GitHub Models API (via GitHub token)."""

    github_token = os.environ.get('GITHUB_TOKEN')
    if not github_token:
        print("⚠️  GITHUB_TOKEN not set, falling back to simple changelog", file=sys.stderr)
        return commits

    try:
        prompt = f"""You are generating release notes for version {version} of the Purposely project.

Purposely is a Purpose-Driven Development Framework - a CLI tool for maintaining project purpose throughout development.

Here are the commit messages since the last release:

{commits}

Please generate concise, well-structured release notes in markdown format. Follow these guidelines:

1. Start with a brief summary (1-2 sentences) of what this release achieves
2. Group changes into categories:
   - ✨ New Features
   - 🐛 Bug Fixes
   - 📚 Documentation
   - 🔧 Internal/Refactoring
   - ⚡ Performance Improvements
3. Each item should be a single line explaining WHAT changed and WHY it matters to users
4. Skip technical details that don't affect users
5. Use clear, simple language
6. If there are breaking changes, add a "⚠️ Breaking Changes" section at the top

Keep it concise but informative. Focus on user impact."""

        # Use GitHub Models API with gpt-4o
        url = "https://models.inference.ai.azure.com/chat/completions"

        data = {
            "messages": [
                {"role": "system", "content": "You are a helpful assistant that generates clear, concise release notes."},
                {"role": "user", "content": prompt}
            ],
            "model": "gpt-4o",
            "temperature": 0.7,
            "max_tokens": 2000
        }

        req = urllib.request.Request(
            url,
            data=json.dumps(data).encode('utf-8'),
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {github_token}'
            }
        )

        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            changelog = result['choices'][0]['message']['content']
            return changelog

    except urllib.error.HTTPError as e:
        print(f"⚠️  HTTP Error {e.code}: {e.reason}", file=sys.stderr)
        print(f"Response: {e.read().decode('utf-8')}", file=sys.stderr)
        print("Falling back to simple changelog", file=sys.stderr)
        return commits
    except Exception as e:
        print(f"⚠️  Failed to generate AI changelog: {e}", file=sys.stderr)
        print("Falling back to simple changelog", file=sys.stderr)
        return commits

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: generate_changelog.py <version> <commits_file>", file=sys.stderr)
        sys.exit(1)

    version = sys.argv[1]
    commits_file = sys.argv[2]

    # Read commits from file
    with open(commits_file, 'r', encoding='utf-8') as f:
        commits = f.read()

    # Generate AI-powered changelog
    changelog = generate_changelog(commits, version)

    # Write to output file
    with open('changelog.txt', 'w', encoding='utf-8') as f:
        f.write(changelog)

    print("✅ Changelog generated successfully", file=sys.stderr)

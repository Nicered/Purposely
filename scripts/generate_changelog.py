#!/usr/bin/env python3
"""
Generate AI-powered release notes using Anthropic Claude API.
Reads commit messages and generates structured, meaningful changelog.
"""

import os
import sys
from anthropic import Anthropic

def generate_changelog(commits: str, version: str) -> str:
    """Generate changelog using Claude AI."""

    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print("⚠️  ANTHROPIC_API_KEY not set, falling back to simple changelog", file=sys.stderr)
        return commits

    try:
        client = Anthropic(api_key=api_key)

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

        message = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=2000,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        changelog = message.content[0].text
        return changelog

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

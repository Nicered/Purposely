#!/bin/bash
set -e

# Release script for Purposely
# Usage: ./scripts/release.sh [version]
# Example: ./scripts/release.sh 0.1.1

VERSION=$1

if [ -z "$VERSION" ]; then
    echo "❌ Error: Version is required"
    echo "Usage: ./scripts/release.sh <version>"
    echo "Example: ./scripts/release.sh 0.1.1"
    exit 1
fi

echo "🚀 Releasing version $VERSION"

# Check if on main branch
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "main" ]; then
    echo "⚠️  Warning: You are not on main branch (current: $CURRENT_BRANCH)"
    read -p "Continue anyway? [y/N] " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Check for uncommitted changes
if ! git diff-index --quiet HEAD --; then
    echo "❌ Error: You have uncommitted changes"
    git status --short
    exit 1
fi

echo "📝 Updating version in pyproject.toml..."
sed -i "s/^version = .*/version = \"$VERSION\"/" pyproject.toml

echo "📝 Committing version bump..."
git add pyproject.toml
git commit -m "Bump version to $VERSION"

echo "🏷️  Creating git tag v$VERSION..."
git tag -a "v$VERSION" -m "Release version $VERSION"

echo "📤 Pushing to GitHub..."
git push origin main
git push origin "v$VERSION"

echo ""
echo "✅ Release $VERSION initiated!"
echo ""
echo "📋 Next steps:"
echo "   1. GitHub Actions will automatically create a release"
echo "   2. Package will be built and attached to the release"
echo "   3. If PYPI_TOKEN is configured, package will be published to PyPI"
echo ""
echo "🔗 Check release status:"
echo "   https://github.com/nicered/purposely/actions"
echo "   https://github.com/nicered/purposely/releases"

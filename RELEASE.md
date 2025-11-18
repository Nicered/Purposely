# Release Process

This document describes how to create a new release for Purposely.

## Automated Release Workflow

Purposely uses GitHub Releases to trigger automated deployment. When you create a release on GitHub, the following happens automatically:

1. **Version Update**: `pyproject.toml` is updated with the release version
2. **Package Build**: Python package is built using Flit
3. **GitHub Release**: Release assets (`.whl` and `.tar.gz`) are uploaded
4. **PyPI Publish**: Package is published to PyPI (if `PYPI_API_TOKEN` is configured)

## How to Create a Release

### Method 1: GitHub Web UI (Recommended)

1. **Go to GitHub Releases**
   - Navigate to https://github.com/Nicered/Purposely/releases
   - Click "Draft a new release"

2. **Create Tag**
   - Click "Choose a tag"
   - Type new version (e.g., `v0.2.3`)
   - Click "Create new tag: v0.2.3 on publish"

3. **Fill Release Details**
   - **Release title**: `Release 0.2.3` or descriptive name
   - **Description**: Click "Generate release notes" or write custom notes

4. **Publish**
   - Click "Publish release"
   - GitHub Actions will automatically:
     - Update `pyproject.toml` version
     - Build and upload package
     - Publish to PyPI

### Method 2: GitHub CLI

```bash
# Create and push a tag
git tag -a v0.2.3 -m "Release v0.2.3 - Description"
git push origin v0.2.3

# Create release from tag
gh release create v0.2.3 \
  --title "Release 0.2.3" \
  --generate-notes
```

### Method 3: Manual (Not Recommended)

If you need to release manually:

```bash
# 1. Update version in pyproject.toml
sed -i 's/version = ".*"/version = "0.2.3"/' pyproject.toml

# 2. Commit and tag
git add pyproject.toml
git commit -m "chore: bump version to 0.2.3"
git tag -a v0.2.3 -m "Release v0.2.3"

# 3. Push
git push origin main
git push origin v0.2.3

# 4. Create GitHub Release (triggers workflow)
gh release create v0.2.3 --title "Release 0.2.3" --generate-notes
```

## Version Numbering

Follow [Semantic Versioning](https://semver.org/):

- **MAJOR** (1.0.0): Breaking changes
- **MINOR** (0.3.0): New features, backward compatible
- **PATCH** (0.2.3): Bug fixes, backward compatible

## PyPI Configuration

To enable automatic PyPI publishing:

1. **Get PyPI API Token**
   - Go to https://pypi.org/manage/account/token/
   - Create token with scope: "Entire account" or "Project: purposely"

2. **Add to GitHub Secrets**
   - Go to https://github.com/Nicered/Purposely/settings/secrets/actions
   - Click "New repository secret"
   - Name: `PYPI_API_TOKEN`
   - Value: `pypi-...` (your token)

3. **Test**
   - Create a release
   - Check Actions: https://github.com/Nicered/Purposely/actions
   - Verify on PyPI: https://pypi.org/project/purposely/

## Release Checklist

Before creating a release:

- [ ] All tests passing (`pytest`)
- [ ] Documentation updated
- [ ] CHANGELOG.md updated (optional)
- [ ] No uncommitted changes
- [ ] Version number follows semver

After creating a release:

- [ ] GitHub Release created successfully
- [ ] GitHub Actions workflow completed
- [ ] Package uploaded to PyPI
- [ ] Documentation deployed (if applicable)

## Workflow Files

- `.github/workflows/release-on-github.yml` - Main release workflow (GitHub Release trigger)
- `.github/workflows/release.yml` - Legacy workflow (tag trigger)
- `.github/workflows/publish.yml` - Separate publish workflow

## Common Issues

### Version Conflict

If `pyproject.toml` already has the release version:
- The workflow will skip the commit
- Package will still be built and published

### PyPI Upload Fails

Check:
1. `PYPI_API_TOKEN` secret is set correctly
2. Version doesn't already exist on PyPI
3. Package name is available

### GitHub Actions Permissions

If workflow fails with permission errors:
1. Go to Settings > Actions > General
2. Set "Workflow permissions" to "Read and write permissions"

## Example Release Notes

```markdown
## What's New in v0.2.3

### Features
- Add Mermaid diagram support in RULES.md
- Improve SEO configuration for GitHub Pages

### Bug Fixes
- Strengthen AI watermark rules for all document types

### Documentation
- Update release process documentation

**Full Changelog**: https://github.com/Nicered/Purposely/compare/v0.2.2...v0.2.3
```

## Testing

To test the release workflow without publishing:

1. Create a draft release
2. Check GitHub Actions logs
3. Delete draft if successful
4. Create actual release

## Rollback

If a release has issues:

1. **Delete GitHub Release**
   ```bash
   gh release delete v0.2.3
   ```

2. **Delete Tag**
   ```bash
   git tag -d v0.2.3
   git push origin :refs/tags/v0.2.3
   ```

3. **Yank from PyPI** (if published)
   - Go to https://pypi.org/project/purposely/
   - Find version > Options > Yank release

## Resources

- [GitHub Releases Documentation](https://docs.github.com/en/repositories/releasing-projects-on-github)
- [Semantic Versioning](https://semver.org/)
- [PyPI Publishing Guide](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/)

# GitHub Actions Setup Guide

This project uses GitHub Actions for automated testing, linting, and PyPI publishing.

## 🔧 Required Secrets

To enable automated PyPI publishing, you need to add the following secrets to your GitHub repository:

### 1. PyPI API Token

1. Go to [PyPI Account Settings](https://pypi.org/manage/account/)
2. Scroll to "API tokens"
3. Click "Add API token"
4. Enter token name (e.g., "github-actions-purposely")
5. Select scope: "Entire account" or specific project
6. Copy the generated token (starts with `pypi-`)

### 2. TestPyPI API Token (Optional)

1. Go to [TestPyPI Account Settings](https://test.pypi.org/manage/account/)
2. Follow the same steps as PyPI
3. Copy the generated token

### 3. Add Secrets to GitHub

1. Go to your repository on GitHub
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add the following secrets:

   - **Name**: `PYPI_API_TOKEN`
     **Value**: Your PyPI token (e.g., `pypi-...`)

   - **Name**: `TEST_PYPI_API_TOKEN`
     **Value**: Your TestPyPI token (e.g., `pypi-...`)

## 📋 Available Workflows

### 1. Tests (`test.yml`)

**Triggers:**
- Push to `main` or `develop` branches
- Pull requests to `main` or `develop` branches

**What it does:**
- Runs tests on Ubuntu, macOS, and Windows
- Tests Python 3.10, 3.11, and 3.12
- Generates coverage report
- Uploads coverage to Codecov (optional)

**Status badge:**
```markdown
![Tests](https://github.com/nicered/purposely/workflows/Tests/badge.svg)
```

### 2. Lint (`lint.yml`)

**Triggers:**
- Push to `main` or `develop` branches
- Pull requests to `main` or `develop` branches

**What it does:**
- Checks code with `ruff` (linter)
- Checks formatting with `black`
- Checks import sorting with `isort`

**Status badge:**
```markdown
![Lint](https://github.com/nicered/purposely/workflows/Lint/badge.svg)
```

### 3. Publish to PyPI (`publish.yml`)

**Triggers:**
- **Automatic**: When a new release is published on GitHub
- **Manual**: Via workflow dispatch

**What it does:**
- Builds the package
- Publishes to TestPyPI (manual trigger)
- Publishes to PyPI (release trigger)

## 🚀 How to Publish

### Automatic Publishing (Recommended)

1. Update version in `pyproject.toml`:
   ```toml
   version = "1.0.1"
   ```

2. Commit and push changes:
   ```bash
   git add pyproject.toml
   git commit -m "Bump version to 1.0.1"
   git push
   ```

3. Create a new release on GitHub:
   - Go to **Releases** → **Draft a new release**
   - Tag: `v1.0.1`
   - Release title: `v1.0.1`
   - Description: Changelog
   - Click **Publish release**

4. GitHub Actions will automatically:
   - Run tests
   - Build the package
   - Publish to PyPI

### Manual Publishing

1. Go to **Actions** tab on GitHub
2. Select **Publish to PyPI** workflow
3. Click **Run workflow**
4. Select branch
5. Click **Run workflow**

This will publish to **TestPyPI** for testing.

## 🎯 Workflow Status

You can monitor workflow runs in the **Actions** tab of your repository.

## 🔍 Troubleshooting

### Tests failing
- Check the test logs in Actions tab
- Run tests locally: `pytest tests/ -v`

### Publishing fails with "Invalid or non-existent authentication"
- Verify that `PYPI_API_TOKEN` secret is correctly set
- Regenerate the token if needed

### Package name already exists
- The package name `purposely` must be unique on PyPI
- Choose a different name in `pyproject.toml` if needed

## 📚 Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [PyPI Publishing Guide](https://packaging.python.org/tutorials/packaging-projects/)
- [Semantic Versioning](https://semver.org/)

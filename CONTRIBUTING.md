# Contributing to Purposely

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/nicered/purposely.git
cd purposely
```

2. Install dependencies:
```bash
pip install -e ".[dev]"
```

3. Run tests:
```bash
pytest
pytest --cov=purposely  # With coverage
```

## Release Process

**Note:** Only project maintainers can create releases.

### Steps to Release

1. **Update the version** in `pyproject.toml`:
```toml
version = "0.1.4"  # Bump to new version
```

2. **Commit the version bump**:
```bash
git add pyproject.toml
git commit -m "[CHORE] Bump version to 0.1.4"
```

3. **Create and push a git tag**:
```bash
git tag -a v0.1.4 -m "Release version 0.1.4"
git push origin main
git push origin v0.1.4
```

4. **GitHub Actions automatically**:
- Builds the package
- Creates a GitHub Release with auto-generated changelog
- Uploads wheel and source distribution
- Publishes to PyPI (if `PYPI_API_TOKEN` is configured)

### Manual PyPI Publish (if needed)

If automatic PyPI publishing fails:

```bash
pip install flit
flit build
flit publish
```

## GitHub Secrets Setup

To enable automated releases and publishing:

### PyPI Token (Required for Publishing)

1. Create a PyPI API token at https://pypi.org/manage/account/token/
2. Add it to GitHub repository secrets as `PYPI_API_TOKEN`
3. Go to: Repository Settings → Secrets and variables → Actions → New repository secret

### Automated Release Notes

The release workflow uses GitHub's native release notes generation feature.
This automatically creates changelog from commits and pull requests between releases.
No API keys or additional setup required.

## Version Numbering

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR** (1.0.0): Breaking changes
- **MINOR** (0.1.0): New features, backward compatible
- **PATCH** (0.0.1): Bug fixes, backward compatible

Examples:
- `0.1.0` → `0.1.1`: Bug fix
- `0.1.0` → `0.2.0`: New features
- `0.9.0` → `1.0.0`: First stable release

## Testing Before Release

Always run tests before releasing:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=purposely --cov-report=html

# Test specific functionality
pytest tests/test_upgrader.py -v
```

## Documentation Updates

When releasing:

1. Update `README.md` if needed
2. Update `docs/` if there are new features
3. Ensure all slash commands are documented

## Commit Message Format

All commit messages must follow this format:

```
[TAG] Brief description in English

- First change or detail
- Second change or detail
- Third change or detail
```

### Commit Tags

Use one of the following tags:

- `[FEATURE]` - New features or functionality
- `[FIX]` - Bug fixes
- `[REFACTOR]` - Code refactoring (no functional changes)
- `[DOCS]` - Documentation updates
- `[TEST]` - Test additions or modifications
- `[CHORE]` - Maintenance tasks (dependencies, configs, etc.)
- `[PERF]` - Performance improvements
- `[STYLE]` - Code style changes (formatting, naming, etc.)

### Examples

```
[FEATURE] Add automatic template upgrade system

- Implement Upgrader class for version management
- Add upgrade CLI command
- Create backup mechanism for user documents
```

```
[FIX] Resolve Windows encoding issue in test files

- Add explicit UTF-8 encoding to all file reads
- Update test files to handle cross-platform compatibility
```

```
[DOCS] Update installation instructions

- Add PyPI installation method
- Include troubleshooting section
- Fix broken links
```

### Rules

- Write commit messages in **English only**
- Use bullet points for multiple changes
- Keep the title under 72 characters
- Start bullet points with action verbs (Add, Fix, Update, Remove, etc.)
- Reference issues when applicable: `Fixes #123` or `Relates to #456`

## Branch Naming Convention

Follow this pattern for branch names:

- `feature/feature-name` - New features
- `fix/issue-description` - Bug fixes
- `refactor/component-name` - Code refactoring
- `docs/topic` - Documentation updates
- `test/test-name` - Test additions

### Examples

```bash
feature/ai-changelog-generation
fix/windows-encoding-error
refactor/upgrader-class
docs/contributing-guide
test/upgrade-workflow
```

### Rules

- Use lowercase letters
- Separate words with hyphens (kebab-case)
- Keep names descriptive but concise
- No special characters except hyphens

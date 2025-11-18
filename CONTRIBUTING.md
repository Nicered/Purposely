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

### Automated Release with GitHub Actions

When you're ready to release a new version:

1. **Update the version** in `pyproject.toml`:
```toml
version = "0.1.1"  # Bump to new version
```

2. **Use the release script**:
```bash
./scripts/release.sh 0.1.1
```

This will:
- Update version in `pyproject.toml`
- Commit the version bump
- Create a git tag (e.g., `v0.1.1`)
- Push to GitHub

3. **GitHub Actions automatically**:
- Builds the package
- Creates a GitHub Release with changelog
- Uploads wheel and source distribution
- Publishes to PyPI (if `PYPI_TOKEN` is configured)

### Manual Release (if needed)

If you need to release manually:

1. Build the package:
```bash
pip install flit
flit build
```

2. Create a git tag:
```bash
git tag -a v0.1.1 -m "Release version 0.1.1"
git push origin v0.1.1
```

3. Publish to PyPI:
```bash
flit publish
```

## PyPI Token Setup

To enable automatic PyPI publishing:

1. Create a PyPI API token at https://pypi.org/manage/account/token/
2. Add it to GitHub repository secrets as `PYPI_TOKEN`
3. Go to: Repository Settings → Secrets and variables → Actions → New repository secret

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

Use clear, descriptive commit messages:

```
Add feature for automatic template upgrades

- Implement Upgrader class
- Add upgrade CLI command
- Create GitHub Actions workflow
```

Good practices:
- Start with a verb (Add, Fix, Update, Remove)
- Use bullet points for details
- Reference issues if applicable (#123)

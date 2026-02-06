# {{ cookiecutter.project_name }} Development Guide

## Project Overview
{{ cookiecutter.project_short_description }}

This project follows modern Python best practices with a complete development toolchain including automated testing, documentation, and release management.

## Development Toolchain

### Package Manager: uv
This project uses **uv** exclusively (not pip). All commands use `uv run`:
```bash
uv sync                           # Install/sync dependencies
uv run pytest                     # Run tests
uv run pytest --cov={{ cookiecutter.project_slug }} --cov-report=term-missing  # Coverage
uv run ruff check .              # Lint
uv run ruff format .             # Format
```

### Code Quality
- **Ruff** configured with strict rules (pyupgrade, bugbear, isort, etc.)
- Line length: 88 characters
- Python {{ cookiecutter.python_version }}+ required
- Type annotations mandatory on all functions
- Docstrings in Google/NumPy style with Args/Returns/Example sections

### Testing Requirements
- **pytest** for testing with comprehensive coverage
- Use `conftest.py` for shared test configuration
- Test structure: `test_<function>_<scenario>` naming
- Coverage tracking configured in `pyproject.toml`

## Project Structure

```
{{ cookiecutter.project_slug }}/
├── src/{{ cookiecutter.project_slug }}/   # Main package code
│   ├── __init__.py                        # Package exports and version
│   └── ...                                # Additional modules
├── tests/                                 # Test suite
│   ├── conftest.py                        # Shared test configuration
│   └── test_*.py                          # Test modules
├── docs/                                  # Sphinx documentation
│   ├── conf.py                            # Sphinx configuration
│   └── *.md                               # Documentation pages
├── .github/workflows/                     # CI/CD pipelines
│   ├── test.yml                           # Test automation
│   ├── release.yml                        # Automated releases
│   └── docs.yml                           # Documentation builds
└── pyproject.toml                         # Project configuration
```

## Documentation (Sphinx + ReadTheDocs)
```bash
cd docs
uv run sphinx-build -b html . _build/html
```
- API docs auto-generated from docstrings (autodoc)
- Markdown support via myst-parser
- ReadTheDocs theme configured

## Release Process
- Uses **semantic-release** for automated versioning
- Conventional commits determine version bumps:
  - `feat:` → minor version
  - `fix:`, `perf:` → patch version
  - `BREAKING CHANGE:` → major version
- Version stored in `pyproject.toml`
- Automated through GitHub Actions on merge to main

## CI/CD Pipelines

### test.yml
- Runs on: push to main/dev, pull requests
- Matrix testing across OS (Ubuntu, Windows, macOS) and Python versions
- Executes: linting, formatting checks, tests with coverage
- Uploads coverage to Codecov

### release.yml
- Runs on: push to main branch
- Analyzes commits since last release
- Bumps version, creates release, publishes to PyPI
- Requires secrets: `PYPI_API_TOKEN`

### docs.yml
- Runs on: push/PR to main
- Builds Sphinx documentation
- Uploads artifacts for review
- Optional GitHub Pages deployment (commented out)

## Common Development Workflows

### Adding a New Feature
1. Create feature branch: `git checkout -b feat/feature-name`
2. Implement with tests
3. Commit with conventional commit: `feat: add new feature`
4. Push and create PR
5. CI runs tests automatically
6. After merge, release workflow publishes automatically

### Pre-commit Hooks
Install once: `uv run pre-commit install`
- Auto-runs ruff formatting and linting
- Catches issues before commit

### Running Tests Locally
```bash
uv run pytest                     # All tests
uv run pytest tests/test_foo.py   # Specific file
uv run pytest -k test_bar         # Specific test
uv run pytest -v                  # Verbose
```

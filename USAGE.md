# Using This Cookiecutter Template

## Installation

To use this template, you need cookiecutter installed:

```bash
pip install cookiecutter
```

## Creating a New Project

### From this directory:

```bash
cookiecutter .
```

### From GitHub (after you push):

```bash
cookiecutter gh:your-username/python-package-template
```

## What You'll Be Prompted For

The template will ask for these variables:

- **project_name**: Human-readable name (e.g., "My Awesome Package")
  - Used in documentation and README
  
- **project_slug**: Package name for PyPI/imports  
  - Auto-generated from project_name (lowercase, underscores)
  - This becomes your package name: `import project_slug`

- **project_short_description**: One-line description
  
- **author_name**: Your name

- **author_email**: Your email

- **github_username**: Your GitHub username
  - Used for repo URLs in documentation

- **python_version**: Python version (default: "3.12")
  - Sets minimum Python version requirement

- **project_version**: Initial version (default: "0.1.0")

- **open_source_license**: Choose from:
  - MIT
  - Apache-2.0
  - GPL-3.0
  - BSD-3-Clause

## After Generation

1. **Navigate to your new project:**
   ```bash
   cd your-project-slug
   ```

2. **Initialize git repository:**
   ```bash
   git init
   git add .
   git commit -m "feat: initial commit from template"
   ```

3. **Install dependencies:**
   ```bash
   # Install uv if you haven't already
   pip install uv
   
   # Install project dependencies
   uv sync
   ```

4. **Set up pre-commit hooks:**
   ```bash
   uv run pre-commit install
   ```

5. **Verify everything works:**
   ```bash
   # Run tests
   uv run pytest
   
   # Check linting
   uv run ruff check .
   
   # Build docs
   cd docs
   uv run sphinx-build -b html . _build/html
   ```

## GitHub Setup

1. **Create a new repository on GitHub** with the same name as your project_slug

2. **Push your code:**
   ```bash
   git remote add origin git@github.com:your-username/your-project-slug.git
   git push -u origin main
   ```

3. **Configure GitHub Secrets** (for CI/CD):
   - Go to Settings → Secrets and variables → Actions
   - Add these secrets:
     - `CODECOV_TOKEN`: Get from [codecov.io](https://codecov.io/) after signing up
     - `PYPI_API_TOKEN`: Get from [PyPI](https://pypi.org/manage/account/token/)

4. **Set up Codecov** (optional but recommended):
   - Sign up at [codecov.io](https://codecov.io/)
   - Add your repository
   - Copy the token to GitHub secrets

5. **Enable GitHub Pages** (optional, for docs):
   - Go to Settings → Pages
   - Source: GitHub Actions
   - Uncomment the deploy job in `.github/workflows/docs.yml`

## Project Structure

```
your-project-slug/
├── .github/
│   ├── workflows/              # CI/CD
│   │   ├── test.yml           # Runs tests, linting, coverage
│   │   ├── release.yml        # Automated releases to PyPI
│   │   └── docs.yml           # Documentation builds
│   └── copilot-instructions.md # AI assistant guidance
├── src/your_project_slug/      # Your package code
│   └── __init__.py
├── tests/                      # Tests
│   ├── conftest.py
│   └── test_core.py
├── docs/                       # Sphinx docs
│   ├── conf.py
│   ├── index.md
│   └── api/
├── pyproject.toml             # All configuration
├── README.md
├── CONTRIBUTING.md
├── LICENSE
└── CHANGELOG.md
```

## Development Workflow

### Adding Features

1. Create a feature branch:
   ```bash
   git checkout -b feat/my-feature
   ```

2. Write code and tests

3. Commit with conventional commit message:
   ```bash
   git commit -m "feat: add awesome new feature"
   ```

4. Push and create pull request

### Running Tests

```bash
# All tests
uv run pytest

# With coverage
uv run pytest --cov=your_project_slug --cov-report=term-missing

# Specific test
uv run pytest tests/test_core.py::test_version
```

### Code Quality

```bash
# Check linting
uv run ruff check .

# Auto-fix issues
uv run ruff check --fix .

# Format code
uv run ruff format .
```

### Building Documentation

```bash
cd docs
uv run sphinx-build -b html . _build/html
# Open _build/html/index.html
```

## Release Process

The template uses **semantic-release** for automated versioning:

1. **Commit types determine version bumps:**
   - `feat:` → minor version bump (0.1.0 → 0.2.0)
   - `fix:` → patch version bump (0.1.0 → 0.1.1)
   - `BREAKING CHANGE:` → major version bump (0.1.0 → 1.0.0)

2. **Merge to main** triggers release workflow:
   - Analyzes commits since last release
   - Bumps version in pyproject.toml
   - Generates CHANGELOG entry
   - Creates GitHub release
   - Publishes to PyPI

3. **Manual release** (if needed):
   ```bash
   uv run semantic-release version
   uv run semantic-release publish
   ```

## Customization Tips

### Adding Dependencies

Edit `pyproject.toml`:
```toml
dependencies = [
    "requests>=2.31.0",
    "numpy>=1.26.0",
]
```

Then sync:
```bash
uv sync
```

### Adding More Test Environments

Edit `.github/workflows/test.yml`:
```yaml
matrix:
  python-version: ["3.11", "3.12", "3.13"]
```

### Changing Documentation Theme

Edit `docs/conf.py`:
```python
html_theme = "sphinx_book_theme"  # or other theme
```

### Adding Pre-commit Hooks

Edit `.pre-commit-config.yaml` to add more hooks.

## Troubleshooting

**Tests fail after generation:**
- Ensure you've run `uv sync`
- Check that Python version matches requirement

**GitHub Actions fail:**
- Verify secrets are set (CODECOV_TOKEN, PYPI_API_TOKEN)
- Check workflow permissions in repo settings

**Import errors in tests:**
- Package may not be installed: run `uv sync`
- Check that paths in tests match generated structure

## Next Steps

1. Replace TODO comments in generated code
2. Update README with actual project details
3. Add your package functionality
4. Write comprehensive tests
5. Document your API
6. Make your first release!

## Getting Help

- Cookiecutter docs: https://cookiecutter.readthedocs.io/
- uv docs: https://github.com/astral-sh/uv
- Semantic release: https://python-semantic-release.readthedocs.io/

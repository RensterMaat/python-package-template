# Python Package Cookiecutter Template

A modern Python package template with complete development tooling and CI/CD pipelines.

## Features

This cookiecutter template provides a complete Python package structure with:

### Development Tools
- **uv** for fast, modern dependency management
- **ruff** for linting and formatting
- **pre-commit** hooks for code quality
- **pytest** with coverage reporting
- **mypy** ready for type checking

### Documentation
- **Sphinx** with ReadTheDocs theme
- **autodoc** for API documentation generation
- **myst-parser** for markdown support
- Automated documentation builds in CI

### CI/CD Pipelines (GitHub Actions)
- **test.yml**: Multi-OS, multi-Python version testing with coverage
- **release.yml**: Automated semantic versioning and PyPI publishing
- **docs.yml**: Documentation building and optional GitHub Pages deployment

### Release Management
- **python-semantic-release** for automated versioning
- Conventional Commits for version bumps
- Automated CHANGELOG generation
- PyPI publishing workflow

## Quick Start

### Prerequisites
- Python {{ cookiecutter.python_version }}+
- [cookiecutter](https://cookiecutter.readthedocs.io/): `pip install cookiecutter`
- [uv](https://github.com/astral-sh/uv): For the generated project

### Create a New Project

```bash
cookiecutter https://github.com/RensterMaat/python-package-template
# Or from local:
cookiecutter /path/to/this/template
```

You'll be prompted for:
- `project_name`: Human-readable name (e.g., "My Awesome Package")
- `project_slug`: Package name for PyPI/imports (auto-generated from project_name)
- `project_short_description`: One-line description
- `author_name`: Your name
- `author_email`: Your email
- `github_username`: Your GitHub username
- `python_version`: Python version (default: 3.12)
- `project_version`: Initial version (default: 0.1.0)
- `open_source_license`: License type (MIT, Apache-2.0, GPL-3.0, BSD-3-Clause)

### After Generation

```bash
cd your-project-slug

# Install dependencies
uv sync

# Set up pre-commit hooks
uv run pre-commit install

# Run tests
uv run pytest

# Build documentation
cd docs
uv run sphinx-build -b html . _build/html
```

## Project Structure

The generated project includes:

```
your-project/
├── .github/
│   ├── workflows/           # CI/CD pipelines
│   │   ├── test.yml        # Testing workflow
│   │   ├── release.yml     # Release workflow
│   │   └── docs.yml        # Documentation workflow
│   └── copilot-instructions.md  # AI coding assistant guidance
├── docs/                    # Sphinx documentation
│   ├── conf.py             # Sphinx configuration
│   ├── index.md            # Documentation home
│   ├── examples.md         # Usage examples
│   └── api/                # API reference (auto-generated)
├── src/your_project/       # Main package
│   └── __init__.py         # Package initialization
├── tests/                   # Test suite
│   ├── conftest.py         # Pytest configuration
│   └── test_core.py        # Example tests
├── pyproject.toml          # Project configuration
├── README.md               # Project readme
├── CONTRIBUTING.md         # Contribution guidelines
├── LICENSE                 # License file
└── CHANGELOG.md            # Version history
```

## Configured Tools

### pyproject.toml
Complete configuration for:
- Hatchling build system
- Ruff linting and formatting
- Pytest and coverage
- Semantic release
- Project metadata

### GitHub Actions
Pre-configured workflows that:
- Run tests on every push/PR
- Check code quality (ruff)
- Generate coverage reports (Codecov)
- Automatically release on main branch merges
- Build and deploy documentation

### Pre-commit Hooks
Automatically run on every commit:
- Ruff formatting and linting
- Trailing whitespace removal
- YAML validation
- Large file prevention

## Customization

### Required Setup
After generating your project, configure these secrets in GitHub:

1. **CODECOV_TOKEN**: Get from [codecov.io](https://codecov.io/) after creating project
2. **PYPI_API_TOKEN**: Get from [PyPI](https://pypi.org/manage/account/token/)

### Optional Configuration

**Enable GitHub Pages for docs:**
Uncomment the `deploy` job in `.github/workflows/docs.yml`

**Adjust Python version matrix:**
Edit `.github/workflows/test.yml` to test multiple Python versions

**Add more dependencies:**
Edit `pyproject.toml` and run `uv sync`

## Development Workflow

This template encourages:
1. **Conventional Commits**: Use `feat:`, `fix:`, `docs:`, etc.
2. **Test-Driven Development**: Write tests, keep coverage high
3. **Documentation-First**: Update docs alongside code
4. **Automated Releases**: Let semantic-release handle versioning

## License

This template is provided under {{ cookiecutter.open_source_license }} license.

## Credits

Created from the pmpl project structure by {{ cookiecutter.author_name }}.

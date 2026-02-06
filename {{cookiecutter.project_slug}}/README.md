# {{ cookiecutter.project_name }}

[![Tests](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/workflows/Tests/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/test.yml)
[![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/badge/?version=latest)](https://{{ cookiecutter.project_slug }}.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
[![PyPI version](https://badge.fury.io/py/{{ cookiecutter.project_slug }}.svg)](https://badge.fury.io/py/{{ cookiecutter.project_slug }})
[![Python {{ cookiecutter.python_version }}+](https://img.shields.io/badge/python-{{ cookiecutter.python_version }}+-blue.svg)](https://www.python.org/downloads/)
[![License: {{ cookiecutter.open_source_license }}](https://img.shields.io/badge/License-{{ cookiecutter.open_source_license }}-yellow.svg)](https://opensource.org/licenses/{{ cookiecutter.open_source_license }})

{{ cookiecutter.project_short_description }}

## Features

- TODO: List your project's key features here

## Installation

```bash
pip install {{ cookiecutter.project_slug }}
```

Or with uv:
```bash
uv add {{ cookiecutter.project_slug }}
```

## Quick Start

```python
import {{ cookiecutter.project_slug }}

# TODO: Add usage examples
```

## Documentation

📚 **Full documentation is available at [{{ cookiecutter.project_slug }}.readthedocs.io](https://{{ cookiecutter.project_slug }}.readthedocs.io/)**

### Build Locally

You can build the documentation locally:

```bash
cd docs
uv run sphinx-build -b html . _build/html
```

Then open `docs/_build/html/index.html` in your browser.

## Development

This project uses:
- [uv](https://github.com/astral-sh/uv) for dependency management
- [ruff](https://github.com/astral-sh/ruff) for linting and formatting
- [pre-commit](https://pre-commit.com/) for code quality checks
- [pytest](https://pytest.org/) for testing with coverage
- [sphinx](https://www.sphinx-doc.org/) with ReadTheDocs theme for documentation
- [semantic-release](https://python-semantic-release.readthedocs.io/) for automated versioning

```bash
# Clone the repository
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}

# Install with dev dependencies
uv sync

# Install pre-commit hooks
uv run pre-commit install

# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov={{ cookiecutter.project_slug }} --cov-report=term-missing

# Lint and format
uv run ruff check .
uv run ruff format .

# Build documentation
cd docs
uv run sphinx-build -b html . _build/html
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

{{ cookiecutter.open_source_license }} License - see [LICENSE](LICENSE) file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

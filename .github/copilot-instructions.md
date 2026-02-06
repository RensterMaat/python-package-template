# Python Package Template - Cookiecutter Development Guide

## What This Is

This is a **cookiecutter template repository** that generates Python package projects. It's NOT a regular Python package itself - it's a meta-project that creates other projects.

**Key Architecture:**
- Root level: Template configuration and documentation ([cookiecutter.json](cookiecutter.json), [README.md](README.md), [USAGE.md](USAGE.md))
- `{{cookiecutter.project_slug}}/`: The actual template that gets rendered when users run `cookiecutter`
- Jinja2 templating: Variables like `{{ cookiecutter.project_name }}` get replaced during generation

## Critical Workflows

### Testing the Template Locally
```bash
# Generate a test project from the template
cookiecutter . --output-dir ../test-output

# The post_gen_project hook automatically:
# - Runs uv sync to install dependencies
# - Installs pre-commit hooks
# - Initializes git and creates initial commit

# Navigate to generated project and verify it works
cd ../test-output/your-project-slug
uv run pytest
```

### Modifying Template Files
**DO NOT** edit files as if they were a regular Python project. When editing files in `{{cookiecutter.project_slug}}/`:
- Preserve all Jinja2 variables: `{{ cookiecutter.* }}`
- Test changes by generating a project (see above)
- Variables are defined in [cookiecutter.json](cookiecutter.json)

### Adding New Template Variables
1. Add variable to [cookiecutter.json](cookiecutter.json)
2. Use in template files as `{{ cookiecutter.your_variable }}`
3. Document in [README.md](README.md) and [USAGE.md](USAGE.md)

### Post-Generation Hook
[hooks/post_gen_project.py](hooks/post_gen_project.py) runs automatically after project generation to:
- Install dependencies via `uv sync`
- Set up pre-commit hooks
- Initialize git repository with initial commit
- Gracefully handles missing tools (uv, git) with helpful messages

## Template Architecture

### Two-Level Structure
- **Template Root** (`/`): Documentation about the template itself
- **Generated Project** (`{{cookiecutter.project_slug}}/`): What users get after running cookiecutter

### Key Template Patterns
- Dynamic package naming: `src/{{cookiecutter.project_slug}}/` becomes `src/my_package/` after generation
- Conditional rendering: Some files use Jinja2 conditionals (though minimal in this template)
- Copy-without-render: `_copy_without_render` in [cookiecutter.json](cookiecutter.json) lists files that bypass Jinja2 processing

## Generated Project Features

The template creates projects with this opinionated stack:
- **uv**: Dependency management (all commands use `uv run`, never plain `python` or `pip`)
- **ruff**: Linting and formatting (strict configuration in [pyproject.toml]({{cookiecutter.project_slug}}/pyproject.toml))
- **pytest**: Testing with coverage tracking
- **Sphinx**: Documentation with ReadTheDocs theme, autodoc, and myst-parser
- **semantic-release**: Automated versioning via conventional commits
- **GitHub Actions**: CI/CD pipelines ([test.yml]({{cookiecutter.project_slug}}/.github/workflows/test.yml), [release.yml]({{cookiecutter.project_slug}}/.github/workflows/release.yml), [docs.yml]({{cookiecutter.project_slug}}/.github/workflows/docs.yml))

### Generated Project Conventions (for the projects this template creates)
- Conventional commits: `feat:`, `fix:`, `docs:`, etc.
- Type hints required on all functions
- Google/NumPy style docstrings
- 100% test coverage goal
- Line length: 88 characters
- Python 3.12+ by default

## Common Development Tasks

### Adding Features to Generated Projects
When adding new boilerplate to what users get:
1. Edit files in `{{cookiecutter.project_slug}}/`
2. Use cookiecutter variables where appropriate
3. Test by generating a project
4. Update [generated project's copilot-instructions.md]({{cookiecutter.project_slug}}/.github/copilot-instructions.md) if it affects workflows

### Updating GitHub Actions Workflows
Workflows in `{{cookiecutter.project_slug}}/.github/workflows/` are templates:
- Keep `{{ cookiecutter.project_slug }}` in paths
- Test by generating a project and running workflows locally

### Modifying pyproject.toml
[pyproject.toml]({{cookiecutter.project_slug}}/pyproject.toml) is heavily templated:
- All project metadata uses cookiecutter variables
- Semantic-release configuration is pre-configured
- Ruff rules are strict and opinionated

## Template Improvements & Fine-Tuning

### Current Integration Points to Consider

**PyPI Trusted Publishing (Already Configured):**
- [release.yml]({{cookiecutter.project_slug}}/.github/workflows/release.yml) uses `id-token: write` for OIDC authentication
- No need for `PYPI_API_TOKEN` if using Trusted Publishers (recommended for new projects)
- To enable: Add GitHub Actions as trusted publisher in PyPI project settings

**Pre-commit Configuration:**
- Currently documented but not included in template files
- Consider adding `.pre-commit-config.yaml` template with ruff hooks

**GitHub Branch Protection:**
- Not automated - users must manually configure
- Could document recommended settings (require PR reviews, status checks)

**Additional Cookiecutter Variables to Consider:**
- `include_cli` - Add typer/click CLI boilerplate
- `include_github_pages` - Auto-uncomment docs deployment
- `use_trusted_publisher` - Toggle between API token vs OIDC in release.yml
- `min_coverage_percent` - Configurable coverage threshold

**Documentation Enhancements:**
- Add `docs/tutorials/` directory structure
- Include example notebook in `docs/examples/`
- Add logo/favicon placeholders

### Testing New Features
Always test template changes end-to-end:
```bash
# Generate test project
cookiecutter . --output-dir ../test-output

# Verify generated project
cd ../test-output/test-project
uv sync
uv run pytest
uv run ruff check .
cd docs && uv run sphinx-build -b html . _build/html
```

## File Navigation

**Template Configuration:**
- [cookiecutter.json](cookiecutter.json) - Variable definitions and defaults
- [README.md](README.md) - Template documentation (for template users)
- [USAGE.md](USAGE.md) - How to use the template

**Generated Project Structure:**
- [{{cookiecutter.project_slug}}/pyproject.toml]({{cookiecutter.project_slug}}/pyproject.toml) - Project config template
- [{{cookiecutter.project_slug}}/src/]({{cookiecutter.project_slug}}/src/) - Source code directory
- [{{cookiecutter.project_slug}}/tests/]({{cookiecutter.project_slug}}/tests/) - Test suite template
- [{{cookiecutter.project_slug}}/docs/]({{cookiecutter.project_slug}}/docs/) - Sphinx docs template
- [{{cookiecutter.project_slug}}/.github/]({{cookiecutter.project_slug}}/.github/) - CI/CD pipelines

## Post-Generation Setup (What Users Need to Do)

After generating a project from this template, users must configure external services:

### Required: PyPI Publishing
1. Create PyPI account at [pypi.org](https://pypi.org)
2. Generate API token: Account Settings → API tokens → "Add API token"
3. Add to GitHub Secrets: `Settings → Secrets → Actions → New repository secret`
   - Name: `PYPI_API_TOKEN`
   - Value: `pypi-...` (the generated token)
4. First release happens automatically on first `feat:` or `fix:` commit to main

### Optional: Code Coverage (Codecov)
1. Sign up at [codecov.io](https://codecov.io/) (free for public repos)
2. Add repository and copy upload token
3. Add to GitHub Secrets as `CODECOV_TOKEN`
4. Note: [test.yml]({{cookiecutter.project_slug}}/.github/workflows/test.yml) sets `fail_ci_if_error: false` so it's truly optional

### Optional: ReadTheDocs
1. Sign up at [readthedocs.org](https://readthedocs.org/)
2. Import repository (auto-detects Sphinx config)
3. Build triggers automatically on push to main
4. No secrets needed - badges in README will work automatically
5. Alternative: Use GitHub Pages by uncommenting deploy job in [docs.yml]({{cookiecutter.project_slug}}/.github/workflows/docs.yml)

### Optional: GitHub Pages for Docs
1. Go to repo `Settings → Pages`
2. Set Source to "GitHub Actions"
3. Uncomment the `deploy` job in [docs.yml]({{cookiecutter.project_slug}}/.github/workflows/docs.yml)
4. Docs will be at `https://username.github.io/project-slug/`

## What Makes This Template Unique

- **uv-first**: Uses uv exclusively, not pip or poetry
- **Fully automated releases**: Semantic-release + conventional commits handle versioning
- **Multi-OS CI**: Tests on Ubuntu, Windows, and macOS
- **Documentation-ready**: Sphinx + autodoc + ReadTheDocs pre-configured
- **Modern tooling**: Ruff replaces pylint/black/isort/pyupgrade in one tool
- **Zero manual versioning**: Version bumps are automated from commit messages
- **Trusted publishing**: Uses PyPI's [Trusted Publishers](https://docs.pypi.org/trusted-publishers/) via OIDC (no long-lived tokens in workflows)

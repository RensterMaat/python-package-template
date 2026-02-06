#!/usr/bin/env python3
"""Post-generation hook for cookiecutter template.

This script runs automatically after the project is generated to set up the
development environment.
"""

import shutil
import subprocess
import sys
from pathlib import Path


def run_command(cmd: list[str], check: bool = True) -> bool:
    """Run a command and return success status."""
    try:
        result = subprocess.run(
            cmd,
            check=check,
            capture_output=True,
            text=True,
        )
        if result.stdout:
            print(result.stdout)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"Error running {' '.join(cmd)}: {e.stderr}", file=sys.stderr)
        return False
    except FileNotFoundError:
        return False


def main() -> None:
    """Execute post-generation setup steps."""
    print("🚀 Setting up your Python package...")
    print()

    # Check if uv is installed
    if not shutil.which("uv"):
        print("⚠️  uv is not installed!")
        print("   Install it from: https://github.com/astral-sh/uv")
        print("   Then run manually:")
        print("   - uv sync")
        print("   - uv run pre-commit install")
        print()
    else:
        # Initialize uv environment
        print("📦 Installing dependencies with uv...")
        if run_command(["uv", "sync"], check=False):
            print("✅ Dependencies installed")
        else:
            print("⚠️  Failed to install dependencies")
        print()

        # Install pre-commit hooks
        print("🔧 Installing pre-commit hooks...")
        if run_command(["uv", "run", "pre-commit", "install"], check=False):
            print("✅ Pre-commit hooks installed")
        else:
            print("⚠️  Failed to install pre-commit hooks")
        print()

    # Initialize git repository
    print("📚 Initializing git repository...")
    if run_command(["git", "init"], check=False):
        print("✅ Git repository initialized")
        
        # Make initial commit
        print("📝 Creating initial commit...")
        run_command(["git", "add", "."], check=False)
        run_command(
            ["git", "commit", "-m", "feat: initial commit from cookiecutter template"],
            check=False,
        )
        print("✅ Initial commit created")
    else:
        print("⚠️  Failed to initialize git (may already exist)")
    print()

    # Success message
    print("=" * 60)
    print("✨ Project setup complete!")
    print("=" * 60)
    print()
    print("📍 Next steps:")
    print()
    print("   1. Review the generated files")
    print("   2. Update README.md with your project details")
    print("   3. Create a GitHub repository:")
    print("      git remote add origin git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git")
    print("      git push -u origin main")
    print()
    print("   4. Configure GitHub secrets for CI/CD:")
    print("      - PYPI_API_TOKEN (required for releases)")
    print("      - CODECOV_TOKEN (optional for coverage)")
    print()
    print("   5. Start developing!")
    print("      uv run pytest              # Run tests")
    print("      uv run ruff check .        # Lint code")
    print("      cd docs && uv run sphinx-build -b html . _build/html  # Build docs")
    print()
    print("📖 See .github/copilot-instructions.md for development guide")
    print()


if __name__ == "__main__":
    main()

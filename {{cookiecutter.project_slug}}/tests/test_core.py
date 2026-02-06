"""Tests for {{ cookiecutter.project_name }}."""

import {{ cookiecutter.project_slug }}


def test_version():
    """Test that version is defined."""
    assert {{ cookiecutter.project_slug }}.__version__ == "{{ cookiecutter.project_version }}"


def test_import():
    """Test that package can be imported."""
    assert {{ cookiecutter.project_slug }} is not None

"""
Tests for TemplateRenderer.
"""

import pytest
from pathlib import Path
from purposely.core.renderer import TemplateRenderer


def test_renderer_loads_english_translations():
    """Test that renderer loads English translations correctly."""
    renderer = TemplateRenderer('en')
    assert renderer.lang == 'en'
    assert renderer.translations is not None
    assert 'meta' in renderer.translations
    assert renderer.translations['meta']['language'] == 'en'


def test_renderer_loads_korean_translations():
    """Test that renderer loads Korean translations correctly."""
    renderer = TemplateRenderer('ko')
    assert renderer.lang == 'ko'
    assert renderer.translations is not None
    assert 'meta' in renderer.translations
    assert renderer.translations['meta']['language'] == 'ko'


def test_renderer_renders_global_purpose():
    """Test that GLOBAL_PURPOSE template renders."""
    renderer = TemplateRenderer('en')
    output = renderer.render('GLOBAL_PURPOSE.md')

    assert 'GLOBAL_PURPOSE' in output
    assert 'Project Core Purpose & Vision' in output
    assert 'Project Overview' in output


def test_renderer_renders_spec():
    """Test that SPEC template renders with variables."""
    renderer = TemplateRenderer('en')
    output = renderer.render('00_SPEC.md', phase_number='01', phase_name='Foundation')

    assert 'Phase 01 - Foundation' in output
    assert 'Phase Specification' in output


def test_now_filter_works():
    """Test that the now filter produces valid dates."""
    renderer = TemplateRenderer('en')
    output = renderer.render('GLOBAL_PURPOSE.md')

    # Should contain a date in YYYY-MM-DD format
    import re
    assert re.search(r'\d{4}-\d{2}-\d{2}', output) is not None


def test_invalid_language_raises_error():
    """Test that invalid language raises error."""
    with pytest.raises(FileNotFoundError):
        TemplateRenderer('invalid')


def test_invalid_template_raises_error():
    """Test that invalid template raises error."""
    renderer = TemplateRenderer('en')
    with pytest.raises(FileNotFoundError):
        renderer.render('NONEXISTENT.md')

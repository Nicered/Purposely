"""
Tests for DocumentCreator functionality.
"""

import pytest
import json
from pathlib import Path
from purposely.core.creator import DocumentCreator
import click


def test_creator_requires_purposely_project(tmp_path):
    """Test that DocumentCreator requires a Purposely project."""
    with pytest.raises(click.ClickException, match="Not a Purposely project"):
        DocumentCreator(project_root=tmp_path)


def test_creator_loads_configuration(tmp_path):
    """Test that DocumentCreator loads configuration correctly."""
    # Create .purposely/config.json
    config_dir = tmp_path / '.purposely'
    config_dir.mkdir()
    config_path = config_dir / 'config.json'
    test_version = '0.0.2'
    config_path.write_text(json.dumps({'language': 'ko', 'version': test_version}))

    # Create docs directory
    (tmp_path / 'docs').mkdir()

    creator = DocumentCreator(project_root=tmp_path)
    assert creator.lang == 'ko'
    assert creator.config['version'] == test_version


def test_create_global_purpose(tmp_path):
    """Test creating GLOBAL_PURPOSE.md."""
    # Setup project
    config_dir = tmp_path / '.purposely'
    config_dir.mkdir()
    (config_dir / 'config.json').write_text(json.dumps({'language': 'en', 'version': '0.0.2'}))
    docs_dir = tmp_path / 'docs'
    docs_dir.mkdir()

    creator = DocumentCreator(project_root=tmp_path)
    output_path = creator.create_global_purpose()

    assert output_path.exists()
    assert output_path == docs_dir / 'GLOBAL_PURPOSE.md'
    content = output_path.read_text(encoding='utf-8')
    assert 'GLOBAL_PURPOSE' in content


def test_create_global_purpose_fails_if_exists(tmp_path):
    """Test that creating GLOBAL_PURPOSE fails if file exists without force."""
    # Setup project
    config_dir = tmp_path / '.purposely'
    config_dir.mkdir()
    (config_dir / 'config.json').write_text(json.dumps({'language': 'en', 'version': '0.0.2'}))
    docs_dir = tmp_path / 'docs'
    docs_dir.mkdir()

    # Create file first
    (docs_dir / 'GLOBAL_PURPOSE.md').write_text("existing content")

    creator = DocumentCreator(project_root=tmp_path)

    with pytest.raises(click.ClickException, match="already exists"):
        creator.create_global_purpose(force=False)


def test_create_global_purpose_force_overwrites(tmp_path):
    """Test that --force overwrites existing GLOBAL_PURPOSE."""
    # Setup project
    config_dir = tmp_path / '.purposely'
    config_dir.mkdir()
    (config_dir / 'config.json').write_text(json.dumps({'language': 'en', 'version': '0.0.2'}))
    docs_dir = tmp_path / 'docs'
    docs_dir.mkdir()

    # Create file first
    existing_file = docs_dir / 'GLOBAL_PURPOSE.md'
    existing_file.write_text("existing content")

    creator = DocumentCreator(project_root=tmp_path)
    output_path = creator.create_global_purpose(force=True)

    assert output_path.exists()
    content = output_path.read_text(encoding='utf-8')
    assert content != "existing content"
    assert 'GLOBAL_PURPOSE' in content


def test_create_spec(tmp_path):
    """Test creating phase SPEC document."""
    # Setup project
    config_dir = tmp_path / '.purposely'
    config_dir.mkdir()
    config_path = config_dir / 'config.json'
    config_path.write_text(json.dumps({'language': 'en', 'version': '0.0.2', 'current_phase': None}))
    docs_dir = tmp_path / 'docs'
    docs_dir.mkdir()

    creator = DocumentCreator(project_root=tmp_path)
    output_path = creator.create_spec(phase='01')

    assert output_path.exists()
    assert output_path == docs_dir / 'phase-01' / '00_SPEC.md'
    content = output_path.read_text(encoding='utf-8')
    assert 'SPEC' in content or 'Phase' in content

    # Check that current_phase was updated
    updated_config = json.loads(config_path.read_text())
    assert updated_config['current_phase'] == '01'


def test_create_research(tmp_path):
    """Test creating research document."""
    # Setup project with phase
    config_dir = tmp_path / '.purposely'
    config_dir.mkdir()
    (config_dir / 'config.json').write_text(json.dumps({'language': 'en', 'version': '0.0.2'}))
    phase_dir = tmp_path / 'docs' / 'phase-01'
    phase_dir.mkdir(parents=True)

    creator = DocumentCreator(project_root=tmp_path)
    output_path = creator.create_research(phase='01', number='01', title='API Research')

    assert output_path.exists()
    assert output_path.name == '01_01_RESEARCH_API_Research.md'
    content = output_path.read_text(encoding='utf-8')
    assert 'Research' in content or 'RESEARCH' in content


def test_create_research_fails_if_phase_missing(tmp_path):
    """Test that creating research fails if phase doesn't exist."""
    # Setup project without phase
    config_dir = tmp_path / '.purposely'
    config_dir.mkdir()
    (config_dir / 'config.json').write_text(json.dumps({'language': 'en', 'version': '0.0.2'}))
    (tmp_path / 'docs').mkdir()

    creator = DocumentCreator(project_root=tmp_path)

    with pytest.raises(click.ClickException, match="Phase directory does not exist"):
        creator.create_research(phase='01', number='01', title='Test')


def test_create_plan(tmp_path):
    """Test creating implementation plan."""
    # Setup project with phase
    config_dir = tmp_path / '.purposely'
    config_dir.mkdir()
    (config_dir / 'config.json').write_text(json.dumps({'language': 'en', 'version': '0.0.2'}))
    phase_dir = tmp_path / 'docs' / 'phase-01'
    phase_dir.mkdir(parents=True)

    creator = DocumentCreator(project_root=tmp_path)
    output_path = creator.create_plan(phase='01')

    assert output_path.exists()
    assert output_path == phase_dir / '03_PLAN.md'
    content = output_path.read_text(encoding='utf-8')
    assert 'Plan' in content or 'PLAN' in content


def test_create_implementation(tmp_path):
    """Test creating implementation log."""
    # Setup project with phase
    config_dir = tmp_path / '.purposely'
    config_dir.mkdir()
    (config_dir / 'config.json').write_text(json.dumps({'language': 'en', 'version': '0.0.2'}))
    phase_dir = tmp_path / 'docs' / 'phase-01'
    phase_dir.mkdir(parents=True)

    creator = DocumentCreator(project_root=tmp_path)
    output_path = creator.create_implementation(phase='01')

    assert output_path.exists()
    assert output_path == phase_dir / '04_IMPLEMENTATION.md'
    content = output_path.read_text(encoding='utf-8')
    assert 'Implementation' in content or 'IMPLEMENTATION' in content

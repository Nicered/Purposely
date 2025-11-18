"""
Tests for Upgrader functionality.
"""

import pytest
import json
from pathlib import Path
from purposely.core.upgrader import Upgrader
from purposely import __version__
import click


def test_upgrade_requires_purposely_project(tmp_path):
    """Test that upgrade requires an existing Purposely project."""
    upgrader = Upgrader()
    upgrader.project_root = tmp_path
    upgrader.config_path = tmp_path / '.purposely' / 'config.json'

    # Should return False without error when no project exists
    result = upgrader._check_project_exists()
    assert result is False


def test_upgrade_detects_current_version(tmp_path):
    """Test that upgrade correctly reads current version."""
    # Create .purposely/config.json with old version
    config_dir = tmp_path / '.purposely'
    config_dir.mkdir()
    config_path = config_dir / 'config.json'
    config_path.write_text(json.dumps({'version': '0.0.1', 'language': 'en'}))

    upgrader = Upgrader()
    upgrader.project_root = tmp_path
    upgrader.config_path = config_path

    current_version = upgrader._get_current_version()
    assert current_version == '0.0.1'


def test_upgrade_skips_when_already_latest(tmp_path):
    """Test that upgrade skips when already at latest version."""
    # Create .purposely/config.json with current version
    config_dir = tmp_path / '.purposely'
    config_dir.mkdir()
    config_path = config_dir / 'config.json'
    config_path.write_text(json.dumps({'version': __version__, 'language': 'en'}))

    upgrader = Upgrader(force=False)
    upgrader.project_root = tmp_path
    upgrader.config_path = config_path

    needs_upgrade = upgrader._needs_upgrade(__version__)
    assert needs_upgrade is False


def test_upgrade_with_force_flag(tmp_path):
    """Test that force flag bypasses version check."""
    upgrader = Upgrader(force=True)
    upgrader.project_root = tmp_path
    upgrader.config_path = tmp_path / '.purposely' / 'config.json'

    needs_upgrade = upgrader._needs_upgrade(__version__)
    assert needs_upgrade is True


def test_upgrade_updates_config_version(tmp_path):
    """Test that upgrade updates config.json version."""
    # Create .purposely/config.json with old version
    config_dir = tmp_path / '.purposely'
    config_dir.mkdir()
    config_path = config_dir / 'config.json'
    old_config = {
        'version': '0.0.1',
        'language': 'ko',
        'current_phase': '01'
    }
    config_path.write_text(json.dumps(old_config, indent=2))

    upgrader = Upgrader()
    upgrader.project_root = tmp_path
    upgrader.config_path = config_path

    upgrader._update_config_version()

    # Read updated config
    with open(config_path) as f:
        new_config = json.load(f)

    # Version should be updated
    assert new_config['version'] == __version__
    # Other fields should be preserved
    assert new_config['language'] == 'ko'
    assert new_config['current_phase'] == '01'


def test_upgrade_creates_backup(tmp_path):
    """Test that upgrade creates backup of .claude folder."""
    # Create existing .claude folder
    claude_dir = tmp_path / '.claude'
    claude_dir.mkdir()
    (claude_dir / 'instructions.md').write_text('old instructions')
    commands_dir = claude_dir / 'commands'
    commands_dir.mkdir()
    (commands_dir / 'test.md').write_text('old command')

    # Create minimal config
    config_dir = tmp_path / '.purposely'
    config_dir.mkdir()
    (config_dir / 'config.json').write_text(json.dumps({'version': '0.0.1', 'language': 'en'}))

    upgrader = Upgrader()
    upgrader.project_root = tmp_path
    upgrader.config_path = tmp_path / '.purposely' / 'config.json'
    upgrader.claude_path = claude_dir

    upgrader._update_claude_folder()

    # Backup should exist
    backup_path = tmp_path / '.claude.backup'
    assert backup_path.exists()
    assert (backup_path / 'instructions.md').exists()
    assert (backup_path / 'commands' / 'test.md').exists()

"""
Tests for CLI functionality.
"""

import pytest
import json
from pathlib import Path
from click.testing import CliRunner
from purposely.cli import cli




def test_cli_version():
    """Test that --version works."""
    runner = CliRunner()
    result = runner.invoke(cli, ['--version'])
    assert result.exit_code == 0
    assert '1.0.0' in result.output


def test_cli_help():
    """Test that --help works."""
    runner = CliRunner()
    result = runner.invoke(cli, ['--help'])
    assert result.exit_code == 0
    assert 'Purposely' in result.output
    assert 'init' in result.output


def test_init_creates_config():
    """Test that init creates .purposely/config.json."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['init', '--lang', 'ko'])
        assert result.exit_code == 0

        # Check config exists
        config_path = Path('.purposely/config.json')
        assert config_path.exists()

        # Check config content
        with open(config_path) as f:
            config = json.load(f)
        assert config['language'] == 'ko'
        assert config['version'] == '1.0.0'
        assert config['current_phase'] is None


def test_init_creates_directories():
    """Test that init creates docs/ and .claude/ directories."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['init', '--lang', 'en'])
        assert result.exit_code == 0

        # Check directories exist
        assert Path('docs').exists()
        assert Path('.claude').exists()
        assert Path('.claude/commands').exists()
        assert Path('.claude/instructions.md').exists()


def test_init_copies_slash_commands():
    """Test that init copies slash command files."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['init', '--lang', 'en'])
        assert result.exit_code == 0

        # Check slash commands exist
        commands_dir = Path('.claude/commands')
        assert (commands_dir / 'purposely-init.md').exists()
        assert (commands_dir / 'purposely-phase.md').exists()
        assert (commands_dir / 'purposely-research.md').exists()
        assert (commands_dir / 'purposely-design.md').exists()
        assert (commands_dir / 'purposely-plan.md').exists()
        assert (commands_dir / 'purposely-implement.md').exists()


def test_init_warns_existing_project():
    """Test that init warns if project already exists."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        # First init
        result1 = runner.invoke(cli, ['init', '--lang', 'en'])
        assert result1.exit_code == 0

        # Second init without force
        result2 = runner.invoke(cli, ['init', '--lang', 'ko'])
        assert result2.exit_code == 1
        assert 'already exists' in result2.output.lower()


def test_init_force_overwrites():
    """Test that init --force overwrites existing project."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        # First init with English
        result1 = runner.invoke(cli, ['init', '--lang', 'en'])
        assert result1.exit_code == 0

        # Second init with Korean and --force
        result2 = runner.invoke(cli, ['init', '--lang', 'ko', '--force'])
        assert result2.exit_code == 0

        # Check language was changed
        with open('.purposely/config.json') as f:
            config = json.load(f)
        assert config['language'] == 'ko'

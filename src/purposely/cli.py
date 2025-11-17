"""
CLI entry point for Purposely.

This module provides the main CLI interface using Click.
Currently implements only the 'init' command for project initialization.
"""

import click
from pathlib import Path
from .core.initializer import Initializer


@click.group()
@click.version_option(version="1.0.0", prog_name="purposely")
def cli():
    """
    Purposely: Purpose-Driven Development Framework

    A CLI tool that helps maintain project purpose throughout the development lifecycle.

    \b
    Workflow:
    1. purposely init          - Initialize project structure
    2. /purposely-init         - Create GLOBAL_PURPOSE.md
    3. /purposely-phase        - Create phase SPEC
    4. /purposely-research     - Research phase
    5. /purposely-design       - Design phase
    6. /purposely-plan         - Planning phase
    7. /purposely-implement    - Implementation tracking
    """
    pass


@cli.command()
@click.option(
    '--lang',
    type=click.Choice(['en', 'ko'], case_sensitive=False),
    default='en',
    help='Language for templates (default: en)'
)
@click.option(
    '--force',
    is_flag=True,
    help='Force initialization even if project already exists'
)
def init(lang: str, force: bool):
    """
    Initialize a new Purposely project.

    This command creates:
    - .purposely/config.json (stores language setting)
    - docs/ directory (for documentation)
    - .claude/ directory (with slash commands and templates)

    Example:
        purposely init --lang ko
        purposely init --lang en --force
    """
    try:
        initializer = Initializer(lang=lang.lower(), force=force)
        initializer.run()
    except Exception as e:
        click.echo(f"❌ Error: {e}", err=True)
        raise click.Abort()


if __name__ == '__main__':
    cli()

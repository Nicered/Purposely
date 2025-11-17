"""
CLI entry point for Purposely.

This module provides the main CLI interface using Click.
Currently implements only the 'init' command for project initialization.
"""

import click
from pathlib import Path
from .core.initializer import Initializer
from .core.creator import DocumentCreator


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


@cli.group()
def create():
    """Create documents from templates."""
    pass


@create.command('global-purpose')
@click.option('--force', is_flag=True, help='Overwrite if file exists')
def create_global_purpose(force: bool):
    """
    Create GLOBAL_PURPOSE.md document.

    Example:
        purposely create global-purpose
        purposely create global-purpose --force
    """
    try:
        creator = DocumentCreator()
        output_path = creator.create_global_purpose(force=force)
        click.echo(f"✅ Created: {output_path}")
    except click.ClickException as e:
        click.echo(f"❌ {e.message}", err=True)
        raise click.Abort()


@create.command('spec')
@click.argument('phase')
@click.option('--force', is_flag=True, help='Overwrite if file exists')
def create_spec(phase: str, force: bool):
    """
    Create phase SPEC document (00_SPEC.md).

    PHASE: Phase number (e.g., '01', '02')

    Example:
        purposely create spec 01
        purposely create spec 02 --force
    """
    try:
        # Ensure phase is zero-padded
        phase = phase.zfill(2)
        creator = DocumentCreator()
        output_path = creator.create_spec(phase=phase, force=force)
        click.echo(f"✅ Created: {output_path}")
    except click.ClickException as e:
        click.echo(f"❌ {e.message}", err=True)
        raise click.Abort()


@create.command('research')
@click.argument('phase')
@click.argument('number')
@click.argument('title')
@click.option('--force', is_flag=True, help='Overwrite if file exists')
def create_research(phase: str, number: str, title: str, force: bool):
    """
    Create research document (01_XX_RESEARCH_*.md).

    PHASE: Phase number (e.g., '01', '02')
    NUMBER: Research document number (e.g., '01', '02')
    TITLE: Research topic/title

    Example:
        purposely create research 01 01 "API Research"
        purposely create research 01 02 "Database Design" --force
    """
    try:
        phase = phase.zfill(2)
        number = number.zfill(2)
        creator = DocumentCreator()
        output_path = creator.create_research(
            phase=phase, number=number, title=title, force=force
        )
        click.echo(f"✅ Created: {output_path}")
    except click.ClickException as e:
        click.echo(f"❌ {e.message}", err=True)
        raise click.Abort()


@create.command('design-overview')
@click.argument('phase')
@click.option('--force', is_flag=True, help='Overwrite if file exists')
def create_design_overview(phase: str, force: bool):
    """
    Create design overview document (02_00_DESIGN_OVERVIEW.md).

    PHASE: Phase number (e.g., '01', '02')

    Example:
        purposely create design-overview 01
        purposely create design-overview 02 --force
    """
    try:
        phase = phase.zfill(2)
        creator = DocumentCreator()
        output_path = creator.create_design_overview(phase=phase, force=force)
        click.echo(f"✅ Created: {output_path}")
    except click.ClickException as e:
        click.echo(f"❌ {e.message}", err=True)
        raise click.Abort()


@create.command('design')
@click.argument('phase')
@click.argument('number')
@click.argument('title')
@click.option('--force', is_flag=True, help='Overwrite if file exists')
def create_design(phase: str, number: str, title: str, force: bool):
    """
    Create detailed design document (02_XX_DESIGN_*.md).

    PHASE: Phase number (e.g., '01', '02')
    NUMBER: Design document number (e.g., '01', '02')
    TITLE: Component/module name

    Example:
        purposely create design 01 01 "UserService"
        purposely create design 01 02 "Database Schema" --force
    """
    try:
        phase = phase.zfill(2)
        number = number.zfill(2)
        creator = DocumentCreator()
        output_path = creator.create_design_detail(
            phase=phase, number=number, title=title, force=force
        )
        click.echo(f"✅ Created: {output_path}")
    except click.ClickException as e:
        click.echo(f"❌ {e.message}", err=True)
        raise click.Abort()


@create.command('plan')
@click.argument('phase')
@click.option('--force', is_flag=True, help='Overwrite if file exists')
def create_plan(phase: str, force: bool):
    """
    Create implementation plan (03_PLAN.md).

    PHASE: Phase number (e.g., '01', '02')

    Example:
        purposely create plan 01
        purposely create plan 02 --force
    """
    try:
        phase = phase.zfill(2)
        creator = DocumentCreator()
        output_path = creator.create_plan(phase=phase, force=force)
        click.echo(f"✅ Created: {output_path}")
    except click.ClickException as e:
        click.echo(f"❌ {e.message}", err=True)
        raise click.Abort()


@create.command('implementation')
@click.argument('phase')
@click.option('--force', is_flag=True, help='Overwrite if file exists')
def create_implementation(phase: str, force: bool):
    """
    Create implementation log (04_IMPLEMENTATION.md).

    PHASE: Phase number (e.g., '01', '02')

    Example:
        purposely create implementation 01
        purposely create implementation 02 --force
    """
    try:
        phase = phase.zfill(2)
        creator = DocumentCreator()
        output_path = creator.create_implementation(phase=phase, force=force)
        click.echo(f"✅ Created: {output_path}")
    except click.ClickException as e:
        click.echo(f"❌ {e.message}", err=True)
        raise click.Abort()


if __name__ == '__main__':
    cli()

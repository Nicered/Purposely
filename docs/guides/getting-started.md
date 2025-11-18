# Getting Started with Purposely

## What is Purposely?

Purposely is a CLI framework that helps development teams maintain project purpose throughout the entire development lifecycle. It integrates seamlessly with Claude Code to provide structured documentation and workflow management.

## Installation

### Using uvx (Recommended)

The easiest way to use Purposely is with `uvx`, which runs the tool without installation:

```bash
uvx --from git+https://github.com/nicered/purposely purposely init
```

### Global Installation

For repeated use, install Purposely globally:

```bash
pip install git+https://github.com/nicered/purposely
```

### Bash Alias (Optional)

Add this to your `~/.bashrc` or `~/.zshrc` for easier access:

```bash
alias purposely="uvx --from git+https://github.com/nicered/purposely purposely"
```

## Quick Start

### 1. Initialize Your Project

For a new project:

```bash
purposely init
```

For an existing project:

```bash
purposely init --existing
```

This creates:
- `.purposely/config.json` - Project configuration
- `.claude/` - Claude Code integration files
- `docs/` - Documentation structure

### 2. Set Your Language

Edit `.purposely/config.json` to set your preferred language:

```json
{
  "language": "en",  // or "ko" for Korean
  "version": "0.1.3"
}
```

### 3. Start Your First Phase

Use Claude Code's slash commands:

```
/purposely-phase
```

This will:
- Create a new development phase
- Generate a SPEC document
- Set up phase objectives

## Next Steps

- [Workflow Guide](workflow.md) - Learn the complete development workflow
- [Commands Reference](commands.md) - All available CLI and slash commands
- [Best Practices](best-practices.md) - Tips for effective purpose-driven development

## Need Help?

- [GitHub Issues](https://github.com/nicered/purposely/issues)
- [Contributing Guide](https://github.com/nicered/purposely/blob/main/CONTRIBUTING.md)

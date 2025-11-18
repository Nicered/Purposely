# Purpose-Driven Development Workflow

## Overview

Purposely guides you through a structured development process that keeps your project's purpose at the center of every decision.

## The 6-Step Workflow

### 1. Define Purpose (`/purposely-init`)

**When to use:** At project start or when clarifying project goals

**What it does:**
- Establishes clear project objectives
- Defines success criteria
- Sets the foundation for all future decisions

**Example:**
```
/purposely-init

# Claude will guide you through:
# - What problem are you solving?
# - Who is this for?
# - What does success look like?
```

### 2. Create Phase (`/purposely-phase`)

**When to use:** Starting a new development iteration

**What it does:**
- Breaks project into manageable chunks
- Creates SPEC document with phase objectives
- Defines deliverables and timeline

**Example:**
```
/purposely-phase

# Creates: docs/phase-01/00_SPEC.md
# Defines: Phase objectives, scope, and deliverables
```

### 3. Research (`/purposely-research`)

**When to use:** Before making technical decisions

**What it does:**
- Investigates technical options
- Documents findings objectively
- Connects research to design decisions

**Example:**
```
/purposely-research

# Creates: docs/phase-01/01_XX_RESEARCH_*.md
# Documents: Options evaluated, pros/cons, recommendations
```

### 4. Design (`/purposely-design`)

**When to use:** After research, before implementation

**What it does:**
- Creates system architecture
- Documents design decisions
- Explains the "why" behind choices

**Example:**
```
/purposely-design

# Creates: docs/phase-01/02_XX_DESIGN_*.md
# Documents: Architecture, components, interactions
```

### 5. Plan (`/purposely-plan`)

**When to use:** Before starting implementation

**What it does:**
- Breaks design into implementation tasks
- Prioritizes work
- Identifies dependencies

**Example:**
```
/purposely-plan

# Creates: docs/phase-01/03_XX_PLAN_*.md
# Documents: Tasks, order, timeline
```

### 6. Implement (`/purposely-implement`)

**When to use:** During actual coding

**What it does:**
- Guides implementation with purpose awareness
- Ensures code aligns with design
- Documents implementation decisions

**Example:**
```
/purposely-implement

# Creates: docs/phase-01/04_XX_IMPLEMENTATION_*.md
# Documents: Code changes, decisions, lessons learned
```

## Document Structure

All documents follow a consistent structure:

```
docs/
├── GLOBAL_PURPOSE.md              # Project-level purpose
└── phase-01/
    ├── 00_SPEC.md                 # Phase specification
    ├── 01_00_RESEARCH_OVERVIEW.md # Research summary
    ├── 01_01_RESEARCH_*.md        # Individual research docs
    ├── 02_00_DESIGN_OVERVIEW.md   # Design summary
    ├── 02_01_DESIGN_*.md          # Individual design docs
    ├── 03_XX_PLAN_*.md            # Planning documents
    └── 04_XX_IMPLEMENTATION_*.md  # Implementation logs
```

## Best Practices

### Start Small
Don't try to document everything upfront. Start with SPEC, do minimal research for immediate decisions, and iterate.

### Keep It Current
Update documents as you learn. If your design changes during implementation, update the design doc.

### Purpose Over Process
If a step doesn't add value for your specific situation, skip it. The framework is a guide, not a rulebook.

### Review Regularly
Refer back to SPEC and GLOBAL_PURPOSE frequently to ensure you're still aligned.

## Example: Adding a New Feature

1. **Phase** - Create phase-02 for "User Authentication"
2. **Research** - Investigate auth libraries (JWT vs OAuth)
3. **Design** - Design auth flow and database schema
4. **Plan** - Break into tasks (models, routes, UI, tests)
5. **Implement** - Build feature, documenting key decisions
6. **Review** - Check against SPEC objectives

## Common Patterns

### Multiple Research Documents
When investigating several options:
```
01_00_RESEARCH_OVERVIEW.md    # Summary of all findings
01_01_RESEARCH_DATABASE.md    # Database options
01_02_RESEARCH_AUTH.md        # Authentication methods
01_03_RESEARCH_HOSTING.md     # Deployment platforms
```

### Iterative Design
Design doesn't have to be complete before implementation:
```
# Initial design
02_01_DESIGN_ARCHITECTURE.md

# Implementation reveals needs
04_01_IMPLEMENTATION_AUTH.md

# Update design based on learnings
02_01_DESIGN_ARCHITECTURE.md (updated)
```

## Next Steps

- [Commands Reference](commands.md) - All available commands
- [Best Practices](best-practices.md) - Tips and tricks

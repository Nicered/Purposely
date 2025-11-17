# Getting Started

A step-by-step guide to start Purpose-Driven Development with Purposely.

## Installation

### 1. Install uv (Recommended)

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Run Purposely

Use directly without installation:

```bash
# In your project directory
uvx --from git+https://github.com/nicered/purposely purposely init --lang en
```

> After PyPI publication: `uvx purposely init --lang en`

## Project Initialization

### Step 1: Create Project Structure

```bash
cd your-project
uvx --from git+https://github.com/nicered/purposely purposely init --lang en
```

Generated structure:
```
your-project/
├── .purposely/
│   └── config.json      # Language settings, etc.
├── docs/                # Documentation repository
└── .claude/             # Claude Code integration
    ├── commands/        # Slash commands
    └── instructions.md  # AI guide
```

### Step 2: Write GLOBAL_PURPOSE

This is **the most important step**.

#### Generate via CLI:

```bash
purposely create global-purpose
```

#### Or in Claude Code:

```
/purposely-init
```

Claude helps you write it through questions:

1. **Why are you building this project?**
   - What pain/problem did you experience?
   - What are the limitations of existing solutions?

2. **Who will use it?**
   - Who are the primary users?
   - In what situations will they use it?

3. **How does it solve the problem?**
   - What's the core approach?
   - What's the differentiation point?

4. **How do you measure success?**
   - What are concrete metrics?
   - When can you say "we succeeded"?

#### GLOBAL_PURPOSE Example:

```markdown
# GLOBAL_PURPOSE

## Why
To solve the problem of developers losing sight of project purpose
and adding unnecessary features, leading to unfinished projects

## Problem
- Purpose that was clear initially becomes fuzzy during development
- Feature creep causes unlimited scope expansion
- Team members have different understandings of project purpose
- Many projects abandoned incomplete

## Solution
A documentation framework and AI assistant that enforces
referencing GLOBAL_PURPOSE at every development stage

## Success Metrics
- 80%+ project completion rate for users
- <10% off-purpose feature additions
- 50% reduction in documentation time (with AI support)
```

## Starting Phase 1

### Step 3: Plan Phase

Divide project into Phases. Each Phase:
- Is **independently completable**
- Is **aligned with GLOBAL_PURPOSE**
- Can be finished within 1-4 weeks

#### Create Phase 1 SPEC:

```bash
purposely create spec 01
```

Or in Claude Code:
```
/purposely-phase
```

#### SPEC Example:

```markdown
# Phase 1 SPEC

## Objective
Project initialization via CLI and basic document templates

## Scope
- `purposely init` command
- GLOBAL_PURPOSE template
- English/Korean i18n support
- Claude Code slash commands

## Out of Scope
- Web UI (Phase 2)
- AI auto-validation (Phase 3)

## Success Criteria
- [ ] init command creates .purposely/, docs/, .claude/
- [ ] Korean/English templates work correctly
- [ ] Slash commands work in Claude Code
```

### Step 4: Research (Optional)

Write research documents when complex decisions needed:

```bash
purposely create research 01 01 "CLI Framework Comparison"
```

Or:
```
/purposely-research
```

### Step 5: Design

Document system design:

```bash
# Overall design overview
purposely create design-overview 01

# Individual component designs
purposely create design 01 01 "Initializer"
purposely create design 01 02 "TemplateRenderer"
```

Or:
```
/purposely-design
```

### Step 6: Implementation Plan

```bash
purposely create plan 01
```

Or:
```
/purposely-plan
```

Implementation plan includes:
- Task list (checklist)
- Dependencies
- Timeline estimates
- Risks and mitigations

### Step 7: Implement and Track

```bash
purposely create implementation 01
```

Or:
```
/purposely-implement
```

Log during implementation:
- What you actually did
- What differed from plan
- What you learned
- Notes for next Phase

## Workflow Summary

```
1. Write GLOBAL_PURPOSE (once)
   ↓
2. Write Phase SPEC (per Phase)
   ↓
3. RESEARCH (if needed)
   ↓
4. DESIGN
   ↓
5. PLAN
   ↓
6. IMPLEMENTATION
   ↓
7. Move to next Phase
```

## Practical Tips

### ✅ Do

1. **Read GLOBAL_PURPOSE frequently**
   - Re-read at least weekly
   - Always check before adding new features

2. **Keep Phases small**
   - Completable within 1-4 weeks
   - Split if too large

3. **Write documents first**
   - Document design before coding
   - Never "just start coding"

4. **Use Claude Code**
   - Interactive writing with slash commands
   - AI automatically checks alignment

### ❌ Don't

1. **Don't change GLOBAL_PURPOSE frequently**
   - Can change if truly fundamental
   - But decide carefully

2. **Don't skip documents**
   - "I'll write it later" → Never happens
   - If not now, never

3. **Don't expand Phase scope infinitely**
   - "Just one more" → Start of feature creep
   - Stick to SPEC

4. **Don't separate docs from code**
   - Documents are version-controlled with code
   - Update docs when code changes

## Claude Code Integration

Purposely integrates perfectly with Claude Code.

### Available Slash Commands:

| Command | Purpose | Generated File |
|---------|---------|----------------|
| `/purposely-init` | Write GLOBAL_PURPOSE | `docs/GLOBAL_PURPOSE.md` |
| `/purposely-phase` | Write Phase SPEC | `docs/phase-XX/00_SPEC.md` |
| `/purposely-research` | Write research | `docs/phase-XX/01_XX_RESEARCH_*.md` |
| `/purposely-design` | Write design | `docs/phase-XX/02_XX_DESIGN_*.md` |
| `/purposely-plan` | Write plan | `docs/phase-XX/03_PLAN.md` |
| `/purposely-implement` | Write log | `docs/phase-XX/04_IMPLEMENTATION.md` |

### Benefits of Slash Commands:

1. **Interactive Writing**: Claude asks questions and fills content
2. **Auto Validation**: Checks alignment with GLOBAL_PURPOSE
3. **Context Retention**: Automatically references previous documents
4. **Time Saving**: 50% reduction in template filling time

## Next Steps

- [Document Types](document-types.md): Detailed explanation of 7 document types
- [Best Practices](best-practices.md): Tips for effective PDD
- [What is PDD?](what-is-pdd.md): PDD philosophy and principles

## Troubleshooting

### Q: I don't know how to write GLOBAL_PURPOSE

A: Use `/purposely-init` in Claude Code. Claude helps you write through questions.

### Q: How should I divide Phases?

A: Use these criteria:
- Completable within 1-4 weeks
- Independently testable/deployable
- Has clear success criteria

### Q: Do I need to write all documents?

A: GLOBAL_PURPOSE, SPEC, and IMPLEMENTATION are required. Write RESEARCH only for complex decisions, DESIGN only for complex systems.

### Q: Is it useful for solo projects?

A: Even more useful! It's easier to lose purpose when working alone.

---

**Next**: [Document Types Detailed](document-types.md)

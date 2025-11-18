# Commands Reference

## CLI Commands

### `purposely init`

Initialize a new Purposely project.

```bash
purposely init              # New project
purposely init --existing   # Existing codebase
```

**Options:**
- `--existing` - Add to existing project with code

**What it creates:**
- `.purposely/config.json` - Configuration
- `.claude/commands/` - Slash commands
- `docs/GLOBAL_PURPOSE.md` - Project purpose

---

### `purposely create spec`

Create a phase specification document.

```bash
purposely create spec <phase_number>
```

**Example:**
```bash
purposely create spec 01
```

**Creates:** `docs/phase-01/00_SPEC.md`

---

### `purposely create research-overview`

Create research overview document.

```bash
purposely create research-overview <phase_number>
```

**Example:**
```bash
purposely create research-overview 01
```

**Creates:** `docs/phase-01/01_00_RESEARCH_OVERVIEW.md`

---

### `purposely create design-overview`

Create design overview document.

```bash
purposely create design-overview <phase_number>
```

**Example:**
```bash
purposely create design-overview 01
```

**Creates:** `docs/phase-01/02_00_DESIGN_OVERVIEW.md`

---

### `purposely upgrade`

Upgrade Purposely templates to latest version.

```bash
purposely upgrade         # Interactive upgrade
purposely upgrade --force # Force upgrade without prompts
```

**What it does:**
- Creates backup of `.claude` folder
- Updates slash command templates
- Preserves your documents in `docs/`

---

## Claude Code Slash Commands

### `/purposely-init`

Initialize or update project purpose.

**Use when:**
- Starting a new project
- Clarifying project goals
- Updating project direction

**What it asks:**
- What problem are you solving?
- Who is this for?
- What does success look like?

**Creates/Updates:** `docs/GLOBAL_PURPOSE.md`

---

### `/purposely-phase`

Start a new development phase.

**Use when:**
- Beginning a new feature set
- Starting a development iteration
- Planning a major change

**What it does:**
- Creates phase directory structure
- Generates SPEC document
- Sets phase objectives

**Creates:** `docs/phase-XX/00_SPEC.md`

---

### `/purposely-research`

Conduct technical research.

**Use when:**
- Evaluating technology options
- Investigating approaches
- Before making technical decisions

**What it does:**
- Auto-creates Research Overview if missing
- Guides systematic investigation
- Documents findings and recommendations

**Creates:** `docs/phase-XX/01_XX_RESEARCH_*.md`

---

### `/purposely-design`

Create system design.

**Use when:**
- After research is complete
- Before starting implementation
- Defining system architecture

**What it does:**
- Auto-creates Design Overview if missing
- Guides design documentation
- Connects design to research findings

**Creates:** `docs/phase-XX/02_XX_DESIGN_*.md`

---

### `/purposely-plan`

Plan implementation tasks.

**Use when:**
- After design is complete
- Before starting to code
- Breaking down work

**What it does:**
- Creates detailed task breakdown
- Identifies dependencies
- Estimates effort

**Creates:** `docs/phase-XX/03_XX_PLAN_*.md`

---

### `/purposely-implement`

Guide implementation.

**Use when:**
- During actual coding
- Implementing planned tasks
- Making implementation decisions

**What it does:**
- References design and plan
- Guides purposeful coding
- Documents key decisions

**Creates:** `docs/phase-XX/04_XX_IMPLEMENTATION_*.md`

---

## Command Workflows

### Starting a New Project

```bash
# 1. Initialize
purposely init

# 2. Define purpose (in Claude Code)
/purposely-init

# 3. Start first phase
/purposely-phase
```

### Adding to Existing Project

```bash
# 1. Initialize with existing flag
purposely init --existing

# 2. Document current purpose
/purposely-init

# 3. Create phase for next work
/purposely-phase
```

### Typical Development Cycle

```bash
# In Claude Code:
/purposely-phase        # Start phase
/purposely-research     # Investigate options
/purposely-design       # Design solution
/purposely-plan         # Plan implementation
/purposely-implement    # Build feature
```

### Upgrading Purposely

```bash
# Check for updates
purposely upgrade

# Backup is automatic, rollback with:
cp -r .claude.backup.* .claude
```

---

## Tips

### Language Selection

All slash commands detect language from `.purposely/config.json`:

```json
{
  "language": "ko"  // "en" or "ko"
}
```

### Overview Documents

Research and Design overviews are auto-created if missing:
- First time using `/purposely-research` → creates `01_00_RESEARCH_OVERVIEW.md`
- First time using `/purposely-design` → creates `02_00_DESIGN_OVERVIEW.md`

### Document Numbering

Follow this pattern:
- `00_SPEC.md` - Phase specification
- `01_XX_RESEARCH_*.md` - Research (01-19)
- `02_XX_DESIGN_*.md` - Design (20-39)
- `03_XX_PLAN_*.md` - Planning (40-59)
- `04_XX_IMPLEMENTATION_*.md` - Implementation (60-79)

---

## Next Steps

- [Getting Started](getting-started.md) - Installation and setup
- [Workflow Guide](workflow.md) - Complete development workflow

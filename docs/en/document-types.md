# Document Types

Detailed explanation of Purposely's 7 document types.

## Document Hierarchy

```
GLOBAL_PURPOSE (Entire Project)
    ├── Phase 01/
    │   ├── 00_SPEC.md
    │   ├── 01_XX_RESEARCH_*.md
    │   ├── 02_00_DESIGN_OVERVIEW.md
    │   ├── 02_XX_DESIGN_*.md
    │   ├── 03_PLAN.md
    │   └── 04_IMPLEMENTATION.md
    ├── Phase 02/
    │   └── ...
    └── Phase 03/
        └── ...
```

## 1. GLOBAL_PURPOSE

### Purpose
Defines the **reason for existence** of your project. The reference point for all documents.

### When to Write
Write **once** at project start.

### Required Sections

#### Why
Why does this project exist?

**Writing Tips:**
- Start with personal motivation
- "This problem exists" rather than "This would be nice"
- Should be summarizable in one sentence

**Example:**
```markdown
## Why
To solve the problem of developers starting but not finishing projects
```

#### Problem
What specific problem does it solve?

**Writing Tips:**
- 3-5 concrete pain points
- "Who, when, in what situation" experiences it
- Measurable problems are better

**Example:**
```markdown
## Problem
- 70% of projects started with initial enthusiasm go unfinished
- Developers forget "why" during development and add unnecessary features
- Team members have different understandings of purpose
- Focus on tech choices while forgetting business purpose
```

#### Solution
How does it solve the problem?

**Writing Tips:**
- Focus on WHAT rather than HOW
- 1-2 sentences on core approach
- Clear differentiation point

**Example:**
```markdown
## Solution
A documentation-centric framework and AI assistant that enforces
referencing GLOBAL_PURPOSE at every development stage
```

#### Success Metrics
How do you measure success?

**Writing Tips:**
- Quantitative metrics preferred
- Must be measurable
- 3-5 core metrics

**Example:**
```markdown
## Success Metrics
- 80%+ project completion rate for users
- <10% off-purpose feature additions
- 50% reduction in documentation time (vs manual)
- 1,000 monthly active users
```

### Generation Command
```bash
purposely create global-purpose
# or
/purposely-init
```

---

## 2. SPEC (00_SPEC.md)

### Purpose
Defines **objectives and scope** of each Phase.

### When to Write
Before starting each Phase.

### Required Sections

#### Objective
Goal to achieve in this Phase

**Example:**
```markdown
## Objective
Project initialization via CLI tool and basic template provision
```

#### Scope
What's **included** in this Phase

**Example:**
```markdown
## Scope
- Implement `purposely init` command
- GLOBAL_PURPOSE.md template
- Korean/English i18n support
- Generate .claude/ directory and slash commands
```

#### Out of Scope
What's **not included** in this Phase

**Important:** Without this, scope keeps expanding!

**Example:**
```markdown
## Out of Scope
- Web UI (Phase 2)
- AI auto-validation (Phase 3)
- GitHub integration (Phase 4)
```

#### Success Criteria
Phase completion criteria (checklist)

**Example:**
```markdown
## Success Criteria
- [ ] `purposely init` creates .purposely/, docs/, .claude/
- [ ] Korean templates render correctly
- [ ] English templates render correctly
- [ ] 6 slash commands work in Claude Code
- [ ] 100% pytest pass rate
```

#### Alignment with GLOBAL_PURPOSE
How it connects to GLOBAL_PURPOSE

**Example:**
```markdown
## Alignment with GLOBAL_PURPOSE
This Phase builds core infrastructure for "documentation-centric framework"
Solution. By making it easy to start, contributes to "80% completion rate" goal.
```

### Generation Command
```bash
purposely create spec 01
# or
/purposely-phase
```

---

## 3. RESEARCH (01_XX_RESEARCH_*.md)

### Purpose
Documents **investigation and rationale** for important decisions.

### When to Write
- Choosing tech stack
- Deciding architecture patterns
- Selecting algorithms
- High-uncertainty decisions

### Required Sections

#### Research Question
What are you trying to find out?

**Example:**
```markdown
## Research Question
Which Python CLI framework should we use?
```

#### Methodology
How did you investigate?

**Example:**
```markdown
## Methodology
- Compare Click, Typer, argparse
- Check GitHub stars, maintenance status
- Implement POC with each framework
- Evaluate documentation quality and community size
```

#### Findings
What you discovered

**Example:**
```markdown
## Findings

### Click
- Pros: Mature, rich features, many use cases
- Cons: Decorator style

### Typer
- Pros: Type hint based, modern
- Cons: Smaller ecosystem vs Click

### argparse
- Pros: Standard library
- Cons: Lots of boilerplate
```

#### Decision
Final decision and reasoning

**Example:**
```markdown
## Decision
Selected Click

**Reasons:**
1. Maturity and stability
2. Rich plugin ecosystem
3. Good integration with pytest
4. Decorator style fits this project
```

### Generation Command
```bash
purposely create research 01 01 "CLI Framework Comparison"
# or
/purposely-research
```

---

## 4. DESIGN_OVERVIEW (02_00_DESIGN_OVERVIEW.md)

### Purpose
**Architecture and design overview** for entire Phase

### When to Write
Before detailed design docs in complex Phases

### Required Sections

#### Architecture
Overall structure

**Example:**
```markdown
## Architecture

```
┌─────────────┐
│     CLI     │
└──────┬──────┘
       │
   ┌───┴────┐
   │ Core   │
   └───┬────┘
       │
┌──────┼──────┐
│      │      │
Initializer Renderer Creator
```
```

#### Components
Major components and responsibilities

**Example:**
```markdown
## Components

### CLI (cli.py)
- Click-based command interface
- Parse user input
- Call Core components

### Initializer
- Create project structure
- Initialize config files

### TemplateRenderer
- Jinja2-based template rendering
- i18n handling
```

### Generation Command
```bash
purposely create design-overview 01
# or
/purposely-design
```

---

## 5. DESIGN_DETAIL (02_XX_DESIGN_*.md)

### Purpose
**Detailed design** of individual components/modules

### When to Write
For each major component

### Required Sections

#### Purpose
Purpose of this component

#### Interface
Public API/methods

**Example:**
```python
class TemplateRenderer:
    def __init__(self, lang: str)
    def render(self, template_name: str, **context) -> str
    def render_to_file(self, template_name: str, output_path: Path, **context)
```

#### Implementation Details
Internal implementation approach

#### Dependencies
Other components it depends on

### Generation Command
```bash
purposely create design 01 01 "TemplateRenderer"
# or
/purposely-design
```

---

## 6. PLAN (03_PLAN.md)

### Purpose
**Concrete plan** for implementation work

### Required Sections

#### Tasks
Task list (checklist)

**Example:**
```markdown
## Tasks

### Phase 1: Core Infrastructure
- [ ] Setup project structure (pyproject.toml, etc.)
- [ ] Create CLI entry point
- [ ] Implement Initializer
  - [ ] Directory creation logic
  - [ ] Generate config.json
  - [ ] Copy template files

### Phase 2: Template System
- [ ] Implement TemplateRenderer
- [ ] Write i18n files (en.json, ko.json)
- [ ] Write Jinja2 templates

### Phase 3: Testing
- [ ] Unit tests
- [ ] Integration tests
- [ ] Setup CI/CD
```

#### Timeline
Estimated schedule

#### Dependencies
Dependencies between tasks

#### Risks
Expected risks and mitigations

### Generation Command
```bash
purposely create plan 01
# or
/purposely-plan
```

---

## 7. IMPLEMENTATION (04_IMPLEMENTATION.md)

### Purpose
**Log** actual implementation process and results

### Required Sections

#### What Was Done
Actual work completed

#### What Changed from Plan
Deviations from plan

**Important:** This is the most valuable section!

**Example:**
```markdown
## What Changed from Plan

### Added Jinja2 Filters
Not in plan, but needed custom filters for date formatting

### Used importlib.resources
Originally planned pkg_resources but
importlib.resources is standard in Python 3.10+, so changed
```

#### Lessons Learned
What you learned

#### Notes for Next Phase
Notes for next Phase

### Generation Command
```bash
purposely create implementation 01
# or
/purposely-implement
```

---

## Document Writing Order

### Required Sequence:
```
GLOBAL_PURPOSE (once only)
↓
SPEC (at each Phase start)
↓
[Optional] RESEARCH (if needed)
↓
[Optional] DESIGN (if complex)
↓
PLAN
↓
IMPLEMENTATION (write while implementing)
```

### Minimal Set:
For simple Phases:
- SPEC
- PLAN
- IMPLEMENTATION

is enough.

### Complex Phase:
- SPEC
- RESEARCH (multiple allowed)
- DESIGN_OVERVIEW
- DESIGN_DETAIL (multiple allowed)
- PLAN
- IMPLEMENTATION

---

## Document Writing Principles

### 1. Always Reference GLOBAL_PURPOSE
All documents have "Alignment with GLOBAL_PURPOSE" section

### 2. Write Concretely
No abstract expressions. Make it measurable.

### 3. Write for Future You
Should be understandable from this doc alone after 6 months

### 4. Write Before Code
Documents → Code order

### 5. Update Together When Changing
When code changes, update docs too

---

**Next:** [Best Practices](best-practices.md)

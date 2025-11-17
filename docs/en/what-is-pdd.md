# What is PDD (Purpose-Driven Development)?

## Overview

**Purpose-Driven Development (PDD)** is a software development methodology that places the core purpose of a project at the center of the development lifecycle.

## Core Philosophy

### The Problem: Why Do Projects Fail?

Most software projects fail because:

1. **Purpose Amnesia**: Developers forget "why are we building this?" during development
2. **Scope Creep**: Features unrelated to the original purpose keep getting added
3. **Loss of Coherence**: Decisions at different stages conflict with each other
4. **Priority Confusion**: No clear criteria for what's important

### The Solution: Purpose-First Approach

PDD solves these problems through:

1. **Single Source of Truth**: GLOBAL_PURPOSE is the criterion for all decisions
2. **Continuous Alignment**: All documents reference and verify GLOBAL_PURPOSE
3. **Intentional Documentation**: Clear recording of intent and rationale at each stage
4. **Traceability**: Every decision can be traced back to the purpose

## Core Components of PDD

### 1. GLOBAL_PURPOSE

A document that defines the **reason for existence** of your project.

**Essential Questions:**
- **Why**: Why does this project exist?
- **Problem**: What problem does it solve?
- **Solution**: How does it solve that problem?
- **Success Metrics**: How do we measure success?

**Example:**
```markdown
## Why
To solve the problem of developers losing sight of their project's purpose and direction

## Problem
- The purpose that was clear at project start becomes fuzzy during development
- Hard to verify alignment with original purpose when adding features
- Team members develop different understandings of the project purpose

## Solution
A framework that enforces all development documents to reference GLOBAL_PURPOSE

## Success Metrics
- 80%+ project completion rate
- <10% off-purpose feature additions
```

### 2. Phase-Based Development

Projects are managed in discrete **Phases**.

Each Phase:
- Has a clear **objective** (SPEC)
- Is **aligned** with GLOBAL_PURPOSE
- Can be **completed** independently

### 3. 7 Document Types

Each Phase follows this document sequence:

```
Phase-01/
├── 00_SPEC.md              # Phase objectives
├── 01_XX_RESEARCH_*.md     # Research findings
├── 02_00_DESIGN_OVERVIEW.md # Overall design
├── 02_XX_DESIGN_*.md       # Detailed designs
├── 03_PLAN.md              # Implementation plan
└── 04_IMPLEMENTATION.md    # Implementation log
```

Each document:
- **Explicitly references GLOBAL_PURPOSE**
- Builds on previous documents
- Provides rationale for next documents

## Benefits of PDD

### 1. Clear Direction
- All team members understand "why"
- Fast and consistent decision-making
- Clear priority judgments

### 2. Scope Management
- Can reject features not aligned with GLOBAL_PURPOSE
- Prevents feature creep
- Focused resource allocation

### 3. Team Collaboration
- Documents serve as common language
- Enables async collaboration
- Easy onboarding for new team members

### 4. Quality Assurance
- Rationale documented at each stage
- AI automatically checks alignment
- Improved code review quality

## PDD vs Traditional Methodologies

| Aspect | Traditional | PDD |
|--------|------------|-----|
| Purpose Definition | Initial only | Continuous reference |
| Documentation | Optional | Required |
| Alignment Check | Manual | AI-automated |
| Scope Management | Difficult | Clear |
| Team Understanding | Uneven | Consistent |

## Projects Suited for PDD

✅ **Good Fit:**
- Projects solving clear problems
- Projects requiring team collaboration
- Long-term maintained projects
- Clear purpose but uncertain implementation

❌ **Poor Fit:**
- Simple experiments/prototypes
- 1-2 day micro-projects
- Exploratory projects with changing purposes

## Getting Started

To start with PDD:

1. **Define GLOBAL_PURPOSE**: Clarify the "why"
2. **Plan First Phase**: What to build first?
3. **Write Documents**: SPEC → RESEARCH → DESIGN → PLAN → IMPLEMENTATION
4. **Continuous Verification**: Check each decision aligns with GLOBAL_PURPOSE

See [Getting Started](getting-started.md) for details.

## Conclusion

PDD is **a development methodology that never forgets "why"**.

By keeping GLOBAL_PURPOSE at the center and ensuring all decisions align with it, PDD helps projects achieve their **originally intended purpose**.

> "More important than completing a project is completing **the right project**."

---

Next: [Getting Started](getting-started.md)

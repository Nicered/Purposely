# Purposely

**Purpose-Driven Development (PDD) Framework**

Purposely helps you stay aligned with your project's core purpose throughout the entire development lifecycle.

## 🎯 Core Concept

Every project must have a **GLOBAL_PURPOSE** that defines:
- Why does this project exist? (Why)
- What problem does it solve? (Problem)
- How will it solve the problem? (Solution)
- How do we measure success? (Success Metrics)

All Phases, Designs, and Implementations must **continuously align** with this GLOBAL_PURPOSE.

## 🚀 Quick Start

### Prerequisites

Install [uv](https://github.com/astral-sh/uv) (recommended):

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Initialize Your Project

Run directly without installation using `uvx`:

```bash
# In your project directory
uvx --from git+https://github.com/nicered/purposely purposely init --lang en

# Or in Korean
uvx --from git+https://github.com/nicered/purposely purposely init --lang ko
```

> **Note**: After PyPI publication, you can simply use `uvx purposely init --lang en`

This command creates:
- `.purposely/config.json` - Project configuration
- `docs/` - Documentation directory
- `.claude/` - Claude Code slash commands and templates

### Using with Claude Code

1. **Create GLOBAL_PURPOSE**: `/purposely-init`
2. **Start a Phase**: `/purposely-phase`
3. **Document Research**: `/purposely-research`
4. **Write Design**: `/purposely-design`
5. **Create Plan**: `/purposely-plan`
6. **Track Implementation**: `/purposely-implement`

## 📁 Document Structure

```
your-project/
├── .purposely/
│   └── config.json
├── docs/
│   ├── GLOBAL_PURPOSE.md
│   └── phase-01/
│       ├── 00_SPEC.md
│       ├── 01_XX_RESEARCH_*.md
│       ├── 02_XX_DESIGN_*.md
│       ├── 03_PLAN.md
│       └── 04_IMPLEMENTATION.md
└── .claude/
    ├── commands/
    └── instructions.md
```

## 🌟 Key Features

- **Purpose-Driven Development**: All documents reference GLOBAL_PURPOSE
- **Structured Documentation**: 7 document types with clear hierarchy
- **i18n Support**: English and Korean
- **Claude Code Integration**: Easy document creation with slash commands
- **Consistency Checking**: AI automatically checks alignment with purpose

## 📚 Document Types

### GLOBAL_PURPOSE
The core purpose of your project. **The foundation of everything**.

### SPEC (00_SPEC.md)
Defines objectives, scope, and success criteria for each phase.

### RESEARCH (01_XX_RESEARCH_*.md)
Research and investigation results. Evidence for design decisions.

### DESIGN (02_XX_DESIGN_*.md)
System design. How will it be implemented?

### PLAN (03_PLAN.md)
Concrete implementation plan. Timeline, dependencies, risks.

### IMPLEMENTATION (04_IMPLEMENTATION.md)
Actual implementation log. What was learned? How did it differ from the plan?

## 🔧 Development

### Local Installation

```bash
git clone https://github.com/nicered/purposely
cd purposely

# Using uv (recommended)
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e ".[dev]"

# Or using pip
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

### Run Tests

```bash
pytest tests/ -v
```

### Build

```bash
uv build
# Or: python -m build
```

## 🤝 Contributing

Issues and Pull Requests are welcome!

## 📄 License

MIT License

## 🙏 Acknowledgments

Purposely was created to help developers complete projects without losing sight of their purpose.

---

**Made with Purpose** ❤️

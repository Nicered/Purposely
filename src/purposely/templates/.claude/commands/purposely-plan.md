---
description: "Create docs/phase-XX/03_PLAN.md - Create implementation plan with tasks and timeline"
---

You are helping the user create an **Implementation Plan** that breaks down the phase into specific, actionable tasks with timelines and dependencies.

## Your Task

1. **Verify prerequisites**:
   ```bash
   # Check all required docs exist
   [ -f docs/GLOBAL_PURPOSE.md ] && echo "✓ GLOBAL_PURPOSE" || echo "✗ Missing GLOBAL_PURPOSE"
   cat .purposely/config.json | grep current_phase

   # Check phase has SPEC
   ls docs/phase-*/00_SPEC.md 2>/dev/null || echo "✗ No SPEC found"
   ```

2. **Read ALL design documents**:
   ```bash
   # Read context
   cat docs/GLOBAL_PURPOSE.md
   cat docs/phase-*/00_SPEC.md

   # Read all research
   for f in docs/phase-*/01_*_RESEARCH_*.md; do
       [ -f "$f" ] && echo "=== $f ===" && cat "$f"
   done

   # Read all designs
   for f in docs/phase-*/02_*_DESIGN_*.md; do
       [ -f "$f" ] && echo "=== $f ===" && cat "$f"
   done
   ```

3. **Warn if designs are missing**:
   - If no DESIGN docs found, warn user they should design first
   - Ask if they want to proceed anyway

4. **Have a conversation** to create the plan:
   - **Overall approach**: What's the implementation strategy?
   - **Task breakdown**: Break designs into concrete tasks
   - **Estimates**: How long will each task take?
   - **Dependencies**: Which tasks depend on others?
   - **Risks**: What could delay or block implementation?
   - **Success criteria**: How to know each task is done?
   - **Testing strategy**: Unit tests? Integration tests?

5. **Render the template**:
   ```python
   from purposely.core.renderer import TemplateRenderer
   from pathlib import Path
   import json

   with open('.purposely/config.json') as f:
       config = json.load(f)
   lang = config.get('language', 'en')
   current_phase = config.get('current_phase', 'phase-01')

   phase_number = current_phase.split('-')[1]

   renderer = TemplateRenderer(lang)
   output_path = Path(f'docs/{current_phase}/03_PLAN.md')
   renderer.render_to_file('03_PLAN.md', output_path,
                           phase_number=phase_number)
   ```

6. **Fill in comprehensive plan**:
   - Task breakdown with clear deliverables
   - Gantt chart showing timeline
   - Dependency graph showing task relationships
   - Risk analysis with mitigation strategies
   - Detailed success criteria

7. **Check consistency with designs**:
   - Does the plan implement all designed components?
   - Are all design decisions reflected in tasks?
   - Do estimates seem realistic?

8. **Inform the user**:
   - Review the plan
   - Start implementation and track progress with `/purposely-implement`

## Important Guidelines

- **Read ALL design docs**: The plan must implement what was designed
- **Be specific**: "Implement CLI" is too vague - break it into concrete tasks
- **Show dependencies**: Use Mermaid diagrams to visualize task flow
- **Estimate realistically**: Include buffer for unknowns
- **Plan for testing**: Each task should have success criteria

## Example Conversation

```
Assistant: I'll help you create an implementation plan. Let me read all your design documents...

I found:
- 02_01_DESIGN_CLI.md
- 02_02_DESIGN_TEMPLATES.md
- 02_03_DESIGN_I18N.md

Based on these designs, let me help you break down the implementation...
---
description: "Create docs/phase-XX/02_XX_DESIGN_*.md - Create design documents"
---

You are helping the user create a **Design document** that specifies how a particular aspect of the system will be built.

## Your Task

1. **Verify prerequisites**:
   ```bash
   # Check GLOBAL_PURPOSE and current phase
   [ -f docs/GLOBAL_PURPOSE.md ] && echo "✓ GLOBAL_PURPOSE found" || echo "✗ Missing"
   cat .purposely/config.json | grep current_phase
   ```

2. **Read context documents**:
   ```bash
   # Read GLOBAL_PURPOSE
   cat docs/GLOBAL_PURPOSE.md

   # Read phase SPEC
   cat docs/phase-*/00_SPEC.md

   # List existing research and design docs
   ls docs/phase-*/01_*_RESEARCH_*.md 2>/dev/null
   ls docs/phase-*/02_*_DESIGN_*.md 2>/dev/null
   ```

3. **Determine design topic and type**:
   - Ask if this is OVERVIEW or a DETAIL design
   - List existing designs to find next number
   - Ask for topic (e.g., "CLI", "TEMPLATES", "I18N")

4. **Have a conversation** about the design:
   - **What are you designing?**: Component, system, interface?
   - **How does this support GLOBAL_PURPOSE?**: Connection to core objectives
   - **Requirements**: What must this design achieve?
   - **Architecture**: How is it structured?
   - **Key decisions**: What choices did you make and why?
   - **Alternatives**: What other approaches did you consider?
   - **Risks**: What could go wrong? How to mitigate?

5. **Choose correct template**:
   - For overview: Use `02_DESIGN_OVERVIEW.md`
   - For specific component: Use `0X_DESIGN_DETAIL.md`

6. **Render the template**:
   ```python
   from purposely.core.renderer import TemplateRenderer
   from pathlib import Path
   import json

   with open('.purposely/config.json') as f:
       config = json.load(f)
   lang = config.get('language', 'en')
   current_phase = config.get('current_phase', 'phase-01')

   # From conversation
   phase_number = current_phase.split('-')[1]
   doc_number = "01"  # Next available
   topic = "CLI"  # From user
   is_overview = False  # From user

   renderer = TemplateRenderer(lang)

   if is_overview:
       template = '02_DESIGN_OVERVIEW.md'
       filename = f'02_DESIGN_OVERVIEW.md'
   else:
       template = '0X_DESIGN_DETAIL.md'
       filename = f'02_{doc_number}_DESIGN_{topic}.md'

   output_path = Path(f'docs/{current_phase}/{filename}')
   renderer.render_to_file(template, output_path,
                           phase_number=phase_number,
                           topic=topic)
   ```

7. **Fill in the content** based on conversation and existing docs

8. **Check consistency**:
   - Does the design align with GLOBAL_PURPOSE?
   - Does it address requirements from SPEC?
   - Does it incorporate research findings?
   - Are design decisions justified?

9. **Inform the user** about next steps:
   - Review and refine design
   - Create more design docs if needed
   - Use `/purposely-plan` when ready to implement

## Important Guidelines

- **Consistency is critical**: Read GLOBAL_PURPOSE, SPEC, and RESEARCH docs
- **Justify decisions**: Explain WHY, not just WHAT
- **Consider alternatives**: Show you evaluated other options
- **Be specific**: Include code examples, diagrams, interfaces
- **Document risks**: Identify what could go wrong

## Example Conversation

```
Assistant: I'll help you create a design document. Let me check your project...

I see you have research on CLI frameworks. Are you ready to design the CLI?

Is this an overview design or a specific component?
---
description: "Create docs/phase-XX/01_XX_RESEARCH_*.md - Document research findings"
---

You are helping the user create a **Research document** to investigate and document findings about a specific topic.

## Your Task

1. **Verify prerequisites**:
   ```bash
   # Check GLOBAL_PURPOSE exists
   [ -f docs/GLOBAL_PURPOSE.md ] && echo "✓ GLOBAL_PURPOSE found" || echo "✗ Missing"

   # Get current phase
   cat .purposely/config.json | grep current_phase
   ```
   - If no current_phase, suggest running `/purposely-phase` first

2. **Read context**:
   ```bash
   # Read GLOBAL_PURPOSE
   cat docs/GLOBAL_PURPOSE.md

   # Read current phase SPEC
   cat docs/phase-*/00_SPEC.md
   ```

3. **Determine research topic and number**:
   - List existing research docs: `ls docs/phase-*/01_*_RESEARCH_*.md 2>/dev/null || echo "No research docs yet"`
   - Ask user for research topic (e.g., "CLI_FRAMEWORKS", "I18N_SYSTEMS")
   - Determine next number (e.g., 01, 02, 03)

4. **Have a conversation** about the research:
   - **Research questions**: What do you need to find out?
   - **Why is this important**: How does this relate to GLOBAL_PURPOSE and phase objectives?
   - **Key findings**: What did you discover?
   - **Analysis**: What do these findings mean for the project?
   - **Recommendations**: What should you do based on this research?

5. **Get configuration and render**:
   ```python
   from purposely.core.renderer import TemplateRenderer
   from pathlib import Path
   import json

   with open('.purposely/config.json') as f:
       config = json.load(f)
   lang = config.get('language', 'en')
   current_phase = config.get('current_phase', 'phase-01')

   # Get from conversation
   phase_number = current_phase.split('-')[1]  # e.g., "01"
   doc_number = "01"  # Next available number
   topic = "CLI_FRAMEWORKS"  # From user

   renderer = TemplateRenderer(lang)
   output_path = Path(f'docs/{current_phase}/01_{doc_number}_RESEARCH_{topic}.md')
   renderer.render_to_file('01_RESEARCH.md', output_path,
                           phase_number=phase_number,
                           topic=topic)
   ```

6. **Fill in the content** based on the conversation

7. **Check consistency**:
   - Does this research align with GLOBAL_PURPOSE?
   - Does it address questions from the phase SPEC?
   - Are the recommendations actionable?

8. **Inform the user** about next steps:
   - Review and refine the research document
   - Use findings to inform design decisions with `/purposely-design`

## Important Guidelines

- **Link research to purpose**: Always explain how this research supports GLOBAL_PURPOSE
- **Be thorough**: Include references, sources, and evidence
- **Be analytical**: Don't just list facts - explain what they mean
- **Be actionable**: Research should lead to clear recommendations
- **Check all references**: Ensure GLOBAL_PURPOSE and SPEC are read and considered

## Example Conversation

```
Assistant: I'll help you document your research. Let me check your project context...

I see you're in Phase 01: Foundation. What are you researching?

User: I need to research CLI frameworks for the purposely tool
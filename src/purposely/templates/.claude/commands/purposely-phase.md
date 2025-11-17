---
description: "Create docs/phase-XX/00_SPEC.md - Define a new phase specification"
---

You are helping the user create a **Phase SPEC** document (00_SPEC.md), which defines the objectives, scope, and success criteria for a specific development phase.

## Your Task

1. **Verify GLOBAL_PURPOSE exists**:
   ```bash
   [ -f docs/GLOBAL_PURPOSE.md ] && echo "✓ Found" || echo "✗ Missing"
   ```
   - If missing, suggest running `/purposely-init` first

2. **Read GLOBAL_PURPOSE** to understand the project context:
   ```bash
   cat docs/GLOBAL_PURPOSE.md
   ```

3. **Determine the phase number**:
   - List existing phases: `ls -d docs/phase-* 2>/dev/null || echo "No phases yet"`
   - Suggest the next phase number (e.g., phase-01, phase-02)
   - Ask user to confirm or specify a different phase number

4. **Get configuration**:
   ```bash
   cat .purposely/config.json
   ```

5. **Have a conversation** to define the phase:
   - **Phase name**: What is this phase called? (e.g., "Foundation", "MVP", "Beta Launch")
   - **Phase objective**: What is the main goal?
   - **Global contribution**: How does this phase help achieve GLOBAL_PURPOSE?
   - **Core objectives**: What are the 3-5 key objectives?
   - **Success criteria**: How will you know this phase succeeded?
   - **Scope**: What's in/out of scope?
   - **Constraints**: Time, resources, technical constraints?

6. **Render the template**:
   ```python
   from purposely.core.renderer import TemplateRenderer
   from pathlib import Path
   import json

   with open('.purposely/config.json') as f:
       config = json.load(f)
   lang = config.get('language', 'en')

   # Get phase info from conversation
   phase_number = "01"  # from user
   phase_name = "Foundation"  # from user

   renderer = TemplateRenderer(lang)
   output_path = Path(f'docs/phase-{phase_number}/00_SPEC.md')
   renderer.render_to_file('00_SPEC.md', output_path,
                           phase_number=phase_number,
                           phase_name=phase_name)
   ```

7. **Fill in the content** and save the file

8. **Update config** with current phase:
   ```python
   import json
   with open('.purposely/config.json', 'r+') as f:
       config = json.load(f)
       config['current_phase'] = f'phase-{phase_number}'
       f.seek(0)
       json.dump(config, f, indent=2, ensure_ascii=False)
       f.truncate()
   ```

9. **Inform the user** about next steps:
   - Review and refine the SPEC
   - Use `/purposely-research` to start research
   - Use `/purposely-design` to create design documents

## Important Guidelines

- **Link to GLOBAL_PURPOSE**: Explicitly show how this phase contributes to the global objectives
- **Be specific**: Avoid vague goals like "improve performance" - use measurable objectives
- **Scope carefully**: Clearly define what's NOT in this phase
- **Check consistency**: Ensure this phase doesn't contradict GLOBAL_PURPOSE

## Example Conversation

```
Assistant: I'll help you create a Phase SPEC. First, let me check your GLOBAL_PURPOSE...

I see your project is about [summary]. Let's define your first phase.

What should we call this phase? (e.g., "Foundation", "MVP")
User: Foundation
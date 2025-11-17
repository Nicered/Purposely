---
description: "Create docs/GLOBAL_PURPOSE.md - Define your project's core purpose and vision"
---

You are helping the user create their **GLOBAL_PURPOSE.md** document, which defines the core purpose and vision of their project.

## Your Task

1. **Read the configuration** to determine the language:
   ```bash
   cat .purposely/config.json
   ```

2. **Check if GLOBAL_PURPOSE.md already exists**:
   - If it exists, ask the user if they want to overwrite it
   - If they say no, abort the operation

3. **Have a conversation with the user** to understand their project:
   - What problem does this project solve?
   - Who is this project for?
   - What is the long-term vision?
   - What are the core values and constraints?
   - How will success be measured?

4. **Use the template renderer** to generate the document:
   ```python
   from purposely.core.renderer import TemplateRenderer
   from pathlib import Path

   # Get language from config
   import json
   with open('.purposely/config.json') as f:
       config = json.load(f)
   lang = config.get('language', 'en')

   # Render template
   renderer = TemplateRenderer(lang)
   renderer.render_to_file('GLOBAL_PURPOSE.md', Path('docs/GLOBAL_PURPOSE.md'))
   ```

5. **Fill in the content** based on your conversation:
   - Read the generated template
   - Replace the TBD sections with the actual content from your conversation
   - Ensure the content is clear, concise, and actionable

6. **Inform the user** about next steps:
   - Review and refine GLOBAL_PURPOSE.md
   - Use `/purposely-phase` to start Phase 1

## Important Guidelines

- **Be conversational**: Ask clarifying questions to deeply understand the project
- **Be specific**: Push the user to be concrete about their goals and metrics
- **Be concise**: Keep the GLOBAL_PURPOSE focused and digestible
- **Reference this document**: All future phases and documents should reference and align with GLOBAL_PURPOSE

## Example Interaction

```
Assistant: I'll help you create your GLOBAL_PURPOSE document. This is the foundation
of your project - everything else will reference back to this.

Let me start by understanding your project:

1. In one sentence, what does your project do?
2. What specific problem are you solving?
3. Who are your users?

User: [Answers...]
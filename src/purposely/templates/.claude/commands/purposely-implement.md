---
description: "Create/update docs/phase-XX/04_IMPLEMENTATION.md - Track what was actually built"
---

You are helping the user document their **Implementation** - what was actually built, challenges faced, and decisions made during development.

## Your Task

1. **Verify prerequisites**:
   ```bash
   # Check required docs
   [ -f docs/GLOBAL_PURPOSE.md ] && echo "✓ GLOBAL_PURPOSE" || echo "✗ Missing"
   cat .purposely/config.json | grep current_phase

   # Check PLAN exists
   ls docs/phase-*/03_PLAN.md 2>/dev/null || echo "⚠️ No PLAN found"
   ```

2. **Read the context**:
   ```bash
   # Read GLOBAL_PURPOSE
   cat docs/GLOBAL_PURPOSE.md

   # Read SPEC
   cat docs/phase-*/00_SPEC.md

   # Read PLAN (if exists)
   [ -f docs/phase-*/03_PLAN.md ] && cat docs/phase-*/03_PLAN.md

   # Check if IMPLEMENTATION already exists
   [ -f docs/phase-*/04_IMPLEMENTATION.md ] && cat docs/phase-*/04_IMPLEMENTATION.md
   ```

3. **Determine the operation**:
   - If 04_IMPLEMENTATION.md exists: Update it
   - If it doesn't exist: Create it

4. **Have a conversation** about implementation:
   - **What did you build?**: Completed tasks, features, components
   - **Commits/PRs**: Link to specific code changes
   - **Challenges**: What problems did you encounter? How did you solve them?
   - **Deviations from plan**: What changed and why?
   - **Learnings**: What did you discover during implementation?
   - **Next steps**: What needs to happen before the next phase?

5. **Render or update**:
   ```python
   from purposely.core.renderer import TemplateRenderer
   from pathlib import Path
   import json

   with open('.purposely/config.json') as f:
       config = json.load(f)
   lang = config.get('language', 'en')
   current_phase = config.get('current_phase', 'phase-01')

   phase_number = current_phase.split('-')[1]
   output_path = Path(f'docs/{current_phase}/04_IMPLEMENTATION.md')

   if not output_path.exists():
       # Create new
       renderer = TemplateRenderer(lang)
       renderer.render_to_file('04_IMPLEMENTATION.md', output_path,
                               phase_number=phase_number)
       # Then fill it in
   else:
       # Read existing and update sections
       pass
   ```

6. **Fill in or update the content**:
   - Log completed tasks with links to code
   - Document challenges and solutions
   - Note any deviations from the plan
   - Record key learnings

7. **Check consistency**:
   - Does the implementation achieve GLOBAL_PURPOSE objectives?
   - Were SPEC requirements met?
   - If there are deviations from PLAN, are they justified?

8. **Inform the user**:
   - Implementation is documented
   - Review before starting next phase
   - Consider updating GLOBAL_PURPOSE if learnings changed the vision

## Important Guidelines

- **Be honest**: Document what actually happened, not what was planned
- **Link to code**: Include commit SHAs, PR numbers, file paths
- **Explain deviations**: If you deviated from the plan, explain why
- **Capture learnings**: What would you do differently next time?
- **Check alignment**: Does the implementation still serve GLOBAL_PURPOSE?

## Example Conversation

```
Assistant: I'll help you document your implementation. Let me check what you planned...

I see you planned 10 tasks. Which tasks did you complete?

User: I finished tasks 1-5 today.
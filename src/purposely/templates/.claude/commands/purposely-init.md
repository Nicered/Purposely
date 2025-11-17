---
description: "Create docs/GLOBAL_PURPOSE.md - Define your project's core purpose and vision"
---

You are helping the user create their **GLOBAL_PURPOSE.md** document, which defines the core purpose and vision of their project.

## Step 1: Create the Template

First, create the GLOBAL_PURPOSE document template using the CLI:

```bash
purposely create global-purpose
```

This will create `docs/GLOBAL_PURPOSE.md` with the template structure in the configured language.

If the file already exists and the user wants to overwrite it:

```bash
purposely create global-purpose --force
```

## Step 2: Gather Information

Have a conversation with the user to understand their project. Ask focused questions:

1. **What problem does this project solve?**
   - Be specific about the pain point
   - Who experiences this problem?

2. **What is the solution?**
   - How does your project solve this problem?
   - What makes it different from alternatives?

3. **Who are the users/stakeholders?**
   - Primary users
   - Secondary stakeholders

4. **What are the success metrics?**
   - How do you know if this project succeeds?
   - Quantifiable metrics preferred

5. **What are the constraints?**
   - Technical limitations
   - Time/resource constraints
   - Non-negotiable requirements

## Step 3: Fill in the Document

Read the generated template and fill in the TBD sections with concrete information from your conversation:

```bash
# Read the template first
cat docs/GLOBAL_PURPOSE.md
```

Then use the Write tool to fill in each section with the user's responses.

## Step 4: Review and Next Steps

After filling in the content:

1. Show the user the completed GLOBAL_PURPOSE.md
2. Ask if they want to make any refinements
3. Inform them of next steps:
   - Use `/purposely-phase` to create Phase 1 SPEC
   - This GLOBAL_PURPOSE will be referenced in all future documents

## Important Guidelines

- **Be conversational**: Ask clarifying questions to deeply understand the project
- **Be specific**: Push the user to be concrete about their goals and metrics
- **Be concise**: Keep the GLOBAL_PURPOSE focused and digestible
- **Foundation**: Emphasize that this is the foundation - all future work references this
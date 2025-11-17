# Best Practices

Practical tips and know-how for effective Purpose-Driven Development.

## Writing GLOBAL_PURPOSE

### ✅ Good GLOBAL_PURPOSE

```markdown
## Why
To solve the problem of developers forgetting their project's purpose
mid-development and adding unnecessary features, leading to unfinished projects

## Problem
- 70% of projects started with initial enthusiasm end up unfinished
- Developers forget "why" during development, causing feature creep
- Team members develop different understandings of project purpose

## Solution
A documentation-centric framework and AI assistant that enforces
referencing GLOBAL_PURPOSE at every development stage

## Success Metrics
- 80%+ project completion rate for users
- <10% off-purpose feature additions
- 50% reduction in documentation time
```

**Why it's good:**
- Clear and relatable Why
- Concrete and measurable Problem
- Concise and understandable Solution
- Quantitative Success Metrics

### ❌ Bad GLOBAL_PURPOSE

```markdown
## Why
To make better development tools

## Problem
Development is difficult

## Solution
Will make good tools

## Success Metrics
Users are satisfied
```

**Why it's bad:**
- Why is too abstract
- Problem is not concrete
- Solution is vague
- Success Metrics unmeasurable

### Core Principles

1. **Be Specific**: Not "better" but "what is better and how"
2. **Be Measurable**: Not "satisfied" but "NPS 50+"
3. **Be Relatable**: Readers should think "Yes, me too!"
4. **Summarizable in One Sentence**: Like an elevator pitch

---

## Dividing Phases

### ✅ Good Phase Division

```
Phase 1: CLI Basic Infrastructure (2 weeks)
- purposely init command
- Template system
- i18n support

Phase 2: Document Generation Commands (2 weeks)
- create subcommands
- 7 document type support
- Write tests

Phase 3: AI Integration (3 weeks)
- Claude Code slash commands
- Auto alignment validation
- Interactive document creation
```

**Why it's good:**
- Each Phase independently completable
- Completable in 1-3 weeks
- Clear scope

### ❌ Bad Phase Division

```
Phase 1: Implement all features (6 months)
- CLI, Web UI, AI, deployment, docs, etc.
```

**Why it's bad:**
- Too large
- No intermediate achievements
- Easy to lose purpose

### Core Principles

1. **1-4 Week Completion**: Larger than that, split it
2. **Independently Completable**: This Phase alone provides value
3. **Clear Boundaries**: Clear In Scope / Out of Scope
4. **Incremental Value**: Each Phase produces usable results

---

## Document Writing Timing

### ✅ Correct Order

```
1. Write SPEC
2. Review and approve SPEC
3. RESEARCH (if needed)
4. Write DESIGN
5. Review DESIGN
6. Start coding
7. Write IMPLEMENTATION concurrently
```

### ❌ Wrong Order

```
1. Just start coding
2. Write docs later (never happens)
```

### Core Principles

1. **Documents First**: Document design before coding
2. **Write Now**: There is no "later"
3. **Update Together**: Code and docs together
4. **Use Reviews**: Validate design through doc reviews

---

## Checking GLOBAL_PURPOSE Alignment

### Questions Before Every Task

Before adding new feature:

1. **Which part of GLOBAL_PURPOSE does this feature support?**
   - Can't answer → Unnecessary feature

2. **Is this feature essential for achieving Success Metrics?**
   - No → Low priority

3. **Does this feature directly contribute to solving the Problem?**
   - No → Scope creep

### Real Example

**Situation:** "Dark mode would be nice"

**Questions:**
1. Which part of GLOBAL_PURPOSE does it support?
   - Unrelated to "project completion rate improvement"
2. Essential for achieving Success Metrics?
   - No
3. Contributes to solving Problem?
   - No

**Conclusion:** Unnecessary for Phase 1. Nice-to-have for later.

---

## Maintaining Document Quality

### SPEC Checklist

After writing SPEC, verify:

- [ ] Is Objective summarizable in one sentence?
- [ ] Are concrete deliverables listed in Scope?
- [ ] Is Out of Scope specified?
- [ ] Are Success Criteria in checklist format?
- [ ] Is connection to GLOBAL_PURPOSE clear?

### DESIGN Checklist

- [ ] Are diagrams included?
- [ ] Are public APIs specified?
- [ ] Are dependencies clear?
- [ ] Can you understand this doc alone after 6 months?

### IMPLEMENTATION Checklist

- [ ] Is "What Changed" written honestly?
- [ ] Are failed attempts recorded?
- [ ] Are there notes for next Phase?
- [ ] Are lessons learned specific?

---

## Claude Code Usage Tips

### When to Use Slash Commands

| Situation | Command | Reason |
|-----------|---------|--------|
| Project start | `/purposely-init` | Help write GLOBAL_PURPOSE |
| Phase start | `/purposely-phase` | Write and validate SPEC |
| Tech choice dilemma | `/purposely-research` | Structure investigation |
| Architecture design | `/purposely-design` | Document design |
| Before implementation | `/purposely-plan` | Establish work plan |
| During/after implementation | `/purposely-implement` | Write log |

### Tips for Talking with Claude

1. **Ask Specifically**: "What should I do?" → "A vs B, which is better?"
2. **Provide Context**: Show GLOBAL_PURPOSE first
3. **Iterative Improvement**: If first result unsatisfactory, request "more specific"
4. **Request Validation**: "Check if this aligns with GLOBAL_PURPOSE"

---

## Team Collaboration

### Document Review Process

1. **SPEC Review (Before Phase start)**
   - Confirm all team members understand Objective
   - Agree on Out of Scope
   - Verify Success Criteria are verifiable

2. **DESIGN Review (Before coding)**
   - Agree on architecture
   - Review API design
   - Consider alternatives

3. **IMPLEMENTATION Review (After Phase completion)**
   - Share what was learned
   - Improvements for next Phase

### Async Collaboration

With documents:
- Collaborate regardless of timezone
- Easy new team member onboarding
- Traceable decision rationale

### Team Conventions

Things team should agree on:
- [ ] Which documents are mandatory
- [ ] Who reviews documents and when
- [ ] Who's responsible for document updates
- [ ] Process for GLOBAL_PURPOSE changes

---

## Common Mistakes and Solutions

### Mistake 1: "I'll write docs later"

**Problem:**
- Later never comes
- Forget context
- End up proceeding without docs

**Solution:**
- Enforce doc writing before coding
- Make docs mandatory in PRs
- Rule: "No docs, no review"

### Mistake 2: "Changing GLOBAL_PURPOSE too often"

**Problem:**
- Shaky purpose → shaky project
- Team confusion

**Solution:**
- GLOBAL_PURPOSE changes require full team consensus
- Change only truly fundamental issues
- Analyze impact on all docs when changing

### Mistake 3: "Continuously expanding Phase scope"

**Problem:**
- Repeated "just one more"
- Never finish

**Solution:**
- Strictly adhere to SPEC's Out of Scope
- "In Phase 2" principle
- Focus only on Success Criteria achievement

### Mistake 4: "Docs out of sync with code"

**Problem:**
- Loss of doc trust
- Eventually stop reading

**Solution:**
- Update docs when code changes
- Include doc updates in PRs
- Regular doc audits

---

## Measurement and Improvement

### Metrics to Track

Project level:
- Phase completion rate
- Estimated vs actual time
- GLOBAL_PURPOSE change count

Individual level:
- Doc writing time
- Code rework rate after docs
- Off-purpose feature proposal count

### Retrospective Questions

After Phase completion:
1. How often did we reference GLOBAL_PURPOSE?
2. Which document was most useful?
3. What problems would have occurred without docs?
4. What to improve in next Phase?

---

## Checklists

### At Project Start

- [ ] GLOBAL_PURPOSE written
- [ ] All team members understand GLOBAL_PURPOSE
- [ ] Phase 1 SPEC written and agreed
- [ ] Doc writing process agreed

### At Each Phase Start

- [ ] SPEC written and reviewed
- [ ] GLOBAL_PURPOSE alignment verified
- [ ] Out of Scope clarified
- [ ] Success Criteria measurable

### Weekly

- [ ] Re-read GLOBAL_PURPOSE
- [ ] Verify ongoing work aligns with purpose
- [ ] Check docs needing updates

### At Phase Completion

- [ ] IMPLEMENTATION doc written
- [ ] All Success Criteria achieved
- [ ] Retrospective conducted
- [ ] Next Phase planned

---

## Closing Advice

### "Done is Better Than Perfect"

Like code, docs:
- Can't be perfect from start
- Improve incrementally
- Write first, then improve

### "Never Forget the Purpose"

Core of PDD:
- GLOBAL_PURPOSE at center of everything
- Read often, check often
- Criterion for all decisions

### "Docs Are Team Memory"

After 6 months:
- Can't understand from code alone
- Docs restore context
- Consideration for future team members

---

**Congratulations!** You're now ready to start Purpose-Driven Development.

To start your project: [Getting Started](getting-started.md)

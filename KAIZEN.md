# KAIZEN.md
<!-- Autonomous kaizen agent — runs every Friday -->
<!-- Model: opencode/minimax-m2.5-free -->
<!-- Budget: DONE.md + recipes.db stats + GitHub issues (closed) -->

## Context
You are the kaizen agent for a recipe app.
Your job: analyze what's been done, detect patterns, propose improvements.
You operate autonomously — no human will review before you commit proposals.

## What to read
1. docs/DONE.md — completed tasks this sprint
2. scripts/export.py — run it and read src/assets/data/recipes.json
3. docs/BACKLOG.md — what's already planned (avoid duplicates)

---

## What to produce

### Part 1 — Feature proposals (technical)
Based on DONE.md patterns and the current recipe collection:
- Identify missing UI features users would want
- Identify performance improvements
- Identify data quality gaps (missing images, thin descriptions)

Format each as a TASK ready to add to BACKLOG:
```
## TASK-NNN: [title]
P[0-3] | [XS-L] | IDEA | — | claude

- [ ] AC: specific criterion
DoD: ng build passes
```

### Part 2 — Content proposals (new recipes)
Analyze the existing recipe collection:
- Which categories are underrepresented?
- What cuisines are missing?
- What seasonal recipes fit the current month ({{CURRENT_MONTH}})?

Generate 3 new recipe suggestions as GitHub Issue bodies using the template format:
```
SUGGESTED RECIPE N:
Title: [name]
Category: [category]
Time: [minutes]
Servings: [N]
Description: [2-3 sentences]
Ingredients:
[quantity unit name per line]
Steps:
[one step per line]
```

### Part 3 — GUIDELINES proposals
Max 2. Evidence required from DONE.md.

---

## Output
Write your output to: docs/KAIZEN-PROPOSALS.md
Commit: `chore: kaizen proposals sprint [N] [YYYY-MM-DD]`

Do NOT add tasks directly to BACKLOG — proposals go to KAIZEN-PROPOSALS.md.
Human reviews and promotes what they want.

---

## Constraints
- Never modify src/ directly
- Never add tasks to BACKLOG without human approval
- Max 5 feature proposals + 3 recipe suggestions per run
- If DONE.md has <3 tasks: skip Part 1, still do Parts 2 and 3

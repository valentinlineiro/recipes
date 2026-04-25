# SPRINT.md

## Sprint 1 — Foundation
**Period:** 2026-04-25 → 2026-05-02
**Goal:** Working recipe app deployed to GitHub Pages
**Committed:** 9

---

## TASK-001: Initialize Angular project
P0 | M | READY | Sprint 1 | claude

- [ ] .gitignore created first (node_modules/, dist/, *.db)
- [ ] `ng new recipes --standalone --routing --style=css` executed
- [ ] Default app.component cleaned up
- [ ] `ng build` passes with zero errors
- [ ] README.md updated

DoD: `ng build` passes | .gitignore committed before node_modules

---

## TASK-002: Create SQLite schema + seed data + export script
P0 | M | READY | Sprint 1 | claude

- [ ] scripts/export.py created
- [ ] recipes.db created with schema
- [ ] 8 seed recipes inserted
- [ ] `python scripts/export.py` produces valid JSON
- [ ] JSON: `{ "version": 1, "recipes": [...] }`
- [ ] recipes.db in .gitignore

DoD: export script runs | JSON valid | 8 recipes

---

## TASK-003: Define TypeScript models
P0 | S | READY | Sprint 1 | claude

- [ ] src/app/models/recipe.model.ts created
- [ ] Interfaces: Recipe, Ingredient, Step, RecipesData
- [ ] No `any`

DoD: TypeScript compiles

**Depends:** TASK-002

---

## TASK-004: Implement RecipeService
P0 | S | READY | Sprint 1 | claude

- [ ] src/app/services/recipe.service.ts created
- [ ] Loads recipes.json via HttpClient
- [ ] Signals: recipes, search(query), getById(id)
- [ ] Unit test for search()

DoD: compiles | test passes

**Depends:** TASK-003

---

## TASK-005: Implement RecipeListComponent
P1 | M | READY | Sprint 1 | claude

- [ ] Standalone component
- [ ] Grid of recipe cards
- [ ] Filters via RecipeService
- [ ] Navigate to /recipes/:id
- [ ] Responsive: 1/2/3 columns
- [ ] Empty state

DoD: `ng build` passes | cards visible | navigation works

**Depends:** TASK-004

---

## TASK-006: Implement RecipeDetailComponent
P1 | M | READY | Sprint 1 | claude

- [ ] Route: /recipes/:id
- [ ] Title, description, time, servings, category
- [ ] Ingredients list
- [ ] Numbered steps
- [ ] Back button
- [ ] 404 state

DoD: `ng build` passes | full recipe visible

**Depends:** TASK-004

---

## TASK-007: SearchBarComponent + routing
P1 | S | READY | Sprint 1 | claude

- [ ] Standalone component
- [ ] Input with 300ms debounce
- [ ] Category dropdown
- [ ] app.routes.ts configured

DoD: `ng build` passes | search works | categories work

**Depends:** TASK-005

---

## TASK-008: Styling — clean minimal design
P2 | M | READY | Sprint 1 | claude

- [ ] CSS variables in styles.css
- [ ] Cards with shadow + hover
- [ ] Mobile-first responsive
- [ ] No external CSS framework
- [ ] Favicon

DoD: `ng build` passes | looks good mobile + desktop

**Depends:** TASK-005, TASK-006

---

## TASK-009: GitHub Actions deploy to GH Pages
P2 | S | READY | Sprint 1 | claude

- [ ] .github/workflows/deploy.yml created
- [ ] Push to main → build → deploy
- [ ] Base href matches repo name

DoD: workflow runs | site live at github.io

---

## Sprint log

| Date | Event |
|------|-------|
| 2026-04-25 | Sprint 1 started — recipes greenfield |

---

## Blocked
_None_

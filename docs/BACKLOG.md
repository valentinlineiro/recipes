# BACKLOG.md

## Status vocabulary
`IDEA` → `READY` → `IN_PROGRESS` → `REVIEW` → `DONE` | `BLOCKED` | `REJECTED`

---

## TASK-001: Initialize Angular project
P0 | M | READY | Sprint 1 | claude

- [ ] .gitignore created first (node_modules/, dist/, *.db)
- [ ] `ng new recipes --standalone --routing --style=css` executed
- [ ] package.json name: recipes
- [ ] Default app.component cleaned up (no boilerplate content)
- [ ] `ng build` passes with zero errors
- [ ] README.md updated with: what this is + how to run locally

DoD: `ng build` passes | .gitignore committed before node_modules

---

## TASK-002: Create SQLite schema + seed data + export script
P0 | M | READY | Sprint 1 | claude

- [ ] `scripts/export.py` created — reads recipes.db, writes src/assets/data/recipes.json
- [ ] `recipes.db` created with schema (recipes, ingredients, steps tables)
- [ ] 8 seed recipes inserted (varied categories: breakfast, lunch, dinner, dessert)
- [ ] Each recipe has: title, description, time_minutes, servings, category, ingredients, steps
- [ ] `python scripts/export.py` produces valid JSON
- [ ] JSON structure: `{ "version": 1, "recipes": [...] }`
- [ ] recipes.db added to .gitignore — only JSON committed

DoD: export script runs without error | JSON valid | 8 recipes in output

**Context-budget:** docs/agents/DO.md + this task

---

## TASK-003: Define TypeScript models
P0 | S | READY | Sprint 1 | claude

- [ ] `src/app/models/recipe.model.ts` created
- [ ] Interfaces: Recipe, Ingredient, Step, RecipesData
- [ ] All fields typed — no `any`
- [ ] Matches JSON structure from TASK-002

DoD: TypeScript compiles with zero errors

**Depends:** TASK-002
**Context-budget:** docs/agents/DO.md + this task + src/assets/data/recipes.json

---

## TASK-004: Implement RecipeService
P0 | S | READY | Sprint 1 | claude

- [ ] `src/app/services/recipe.service.ts` created
- [ ] Loads recipes.json via HttpClient
- [ ] Exposes: `recipes` signal, `getById(id)` method, `search(query)` method
- [ ] search() filters by title and category (case-insensitive)
- [ ] Handles loading and error states

DoD: service compiles | unit test for search() passes

**Depends:** TASK-003
**Context-budget:** docs/agents/DO.md + this task + src/app/models/

---

## TASK-005: Implement RecipeListComponent
P1 | M | READY | Sprint 1 | claude

- [ ] `src/app/components/recipe-list/` created standalone component
- [ ] Displays grid of recipe cards (title, category, time, image placeholder)
- [ ] Accepts search query input — filters via RecipeService
- [ ] Clicking a card navigates to /recipes/:id
- [ ] Responsive: 1 column mobile, 2 tablet, 3 desktop
- [ ] Empty state when no results found

DoD: `ng build` passes | cards visible | navigation works

**Depends:** TASK-004
**Context-budget:** docs/agents/DO.md + this task + src/app/services/ + src/app/models/

---

## TASK-006: Implement RecipeDetailComponent
P1 | M | READY | Sprint 1 | claude

- [ ] `src/app/components/recipe-detail/` created standalone component
- [ ] Route: /recipes/:id
- [ ] Displays: title, description, time, servings, category
- [ ] Displays ingredients list with quantity + unit + name
- [ ] Displays numbered steps
- [ ] Back button → /recipes
- [ ] 404 state if recipe not found

DoD: `ng build` passes | full recipe visible | back navigation works

**Depends:** TASK-004
**Context-budget:** docs/agents/DO.md + this task + src/app/services/ + src/app/models/

---

## TASK-007: Implement SearchBarComponent + routing
P1 | S | READY | Sprint 1 | claude

- [ ] `src/app/components/search-bar/` created standalone component
- [ ] Input field with debounce (300ms)
- [ ] Category filter dropdown (All, Breakfast, Lunch, Dinner, Dessert)
- [ ] Emits search query to RecipeListComponent via signal or @Output
- [ ] app.routes.ts configured: / → RecipeList, /recipes/:id → RecipeDetail

DoD: `ng build` passes | search filters results | category filter works

**Depends:** TASK-005
**Context-budget:** docs/agents/DO.md + this task + src/app/components/recipe-list/

---

## TASK-008: Styling — clean minimal design
P2 | M | READY | Sprint 1 | claude

- [ ] CSS variables in styles.css: colors, spacing, typography
- [ ] Recipe cards: clean white card, shadow, hover state
- [ ] Typography: system font stack, readable sizes
- [ ] Mobile-first responsive layout
- [ ] No external CSS framework — vanilla CSS only
- [ ] Favicon added (emoji or simple SVG)

DoD: `ng build` passes | looks good on mobile + desktop

**Depends:** TASK-005, TASK-006

---

## TASK-009: GitHub Actions deploy to GH Pages
P2 | S | READY | Sprint 1 | claude

- [ ] `.github/workflows/deploy.yml` created
- [ ] Triggers on push to main
- [ ] Steps: checkout → setup node → npm ci → ng build --base-href → deploy to gh-pages
- [ ] Uses `peaceiris/actions-gh-pages` or `JamesIves/github-pages-deploy-action`
- [ ] Base href matches repo name in angular.json

DoD: workflow runs without error | site accessible at github.io URL

**Context-budget:** docs/agents/DO.md + this task + angular.json

---

## ── BACKLOG (not in sprint 1) ────────────────────────────────────

## TASK-010: Print-friendly recipe view
P3 | S | BACKLOG | — | claude

- [ ] `@media print` CSS for clean printable recipe
- [ ] Hide nav, search, back button when printing

## TASK-011: Recipe categories page
P3 | S | BACKLOG | — | claude

- [ ] /categories route showing all categories as tiles
- [ ] Clicking a category filters recipe list

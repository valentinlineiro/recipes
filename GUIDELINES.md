# GUIDELINES.md

## CORE

- Commits follow prefix table in docs/agents/DO.md
- Every PR references a TASK-ID
- No agent merges its own PR
- `ng build` must pass before any PR is opened
- No runtime dependencies beyond Angular core — zero external libs
- No backend code — static files only
- .gitignore committed before any npm install

---

## Angular conventions

- Standalone components only — no NgModules
- Signals for state — no BehaviorSubject or RxJS for local state
- CSS per component — no global styles except reset + variables in styles.css
- Lazy load route components — RecipeDetailComponent loaded on demand
- No `any` in TypeScript — all models fully typed

---

## Data conventions

- Single source of truth: `recipes.db`
- Export script: `scripts/export.py` → `src/assets/data/recipes.json`
- Run export before build when recipes change: `python scripts/export.py`
- JSON schema version tracked in recipes.json root: `{ "version": 1, "recipes": [...] }`

---

## Deploy conventions

- GH Pages serves from `gh-pages` branch
- Base href must match repo name: `/<repo-name>/`
- GitHub Actions workflow: `.github/workflows/deploy.yml`
- Never push dist/ to main

---

## Rules changelog

| Rule | Added | Evidence |
|------|-------|----------|
| No external libs | Sprint 1 | ADR-001 — static site constraint |
| ng build before PR | Sprint 1 | Static site has no runtime error recovery |

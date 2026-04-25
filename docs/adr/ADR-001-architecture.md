# ADR-001: Core architecture — static Angular app on GitHub Pages

**Date:** 2026-04-25
**Status:** ACCEPTED
**Deciders:** Valen

---

## Context

Build a recipe app that:
- Works as a GitHub Pages static site (no server)
- Has a proper database for recipe management in development
- Uses a familiar stack (Angular)
- Can be built and deployed automatically

## Decision

**Angular 21 standalone + JSON static + SQLite as dev-only source + GitHub Actions**

Data flow:
```
recipes.db (SQLite, dev only)
    └── scripts/export.py → src/assets/data/recipes.json
                                  └── Angular RecipeService (signals)
                                            └── components
```

## Rationale

- **No backend at runtime:** GH Pages only serves static files. Flask would require a server.
- **SQLite as dev source:** Better than editing JSON directly. Queries, relationships, integrity.
- **JSON at runtime:** Angular can fetch local JSON assets. No WASM complexity. Works offline.
- **Signals over RxJS:** Angular 21 pattern. Simpler, less boilerplate.
- **Standalone components:** No NgModules overhead. Consistent with apps-platform.

## Consequences

**Positive:**
- Zero hosting cost
- No backend to maintain
- Data editing via SQLite tools (DB Browser, etc.)
- Fast build → deploy pipeline

**Negative / trade-offs:**
- No real-time updates — rebuild required to publish new recipes
- No user-generated content (no forms that persist)
- Export script required to sync db → JSON

---

*This ADR is permanent. To add user-generated content, create a new ADR.*

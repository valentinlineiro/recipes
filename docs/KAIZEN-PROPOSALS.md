# KAIZEN-PROPOSALS.md

Generated: 2026-05-15

---

## Part 1 — Feature Proposals

Based on DONE.md patterns and current recipe collection analysis:

### Observations from DONE.md (Sprint 1)
- All 9 tasks completed: project init, data layer, models, services, components, routing, styling, deployment
- Core MVP is functional
- No search/filter features beyond basic text search
- No user personalization features

### Data Quality Issues Detected
- **CRITICAL BUG**: recipes.json has severe duplication — each ingredient and step is repeated 6 times per recipe
- Likely caused by export script bug in `scripts/export.py`
- This bloats the JSON file significantly and may cause rendering issues

### UI Feature Gaps
- No category filtering on list page (only search)
- No favorites/bookmarks functionality
- No recipe images (all have image placeholder)
- No lazy loading for recipes

---

## TASK-012: Fix recipe data export bug (duplicate entries)
P0 | S | IDEA | — | kaizen

- [ ] AC: Run `python scripts/export.py` and verify no duplicate ingredients/steps
- [ ] AC: recipes.json contains exactly 1 set of ingredients and steps per recipe

DoD: export produces clean JSON | ng build passes

---

## TASK-013: Add category filter UI
P1 | M | IDEA | — | kaizen

- [ ] AC: RecipeListComponent shows category filter buttons (Breakfast, Lunch, Dinner, Dessert)
- [ ] AC: Clicking a category filters the recipe list
- [ ] AC: "All" button resets filter

DoD: ng build passes | category filter works

---

## TASK-014: Add favorites functionality
P1 | M | IDEA | — | kaizen

- [ ] AC: Heart icon on each recipe card
- [ ] AC: Clicking heart toggles favorite state (persisted in localStorage)
- [ ] AC: /favorites route shows only favorited recipes

DoD: ng build passes | favorites persist across sessions

---

## TASK-015: Add recipe images
P2 | L | IDEA | — | kaizen

- [ ] AC: Recipes have image field in JSON
- [ ] AC: RecipeList shows thumbnail images
- [ ] AC: RecipeDetail shows hero image

DoD: ng build passes | images render correctly

---

## TASK-016: Implement lazy loading for recipe list
P2 | S | IDEA | — | kaizen

- [ ] AC: Initial load shows 10 recipes
- [ ] AC: "Load More" button fetches next batch
- [ ] AC: Smooth transition when loading more

DoD: ng build passes | lazy loading works

---

## Part 2 — Content Proposals (New Recipes)

### Recipe Collection Analysis
- **Current categories**: breakfast (1), lunch (1), dinner (1), dessert (1) — very limited
- **Cuisines represented**: Italian (Carbonara), American (cookies), Mediterranean (Greek salad) — mostly Western
- **Missing cuisines**: Asian, Mexican, Indian, Japanese, Thai
- **Current month**: May (late spring) — seasonal ingredients: asparagus, peas, strawberries, tomatoes

### Gaps Identified
1. No Asian recipes
2. No Mexican recipes
3. No quick weeknight dinners (< 20 min)
4. No vegetarian main dishes
5. No spring seasonal recipes

---

### SUGGESTED RECIPE 1
Title: Sesame Noodles with Vegetables
Category: dinner
Time: 20
Servings: 4
Description: Quick sesame peanut noodles with crisp spring vegetables. Perfect for busy weeknights in late spring.

Ingredients:
200g wheat noodles
2 tbsp sesame paste
1 tbsp soy sauce
1 tbsp rice vinegar
1 tsp sugar
2 tbsp vegetable oil
1 cup shredded carrots
1 cup edamame beans
2 green onions, sliced
1 tbsp sesame seeds

Steps:
Cook noodles according to package directions, drain and rinse.
Whisk sesame paste, soy sauce, rice vinegar, sugar, and 2 tbsp water.
Heat oil in a wok over high heat.
Stir-fry carrots and edamame for 2 minutes.
Add noodles and sauce, toss for 3 minutes.
Top with green onions and sesame seeds.

---

### SUGGESTED RECIPE 2
Title: Spring Asparagus Risotto
Category: dinner
Time: 35
Servings: 4
Description: Creamy Italian risotto with fresh spring asparagus tips. A elegant spring dinner that's worth the stir.

Ingredients:
300g arborio rice
1 liter vegetable broth
1 bunch asparagus, trimmed
1 small onion, diced
1/2 cup white wine
3 tbsp butter
1/2 cup parmesan, grated
Salt and pepper to taste

Steps:
Bring broth to a simmer in a separate pot.
Cut asparagus tips off, chop remaining stalks.
Cook asparagus stalks in broth for 10 minutes, strain and keep broth.
Sauté onion in 1 tbsp butter until soft.
Add rice, toast for 2 minutes.
Add wine, stir until absorbed.
Add broth one ladle at a time, stirring constantly.
After 15 minutes, add asparagus tips.
When rice is tender, remove from heat.
Stir in remaining butter and parmesan.
Season and serve immediately.

---

### SUGGESTED RECIPE 3
Title: Strawberry Margarita Mocktail
Category: dessert
Time: 10
Servings: 2
Description: Refreshing non-alcoholic strawberry lime drink perfect for spring gatherings. Sweet, tangy, and beautifully pink.

Ingredients:
1 cup fresh strawberries
1/2 cup fresh lime juice
2 tbsp honey
1 cup sparkling water
Ice
Lime slices for garnish

Steps:
Blend strawberries with lime juice and honey until smooth.
Strain through a fine mesh if desired.
Fill glasses with ice.
Divide strawberry mixture between glasses.
Top with sparkling water.
Garnish with lime slices and serve.

---

## Part 3 — Guidelines Proposals

### Guideline 1: Fix data export to prevent duplication
**Evidence**: recipes.json shows each ingredient and step repeated 6 times. This is clearly a bug in the export script that needs fixing before adding more recipes.

**Proposal**: Add a validation step to export.py that verifies no duplicate entries, and add a test case in the DoD: "export produces JSON with no duplicate ingredients or steps"

---

### Guideline 2: Include iteration count in DONE.md
**Evidence**: DONE.md shows all tasks with 0 iterations. This may be unrealistic for complex tasks.

**Proposal**: Track actual iteration count (how many times a task was attempted) to better estimate sprint capacity. Add as a column in DONE.md table.
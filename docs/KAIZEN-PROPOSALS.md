# KAIZEN-PROPOSALS.md

Generated: 2026-05-01

---

## Part 1 — Feature Proposals

### TASK-012: Fix duplicate data in recipes.json
P0 | XS | IDEA | — | kaizen

- [ ] AC: Run scripts/export.py to regenerate clean JSON without duplicates
- [ ] Each ingredient should appear once per recipe
- [ ] Each step should appear once per recipe
- [ ] Verify recipes.json has valid structure

DoD: recipes.json passes JSON validation | No duplicate entries

**Evidence:** recipes.json lines 12-221 show each ingredient repeated 6x, same for steps

---

### TASK-013: Add recipe image support
P1 | S | IDEA | — | kaizen

- [ ] Add `image_url` field to Recipe model
- [ ] Add placeholder images or use external food image APIs
- [ ] Display images in RecipeListComponent cards
- [ ] Display hero image in RecipeDetailComponent

DoD: Images display in both list and detail views | ng build passes

**Evidence:** TASK-005 mentions "image placeholder" but no implementation exists

---

### TASK-014: Add recipe favoriting/bookmarking
P1 | M | IDEA | — | kaizen

- [ ] Add `isFavorite` field to Recipe model
- [ ] Add heart icon to recipe cards and detail view
- [ ] Store favorites in localStorage
- [ ] Add /favorites route to view saved recipes

DoD: Favorites persist across sessions | Can view all favorites

**Evidence:** Common recipe app feature missing from current implementation

---

### TASK-015: Add recipe filtering by time/difficulty
P2 | S | IDEA | — | kaizen

- [ ] Add time filter (Quick <15min, Medium 15-30, Long 30+)
- [ ] Add difficulty field (derived from time and ingredient count)
- [ ] Update SearchBarComponent with filter UI

DoD: Time filters work correctly | Filter results match expected recipes

**Evidence:** SearchBarComponent exists but only has category filter

---

### TASK-016: Optimize bundle size with lazy loading
P2 | S | IDEA | — | kaizen

- [ ] Implement route-level lazy loading for RecipeDetail
- [ ] Add budget warnings in angular.json
- [ ] Optimize images with lazy loading

DoD: Initial bundle < 200KB | Lazy routes load on demand

**Evidence:** No lazy loading configured, all code in main bundle

---

## Part 2 — Content Proposals (New Recipes for May)

### SUGGESTED RECIPE 1
Title: Spring Asparagus Risotto
Category: dinner
Time: 35
Servings: 4
Description: A creamy Italian risotto featuring fresh asparagus spears and parmesan, perfect for spring dinners. The bright green asparagus adds color and nutrition to this comforting dish.

Ingredients:
1 bunch asparagus
300g arborio rice
1L vegetable broth
1 small onion
3 cloves garlic
100ml white wine
50g parmesan cheese
2 tbsp butter
1 tbsp olive oil
fresh thyme
salt and pepper

Steps:
Trim asparagus and cut into 1-inch pieces, reserving tips.
Sauté onion in butter until softened.
Add rice and toast for 2 minutes.
Pour in wine and stir until absorbed.
Add broth one ladle at a time, stirring constantly.
Add asparagus pieces halfway through cooking.
Add reserved tips in the last 5 minutes.
Stir in parmesan and season with salt, pepper, and thyme.
Serve immediately.

---

### SUGGESTED RECIPE 2
Title: Strawberry Spinach Salad
Category: lunch
Time: 10
Servings: 2
Description: A refreshing spring salad combining sweet strawberries with peppery spinach, topped with pecans and balsamic glaze. Perfect for light summer lunches.

Ingredients:
200g fresh spinach
150g strawberries
50g pecans
50g feta cheese
2 tbsp balsamic vinegar
2 tbsp olive oil
1 tsp honey
salt and pepper

Steps:
Wash and dry spinach leaves.
Hull and slice strawberries.
Toast pecans in a dry pan until fragrant.
Whisk together olive oil, balsamic vinegar, and honey.
Toss spinach and strawberries with dressing.
Top with pecans and crumbled feta.
Season with salt and pepper.
Serve immediately.

---

### SUGGESTED RECIPE 3
Title: May Memorial Day BBQ Ribs
Category: dinner
Time: 180
Servings: 6
Description: Fall-off-the-bone tender BBQ ribs perfect for Memorial Day gatherings. Slow-cooked with a homemade spice rub and tangy BBQ sauce.

Ingredients:
2 racks pork ribs
2 tbsp brown sugar
1 tbsp paprika
1 tsp garlic powder
1 tsp onion powder
1 tsp cayenne pepper
1 tsp salt
1 tsp black pepper
200ml BBQ sauce
60ml apple cider vinegar

Steps:
Remove membrane from back of ribs.
Mix all dry rub ingredients.
Generously coat ribs with rub, wrap in plastic, refrigerate 2 hours.
Preheat oven to 275°F (135°C).
Place ribs on foil-lined baking sheet, cover tightly.
Bake for 2.5 hours until tender.
Brush with BBQ sauce.
Grill or broil for 5 minutes to caramelize sauce.
Rest 10 minutes before slicing.
Serve with extra BBQ sauce.

---

## Part 3 — GUIDELINES Proposals

### GUIDELINE-001: Maintain zero-iteration completion standard
Status: IDEA

All 9 tasks in Sprint 1 completed with 0 iterations. This demonstrates that well-scoped tasks with clear DoD criteria can be completed efficiently without rework.

**Recommendation:** Continue sizing tasks to enable zero-iteration completions. Before marking a task READY, verify all DoD criteria are demonstrably met.

**Evidence:** DONE.md shows all TASK-001 through TASK-009 have 0 iterations.

---

### GUIDELINE-002: Fix data at source before building features
Status: IDEA

recipes.json contains duplicate ingredients (6x per item) and duplicate steps (6x per step). This data quality issue should be fixed at the source (scripts/export.py) rather than building workarounds.

**Recommendation:** Before implementing new features, validate data quality. Fix export脚本 to prevent duplicates from being generated.

**Evidence:** recipes.json shows each ingredient/step repeated multiple times, suggesting seed data or export script bug.

---

## Summary

- 5 feature proposals (TASK-012 through TASK-016)
- 3 new recipe suggestions for May
- 2 guidelines proposals

Commit: chore: kaizen proposals sprint 1 2026-05-01
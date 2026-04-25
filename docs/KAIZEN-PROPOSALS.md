# KAIZEN-PROPOSALS.md

Sprint 2 | 2026-04-25

---

## Part 1 — Feature proposals

### TASK-012: Fix recipe data duplication in export script
P0 | S | IDEA | — | claude

- [ ] AC: recipes.json contains ~6x duplicate ingredients/steps per recipe
- [ ] export.py writes each ingredient/step multiple times

DoD: recipes.json has correct unique ingredients/steps after re-export

**Evidence:** recipes.json lines 11-392 show 6x repeated ingredients for Avocado Toast. Caused by seed data or export script bug.

---

### TASK-013: Add recipe images
P1 | M | IDEA | — | claude

- [ ] AC: Add image_url field to recipe model
- [ ] Add placeholder images or external URLs to recipes.json
- [ ] Display images in recipe cards and detail view

DoD: `ng build` passes | images visible

**Evidence:** No recipe has an image. User experience gap.

---

### TASK-014: Add recipe favorites
P1 | M | IDEA | — | claude

- [ ] AC: Heart icon on recipe cards
- [ ] Persist favorites in localStorage
- [ ] Filter to show only favorites

DoD: `ng build` passes | favorites persist across sessions

**Evidence:** Common recipe app feature missing.

---

### TASK-015: Add cooking timer for steps
P2 | S | IDEA | — | claude

- [ ] AC: Timer button on each step
- [ ] Start/pause/reset functionality
- [ ] Audio alert when complete

DoD: Timer works per step

---

### TASK-016: Add recipe scale (servings multiplier)
P2 | S | IDEA | — | claude

- [ ] AC: Servings adjuster (1x, 2x, 3x)
- [ ] Auto-scale ingredient quantities

DoD: Ingredients scale correctly

---

## Part 2 — Content proposals

### SUGGESTED RECIPE 5
Title: Chicken Teriyaki
Category: dinner
Time: 25
Servings: 4
Description: Quick weeknight teriyaki chicken with tender vegetables in a savory sauce. A Japanese classic that's easy to make at home.
Ingredients:
200g chicken breast
2 tbsp soy sauce
2 tbsp mirin
1 tbsp sugar
1 tbsp vegetable oil
1 cup broccoli florets
1 red bell pepper
Steps:
Slice chicken into bite-sized pieces.
Mix soy sauce, mirin, and sugar in a small bowl.
Heat oil in a wok over high heat.
Stir-fry chicken until golden, about 4 minutes.
Add vegetables and cook 3 minutes more.
Pour sauce over chicken and vegetables.
Simmer until sauce thickens, about 2 minutes.
Serve over rice.

---

### SUGGESTED RECIPE 6
Title: Mango Chia Pudding
Category: breakfast
Time: 10
Servings: 2
Description: Overnight chia pudding topped with fresh mango. Perfect for busy mornings - prep the night before and grab on your way out.
Ingredients:
4 tbsp chia seeds
1 cup coconut milk
1 ripe mango
1 tbsp honey
Steps:
Mix chia seeds and coconut milk in a jar.
Stir well, cover, refrigerate overnight.
Peel and dice the mango.
Top pudding with mango cubes.
Drizzle with honey before serving.

---

### SUGGESTED RECIPE 7
Title: Fish Tacos
Category: dinner
Time: 20
Servings: 4
Description: Crispy white fish in warm tortillas with fresh slaw and creamy sauce. A light Mexican favorite perfect for spring.
Ingredients:
400g white fish fillets
8 small flour tortillas
2 cups cabbage slaw
1/2 cup mayonnaise
2 tbsp lime juice
1 tsp cumin
Salt and pepper to taste
Steps:
Season fish with cumin, salt, and pepper.
Pan-fry fish in a hot pan until flaky, about 3 minutes per side.
Warm tortillas in a dry pan.
Mix mayonnaise and lime juice for sauce.
Assemble tacos with fish, slaw, and lime mayo.
Serve immediately.

---

## Part 3 — GUIDELINES proposals

### GUIDELINE 1
Add data validation to export script to prevent duplicates.

**Evidence:** recipes.json shows 6x duplication (lines 11-392). Export script needs deduplication.

---

### GUIDELINE 2
Require image_url field when adding new recipes.

**Evidence:** All 4 recipes lack images. Better to enforce at data layer than retrofit later.
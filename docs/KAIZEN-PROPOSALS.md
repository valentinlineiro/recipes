# KAIZEN-PROPOSALS.md

**Sprint:** 1 | **Date:** 2026-05-08 | **Agent:** kaizen

---

## Part 1 — Feature proposals

### Observations from DONE.md
- Sprint 1 completed 9 tasks with 0 iterations — clear specs, smooth execution
- Core UI components (list, detail, search) implemented
- No image URLs in any recipe — all recipes lack visual assets
- Data quality issue: recipes.json has severe duplication (ingredients/steps repeated 6x per recipe)
- Backlog already has TASK-010 (print-friendly) and TASK-011 (categories page)

---

## TASK-010: Fix recipe data duplication in export script
P1 | M | IDEA | — | kaizen

- [ ] AC: Export script de-duplicates ingredients and steps before writing JSON
- [ ] AC: Each ingredient appears once per recipe
- [ ] AC: Each step appears once per recipe (step_number ensures order)
DoD: `ng build` passes | python scripts/export.py produces clean JSON

---

## TASK-011: Add image URLs to seed data
P2 | S | IDEA | — | kaizen

- [ ] AC: recipes.db schema includes image_url column
- [ ] AC: Export script includes image_url in JSON output
- [ ] AC: Recipe model includes imageUrl?: string
- [ ] AC: RecipeDetailComponent displays image if present, placeholder if not
DoD: `ng build` passes | images render in UI

---

## TASK-012: Add favorites functionality
P2 | M | IDEA | — | kaizen

- [ ] AC: Heart icon on recipe cards (toggle favorite)
- [ ] AC: Favorites stored in localStorage
- [ ] AC: /favorites route shows only favorited recipes
- [ ] AC: Favorites persist across page reloads
DoD: `ng build` passes | favorites persist

---

## TASK-013: Add recipe cooking timer
P2 | S | IDEA | — | kaizen

- [ ] AC: Timer component accepts minutes input
- [ ] AC: Play/pause/reset controls
- [ ] AC: Audio alert when timer completes
- [ ] AC: Visible on RecipeDetailComponent
DoD: `ng build` passes | timer counts down

---

## TASK-014: Add pagination to recipe list
P2 | M | IDEA | — | kaizen

- [ ] AC: Display 12 recipes per page
- [ ] AC: Previous/Next buttons
- [ ] AC: Shows "Page X of Y" indicator
- [ ] AC: Persists page number in URL query param
DoD: `ng build` passes | pagination works

---

## Part 2 — Content proposals

### Category analysis
- **breakfast:** 1 recipe (Avocado Toast with Eggs)
- **lunch:** 1 recipe (Greek Salad)
- **dinner:** 1 recipe (Spaghetti Carbonara)
- **dessert:** 1 recipe (Chocolate Chip Cookies)
- **Missing:** snacks, beverages, soups, salads, vegetarian mains

### Cuisine analysis
- **Italian:** Carbonara
- **Mediterranean:** Greek Salad
- **American:** Chocolate Chip Cookies
- **Missing:** Asian, Mexican, Indian, Middle Eastern

### Seasonal (May)
Spring produce: asparagus, peas, strawberries, rhubarb, artichokes

---

SUGGESTED RECIPE 1:
Title: Strawberry Spinach Salad
Category: lunch
Time: 15
Servings: 4
Description: A fresh spring salad with tender spinach, juicy strawberries, goat cheese, and a light balsamic vinaigrette perfect for May.
Ingredients:
200g baby spinach
200g fresh strawberries
100g goat cheese
50g candied pecans
30ml balsamic vinegar
60ml olive oil
1 tsp honey
salt to taste
black pepper to taste
Steps:
Wash and dry spinach leaves thoroughly.
Hull and slice strawberries into halves.
Crumble goat cheese into small pieces.
Whisk together balsamic vinegar, olive oil, honey, salt, and pepper.
Toss spinach with dressing in a large bowl.
Top with strawberries, goat cheese, and candied pecans.
Serve immediately.

---

SUGGESTED RECIPE 2:
Title: Teriyaki Chicken Stir-Fry
Category: dinner
Time: 25
Servings: 4
Description: A quick and flavorful Asian-inspired stir-fry with tender chicken, crisp vegetables, and a sweet savory teriyaki sauce.
Ingredients:
500g chicken breast
200g broccoli florets
1 red bell pepper
150g snap peas
60ml soy sauce
30ml mirin
15ml sesame oil
2 cloves garlic
1 tsp ginger
1 tbsp cornstarch
2 tbsp vegetable oil
Steps:
Slice chicken into thin strips and season with salt.
Mix soy sauce, mirin, sesame oil, garlic, ginger, and cornstarch for sauce.
Heat vegetable oil in a wok over high heat.
Stir-fry chicken until golden, about 4 minutes. Remove and set aside.
Add broccoli, bell pepper, and snap peas. Stir-fry 3 minutes.
Return chicken to wok, add sauce, and toss until coated and thickened.
Serve over steamed rice.

---

SUGGESTED RECIPE 3:
Title: Guacamole with Homemade Chips
Category: snacks
Time: 20
Servings: 6
Description: Fresh homemade guacamole with creamy avocado, lime, cilantro, and crispy tortilla chips — perfect for May gatherings.
Ingredients:
3 ripe avocados
1 lime
1/4 red onion
2 Roma tomatoes
1 jalapeño
20g fresh cilantro
1/2 tsp garlic
salt to taste
6 small flour tortillas
vegetable oil for frying
Steps:
Cut avocados in half, remove pit, scoop into a bowl.
Mash with a fork to desired consistency.
Dice tomatoes, red onion, jalapeño, and chop cilantro.
Add vegetables to avocado with lime juice, garlic, and salt.
Mix well and taste for seasoning.
Cut tortillas into triangle shapes.
Heat oil to 350°F (175°C) and fry chips until golden, about 2 minutes.
Drain on paper towels and serve with guacamole.

---

## Part 3 — Guidelines proposals

### Guideline 1: Validate JSON output in export script
**Evidence:** TASK-002 completed but recipes.json has data quality issues (duplicated entries). The export script should validate that each recipe's arrays have unique entries before writing.

### Guideline 2: Add image_url column to schema from the start
**Evidence:** All 4 seed recipes lack image URLs. Future seed data tasks should include placeholder image URLs to avoid retrofitting the model later.

---

*Human: Review and promote what you want to BACKLOG. Do NOT merge — this is a proposal only.*
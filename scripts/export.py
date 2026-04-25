#!/usr/bin/env python3
import sqlite3
import json
import os

DB_PATH = 'recipes.db'
OUTPUT_PATH = 'src/assets/data/recipes.json'

def create_schema(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            time_minutes INTEGER,
            servings INTEGER,
            category TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ingredients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipe_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            quantity TEXT,
            unit TEXT,
            FOREIGN KEY (recipe_id) REFERENCES recipes(id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS steps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipe_id INTEGER NOT NULL,
            step_number INTEGER NOT NULL,
            instruction TEXT NOT NULL,
            FOREIGN KEY (recipe_id) REFERENCES recipes(id)
        )
    ''')
    conn.commit()

def seed_data(conn):
    recipes = [
        {
            'title': 'Avocado Toast with Eggs',
            'description': 'A quick and nutritious breakfast featuring creamy avocado on toasted bread topped with perfectly cooked eggs.',
            'time_minutes': 15,
            'servings': 2,
            'category': 'breakfast',
            'ingredients': [
                {'name': 'bread', 'quantity': '2', 'unit': 'slices'},
                {'name': 'avocado', 'quantity': '1', 'unit': 'whole'},
                {'name': 'eggs', 'quantity': '2', 'unit': 'large'},
                {'name': 'olive oil', 'quantity': '1', 'unit': 'tbsp'},
                {'name': 'salt', 'quantity': '1', 'unit': 'pinch'},
                {'name': 'black pepper', 'quantity': '1', 'unit': 'pinch'},
                {'name': 'red pepper flakes', 'quantity': '1', 'unit': 'pinch'},
            ],
            'steps': [
                {'step_number': 1, 'instruction': 'Toast the bread slices until golden brown.'},
                {'step_number': 2, 'instruction': 'Cut the avocado in half, remove the pit, and scoop the flesh into a bowl.'},
                {'step_number': 3, 'instruction': 'Mash the avocado with a fork and season with salt and pepper.'},
                {'step_number': 4, 'instruction': 'Heat olive oil in a pan over medium heat. Fry eggs to desired doneness.'},
                {'step_number': 5, 'instruction': 'Spread mashed avocado on toast, top with fried eggs.'},
                {'step_number': 6, 'instruction': 'Sprinkle with red pepper flakes and serve immediately.'},
            ]
        },
        {
            'title': 'Greek Salad',
            'description': 'A refreshing Mediterranean salad with crisp vegetables, feta cheese, and a tangy olive oil dressing.',
            'time_minutes': 10,
            'servings': 4,
            'category': 'lunch',
            'ingredients': [
                {'name': 'cucumber', 'quantity': '1', 'unit': 'large'},
                {'name': 'tomatoes', 'quantity': '3', 'unit': 'medium'},
                {'name': 'red onion', 'quantity': '1/2', 'unit': 'small'},
                {'name': 'feta cheese', 'quantity': '200', 'unit': 'g'},
                {'name': 'kalamata olives', 'quantity': '100', 'unit': 'g'},
                {'name': 'olive oil', 'quantity': '3', 'unit': 'tbsp'},
                {'name': 'red wine vinegar', 'quantity': '1', 'unit': 'tbsp'},
                {'name': 'dried oregano', 'quantity': '1', 'unit': 'tsp'},
            ],
            'steps': [
                {'step_number': 1, 'instruction': 'Chop cucumber and tomatoes into bite-sized pieces.'},
                {'step_number': 2, 'instruction': 'Thinly slice the red onion.'},
                {'step_number': 3, 'instruction': 'Combine vegetables in a large bowl.'},
                {'step_number': 4, 'instruction': 'Add olives and crumbled feta cheese on top.'},
                {'step_number': 5, 'instruction': 'Whisk olive oil, vinegar, and oregano. Drizzle over salad.'},
                {'step_number': 6, 'instruction': 'Toss gently and serve immediately.'},
            ]
        },
        {
            'title': 'Spaghetti Carbonara',
            'description': 'A classic Italian pasta dish with creamy egg sauce, crispy pancetta, and parmesan cheese.',
            'time_minutes': 30,
            'servings': 4,
            'category': 'dinner',
            'ingredients': [
                {'name': 'spaghetti', 'quantity': '400', 'unit': 'g'},
                {'name': 'pancetta', 'quantity': '200', 'unit': 'g'},
                {'name': 'eggs', 'quantity': '4', 'unit': 'large'},
                {'name': 'egg yolks', 'quantity': '2', 'unit': 'large'},
                {'name': 'parmesan cheese', 'quantity': '100', 'unit': 'g'},
                {'name': 'black pepper', 'quantity': '2', 'unit': 'tsp'},
                {'name': 'salt', 'quantity': '1', 'unit': 'tbsp'},
            ],
            'steps': [
                {'step_number': 1, 'instruction': 'Bring a large pot of salted water to boil. Cook spaghetti according to package directions.'},
                {'step_number': 2, 'instruction': 'While pasta cooks, cut pancetta into small cubes and fry until crispy.'},
                {'step_number': 3, 'instruction': 'In a bowl, whisk together eggs, egg yolks, and grated parmesan.'},
                {'step_number': 4, 'instruction': 'Reserve 1 cup pasta water, then drain the spaghetti.'},
                {'step_number': 5, 'instruction': 'Add hot pasta to the pancetta pan, remove from heat.'},
                {'step_number': 6, 'instruction': 'Quickly stir in egg mixture, tossing constantly. Add pasta water as needed.'},
                {'step_number': 7, 'instruction': 'Season generously with black pepper and serve immediately.'},
            ]
        },
        {
            'title': 'Chocolate Chip Cookies',
            'description': 'Chewy, golden chocolate chip cookies with melted chocolate in every bite.',
            'time_minutes': 45,
            'servings': 24,
            'category': 'dessert',
            'ingredients': [
                {'name': 'all-purpose flour', 'quantity': '280', 'unit': 'g'},
                {'name': 'butter', 'quantity': '230', 'unit': 'g'},
                {'name': 'brown sugar', 'quantity': '200', 'unit': 'g'},
                {'name': 'white sugar', 'quantity': '100', 'unit': 'g'},
                {'name': 'eggs', 'quantity': '2', 'unit': 'large'},
                {'name': 'vanilla extract', 'quantity': '1', 'unit': 'tsp'},
                {'name': 'baking soda', 'quantity': '1', 'unit': 'tsp'},
                {'name': 'salt', 'quantity': '1', 'unit': 'tsp'},
                {'name': 'chocolate chips', 'quantity': '340', 'unit': 'g'},
            ],
            'steps': [
                {'step_number': 1, 'instruction': 'Preheat oven to 375°F (190°C).'},
                {'step_number': 2, 'instruction': 'Cream together softened butter and sugars until fluffy.'},
                {'step_number': 3, 'instruction': 'Beat in eggs one at a time, then add vanilla extract.'},
                {'step_number': 4, 'instruction': 'Mix flour, baking soda, and salt in a separate bowl.'},
                {'step_number': 5, 'instruction': 'Gradually add dry ingredients to wet ingredients.'},
                {'step_number': 6, 'instruction': 'Fold in chocolate chips.'},
                {'step_number': 7, 'instruction': 'Drop rounded tablespoons of dough onto baking sheets.'},
                {'step_number': 8, 'instruction': 'Bake for 9-11 minutes until edges are golden.'},
                {'step_number': 9, 'instruction': 'Cool on baking sheet for 5 minutes before transferring to wire rack.'},
            ]
        },
        {
            'title': 'Overnight Oats',
            'description': 'Easy no-cook breakfast prepared the night before with oats, milk, and your favorite toppings.',
            'time_minutes': 5,
            'servings': 2,
            'category': 'breakfast',
            'ingredients': [
                {'name': 'rolled oats', 'quantity': '160', 'unit': 'g'},
                {'name': 'milk', 'quantity': '400', 'unit': 'ml'},
                {'name': 'greek yogurt', 'quantity': '120', 'unit': 'g'},
                {'name': 'honey', 'quantity': '2', 'unit': 'tbsp'},
                {'name': 'chia seeds', 'quantity': '2', 'unit': 'tbsp'},
                {'name': 'mixed berries', 'quantity': '100', 'unit': 'g'},
            ],
            'steps': [
                {'step_number': 1, 'instruction': 'Combine oats, milk, yogurt, and honey in a jar or container.'},
                {'step_number': 2, 'instruction': 'Stir in chia seeds.'},
                {'step_number': 3, 'instruction': 'Cover and refrigerate overnight (at least 6 hours).'},
                {'step_number': 4, 'instruction': 'In the morning, stir and top with fresh berries.'},
                {'step_number': 5, 'instruction': 'Enjoy cold or heated in the microwave for 1-2 minutes.'},
            ]
        },
        {
            'title': 'Chicken Stir-Fry',
            'description': 'Quick and healthy Asian-inspired dish with tender chicken and crisp vegetables in a savory sauce.',
            'time_minutes': 25,
            'servings': 4,
            'category': 'dinner',
            'ingredients': [
                {'name': 'chicken breast', 'quantity': '500', 'unit': 'g'},
                {'name': 'broccoli', 'quantity': '200', 'unit': 'g'},
                {'name': 'bell peppers', 'quantity': '2', 'unit': 'medium'},
                {'name': 'soy sauce', 'quantity': '3', 'unit': 'tbsp'},
                {'name': 'sesame oil', 'quantity': '2', 'unit': 'tbsp'},
                {'name': 'garlic', 'quantity': '3', 'unit': 'cloves'},
                {'name': 'ginger', 'quantity': '1', 'unit': 'inch'},
                {'name': 'cornstarch', 'quantity': '1', 'unit': 'tbsp'},
                {'name': 'vegetable oil', 'quantity': '2', 'unit': 'tbsp'},
            ],
            'steps': [
                {'step_number': 1, 'instruction': 'Cut chicken into bite-sized pieces and toss with cornstarch.'},
                {'step_number': 2, 'instruction': 'Chop broccoli into florets and slice bell peppers.'},
                {'step_number': 3, 'instruction': 'Mince garlic and grate ginger.'},
                {'step_number': 4, 'instruction': 'Heat vegetable oil in a wok over high heat.'},
                {'step_number': 5, 'instruction': 'Stir-fry chicken for 5-6 minutes until cooked through. Set aside.'},
                {'step_number': 6, 'instruction': 'Add vegetables to the wok and stir-fry for 3-4 minutes.'},
                {'step_number': 7, 'instruction': 'Return chicken to wok, add soy sauce, sesame oil, garlic, and ginger.'},
                {'step_number': 8, 'instruction': 'Toss everything together and serve over steamed rice.'},
            ]
        },
        {
            'title': 'Tuna Wrap',
            'description': 'Light and satisfying wrap filled with flaky tuna, crisp vegetables, and creamy dressing.',
            'time_minutes': 10,
            'servings': 2,
            'category': 'lunch',
            'ingredients': [
                {'name': 'flour tortillas', 'quantity': '2', 'unit': 'large'},
                {'name': 'canned tuna', 'quantity': '200', 'unit': 'g'},
                {'name': 'mayonnaise', 'quantity': '2', 'unit': 'tbsp'},
                {'name': 'lettuce', 'quantity': '4', 'unit': 'leaves'},
                {'name': 'tomato', 'quantity': '1', 'unit': 'medium'},
                {'name': 'cucumber', 'quantity': '1/2', 'unit': 'medium'},
                {'name': 'red onion', 'quantity': '1/4', 'unit': 'small'},
            ],
            'steps': [
                {'step_number': 1, 'instruction': 'Drain canned tuna and flake into a bowl.'},
                {'step_number': 2, 'instruction': 'Mix tuna with mayonnaise.'},
                {'step_number': 3, 'instruction': 'Shred lettuce, slice tomato, cucumber, and red onion thinly.'},
                {'step_number': 4, 'instruction': 'Lay tortilla flat and spread tuna mixture down the center.'},
                {'step_number': 5, 'instruction': 'Top with lettuce, tomato, cucumber, and onion.'},
                {'step_number': 6, 'instruction': 'Fold in the sides, then roll up tightly from the bottom.'},
                {'step_number': 7, 'instruction': 'Cut in half diagonally and serve.'},
            ]
        },
        {
            'title': 'Banana Nice Cream',
            'description': 'Healthy frozen dessert made from blended frozen bananas - creamy like ice cream but guilt-free.',
            'time_minutes': 10,
            'servings': 4,
            'category': 'dessert',
            'ingredients': [
                {'name': 'frozen bananas', 'quantity': '4', 'unit': 'large'},
                {'name': 'cocoa powder', 'quantity': '2', 'unit': 'tbsp'},
                {'name': 'peanut butter', 'quantity': '2', 'unit': 'tbsp'},
                {'name': 'almond milk', 'quantity': '60', 'unit': 'ml'},
                {'name': 'vanilla extract', 'quantity': '1/2', 'unit': 'tsp'},
            ],
            'steps': [
                {'step_number': 1, 'instruction': 'Slice bananas into coins and freeze for at least 4 hours before making.'},
                {'step_number': 2, 'instruction': 'Add frozen banana coins to a food processor.'},
                {'step_number': 3, 'instruction': 'Pulse until bananas start to break down.'},
                {'step_number': 4, 'instruction': 'Add cocoa powder, peanut butter, almond milk, and vanilla.'},
                {'step_number': 5, 'instruction': 'Blend until smooth and creamy, scraping sides as needed.'},
                {'step_number': 6, 'instruction': 'Serve immediately for soft-serve texture or freeze 30 minutes for firmer texture.'},
            ]
        },
    ]

    for recipe in recipes:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO recipes (title, description, time_minutes, servings, category) VALUES (?, ?, ?, ?, ?)',
            (recipe['title'], recipe['description'], recipe['time_minutes'], recipe['servings'], recipe['category'])
        )
        recipe_id = cursor.lastrowid

        for ing in recipe['ingredients']:
            cursor.execute(
                'INSERT INTO ingredients (recipe_id, name, quantity, unit) VALUES (?, ?, ?, ?)',
                (recipe_id, ing['name'], ing['quantity'], ing['unit'])
            )

        for step in recipe['steps']:
            cursor.execute(
                'INSERT INTO steps (recipe_id, step_number, instruction) VALUES (?, ?, ?)',
                (recipe_id, step['step_number'], step['instruction'])
            )

    conn.commit()

def export_json(conn):
    cursor = conn.cursor()
    cursor.execute('''
        SELECT r.id, r.title, r.description, r.time_minutes, r.servings, r.category,
               i.name, i.quantity, i.unit,
               s.step_number, s.instruction
        FROM recipes r
        LEFT JOIN ingredients i ON r.id = i.recipe_id
        LEFT JOIN steps s ON r.id = s.recipe_id
        ORDER BY r.id, i.id, s.step_number
    ''')
    rows = cursor.fetchall()

    recipes_data = {}
    for row in rows:
        recipe_id, title, description, time_minutes, servings, category, ing_name, ing_qty, ing_unit, step_num, step_inst = row
        if recipe_id not in recipes_data:
            recipes_data[recipe_id] = {
                'id': recipe_id,
                'title': title,
                'description': description,
                'time_minutes': time_minutes,
                'servings': servings,
                'category': category,
                'ingredients': [],
                'steps': []
            }
        if ing_name:
            recipes_data[recipe_id]['ingredients'].append({
                'name': ing_name,
                'quantity': ing_qty,
                'unit': ing_unit
            })
        if step_num:
            recipes_data[recipe_id]['steps'].append({
                'step_number': step_num,
                'instruction': step_inst
            })

    output = {
        'version': 1,
        'recipes': list(recipes_data.values())
    }

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        json.dump(output, f, indent=2)

    print(f'Exported {len(output["recipes"])} recipes to {OUTPUT_PATH}')
    return output

if __name__ == '__main__':
    conn = sqlite3.connect(DB_PATH)
    create_schema(conn)
    seed_data(conn)
    output = export_json(conn)

    if len(output['recipes']) == 8:
        print('SUCCESS: 8 recipes exported')
    else:
        print(f'ERROR: Expected 8 recipes, got {len(output["recipes"])}')
        exit(1)

    conn.close()
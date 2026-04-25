#!/usr/bin/env python3
"""
parse_issue.py — reads a GitHub Issue body and adds recipe to recipes.db
Usage: python3 scripts/parse_issue.py --issue-body "..." --issue-number 42
"""

import argparse
import re
import sqlite3
import sys
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'recipes.db')


def parse_field(body: str, field_id: str) -> str:
    """Extract field value from GitHub issue body markdown."""
    # GitHub renders issue templates as:
    # ### Field Label
    # \nvalue\n
    patterns = [
        rf'### {field_id}\s*\n\s*(.+?)(?=\n###|\Z)',
    ]
    for pattern in patterns:
        match = re.search(pattern, body, re.DOTALL | re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return ''


def parse_issue_body(body: str) -> dict:
    """Parse structured issue body into recipe dict."""
    return {
        'title':       parse_field(body, 'Nombre de la receta'),
        'category':    parse_field(body, 'Categoría').lower().strip(),
        'time':        parse_field(body, 'Tiempo \\(minutos\\)'),
        'servings':    parse_field(body, 'Raciones'),
        'description': parse_field(body, 'Descripción'),
        'ingredients': parse_field(body, 'Ingredientes'),
        'steps':       parse_field(body, 'Pasos'),
        'image_url':   parse_field(body, 'Imagen \\(URL, opcional\\)'),
    }


def parse_ingredients(raw: str) -> list[dict]:
    """Parse ingredient lines: 'quantity unit name'"""
    ingredients = []
    for i, line in enumerate(raw.strip().split('\n')):
        line = line.strip()
        if not line:
            continue
        parts = line.split(None, 2)
        if len(parts) >= 3:
            ingredients.append({
                'quantity': parts[0],
                'unit':     parts[1],
                'name':     parts[2],
                'order':    i + 1,
            })
        elif len(parts) == 2:
            ingredients.append({
                'quantity': parts[0],
                'unit':     '',
                'name':     parts[1],
                'order':    i + 1,
            })
        else:
            ingredients.append({
                'quantity': '',
                'unit':     '',
                'name':     line,
                'order':    i + 1,
            })
    return ingredients


def parse_steps(raw: str) -> list[str]:
    """Parse step lines."""
    return [s.strip() for s in raw.strip().split('\n') if s.strip()]


def insert_recipe(recipe: dict, issue_number: int) -> int:
    """Insert recipe into SQLite and return new recipe ID."""
    conn = sqlite3.connect(DB_PATH)
    cur  = conn.cursor()

    # Validate required fields
    required = ['title', 'category', 'description', 'ingredients', 'steps']
    for field in required:
        if not recipe.get(field):
            print(f"ERROR: missing required field: {field}", file=sys.stderr)
            sys.exit(1)

    # Validate category
    valid_categories = ['breakfast', 'lunch', 'dinner', 'dessert', 'snack']
    if recipe['category'] not in valid_categories:
        print(f"WARNING: unknown category '{recipe['category']}', defaulting to 'lunch'")
        recipe['category'] = 'lunch'

    try:
        time_min  = int(recipe.get('time', 30))
        servings  = int(recipe.get('servings', 4))
    except ValueError:
        time_min  = 30
        servings  = 4

    # Insert recipe
    cur.execute('''
        INSERT INTO recipes (title, description, time_minutes, servings, category, image_url, issue_number)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        recipe['title'],
        recipe['description'],
        time_min,
        servings,
        recipe['category'],
        recipe.get('image_url', '') or '',
        issue_number,
    ))
    recipe_id = cur.lastrowid

    # Insert ingredients
    for ing in parse_ingredients(recipe['ingredients']):
        cur.execute('''
            INSERT INTO ingredients (recipe_id, quantity, unit, name, "order")
            VALUES (?, ?, ?, ?, ?)
        ''', (recipe_id, ing['quantity'], ing['unit'], ing['name'], ing['order']))

    # Insert steps
    for i, step in enumerate(parse_steps(recipe['steps']), 1):
        cur.execute('''
            INSERT INTO steps (recipe_id, "order", instruction)
            VALUES (?, ?, ?)
        ''', (recipe_id, i, step))

    conn.commit()
    conn.close()

    print(f"✓ Recipe '{recipe['title']}' added with ID {recipe_id}")
    return recipe_id


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--issue-body',   required=True)
    parser.add_argument('--issue-number', required=True, type=int)
    args = parser.parse_args()

    recipe = parse_issue_body(args.issue_body)
    print(f"Parsed: {recipe['title']} ({recipe['category']})")
    insert_recipe(recipe, args.issue_number)


if __name__ == '__main__':
    main()

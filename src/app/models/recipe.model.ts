export interface Ingredient {
  name: string;
  quantity: string;
  unit: string;
}

export interface Step {
  step_number: number;
  instruction: string;
}

export interface Recipe {
  id: number;
  title: string;
  description: string;
  time_minutes: number;
  servings: number;
  category: string;
  ingredients: Ingredient[];
  steps: Step[];
}

export interface RecipesData {
  version: number;
  recipes: Recipe[];
}
import { Injectable, inject, signal, computed } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { toSignal } from '@angular/core/rxjs-interop';
import { Recipe, RecipesData } from '../models/recipe.model';

@Injectable({
  providedIn: 'root'
})
export class RecipeService {
  private http = inject(HttpClient);

  private recipesData = signal<Recipe[]>([]);
  private loading = signal(true);
  private error = signal<string | null>(null);
  private searchQuery = signal('');
  private categoryFilter = signal('');

  recipes = computed(() => {
    const query = this.searchQuery().toLowerCase();
    const category = this.categoryFilter().toLowerCase();
    return this.recipesData().filter(recipe => {
      const matchesQuery = !query || recipe.title.toLowerCase().includes(query) || recipe.description.toLowerCase().includes(query);
      const matchesCategory = !category || recipe.category.toLowerCase() === category;
      return matchesQuery && matchesCategory;
    });
  });

  isLoading = computed(() => this.loading());
  hasError = computed(() => this.error());

  constructor() {
    this.loadRecipes();
  }

  private loadRecipes(): void {
    this.http.get<RecipesData>('assets/data/recipes.json').subscribe({
      next: (data) => {
        this.recipesData.set(data.recipes);
        this.loading.set(false);
      },
      error: (err) => {
        this.error.set('Failed to load recipes');
        this.loading.set(false);
      }
    });
  }

  getById(id: number): Recipe | undefined {
    return this.recipesData().find(recipe => recipe.id === id);
  }

  search(query: string): void {
    this.searchQuery.set(query);
  }

  filterByCategory(category: string): void {
    this.categoryFilter.set(category);
  }

  clearFilters(): void {
    this.searchQuery.set('');
    this.categoryFilter.set('');
  }

  getCategories(): string[] {
    const categories = new Set(this.recipesData().map(r => r.category));
    return Array.from(categories).sort();
  }
}
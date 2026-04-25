import { Component, inject, signal, computed, output } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RecipeService } from '../../services/recipe.service';

@Component({
  selector: 'app-search-bar',
  imports: [CommonModule, FormsModule],
  templateUrl: './search-bar.html',
  styleUrl: './search-bar.css'
})
export class SearchBarComponent {
  private recipeService = inject(RecipeService);

  searchQuery = signal('');
  selectedCategory = signal('');

  categories = computed(() => this.recipeService.getCategories());

  private debounceTimeout: ReturnType<typeof setTimeout> | null = null;

  onSearchInput(value: string): void {
    if (this.debounceTimeout) {
      clearTimeout(this.debounceTimeout);
    }
    this.debounceTimeout = setTimeout(() => {
      this.searchQuery.set(value);
      this.recipeService.search(value);
    }, 300);
  }

  onCategoryChange(value: string): void {
    this.selectedCategory.set(value);
    this.recipeService.filterByCategory(value);
  }

  clearFilters(): void {
    this.searchQuery.set('');
    this.selectedCategory.set('');
    this.recipeService.clearFilters();
  }
}
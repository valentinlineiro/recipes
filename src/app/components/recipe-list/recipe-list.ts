import { Component, Input, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { Recipe } from '../../models/recipe.model';
import { RecipeService } from '../../services/recipe.service';

@Component({
  selector: 'app-recipe-list',
  imports: [CommonModule, RouterLink],
  templateUrl: './recipe-list.html',
  styleUrl: './recipe-list.css'
})
export class RecipeListComponent {
  @Input() set searchQuery(value: string) {
    this.recipeService.search(value);
  }
  @Input() set category(value: string) {
    this.recipeService.filterByCategory(value);
  }

  private recipeService = inject(RecipeService);

  recipes = this.recipeService.recipes;
  isLoading = this.recipeService.isLoading;
  hasError = this.recipeService.hasError;
}
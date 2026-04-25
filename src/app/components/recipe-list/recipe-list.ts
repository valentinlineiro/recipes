import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { RecipeService } from '../../services/recipe.service';

@Component({
  selector: 'app-recipe-list',
  imports: [CommonModule, RouterLink],
  templateUrl: './recipe-list.html',
  styleUrl: './recipe-list.css'
})
export class RecipeListComponent {
  private recipeService = inject(RecipeService);

  recipes = this.recipeService.recipes;
  isLoading = this.recipeService.isLoading;
  hasError = this.recipeService.hasError;
}
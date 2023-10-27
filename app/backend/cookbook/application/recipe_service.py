from pydantic import BaseModel

from cookbook.domain.recipe.models import Recipe, NewRecipe
from cookbook.domain.recipe.repository import AbstractRecipeRepository


class RecipeService:
    def __init__(self, repository: AbstractRecipeRepository):
        self.repository = repository

    def get(self, recipe_id: int) -> Recipe:
        return self.repository.get_recipe(recipe_id)

    def set(self, recipe_id: int, recipe: NewRecipe) -> Recipe:
        return self.repository.set_recipe(recipe_id, recipe)

    def get_recipe_list(self) -> list[Recipe]:
        return self.repository.get_recipes()

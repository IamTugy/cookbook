from sqlalchemy.orm import Session

from cookbook.domain.recipe.models import Recipe, NewRecipe
from cookbook.domain.recipe.repository import AbstractRecipeRepository

from . import models


class RecipeSQLRepository(AbstractRecipeRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_recipe(self, recipe_id: int) -> Recipe | None:
        recipe: models.Recipe | None = self.session.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
        return recipe and recipe.to_domain()

    def set_recipe(self, recipe_id: int, recipe: NewRecipe) -> Recipe:
        self.session.add(models.Recipe.from_domain())

    def get_recipes(self) -> list[Recipe]:
        pass


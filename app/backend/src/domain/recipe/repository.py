from abc import abstractmethod, ABC

from src.domain.recipe.models import Recipe, NewRecipe


class AbstractRecipeRepository(ABC):
    # db interface

    @abstractmethod
    def get_recipe(self, recipe_id) -> Recipe:
        pass

    @abstractmethod
    def set_recipe(self, recipe_id: int, recipe: NewRecipe) -> Recipe:
        pass


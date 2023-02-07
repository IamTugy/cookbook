from abc import ABC, abstractmethod

from src.application.recipe_service import RecipeService
from src.domain.authentication.repository import AbstractAuthenticationRepository
from src.domain.recipe.repository import AbstractRecipeRepository


class Bindings(ABC):
    @abstractmethod
    def get_auth(self) -> AbstractAuthenticationRepository:
        pass

    @abstractmethod
    def get_recipe_service(self, repository: AbstractRecipeRepository) -> RecipeService:
        pass

from fastapi import Depends

from src.adapters.auth0.authenticator import Auth0
from src.adapters.auth0.constants import AUTH0_DOMAIN, API_AUDIENCE, ALGORITHMS
from src.adapters.local_test_dict.recipe import LocalRecipe
from src.application.recipe_service import RecipeService
from src.application.user_service import UserService
from src.domain.authentication.repository import AbstractAuthenticationRepository
from src.domain.recipe.repository import AbstractRecipeRepository
from src.domain.user.repository import AbstractUserRepository
from src.ports.bindings.bindings_schema import Bindings


class DevBindings(Bindings):

    def get_auth(self) -> AbstractAuthenticationRepository:
        return Auth0(
            domain=AUTH0_DOMAIN,
            api_audience=API_AUDIENCE,
            algorithms=ALGORITHMS
        )

    def get_recipe_service(self, repository: AbstractRecipeRepository = Depends(LocalRecipe)) -> RecipeService:
        return RecipeService(repository)

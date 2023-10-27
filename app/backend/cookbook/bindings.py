from cookbook.adapters.local_test_dict.recipe import LocalRecipeRepository
from cookbook.application.recipe_service import RecipeService
from cookbook.ports.bindings_schema import Bindings

LocalHostBindings = Bindings(
    auth_repository=None,
    recipe_service=RecipeService(LocalRecipeRepository())
)

DevBindings = Bindings(
    auth_repository=None,
    recipe_service=RecipeService(LocalRecipeRepository())
)

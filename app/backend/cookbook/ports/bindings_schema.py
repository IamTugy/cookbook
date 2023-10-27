import dataclasses
from abc import ABC

from cookbook.application.recipe_service import RecipeService
from cookbook.domain.authentication.repository import AbstractAuthenticationRepository


@dataclasses.dataclass
class Bindings:
    auth_repository: AbstractAuthenticationRepository
    recipe_service: RecipeService


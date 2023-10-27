from typing import List

from fastapi import APIRouter, Depends

from cookbook.ports.dependencies.common import authenticate, BindingsDependency, UserDetailsDependency
from cookbook.ports.schemas.recipe import Recipe, NewRecipe
from cookbook.domain.recipe.models import NewRecipe as DomainRecipe

router = APIRouter()


@router.get("/")
async def get_recipes(bindings: BindingsDependency) -> List[Recipe]:
    return bindings.recipe_service.get_recipe_list()


@router.get("/{recipe_id}", dependencies=[Depends(authenticate)])
async def get_recipes_by_id(
        recipe_id: int,
        bindings: BindingsDependency,
        user: UserDetailsDependency,
) -> Recipe:
    return Recipe(**bindings.recipe_service.get(recipe_id).dict())


@router.post("/{recipe_id}", dependencies=[Depends(authenticate)])
async def set_recipes_by_id(
        recipe_id: int,
        recipe: NewRecipe,
        bindings: BindingsDependency,
        user: UserDetailsDependency,
) -> Recipe:
    new_recipe = bindings.recipe_service.set(recipe_id, recipe=DomainRecipe(
        owner_id=user.id,
        **recipe.dict()
    ))
    return Recipe(**new_recipe.dict())

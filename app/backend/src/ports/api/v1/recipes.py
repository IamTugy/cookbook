from typing import List

from fastapi import APIRouter, Depends, Security

from src.adapters.auth0.models import Auth0TokenDetails
from src.application.recipe_service import RecipeService
from src.ports.bindings import bindings
from src.ports.schemas.recipe import Recipe, NewRecipe
from src.domain.recipe.models import NewRecipe as DomainRecipe

router = APIRouter()


@router.get("/")
async def get_recipes() -> List[Recipe]:
    return []


@router.get("/{recipe_id}", dependencies=[Depends(bindings.get_auth().authenticate)])
async def get_recipes_by_id(
        recipe_id: int,
        recipe_service: RecipeService = Depends(bindings.get_recipe_service),
        user: Auth0TokenDetails = Security(bindings.get_auth().get_user),
) -> Recipe:
    try:
        return Recipe(**recipe_service.get(recipe_id).dict())
    except Exception as e:
        pass


@router.post("/{recipe_id}", dependencies=[Depends(bindings.get_auth().authenticate)])
async def set_recipes_by_id(
        recipe_id: int,
        recipe: NewRecipe,
        recipe_service: RecipeService = Depends(bindings.get_recipe_service),
        user: Auth0TokenDetails = Security(bindings.get_auth().get_user),
) -> Recipe:
    new_recipe = recipe_service.set(recipe_id, recipe=DomainRecipe(
        owner_id=user.id,
        **recipe.dict()
    ))
    return Recipe(**new_recipe.dict())

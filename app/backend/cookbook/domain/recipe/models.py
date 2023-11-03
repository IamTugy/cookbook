from enum import Enum
from typing import Union, List

from pydantic import BaseModel

from cookbook.ports.schemas.user import User


class BaseInformation(BaseModel):
    id: int
    title: str
    description: str | None = None
    pictures_url: List[str] | None = None


class SimpleStep(BaseInformation):
    ingredients: list["Ingredient"]
    recipe_id: int


class TimeStep(BaseInformation):
    ingredients: list["Ingredient"]
    timer: int | None = None  # seconds
    recipe_id: int


class ScaleOption(Enum):
    gram = 'g'
    kilo = 'K'
    cup = 'cup'
    aunce = 'aunce'
    teaspoon = 'teaspoon'
    spoon = 'spoon'


class NutritionValue(BaseModel):
    name: str
    scale: ScaleOption | None
    value: int

    class Config:
        use_enum_values = True


class Ingredient(BaseModel):
    name: str
    scale: ScaleOption | None
    value: float | None

    class Config:
        use_enum_values = True


class Tag(BaseModel):
    name: str


class RatingVote(BaseInformation):
    user: User  # not defined yet
    rating: int  # range note defined yet


class Owner(User):
    description: str


class RecipeAdditionalInformation(BaseModel):
    prep_time: int  # minutes
    work_time: int  # minutes
    servings: int


Instruction = SimpleStep | TimeStep


class Recipe(BaseInformation):
    owner: Owner  # not defined yet
    additional_info: RecipeAdditionalInformation
    instructions: list[Instruction]
    tags: List[str] | None = None
    nutrition: List[NutritionValue] | None = None
    equipment: List[str] | None = None

    class Config:
        orm_mode = True


class NewRecipe(BaseInformation):
    owner_id: int
    tags: List[str] | None = None

    additional_info: RecipeAdditionalInformation

    nutrition: List[NutritionValue] | None
    equipment: List[str] | None
    ingredients: List[Ingredient]

    sections: List[Union[SimpleStep, TimeStep]]

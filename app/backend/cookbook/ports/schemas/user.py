from typing import List

from pydantic import BaseModel


class User(BaseModel):
    id: int
    profile_picture: str
    name: str
    recipes: List[int]

    class Config:
        orm_mode = True

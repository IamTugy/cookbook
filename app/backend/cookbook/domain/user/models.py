from pydantic import BaseModel


class User(BaseModel):
    id: int
    profile_picture: str
    name: str

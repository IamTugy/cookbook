from pydantic import BaseModel


class AuthenticatedUser(BaseModel):
    id: str
    permissions: list[str] | None
    email: str | None
    picture: str | None
    name: str | None

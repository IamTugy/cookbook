from typing import List

from pydantic import BaseModel, Field

from cookbook.adapters.auth0.constants import AUTH0_NAMESPACE


class Auth0TokenDetails(BaseModel):
    id: str = Field(..., alias='sub')
    permissions: List[str] | None
    email: str | None = Field(None, alias=f'{AUTH0_NAMESPACE}/email')
    picture: str | None
    name: str | None


class Auth0User:
    created_at: str
    email: str
    email_verified: bool
    name: str
    nickname: str
    picture: str
    updated_at: str
    user_id: str
    last_login: str
    logins_count: int

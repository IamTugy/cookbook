from typing import List

from fastapi import APIRouter, Depends, Security

from src.adapters.auth0.models import Auth0User
from src.ports.bindings import bindings
from src.ports.schemas.user import User

router = APIRouter()


@router.get("/")
async def get_users() -> List[User]:  # , user_service: Depends(get_user_service)) -> User:
    return []


@router.get("/{user_id}")
async def get_user_by_id(user_id: int) -> User:  # , user_service: Depends(get_user_service)) -> User:
    pass


@router.get("/secure", dependencies=[Depends(bindings.get_auth().authenticate)])
async def get_secure(user: Auth0User = Security(bindings.get_auth().get_user)) -> str:
    return f"{user}"

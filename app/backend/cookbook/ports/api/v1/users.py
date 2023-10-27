from typing import List

from fastapi import APIRouter, Depends

from cookbook.ports.dependencies.common import authenticate, UserDetailsDependency
from cookbook.ports.schemas.user import User

router = APIRouter()


@router.get("/")
async def get_users() -> List[User]:  # , user_service: Depends(get_user_service)) -> User:
    return []


@router.get("/{user_id}")
async def get_user_by_id(user_id: int) -> User:  # , user_service: Depends(get_user_service)) -> User:
    pass


@router.get("/secure", dependencies=[Depends(authenticate)])
async def get_secure(user: UserDetailsDependency) -> str:
    return f"{user}"

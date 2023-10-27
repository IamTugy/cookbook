import typing

from fastapi import Depends, Security
from fastapi.security import OAuth2
from starlette.requests import Request

from cookbook.domain.authentication.models import AuthenticatedUser
from cookbook.ports.bindings_schema import Bindings


def get_bindings(request: Request) -> Bindings:
    return typing.cast(Bindings, request.app.state.bindings)


BindingsDependency = typing.Annotated[Bindings, Depends(get_bindings)]


def get_user_details(bindings: BindingsDependency) -> AuthenticatedUser:
    return Security(bindings.auth_repository.get_user)


UserDetailsDependency = typing.Annotated[AuthenticatedUser, Depends(get_user_details)]


def authenticate(bindings: BindingsDependency) -> OAuth2:
    return bindings.auth_repository.authenticate()

from fastapi import FastAPI

from . import recipes, users
from cookbook.ports.bindings_schema import Bindings


def get_v1(bindings: Bindings):
    api_v1 = FastAPI(openapi_prefix="/api/v1", debug=True)
    api_v1.state.bindings = bindings

    api_v1.include_router(
        recipes.router,
        prefix="/recipes",
        tags=["recipes"],
    )

    api_v1.include_router(
        users.router,
        prefix="/users",
        tags=["users"],
    )

    return api_v1

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from cookbook.adapters.local_test_dict.recipe import LocalRecipeRepository
from cookbook.adapters.sql.base import Base
from cookbook.adapters.sql.recipe.repository import RecipeSQLRepository
from cookbook.application.recipe_service import RecipeService
from cookbook.ports.bindings_schema import Bindings


def get_bindings(environment: str) -> Bindings:
    SQLALCHEMY_DATABASE_URL = "postgresql://admin:admin@db/db"

    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)

    return Bindings(
        auth_repository=None,
        recipe_service=RecipeService(RecipeSQLRepository(session=SessionLocal()))
    )

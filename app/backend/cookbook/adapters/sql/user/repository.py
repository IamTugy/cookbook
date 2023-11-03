from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from cookbook.domain.user.models import User
from cookbook.domain.user.repository import AbstractUserRepository


class UserSQLRepository(AbstractUserRepository):
    def __init__(self, session: Session):
        self.session = session

    def get(self, user_id: int) -> User:
        pass

    def create(self, user: User) -> User:
        pass

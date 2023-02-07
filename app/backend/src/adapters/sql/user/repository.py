from src.domain.user.models import User
from src.domain.user.repository import AbstractUserRepository


class UserRepository(AbstractUserRepository):
    def create(self, user: User) -> User:
        pass

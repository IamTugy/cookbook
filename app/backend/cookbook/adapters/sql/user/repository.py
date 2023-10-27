from cookbook.domain.user.models import User
from cookbook.domain.user.repository import AbstractUserRepository


class UserRepository(AbstractUserRepository):
    def create(self, user: User) -> User:
        pass

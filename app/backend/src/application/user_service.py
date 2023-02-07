from src.domain.user.models import User
from src.domain.user.repository import AbstractUserRepository


class UserService:
    def __init__(self, repository: AbstractUserRepository):
        pass

    def get(self, user_id: int) -> User:
        pass

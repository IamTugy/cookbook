from abc import ABC, abstractmethod

from src.domain.user.models import User


class AbstractUserRepository(ABC):
    # db interface

    @abstractmethod
    def get(self, user_id: int) -> User:
        pass

    @abstractmethod
    def create(self, user: User) -> User:
        pass

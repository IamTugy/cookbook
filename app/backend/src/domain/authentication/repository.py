from abc import abstractmethod, ABC

from fastapi.security import OAuth2, SecurityScopes, HTTPAuthorizationCredentials

from src.domain.authentication.models import AuthenticatedUser


class AbstractAuthenticationRepository(ABC):
    # authenticator interface

    @abstractmethod
    def authenticate(self) -> OAuth2:
        pass

    @abstractmethod
    def get_user(self, security_scopes: SecurityScopes,
                 creds: HTTPAuthorizationCredentials | None) -> AuthenticatedUser:
        pass

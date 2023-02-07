import json
import logging
from typing import Dict, List, Type
import urllib.parse
import urllib.request
from jose import jwt  # type: ignore
from fastapi import HTTPException, Depends, Request
from fastapi.security import SecurityScopes, HTTPBearer, OAuth2, HTTPAuthorizationCredentials
from fastapi.openapi.models import OAuthFlows
from pydantic import BaseModel, ValidationError
from typing_extensions import TypedDict

from src.adapters.auth0.constants import AUTH0_NAMESPACE
from src.adapters.auth0.models import Auth0TokenDetails

from auth0.v3.management import Auth0 as Auth0Management

from src.domain.authentication.models import AuthenticatedUser
from src.domain.authentication.repository import AbstractAuthenticationRepository

logger = logging.getLogger('fastapi_auth0')


class Auth0UnauthenticatedException(HTTPException):
    def __init__(self, detail: str, **kwargs):
        """Returns HTTP 401"""
        super().__init__(401, detail, **kwargs)


class Auth0UnauthorizedException(HTTPException):
    def __init__(self, detail: str, **kwargs):
        """Returns HTTP 403"""
        super().__init__(403, detail, **kwargs)


class HTTPAuth0Error(BaseModel):
    detail: str


unauthenticated_response: Dict = {401: {'model': HTTPAuth0Error}}
unauthorized_response: Dict = {403: {'model': HTTPAuth0Error}}
security_responses: Dict = {**unauthenticated_response, **unauthorized_response}


class Auth0HTTPBearer(HTTPBearer):
    async def __call__(self, request: Request):
        return await super().__call__(request)


class OAuth2ImplicitBearer(OAuth2):
    def __init__(
            self,
            authorization_url: str,
            scopes: Dict[str, str] = None,
            scheme_name: str | None = None,
            auto_error: bool = True
    ):
        scopes = scopes or dict()
        flows = OAuthFlows(implicit={'authorizationUrl': authorization_url, 'scopes': scopes})
        super().__init__(flows=flows, scheme_name=scheme_name, auto_error=auto_error)

    async def __call__(self, request: Request) -> str | None:
        # Overwrite parent call to prevent useless overhead, the actual auth is done in Auth0.get_user
        # This scheme is just for Swagger UI
        return None


class JwksKeyDict(TypedDict):
    kid: str
    kty: str
    use: str
    n: str
    e: str


class JwksDict(TypedDict):
    keys: List[JwksKeyDict]


class Auth0(AbstractAuthenticationRepository):
    def __init__(
            self,
            domain: str,
            api_audience: str,
            algorithms: List[str],
            scopes: Dict[str, str] = None,
            auto_error: bool = True,
            scope_auto_error: bool = True,
            email_auto_error: bool = False,
            auth0user_model: Type[Auth0TokenDetails] = Auth0TokenDetails
    ):
        self.domain = domain
        self.audience = api_audience
        self._scopes = scopes or dict()

        authorization_url_qs = urllib.parse.urlencode({'audience': api_audience})
        self.auth_namespace = f'https://{domain}'
        self._authorization_url = f'{self.auth_namespace}/authorize?{authorization_url_qs}'

        self.auto_error = auto_error
        self.scope_auto_error = scope_auto_error
        self.email_auto_error = email_auto_error

        self.auth0_user_model = auth0user_model

        self.algorithms = algorithms
        r = urllib.request.urlopen(f'{self.auth_namespace}/.well-known/jwks.json')
        self.jwks: JwksDict = json.loads(r.read())

    def authenticate(self) -> OAuth2:
        return OAuth2ImplicitBearer(
            authorization_url=self._authorization_url,
            scopes=self._scopes,
            scheme_name='Auth0ImplicitBearer')

    async def get_user(
            self,
            security_scopes: SecurityScopes,
            creds: HTTPAuthorizationCredentials | None = Depends(Auth0HTTPBearer(auto_error=False)),
    ) -> AuthenticatedUser | None:
        """
        Verify the Authorization: Bearer token and return the user.
        If there is any problem and auto_error = True then raise Auth0UnauthenticatedException or Auth0UnauthorizedException,
        otherwise return None.
        Not to be called directly, but to be placed within a Depends() or Security() wrapper.
        Example: def path_op_func(user: Auth0User = Security(auth.get_user)).
        """
        if creds is None:
            if self.auto_error:
                # See HTTPBearer from FastAPI:
                # latest - https://github.com/tiangolo/fastapi/blob/master/fastapi/security/http.py
                # 0.65.1 - https://github.com/tiangolo/fastapi/blob/aece74982d7c9c1acac98e2c872c4cb885677fc7/fastapi/security/http.py
                raise HTTPException(403, detail='Missing bearer token')
                # must be 403 until solving https://github.com/tiangolo/fastapi/pull/2120
            else:
                return None

        token = creds.credentials

        try:
            unverified_header = jwt.get_unverified_header(token)
            rsa_key = {}
            for key in self.jwks['keys']:
                if key['kid'] == unverified_header['kid']:
                    rsa_key = {
                        'kty': key['kty'],
                        'kid': key['kid'],
                        'use': key['use'],
                        'n': key['n'],
                        'e': key['e']
                    }
                    break
            if rsa_key:
                payload = jwt.decode(
                    token,
                    rsa_key,
                    algorithms=self.algorithms,
                    audience=self.audience,
                    issuer=f'{self.auth_namespace}/'
                )
            else:
                msg = 'Invalid kid header (wrong tenant or rotated public key)'
                if self.auto_error:
                    raise Auth0UnauthenticatedException(detail=msg)
                else:
                    logger.warning(msg)
                    return None

        except jwt.ExpiredSignatureError:
            msg = 'Expired token'
            if self.auto_error:
                raise Auth0UnauthenticatedException(detail=msg)
            else:
                logger.warning(msg)
                return None

        except jwt.JWTClaimsError:
            msg = 'Invalid token claims (wrong issuer or audience)'
            if self.auto_error:
                raise Auth0UnauthenticatedException(detail=msg)
            else:
                logger.warning(msg)
                return None

        except jwt.JWTError:
            msg = 'Malformed token'
            if self.auto_error:
                raise Auth0UnauthenticatedException(detail=msg)
            else:
                logger.warning(msg)
                return None

        except Auth0UnauthenticatedException:
            raise

        except Exception as e:
            # This is an unlikely case but handle it just to be safe (maybe the token is specially crafted to bug our code)
            logger.error(f'Handled exception decoding token: "{e}"', exc_info=True)
            if self.auto_error:
                raise Auth0UnauthenticatedException(detail='Error decoding token')
            else:
                return None

        # payload = self.verify(token)

        if self.scope_auto_error:
            token_scope_str: str = payload.get('scope', '')

            if isinstance(token_scope_str, str):
                token_scopes = token_scope_str.split()

                for scope in security_scopes.scopes:
                    if scope not in token_scopes:
                        raise Auth0UnauthorizedException(
                            detail=f'Missing "{scope}" scope',
                            headers={'WWW-Authenticate': f'Bearer scope="{security_scopes.scope_str}"'}
                        )
            else:
                # This is an unlikely case but handle it just to be safe (perhaps auth0 will change the scope format)
                raise Auth0UnauthorizedException(detail='Token "scope" field must be a string')

        try:
            user = self.auth0_user_model(**payload)

            if self.email_auto_error and not user.email:
                raise Auth0UnauthorizedException(
                    detail=f'Missing email claim (check auth0 rule "Add email to access token")')

            return AuthenticatedUser(**user.dict())

        except ValidationError as e:
            logger.error(f'Handled exception parsing Auth0User: "{e}"', exc_info=True)
            if self.auto_error:
                raise Auth0UnauthorizedException(detail='Error parsing Auth0User')
            else:
                return None

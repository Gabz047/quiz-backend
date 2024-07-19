from typing import List
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from drf_spectacular.extensions import _SchemaType, OpenApiAuthenticationExtension
from drf_spectacular.openapi import AutoSchema
from drf_spectacular.plumbing import build_bearer_security_scheme_object
from passageidentity import Passage, PassageError
from passageidentity.openapi_client.models import UserInfo
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed

from usuario.models import Usuario as User

PASSAGE_APP_ID = settings.PASSAGE_APP_ID
PASSAGE_API_KEY = settings.PASSAGE_API_KEY
PASSAGE_AUTH_STRATEGY = settings.PASSAGE_AUTH_STRATEGY
psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY, auth_strategy=PASSAGE_AUTH_STRATEGY)

class TokenAuthehticationScheme(OpenApiAuthenticationExtension):
    target_class = 'usuario.authentication.TokenAuthentication'
    name = 'tokenAuth'
    match_subclasses = True
    priority = -1

    def get_security_definition(self, auto_schema):
        return build_bearer_security_scheme_object(
            header_name='Authorization',
            token_prefix='Bearer'
        )
    
class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request) -> tuple[User, None]:
        if not request.headers.get('Authorization'):
            return None
        psg_user_id: str = self._get_user_id(request)
        user: User = self._get_or_create_user(psg_user_id)

    def _get_or_create_user(self, psg_user_id) -> User:
        try:
            user: User = User.objects.get(passage_id=psg_user_id)
        except ObjectDoesNotExist:
            psg_user: UserInfo = psg.getUser(psg_user_id)
            user: User = User.objects.create_user(
                passage_id=psg_user.id,
                email=psg_user.email,
            )

    def _get_user_id(self, request) -> str:
        try:
            psg_user_id: str = psg.authenticateRequest(request)
        except PassageError as Er:
            raise AuthenticationFailed(Er.message) from Er
        return psg_user_id

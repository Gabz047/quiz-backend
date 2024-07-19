from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from drf_spectacular.extensions import OpenApiAuthenticationExtension
from drf_spectacular.plumbing import build_bearer_security_scheme_object
from passageidentity.openapi_client.models import UserInfo
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed

from usuario.models import Usuario as User

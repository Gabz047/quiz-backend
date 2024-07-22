from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

from .models import Usuario as User
from .serializers import UsuarioSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = UsuarioSerializer

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
      user = request.user
      serializer = UsuarioSerializer(user)
      return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def verify_user(request, verification_token):
  try:
     user = User.objects.get(verification_token=verification_token)
  except User.DoesNotExist:
      return Response({'error': 'Invalid Verification Token'}, status=status.HTTP_404_NOT_FOUND)

  user.is_verified = True
  user.verification_token = None
  user.save()

  return Response({'message': 'User verified with succes'}, status=status.HTTP_200_OK)
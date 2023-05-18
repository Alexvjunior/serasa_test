from django.contrib.auth import authenticate
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
import asyncio

from apps.user_api.filters import UserFilter
from apps.user_api.models import User
from apps.user_api.serializers import UserAPISerializer
from apps.user_api.services import UserService


class UserAPIViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    basename = "user"
    service = UserService()
    serializer_class = UserAPISerializer
    queryset = User.objects.all()
    http_method_names = ["post", "patch", "get", "delete"]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        asyncio.run(self.service.delete_cache((instance.cpf.raw_input)))
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class TokenObtainView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "username": openapi.Schema(type=openapi.TYPE_STRING),
                "password": openapi.Schema(type=openapi.TYPE_STRING),
            },
        )
    )
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "token": token.key,
                }
            )
        else:
            return Response(
                {"error": "Credenciais inválidas"},
                status=status.HTTP_401_UNAUTHORIZED
            )

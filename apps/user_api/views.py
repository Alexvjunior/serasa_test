from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from apps.user_api.serializers import UserAPISerializer
from apps.user_api.models import User
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class UserAPIViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    basename = 'user'
    serializer_class = UserAPISerializer
    queryset = User.objects.all()
    http_method_names = ["post", "patch", "get", "delete"]


class TokenObtainView(APIView):
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING),
            'password': openapi.Schema(type=openapi.TYPE_STRING)
        }
    ))
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
            })
            # token = RefreshToken.for_user(user)
            # return Response({'token': str(token.access_token)})
        else:
            return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZE)

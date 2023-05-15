from rest_framework import viewsets
from apps.user_api.serializers import UserAPISerializer
from apps.user_api.models import User


class UserAPIViewSet(viewsets.ModelViewSet):
    basename = 'user'
    serializer_class = UserAPISerializer
    queryset = User.objects.all()
    http_method_names = ["post", "patch", "get", "delete"]

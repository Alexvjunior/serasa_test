from rest_framework import serializers

from apps.user_api.models import User


class UserAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

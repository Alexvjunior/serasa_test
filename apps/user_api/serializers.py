from rest_framework import serializers
from cpf_field.validators import validate_cpf
from apps.user_api.models import User


class UserAPISerializer(serializers.ModelSerializer):
    cpf = serializers.CharField(validators=[validate_cpf])

    class Meta:
        model = User
        fields = "__all__"

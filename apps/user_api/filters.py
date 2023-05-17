from django_filters import CharFilter, FilterSet

from apps.user_api.models import User


class UserFilter(FilterSet):
    cpf = CharFilter(field_name="cpf", lookup_expr="icontains")

    class Meta:
        model = User
        fields = ["cpf"]

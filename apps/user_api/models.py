from django.db import models
from django_extensions.db.models import TimeStampedModel
from django_cpf_cnpj.fields import CPFField


class User(TimeStampedModel):

    name = models.CharField(max_length=255)

    cpf = CPFField(masked=True, unique=True)

    email = models.EmailField(unique=True)

    phone_number = models.CharField(max_length=20)

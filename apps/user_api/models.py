from django.db import models
from django_extensions.db.models import TimeStampedModel


class User(TimeStampedModel):
    name = models.CharField(max_length=255)

    cpf = models.CharField(max_length=14, unique=True)

    email = models.EmailField(unique=True)

    phone_number = models.CharField(max_length=20)

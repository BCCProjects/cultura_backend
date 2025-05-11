# usuarios/models.py
from django.contrib.auth.models import AbstractUser

from django.db import models
from locais.models import Cidade

class Usuario(AbstractUser):
    cidade = models.ForeignKey(
        Cidade,
        related_name="usuarios",
        on_delete=models.PROTECT,
        null=True,
        blank=True
     )

    def __str__(self):
        return self.username
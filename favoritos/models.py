# favoritos/models.py
from django.db import models
from django.utils import timezone
from usuarios.models import Usuario
from locais.models import LocalCultural

class Favorito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,
                                related_name="favoritos")
    local = models.ForeignKey(LocalCultural, on_delete=models.CASCADE,
                              related_name="favoritos")
    visitado = models.BooleanField(default=False)
    favoritado_em = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ("usuario", "local")

    def __str__(self):
        return f"{self.usuario} ➜ {self.local}"

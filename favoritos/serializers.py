# favoritos/serializers.py
from rest_framework import serializers
from .models import Favorito
from locais.serializers import LocalCulturalSerializer

class FavoritoSerializer(serializers.ModelSerializer):
    local_detalhe = LocalCulturalSerializer(source="local", read_only=True)

    class Meta:
        model = Favorito
        fields = ("id", "local", "local_detalhe", "visitado",
                  "favoritado_em")
        read_only_fields = ("favoritado_em",)

# locais/serializers.py
from rest_framework import serializers
from .models import Cidade, Estado, LocalCultural, LocalImagem


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ["id", "nome", "sigla"]

class CidadeSerializer(serializers.ModelSerializer):
    estado = EstadoSerializer(read_only=True)

    class Meta:
        model = Cidade
        fields = ["id", "nome", "estado"]

class LocalImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalImagem
        fields = ("id", "arquivo_url", "legenda")

class LocalCulturalSerializer(serializers.ModelSerializer):
    imagens = LocalImagemSerializer(many=True, read_only=True)
    cidade_nome = serializers.CharField(source="cidade.nome", read_only=True)
    estado_sigla = serializers.CharField(source="cidade.estado.sigla", read_only=True)

    class Meta:
        model = LocalCultural
        fields = "__all__"

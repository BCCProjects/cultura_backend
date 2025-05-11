# usuarios/serializers.py
from rest_framework import serializers

from locais.models import Cidade
from .models import Usuario
from django.contrib.auth.password_validation import validate_password

class RegistroUsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    cidade_id = serializers.IntegerField(write_only=True, required=True)  # ID da cidade no cadastro

    class Meta:
        model = Usuario
        fields = ("id", "username", "email", "password", "cidade_id")

    def create(self, validated_data):
        cidade_id = validated_data.pop("cidade_id")
        cidade = Cidade.objects.get(id=cidade_id)
        user = Usuario.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            cidade=cidade,
        )
        return user

# usuarios/views.py
from rest_framework import generics, permissions
from .serializers import RegistroUsuarioSerializer
from .models import Usuario

class RegistroUsuarioView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegistroUsuarioSerializer

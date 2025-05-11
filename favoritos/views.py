# favoritos/views.py
from rest_framework import generics, permissions
from .models import Favorito
from .serializers import FavoritoSerializer

class FavoritoListCreateView(generics.ListCreateAPIView):
    serializer_class = FavoritoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Favorito.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class FavoritoDeleteView(generics.DestroyAPIView):
    serializer_class = FavoritoSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_url_kwarg = "id"

    def get_queryset(self):
        return Favorito.objects.filter(usuario=self.request.user)

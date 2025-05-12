# locais/views.py
from rest_framework import viewsets, permissions,filters
from .models import Cidade, Estado, LocalCultural, LocalImagem
from .serializers import CidadeSerializer, EstadoSerializer, LocalCulturalSerializer, LocalImagemSerializer
from django_filters.rest_framework import DjangoFilterBackend
from config.supabase_service import upload_imagem_supabase
from rest_framework.parsers import MultiPartParser, FormParser



class LocalCulturalViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_value_regex = r'\d+'    
    """
    API pública de locais culturais
    """
    queryset = LocalCultural.objects.select_related('cidade__estado').all()
    serializer_class = LocalCulturalSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields   = ['nome']                 # <– busca só pelo nome
    filterset_fields = ['cidade', 'cidade__estado']  # mantém filtros exatos


class EstadoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    /api/locais/estados/ (GET) ─ lista de estados
    /api/locais/estados/{id}/ (GET) ─ estado específico
    """
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    search_fields = ['nome', 'sigla']
    filterset_fields = ["sigla", "nome"]

class CidadeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cidade.objects.select_related('estado')
    serializer_class = CidadeSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    search_fields = ['nome', 'estado__sigla']
    filterset_fields = ["estado", "estado__sigla", "nome"]

class LocalImagemAdminViewSet(viewsets.ModelViewSet):
    serializer_class = LocalImagemSerializer
    permission_classes = (permissions.IsAdminUser,)
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return LocalImagem.objects.filter(local_id=self.kwargs["local_pk"])

    def perform_create(self, serializer):
        local_id = self.kwargs["local_pk"]
        arquivo = self.request.FILES["arquivo"]
        nome_no_bucket = f"locais/galeria/{arquivo.name}"

        # Salva temporariamente o arquivo para upload
        temp_path = f"/tmp/{arquivo.name}"
        with open(temp_path, "wb+") as f:
            for chunk in arquivo.chunks():
                f.write(chunk)

        url = upload_imagem_supabase(temp_path, nome_no_bucket)
        serializer.save(local_id=local_id, arquivo=url)


class LocalCulturalAdminViewSet(viewsets.ModelViewSet):
    """
    /api/locais/admin/ (POST, GET, PUT, PATCH, DELETE) ─ apenas staff
    """
    queryset = LocalCultural.objects.all()
    serializer_class = LocalCulturalSerializer
    permission_classes = (permissions.IsAdminUser,)
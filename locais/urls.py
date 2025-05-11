# locais/urls.py
from rest_framework.routers import DefaultRouter
from .views import (
    LocalCulturalViewSet,
    LocalCulturalAdminViewSet,
    LocalImagemAdminViewSet,
    EstadoViewSet,
    CidadeViewSet,
)
from rest_framework_nested.routers import NestedDefaultRouter

router = DefaultRouter()
router.register(r"", LocalCulturalViewSet, basename="locais-publico")
router.register(r"admin", LocalCulturalAdminViewSet, basename="locais-admin")
router.register(r"estados", EstadoViewSet, basename="estados")
router.register(r"cidades", CidadeViewSet, basename="cidades")

# Sub-rotas: imagens dos locais
nested = NestedDefaultRouter(router, r"admin", lookup="local")
nested.register(r"imagens", LocalImagemAdminViewSet, basename="local-imagens")

urlpatterns = router.urls + nested.urls

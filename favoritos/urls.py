# favoritos/urls.py
from django.urls import path
from .views import FavoritoListCreateView, FavoritoDeleteView

urlpatterns = [
    path("", FavoritoListCreateView.as_view(), name="favorito-list-create"),
    path("<int:id>/", FavoritoDeleteView.as_view(), name="favorito-delete"),
]

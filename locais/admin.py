# locais/admin.py
from django.contrib import admin
from .models import Cidade, Estado, LocalCultural, LocalImagem


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ("nome", "sigla")
    search_fields = ("nome", "sigla")

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ("nome", "estado")
    list_filter = ("estado",)
    search_fields = ("nome", "estado__sigla")

class LocalImagemInline(admin.TabularInline):
    model = LocalImagem
    extra = 1

@admin.register(LocalCultural)
class LocalCulturalAdmin(admin.ModelAdmin):
    list_display = ("nome", "tipo", "bairro")
    inlines = (LocalImagemInline,)      # arrasta‑e‑solta no painel

@admin.register(LocalImagem)
class LocalImagemAdmin(admin.ModelAdmin):
    list_display = ("local", "legenda")
    search_fields = ("local__nome", "legenda")

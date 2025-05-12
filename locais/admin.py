from django import forms
from django.contrib import admin
from .models import Cidade, Estado, LocalCultural, LocalImagem
from config.supabase_service import upload_imagem_supabase
import os
import uuid

class LocalImagemInlineForm(forms.ModelForm):
    upload = forms.FileField(required=False, label="Upload da imagem")

    class Meta:
        model = LocalImagem
        fields = ["upload", "legenda", "arquivo"]

    def save(self, commit=True):
        instance = super().save(commit=False)
        file = self.cleaned_data.get("upload")

        if file:
            temp_path = f"/tmp/{file.name}"
            with open(temp_path, "wb+") as f:
                for chunk in file.chunks():
                    f.write(chunk)

            nome_no_bucket = f"locais/galeria/{uuid.uuid4()}_{file.name}"
            url = upload_imagem_supabase(temp_path, nome_no_bucket)

            instance.arquivo = url

            os.remove(temp_path)

        if commit:
            instance.save()
        return instance

class LocalImagemInline(admin.TabularInline):
    model = LocalImagem
    form = LocalImagemInlineForm
    extra = 1
    fields = ["upload", "legenda", "arquivo"]
    readonly_fields = ["arquivo"]


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ("nome", "sigla")
    search_fields = ("nome", "sigla")


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ("nome", "estado")
    list_filter = ("estado",)
    search_fields = ("nome", "estado__sigla")


@admin.register(LocalCultural)
class LocalCulturalAdmin(admin.ModelAdmin):
    list_display = ("nome", "tipo", "bairro")
    inlines = (LocalImagemInline,) 


@admin.register(LocalImagem)
class LocalImagemAdmin(admin.ModelAdmin):
    list_display = ("local", "legenda")
    search_fields = ("local__nome", "legenda")

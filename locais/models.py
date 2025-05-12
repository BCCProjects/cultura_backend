# locais/models.py
from django.db import models

class Estado(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2, unique=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, related_name="cidades", on_delete=models.CASCADE)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} - {self.estado.sigla}"

class LocalCultural(models.Model):
    TIPOS = (
        ("museu", "Museu"),
        ("teatro", "Teatro"),
        ("biblioteca", "Biblioteca"),
        ("centro", "Centro Cultural"),
        ("zoologico", "Zoológico"),
        ("parque", "Parque de Diversões"),
        ("igreja", "Igreja"),
        ("jardim", "Jardim"),
        ("shopping", "Shopping"),
    )
    nome = models.CharField(max_length=120)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    descricao = models.TextField()
    endereco = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)
    telefone = models.CharField(max_length=50)
    horario_funcionamento = models.CharField(max_length=120)
    link_externo = models.URLField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    cidade = models.ForeignKey(Cidade, related_name="locais", on_delete=models.PROTECT, null=True, blank=True)


    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome
    
class LocalImagem(models.Model):
    local = models.ForeignKey(LocalCultural, related_name="imagens", on_delete=models.CASCADE)
    arquivo_url = models.URLField(max_length=500)  # Agora é URL
    legenda = models.CharField(max_length=140, blank=True)

    def __str__(self):
        return f"{self.local.nome} – {self.legenda or 'imagem'}"



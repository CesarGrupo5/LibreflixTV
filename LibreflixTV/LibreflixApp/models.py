from django.db import models
from django.contrib.auth.models import User

# ENTIDADES

class Obra(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    genero = models.CharField(max_length=20)
    imagem = models.URLField()
    dataLancamento = models.DateField()
    diretor = models.CharField(max_length=20)
    trailer = models.URLField()
    isDestaque = models.BooleanField()
    isPopular = models.BooleanField()
    isRecente = models.BooleanField()

class Filme(Obra):
    duracao = models.IntegerField()

class Serie(Obra):
    qntEpisodios = models.IntegerField()

class Episodio(models.Model):
    titulo = models.CharField(max_length=20)
    descricao = models.TextField()
    imagem = models.URLField()
    duracao = models.IntegerField()
    obra = models.ForeignKey(Serie, on_delete=models.CASCADE)

class Favoritados(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class ContinuarAssistindo(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class Avaliacao(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name="avaliacoes")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="avaliacoes")
    estrelas = models.PositiveSmallIntegerField(default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)
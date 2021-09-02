from django.db import models
from datetime import datetime


class Receita(models.Model):
    nome = models.CharField(max_length=100)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.CharField(max_length=50)
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.nome

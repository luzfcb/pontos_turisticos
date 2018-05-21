from django.db import models


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField('atracoes.Atracao')
    comentarios = models.ManyToManyField('comentarios.Comentario')

    def __str__(self):
        return self.nome

from django.db import models
from django.conf import settings


class Comentario(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=True)

    def __str__(self):
        return self.usuario.username

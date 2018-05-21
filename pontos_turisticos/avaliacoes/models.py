from django.db import models
from django.conf import settings


class Avaliacao(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comentario = models.TextField(null=True, blank=True)
    nota = models.DecimalField(max_digits=3, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

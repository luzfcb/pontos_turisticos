from django.contrib import admin

from . import models


@admin.register(models.Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = (
        'usuario',
        'comentario',
        'data',
        'aprovado'
    )

from django.contrib import admin

from . import models


@admin.register(models.Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'comentario',
        'nota',
        'data',
    )

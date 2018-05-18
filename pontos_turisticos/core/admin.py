from django.contrib import admin

from . import models


@admin.register(models.PontoTuristico)
class PontoTuristicoAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'descricao',
        'aprovado'
    )

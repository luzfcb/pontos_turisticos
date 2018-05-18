from django.contrib import admin

from . import models


@admin.register(models.Atracao)
class AtracaoAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'descricao',
        'horario_func',
        'idade_minima',
    )

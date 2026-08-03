from django.contrib import admin
from .models import Ocorrencia

@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'localizacao', 'data_criacao', 'status')
    list_filter = ('categoria', 'data_criacao', 'status')
    list_editable = ('status',)
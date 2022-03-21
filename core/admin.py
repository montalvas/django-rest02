from django.contrib import admin
from .models import Curso, Avaliacao

# Register your models here.
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'ativo', 'data_criacao', 'data_atualizacao')
    
@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'usuario', 'email', 'comentario', 'avaliacao', 'data_criacao')
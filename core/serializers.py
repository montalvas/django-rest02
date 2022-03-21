from rest_framework import serializers
from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        # habilita o campo e-mail apenas para escrita (POST)
        # evitar problemas de segurança
        
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'usuario',
            'email',
            'comentario',
            'avaliacao',
            'data_criacao',
            'ativo'
        )
        
class CursoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'data_criacao',
            'ativo'
        )
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
    # Nested Relationship - bom para relacionamento 1 para 1
    # Para mais relações pode tornar o sistema lento
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    
    # HyperLinked Related Field - cria links para cada relacionamento
    avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')
    
    # Primary Key Related Field
    # avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'data_criacao',
            'ativo',
            'avaliacoes'
        )
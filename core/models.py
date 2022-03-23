from django.db import models
from django.db.models import UniqueConstraint

# Create your models here.
class Base(models.Model):
    data_criacao = models.DateTimeField('Data criação', auto_now_add=True)
    data_atualizacao = models.DateTimeField('Data atualização', auto_now=True)
    ativo = models.BooleanField(default=True)
    
    class Meta:
        abstract = True
        
class Curso(Base):
    titulo = models.CharField('Título', max_length=100)
    url = models.URLField(unique=True)
    
    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return self.titulo
    
class Avaliacao(Base):
    curso = models.ForeignKey(Curso, related_name='avaliacoes' ,on_delete=models.PROTECT)
    usuario = models.CharField('Usuário', max_length=100)
    email = models.EmailField('E-mail')
    comentario = models.TextField('Comentário', blank=True, default='')
    avaliacao = models.DecimalField('Avaliação', max_digits=2, decimal_places=1)
    
    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        ordering = ['id']
        # torna os campos abaixo como únicos
        constraints = [
        UniqueConstraint(fields=['email', 'curso'], name='unique email e curso')
        ]
    
    def __str__(self):
        return f'{self.usuario} avaliou o curso {self.curso} com nota {self.avaliacao}'
from django.urls import path
from .views import CursosAPIView, CursoAPIView, AvaliacoesAPIView, AvaliacaoAPIView


urlpatterns = [
    # LIST / CREATE
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    
    # UPDATE / DESTROY
    path('cursos/<int:pk>', CursoAPIView.as_view(), name='curso'),
    path('avaliacoes/<int:pk>', AvaliacaoAPIView.as_view(), name='avaliacao'),
]
from django.urls import path
from . import api_views

urlpatterns = [
    path('filmes/', api_views.api_listar_filmes, name='api_listar_filmes'),
    path('filmes/<int:filme_id>/', api_views.api_detalhar_filme, name='api_detalhar_filme'),
    path('filmes/<int:filme_id>/avaliacoes/', api_views.api_avaliar_filme, name='api_avaliar_filme'),
    path('filmes/<int:filme_id>/favoritos/', api_views.api_favoritar_filme, name='api_favoritar_filme'),
]

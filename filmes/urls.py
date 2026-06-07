from django.urls import path
from . import views

app_name = 'filmes'

urlpatterns = [
    path('', views.listar_filmes, name='listar'),
    path('<int:filme_id>/', views.detalhar_filme, name='detalhar'),
    path('<int:filme_id>/avaliar/', views.avaliar_filme, name='avaliar'),
    path('<int:filme_id>/favoritar/', views.alternar_favorito, name='favoritar'),
]

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from filmes.models import AvaliacaoFilme, FilmeFavorito


@login_required
def perfil(request):
    contexto = {
        'favoritos': FilmeFavorito.objects.filter(usuario=request.user).select_related('filme'),
        'avaliacoes': AvaliacaoFilme.objects.filter(usuario=request.user).select_related('filme'),
    }
    return render(request, 'usuarios/perfil.html', contexto)

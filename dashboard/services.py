from filmes.factories import RecommendationCreatorFactory
from filmes.models import AvaliacaoFilme, Filme, FilmeFavorito


class DashboardService:
    def montar_contexto(self, usuario):
        contexto = {
            'total_filmes': Filme.objects.count(),
            'filmes_populares': Filme.objects.order_by('-total_visualizacoes')[:5],
        }

        if usuario.is_authenticated:
            contexto.update({
                'total_favoritos': FilmeFavorito.objects.filter(usuario=usuario).count(),
                'total_avaliacoes': AvaliacaoFilme.objects.filter(usuario=usuario).count(),
                'recomendacoes': RecommendationCreatorFactory.criar('popularidade').recomendar(usuario),
            })
        else:
            contexto.update({
                'total_favoritos': 0,
                'total_avaliacoes': 0,
                'recomendacoes': Filme.objects.order_by('-total_visualizacoes')[:5],
            })

        return contexto

from abc import ABC, abstractmethod
from .models import AvaliacaoFilme, Filme


class RecommendationStrategy(ABC):
    @abstractmethod
    def recommend(self, usuario):
        raise NotImplementedError


class GeneroRecommendationStrategy(RecommendationStrategy):
    def recommend(self, usuario):
        generos_avaliados = (
            AvaliacaoFilme.objects
            .filter(usuario=usuario, nota__gte=4)
            .values_list('filme__genero', flat=True)
            .distinct()
        )
        return Filme.objects.filter(genero__in=generos_avaliados).exclude(avaliacoes__usuario=usuario)[:10]


class PopularidadeRecommendationStrategy(RecommendationStrategy):
    def recommend(self, usuario):
        return Filme.objects.order_by('-total_visualizacoes', 'titulo')[:10]


class FilmesRecentesRecommendationStrategy(RecommendationStrategy):
    def recommend(self, usuario):
        return Filme.objects.order_by('-data_cadastro')[:10]

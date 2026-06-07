from abc import ABC, abstractmethod
from .strategies import (
    FilmesRecentesRecommendationStrategy,
    GeneroRecommendationStrategy,
    PopularidadeRecommendationStrategy,
    RecommendationStrategy,
)


class RecommendationCreator(ABC):
    @abstractmethod
    def create_strategy(self) -> RecommendationStrategy:
        raise NotImplementedError

    def recomendar(self, usuario):
        strategy = self.create_strategy()
        return strategy.recommend(usuario)


class GeneroRecommendationCreator(RecommendationCreator):
    def create_strategy(self) -> RecommendationStrategy:
        return GeneroRecommendationStrategy()


class PopularidadeRecommendationCreator(RecommendationCreator):
    def create_strategy(self) -> RecommendationStrategy:
        return PopularidadeRecommendationStrategy()


class RecentesRecommendationCreator(RecommendationCreator):
    def create_strategy(self) -> RecommendationStrategy:
        return FilmesRecentesRecommendationStrategy()


class RecommendationCreatorFactory:
    creators = {
        'genero': GeneroRecommendationCreator,
        'popularidade': PopularidadeRecommendationCreator,
        'recentes': RecentesRecommendationCreator,
    }

    @classmethod
    def criar(cls, criterio: str) -> RecommendationCreator:
        creator_class = cls.creators.get(criterio, PopularidadeRecommendationCreator)
        return creator_class()

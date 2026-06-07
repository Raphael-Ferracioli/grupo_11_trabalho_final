from decimal import Decimal
from django.core.exceptions import ValidationError
from .repositories import AvaliacaoRepository, FavoritoRepository, VisualizacaoRepository


class AvaliacaoService:
    def __init__(self, avaliacao_repository=None):
        self.avaliacao_repository = avaliacao_repository or AvaliacaoRepository()

    def avaliar_filme(self, usuario, filme, nota, comentario=''):
        nota_decimal = Decimal(str(nota))
        if nota_decimal < 0 or nota_decimal > 5:
            raise ValidationError('A nota deve estar entre 0 e 5.')
        return self.avaliacao_repository.salvar_ou_atualizar(usuario, filme, nota_decimal, comentario)


class FavoritoService:
    def __init__(self, favorito_repository=None):
        self.favorito_repository = favorito_repository or FavoritoRepository()

    def alternar_favorito(self, usuario, filme) -> bool:
        if self.favorito_repository.existe(usuario, filme):
            self.favorito_repository.remover(usuario, filme)
            return False
        self.favorito_repository.criar(usuario, filme)
        return True


class VisualizacaoService:
    def __init__(self, visualizacao_repository=None):
        self.visualizacao_repository = visualizacao_repository or VisualizacaoRepository()

    def registrar_visualizacao(self, usuario, filme):
        filme.total_visualizacoes += 1
        filme.save(update_fields=['total_visualizacoes'])
        return self.visualizacao_repository.registrar(usuario, filme)

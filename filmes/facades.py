from .models import AvaliacaoFilme, FilmeFavorito
from .repositories import AvaliacaoRepository, DjangoFilmeRepository
from .services import VisualizacaoService


class FilmeFacade:
    def __init__(self, filme_repository=None, avaliacao_repository=None, visualizacao_service=None):
        self.filme_repository = filme_repository or DjangoFilmeRepository()
        self.avaliacao_repository = avaliacao_repository or AvaliacaoRepository()
        self.visualizacao_service = visualizacao_service or VisualizacaoService()

    def detalhar_filme(self, usuario, filme_id: int):
        filme = self.filme_repository.buscar_por_id(filme_id)
        self.visualizacao_service.registrar_visualizacao(usuario, filme)

        media = self.avaliacao_repository.media_do_filme(filme)
        favorito = False
        avaliacao_usuario = None

        if usuario.is_authenticated:
            favorito = FilmeFavorito.objects.filter(usuario=usuario, filme=filme).exists()
            avaliacao_usuario = AvaliacaoFilme.objects.filter(usuario=usuario, filme=filme).first()

        return {
            'filme': filme,
            'media_avaliacoes': media,
            'favorito': favorito,
            'avaliacao_usuario': avaliacao_usuario,
        }

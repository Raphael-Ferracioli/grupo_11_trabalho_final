from typing import Protocol
from django.db.models import QuerySet
from .models import AvaliacaoFilme, Filme, FilmeFavorito, FilmeVisualizacao


class FilmeReader(Protocol):
    def listar(self) -> QuerySet[Filme]: ...
    def buscar_por_id(self, filme_id: int) -> Filme: ...


class FilmeWriter(Protocol):
    def salvar(self, filme: Filme) -> Filme: ...
    def remover(self, filme_id: int) -> None: ...


class DjangoFilmeRepository:
    def listar(self) -> QuerySet[Filme]:
        return Filme.objects.all()

    def buscar_por_id(self, filme_id: int) -> Filme:
        return Filme.objects.get(id=filme_id)

    def salvar(self, filme: Filme) -> Filme:
        filme.save()
        return filme

    def remover(self, filme_id: int) -> None:
        Filme.objects.filter(id=filme_id).delete()


class AvaliacaoRepository:
    def salvar_ou_atualizar(self, usuario, filme, nota, comentario='') -> AvaliacaoFilme:
        avaliacao, _created = AvaliacaoFilme.objects.update_or_create(
            usuario=usuario,
            filme=filme,
            defaults={'nota': nota, 'comentario': comentario},
        )
        return avaliacao

    def media_do_filme(self, filme):
        from django.db.models import Avg
        return AvaliacaoFilme.objects.filter(filme=filme).aggregate(media=Avg('nota'))['media']


class FavoritoRepository:
    def existe(self, usuario, filme) -> bool:
        return FilmeFavorito.objects.filter(usuario=usuario, filme=filme).exists()

    def criar(self, usuario, filme) -> FilmeFavorito:
        favorito, _created = FilmeFavorito.objects.get_or_create(usuario=usuario, filme=filme)
        return favorito

    def remover(self, usuario, filme) -> int:
        removidos, _ = FilmeFavorito.objects.filter(usuario=usuario, filme=filme).delete()
        return removidos


class VisualizacaoRepository:
    def registrar(self, usuario, filme) -> FilmeVisualizacao:
        if usuario.is_authenticated:
            return FilmeVisualizacao.objects.create(usuario=usuario, filme=filme)
        return FilmeVisualizacao.objects.create(filme=filme)

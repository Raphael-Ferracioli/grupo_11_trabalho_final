from django.contrib import admin
from .models import AvaliacaoFilme, Filme, FilmeFavorito, FilmeVisualizacao


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'ano_lancamento', 'diretor', 'total_visualizacoes')
    search_fields = ('titulo', 'titulo_original', 'diretor', 'genero')
    list_filter = ('genero', 'ano_lancamento')


@admin.register(AvaliacaoFilme)
class AvaliacaoFilmeAdmin(admin.ModelAdmin):
    list_display = ('filme', 'usuario', 'nota', 'atualizada_em')
    search_fields = ('filme__titulo', 'usuario__username')
    list_filter = ('nota',)


@admin.register(FilmeFavorito)
class FilmeFavoritoAdmin(admin.ModelAdmin):
    list_display = ('filme', 'usuario', 'criado_em')
    search_fields = ('filme__titulo', 'usuario__username')


@admin.register(FilmeVisualizacao)
class FilmeVisualizacaoAdmin(admin.ModelAdmin):
    list_display = ('filme', 'usuario', 'visualizado_em')
    search_fields = ('filme__titulo', 'usuario__username')

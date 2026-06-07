from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Filme(models.Model):
    titulo = models.CharField(max_length=180)
    titulo_original = models.CharField(max_length=180, blank=True)
    ano_lancamento = models.PositiveIntegerField(null=True, blank=True)
    diretor = models.CharField(max_length=120, blank=True)
    genero = models.CharField(max_length=80, db_index=True)
    duracao_minutos = models.PositiveIntegerField(null=True, blank=True)
    sinopse = models.TextField(blank=True)
    poster = models.URLField(blank=True)
    total_visualizacoes = models.PositiveIntegerField(default=0)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['titulo']
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'

    def __str__(self):
        return self.titulo


class AvaliacaoFilme(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, related_name='avaliacoes')
    nota = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )
    comentario = models.TextField(blank=True)
    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('usuario', 'filme')
        verbose_name = 'Avaliação de filme'
        verbose_name_plural = 'Avaliações de filmes'

    def __str__(self):
        return f'{self.usuario} avaliou {self.filme} com {self.nota}'


class FilmeFavorito(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, related_name='favoritado_por')
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'filme')
        verbose_name = 'Filme favorito'
        verbose_name_plural = 'Filmes favoritos'

    def __str__(self):
        return f'{self.usuario} favoritou {self.filme}'


class FilmeVisualizacao(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, related_name='visualizacoes')
    visualizado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Visualização de filme'
        verbose_name_plural = 'Visualizações de filmes'

    def __str__(self):
        return f'Visualização de {self.filme} em {self.visualizado_em:%d/%m/%Y}'

from django.contrib.auth.models import User
from django.test import TestCase
from .models import AvaliacaoFilme, Filme, FilmeFavorito
from .services import AvaliacaoService, FavoritoService


class AvaliacaoServiceTest(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username='teste', password='123456')
        self.filme = Filme.objects.create(titulo='Matrix', genero='Ficção científica')

    def test_deve_criar_avaliacao(self):
        avaliacao = AvaliacaoService().avaliar_filme(self.usuario, self.filme, 5, 'Excelente')
        self.assertEqual(AvaliacaoFilme.objects.count(), 1)
        self.assertEqual(avaliacao.comentario, 'Excelente')


class FavoritoServiceTest(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username='teste', password='123456')
        self.filme = Filme.objects.create(titulo='Interestelar', genero='Ficção científica')

    def test_deve_alternar_favorito(self):
        service = FavoritoService()
        self.assertTrue(service.alternar_favorito(self.usuario, self.filme))
        self.assertEqual(FilmeFavorito.objects.count(), 1)
        self.assertFalse(service.alternar_favorito(self.usuario, self.filme))
        self.assertEqual(FilmeFavorito.objects.count(), 0)

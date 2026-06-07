from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from .facades import FilmeFacade
from .forms import AvaliacaoFilmeForm
from .models import Filme
from .services import AvaliacaoService, FavoritoService


def listar_filmes(request):
    filmes = Filme.objects.all()
    genero = request.GET.get('genero')
    busca = request.GET.get('q')

    if genero:
        filmes = filmes.filter(genero__icontains=genero)
    if busca:
        filmes = filmes.filter(titulo__icontains=busca)

    paginator = Paginator(filmes, 10)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'filmes/lista.html', {'page_obj': page_obj})


def detalhar_filme(request, filme_id):
    contexto = FilmeFacade().detalhar_filme(request.user, filme_id)
    contexto['form'] = AvaliacaoFilmeForm(instance=contexto['avaliacao_usuario'])
    return render(request, 'filmes/detalhe.html', contexto)


@login_required
def avaliar_filme(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)

    if request.method != 'POST':
        return redirect('filmes:detalhar', filme_id=filme.id)

    form = AvaliacaoFilmeForm(request.POST)
    if form.is_valid():
        AvaliacaoService().avaliar_filme(
            usuario=request.user,
            filme=filme,
            nota=form.cleaned_data['nota'],
            comentario=form.cleaned_data['comentario'],
        )
        messages.success(request, 'Avaliação registrada com sucesso.')
    else:
        messages.error(request, 'Não foi possível registrar a avaliação.')

    return redirect('filmes:detalhar', filme_id=filme.id)


@login_required
def alternar_favorito(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    favoritado = FavoritoService().alternar_favorito(request.user, filme)

    if favoritado:
        messages.success(request, 'Filme adicionado aos favoritos.')
    else:
        messages.info(request, 'Filme removido dos favoritos.')

    return redirect('filmes:detalhar', filme_id=filme.id)

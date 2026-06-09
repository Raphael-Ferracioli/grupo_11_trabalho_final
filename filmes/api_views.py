import json

from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET, require_http_methods

from .models import Filme
from .services import AvaliacaoService, FavoritoService


def filme_to_dict(filme):
    return {
        'id': filme.id,
        'titulo': filme.titulo,
        'titulo_original': filme.titulo_original,
        'ano_lancamento': filme.ano_lancamento,
        'diretor': filme.diretor,
        'genero': filme.genero,
        'duracao_minutos': filme.duracao_minutos,
        'sinopse': filme.sinopse,
        'poster': filme.poster,
        'total_visualizacoes': filme.total_visualizacoes,
    }


@require_GET
def api_listar_filmes(request):
    filmes = Filme.objects.all()
    genero = request.GET.get('genero')
    if genero:
        filmes = filmes.filter(genero__icontains=genero)

    page_number = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)
    paginator = Paginator(filmes, page_size)
    page_obj = paginator.get_page(page_number)

    return JsonResponse({
        'results': [filme_to_dict(filme) for filme in page_obj],
        'page': page_obj.number,
        'total_pages': paginator.num_pages,
        'total_items': paginator.count,
    })


@require_GET
def api_detalhar_filme(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    return JsonResponse(filme_to_dict(filme))


@login_required
@require_http_methods(['POST'])
def api_avaliar_filme(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)

    try:
        payload = json.loads(request.body.decode('utf-8') or '{}')
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON inválido.'}, status=400)

    nota = payload.get('nota')
    if nota is None:
        return JsonResponse({'error': 'O campo "nota" é obrigatório.'}, status=400)

    try:
        avaliacao = AvaliacaoService().avaliar_filme(
            usuario=request.user,
            filme=filme,
            nota=nota,
            comentario=payload.get('comentario', ''),
        )
    except (ValidationError, ValueError) as exc:
        return JsonResponse({'error': str(exc)}, status=400)

    return JsonResponse({'id': avaliacao.id, 'message': 'Avaliação registrada.'}, status=201)


@login_required
@require_http_methods(['POST', 'DELETE'])
def api_favoritar_filme(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    service = FavoritoService()

    if request.method == 'DELETE':
        service.desfavoritar(request.user, filme)
        return JsonResponse({}, status=204)

    service.favoritar(request.user, filme)
    return JsonResponse({'message': 'Filme favoritado.'}, status=201)

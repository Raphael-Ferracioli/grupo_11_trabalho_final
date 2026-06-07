# ADR-006: Remover entidades do domínio antigo de serviços

## Status

Accepted

## Contexto

O sistema original possuía conceitos de marketplace de serviços que não fazem sentido para o domínio de filmes.

## Decisão

Substituir conceitos antigos, como `Servico`, por conceitos do domínio atual, como `Filme`, `AvaliacaoFilme` e `FilmeFavorito`.

## Consequências

A decisão reduz inconsistência conceitual, mas exige ajustes em models, views, templates e consultas.

# ADR-003: Usar Django ORM como camada de persistência

## Status

Accepted

## Contexto

O projeto utiliza Django e precisa de produtividade para criar modelos, consultas e migrações.

## Decisão

Usar Django ORM para modelar Filme, AvaliacaoFilme, FilmeFavorito e FilmeVisualizacao.

## Consequências

A equipe ganha produtividade e integração com o admin, mas cria dependência do framework na infraestrutura.

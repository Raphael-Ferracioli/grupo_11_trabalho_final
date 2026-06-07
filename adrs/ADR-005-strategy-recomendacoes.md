# ADR-005: Aplicar Strategy para recomendações

## Status

Accepted

## Contexto

As recomendações podem mudar conforme o critério: gênero, popularidade, histórico ou avaliações.

## Decisão

Criar uma abstração `RecommendationStrategy` e implementações concretas para cada algoritmo.

## Consequências

Novas estratégias podem ser adicionadas com menor alteração no serviço principal. O custo é o aumento no número de classes.

# ADR-002: Organizar o código em camadas internas

## Status

Accepted

## Contexto

Views com muita regra de negócio dificultam testes, leitura e manutenção.

## Decisão

Separar o código em apresentação, aplicação/serviços, domínio e infraestrutura.

## Consequências

A solução melhora a testabilidade e a clareza do projeto, mas aumenta a quantidade de arquivos.

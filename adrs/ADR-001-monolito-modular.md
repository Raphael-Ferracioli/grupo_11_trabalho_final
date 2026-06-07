# ADR-001: Adotar monolito modular

## Status

Accepted

## Contexto

A equipe é pequena, o prazo é acadêmico e o sistema possui um domínio principal: catálogo, avaliação e favoritos de filmes. Uma arquitetura de microsserviços traria complexidade de deploy, comunicação em rede e observabilidade.

## Decisão

Implementar o GoodFilms como uma única aplicação Django, organizada internamente por módulos de domínio.

## Consequências

A decisão reduz a complexidade de desenvolvimento e facilita a entrega. Como custo, exige disciplina na organização interna para evitar acoplamento excessivo.

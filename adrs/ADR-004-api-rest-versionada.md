# ADR-004: Expor API REST versionada por URL

## Status

Accepted

## Contexto

O sistema pode evoluir para integração com frontend separado ou aplicativo móvel.

## Decisão

Criar rotas de API iniciadas por `/api/v1/` e documentar o contrato em OpenAPI.

## Consequências

Facilita integração e evolução futura, mas exige manter documentação e endpoints sincronizados.

# GoodFilms

Plataforma web para catálogo, avaliação e favoritos de filmes.

Este repositório foi montado para a disciplina **Padrões e Arquitetura de Software** e organiza o projeto como um **monolito modular em Django**, com separação interna entre apresentação, serviços, domínio e infraestrutura.

## Objetivo

Permitir que usuários autenticados possam:

- consultar filmes cadastrados;
- visualizar detalhes de filmes;
- avaliar filmes com nota e comentário;
- marcar e remover favoritos;
- acompanhar informações no dashboard;
- acessar uma API REST versionada em `/api/v1/`.

## Arquitetura

O projeto segue a ideia de monolito modular:

```text
goodfilms/
├── goodfilms/          # configuração principal Django
├── filmes/             # domínio de filmes, avaliações, favoritos e recomendações
├── usuarios/           # perfil e autenticação básica
├── dashboard/          # agregação de dados para tela inicial
├── adrs/               # decisões arquiteturais
├── diagrams/           # fontes Mermaid dos diagramas
├── docs/               # documentação da API e apoio
├── templates/          # templates HTML
└── manage.py
```

## Padrões aplicados

- **Strategy**: variação dos algoritmos de recomendação de filmes.
- **Factory Method**: criação das estratégias de recomendação.
- **Facade**: simplificação da busca de dados para a tela de detalhe do filme.

## Princípios SOLID aplicados

- **SRP**: views delegam regras de negócio para serviços.
- **OCP**: novas recomendações podem ser criadas sem alterar o serviço principal.
- **LSP**: serviços dependem de contratos/protocolos de repositório.
- **ISP**: contratos pequenos para leitura e escrita de filmes.
- **DIP**: serviços dependem de abstrações, não diretamente do ORM em todos os pontos.

## Requisitos

- Python 3.12 ou superior
- Django 5.x
- SQLite para ambiente local

## Como executar localmente

Crie o ambiente virtual:

Windows:

```bash
python -m venv venv
```

Linux/macOS:

```bash
python3 -m venv venv
```

Ative o ambiente virtual:

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Gere e execute as migrações:

1. **makemigrations**: Lê os arquivos `models.py` dos apps e gera os arquivos de migration (se a pasta `migrations/` não existir no app, o Django a cria automaticamente). 
   ```bash
   python manage.py makemigrations filmes
   ```
   *(Nota: Como os apps `usuarios` e `dashboard` não possuem modelos customizados em seu `models.py`, rodar `makemigrations` para eles não gerará novos arquivos).*

2. **migrate**: Lê as migrations geradas e de fato cria as tabelas correspondentes no banco de dados (ex: SQLite).
   ```bash
   python manage.py migrate
   ```

3. **loaddata**: Popula o banco com os registros iniciais (filmes, avaliações, etc.). Este passo **precisa** que as tabelas já tenham sido criadas no banco pelo comando `migrate` anterior:
   ```bash
   python manage.py loaddata data/fixtures/filmes.json
   ```

*(Dica: Se preferir executar os comandos sem ativar explicitamente o venv, você pode referenciar o executável do Python diretamente pela pasta do ambiente virtual, por exemplo: `venv/bin/python manage.py ...` no Linux/macOS ou `venv\Scripts\python manage.py ...` no Windows).*

Crie um superusuário:

```bash
python manage.py createsuperuser
```

Inicie o servidor:

```bash
python manage.py runserver
```

Acesse:

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/admin/
http://127.0.0.1:8000/api/v1/filmes/
```

## Rotas principais

```text
/                         Dashboard inicial
/filmes/                  Lista de filmes
/filmes/<id>/             Detalhe do filme
/filmes/<id>/avaliar/     Avaliar filme
/filmes/<id>/favoritar/   Favoritar/remover favorito
/usuarios/perfil/         Perfil do usuário
/api/v1/filmes/           API de listagem de filmes
/api/v1/filmes/<id>/      API de detalhe do filme
```

## Documentação da API

A especificação OpenAPI resumida está em:

```text
docs/openapi.yml
```

## Decisões arquiteturais

Os ADRs estão na pasta:

```text
adrs/
```

## Diagramas

Os fontes Mermaid estão na pasta:

```text
diagrams/
```

## Checklist de entrega

- [x] README com instalação e execução.
- [x] Pasta `/adrs` com decisões arquiteturais.
- [x] Pasta `/diagrams` com fontes dos diagramas.
- [x] API documentada em OpenAPI.
- [x] Estrutura compatível com monolito modular.
- [ ] Subir o repositório no GitHub e substituir o link no documento final.

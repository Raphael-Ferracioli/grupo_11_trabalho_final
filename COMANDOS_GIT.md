# Como subir este projeto no GitHub

Depois de extrair a pasta, abra o terminal dentro dela.

## 1. Conferir se o Git está funcionando

```bash
git status
```

## 2. Criar um repositório vazio no GitHub

No GitHub:

1. Clique em **New repository**.
2. Nome sugerido: `goodfilms`.
3. Deixe como público, se o professor pediu repositório público.
4. Não marque README, `.gitignore` ou licença, porque este pacote já tem esses arquivos.

## 3. Conectar o projeto local ao GitHub

Troque `SEU_USUARIO` pelo seu usuário do GitHub:

```bash
git remote add origin https://github.com/SEU_USUARIO/goodfilms.git
git branch -M main
git push -u origin main
```

## 4. Copiar o link para o Word

Depois de enviar, coloque este link no Anexo A do documento:

```text
https://github.com/SEU_USUARIO/goodfilms
```

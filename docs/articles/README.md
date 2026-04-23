# Articles

Esta pasta guarda os artigos editoriais ja finalizados neste projeto.

Os rascunhos, variantes e candidatos continuam fora daqui, principalmente em
`docs/reports/article-candidates/`. Aqui devem ficar apenas os textos que ja
passaram pela curadoria e foram fechados como versao editorial estavel.

## Papel

Use `articles/` quando um texto ja tiver sido aprovado para sair do modo
relatorio e virar artigo final.

Antes disso, a investigacao deve passar por:

1. `docs/plans/002-editorial-articles-from-project-history/`
2. `docs/reports/`
3. `docs/reports/article-candidates/`
4. curadoria humana
5. artigo final em `docs/articles/`

## Regras Para Artigos Finais

- Frontmatter obrigatorio com metadados editoriais.
- Formato de post de blog.
- Contexto real do projeto preservado.
- Sinais cruzados entre commits, docs, memoria, planos e conversas.
- Sem tratar uma unica fonte como verdade absoluta.
- Rodape informando coautoria entre Vitor Sampaio e Codex.
- `version` deve indicar o estado editorial do texto.

## Artigos Finalizados

- [`experiencia-desenvolvimento-ia-sem-dominar-stack.md`](./experiencia-desenvolvimento-ia-sem-dominar-stack.md): artigo de experiencia sobre conduzir o desenvolvimento do app com apoio de IA. Status final `1.0.0`.
- [`linux-gtk-flatpak-com-ia.md`](./linux-gtk-flatpak-com-ia.md): artigo tecnico sobre estrutura, persistencia e empacotamento do app. Status final `1.0.0`.

## Rascunhos e Variantes

Rascunhos gerados durante a pesquisa editorial nao devem ficar na raiz do
repositorio.

Os dois rascunhos sinteticos gerados no fluxo Gemini foram preservados em:

- [`../reports/article-candidates/artigo_experiencia_ai.md`](../reports/article-candidates/artigo_experiencia_ai.md)
- [`../reports/article-candidates/artigo_tecnico_linux_gtk.md`](../reports/article-candidates/artigo_tecnico_linux_gtk.md)

## Rodape Padrao

```text
Este artigo foi escrito em coautoria por Vitor Sampaio e Codex, a partir da
historia real do projeto TodoList GTK e dos registros de desenvolvimento
mantidos no repositorio.
```

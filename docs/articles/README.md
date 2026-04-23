# Articles

Esta pasta e a camada editorial futura do framework neste projeto.

Ela deve guardar artigos finais ou rascunhos editoriais prontos para virar posts
de blog. No momento, a regra e simples: **nao gerar artigos finais antes da
curadoria em `docs/reports/article-candidates/`**.

## Papel

Use `articles/` apenas quando um texto ja tiver sido aprovado para sair do modo
relatorio e virar post.

Antes disso, a investigacao deve passar por:

1. `docs/plans/002-editorial-articles-from-project-history/`
2. `docs/reports/`
3. `docs/reports/article-candidates/`
4. curadoria humana
5. artigo final em `docs/articles/`

## Regras Para Artigos Finais

- Formato de post de blog.
- Contexto real do projeto preservado.
- Sinais cruzados entre commits, docs, memoria, planos e conversas.
- Sem tratar uma unica fonte como verdade absoluta.
- Rodape informando coautoria entre Vitor Sampaio e Codex.

## Artigos Em Curadoria

- [`experiencia-desenvolvimento-ia-sem-dominar-stack.md`](./experiencia-desenvolvimento-ia-sem-dominar-stack.md): relato sobre construir um app Linux nativo guiando IA sem dominar previamente a stack. Aguarda curadoria humana.
- [`linux-gtk-flatpak-com-ia.md`](./linux-gtk-flatpak-com-ia.md): tutorial tecnico sobre estruturar, persistir, empacotar e testar um app Python/GTK4/Libadwaita com Flatpak. Aguarda curadoria humana.

## Rodape Padrao

```text
Este artigo foi escrito em coautoria por Vitor Sampaio e Codex, a partir da
historia real do projeto TodoList GTK e dos registros de desenvolvimento
mantidos no repositorio.
```

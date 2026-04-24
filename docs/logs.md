# Logs da Camada Docs

Este arquivo registra mudancas estruturais da pasta `docs/`.

Use este log quando a organizacao documental mudar, nao para registrar cada
alteracao tecnica do aplicativo. Logs de execucao de uma frente devem continuar
no `logs.md` do plano correspondente.

## 2026-04-23 - Instrumentalizacao minima com studio-coding

- Criado `docs/README.md` como ponto de entrada da camada documental.
- Criados indices minimos para `knowledge/`, `patterns/` e `plans/`.
- Registrado que este repo usa apenas uma instancia reduzida do framework `studio-coding`.
- Naquele momento, mantida a decisao de nao criar camadas vazias como `skills/`, `routines/`, `agents/`, `product/`, `team/`, `reports` ou `resources`.

## 2026-04-23 - Frente editorial de artigos

- Criado `docs/articles/` como camada futura de artigos finais ou rascunhos aprovados.
- Criado `docs/reports/` como camada intermediaria para investigacao, sintese e curadoria.
- Criado plano `docs/plans/002-editorial-articles-from-project-history/`.
- Criados reports iniciais para linha do tempo, decisoes tecnicas, evolucao documental, memoria, conversas, temas editoriais e candidatos a artigos.
- Atualizada a taxonomia: `reports/` e `articles/` agora existem porque ha uso real nesta frente.

## 2026-04-23 - Renumeracao dos planos

- Criado `docs/plans/000-desktop/` como entrada operacional para inbox e backlog.
- Movidos `todolist.md` e `backlog.md` para `docs/plans/000-desktop/`.
- Renomeado `docs/plans/v1_todolist/` para `docs/plans/001-v1-todolist/`.
- Renomeado `docs/plans/editorial_articles_from_project_history/` para `docs/plans/002-editorial-articles-from-project-history/`.
- Renomeado `docs/plans/002-articles-from-drafts/` para `docs/plans/003-articles-from-drafts/`.

## 2026-04-23 - Header contextual e alinhamento documental

- Atualizado o header da janela principal para exibir lista ativa, icone da sessao e contagem de tarefas.
- Removida a duplicacao do titulo da lista dentro do corpo do conteudo principal.
- Ajustados `README.md` e `docs/knowledge/ui-ux-patterns.md` para refletir o comportamento real do header e do estado vazio.

## 2026-04-23 - Organizacao editorial final

- Movidos `artigo_experiencia_ai.md` e `artigo_tecnico_linux_gtk.md` da raiz para `docs/reports/article-candidates/`.
- Atualizado `docs/articles/README.md` para tratar `articles/` como camada de artigos finalizados e apontar rascunhos para `reports/article-candidates/`.
- Adicionado frontmatter editorial aos dois artigos finais com status, versao, autores, serie e metadados de manutencao.

## 2026-04-23 - Plano da landing page institucional

- Criado `docs/plans/004-landing-page-do-projeto/` como nova frente para descoberta, narrativa e implementacao de uma landing page.
- Registrada a necessidade de absorver um prompt-base detalhado antes de fechar copy, hierarquia visual e escopo tecnico da pagina.
- Atualizado o indice `docs/plans/README.md` para incluir a nova frente.

## 2026-04-23 - Frontmatter nos planos

- Adicionado frontmatter aos `plan.md` em `docs/plans/`.
- Registrado `status` diretamente nos planos com taxonomia curta: `active`, `in_progress` e `completed`.
- Atualizados `docs/patterns/plan-patterns.md` e `docs/plans/README.md` para explicitar o novo cabecalho minimo.

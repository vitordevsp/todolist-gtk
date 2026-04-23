# Documentacao do Projeto

Esta pasta organiza a camada estrutural de documentacao do TodoList GTK.

Neste repositorio ela e uma instancia pequena do framework **studio-coding**:
nao tenta criar todas as camadas do framework, mas usa a mesma ideia central de
transformar documentacao, planos, memoria e logs em apoio operacional para
desenvolvimento humano + IA.

## Papel de `docs/`

Use esta pasta para entender:

- como o projeto foi planejado e validado;
- quais decisoes tecnicas ja viraram conhecimento reutilizavel;
- quais padroes documentais estao sendo testados;
- onde procurar contexto antes de alterar build, Flatpak, persistencia ou UI.

O valor aqui nao e o volume de arquivos. E a funcao: manter o projeto navegavel,
auditavel e reproduzivel mesmo quando o trabalho atravessa varias sessoes e
modelos de IA.

## Camadas Atuais

- [`knowledge/`](./knowledge/README.md): conhecimento tecnico consolidado sobre o app.
- [`patterns/`](./patterns/README.md): pequenos padroes usados para organizar documentacao e memoria.
- [`plans/`](./plans/README.md): frentes de trabalho, tarefas, perguntas e logs.
- [`reports/`](./reports/README.md): relatorios intermediarios para sintese, diagnostico e curadoria.
- [`articles/`](./articles/README.md): camada futura para artigos finais ou rascunhos aprovados.
- [`logs.md`](./logs.md): linha do tempo curta da propria camada `docs/`.

Camadas do studio-coding como `skills/`, `routines/`, `agents/`, `product/`,
`team/` e `resources/` nao foram criadas aqui porque ainda nao ha necessidade
real neste projeto.

## Como Navegar

Para entender o produto:

1. Leia [`../README.md`](../README.md).
2. Leia o plano ativo em [`plans/001-v1-todolist/plan.md`](./plans/001-v1-todolist/plan.md).
3. Consulte [`knowledge/`](./knowledge/README.md) conforme a area tocada.

Para continuar uma frente de trabalho:

1. Comece por [`plans/README.md`](./plans/README.md).
2. Abra o plano da frente em `plans/<nome>/`.
3. Atualize `tasks.md`, `logs.md` ou `questions.md` quando a execucao mudar o estado da frente.

Para registrar conhecimento aprendido:

1. Use [`knowledge/`](./knowledge/README.md) quando for conhecimento tecnico do app.
2. Use [`patterns/`](./patterns/README.md) quando for uma convencao reutilizavel da camada documental.
3. Use [`../MEMORY.md`](../MEMORY.md) quando for aprendizado operacional importante para agentes futuros.

Para transformar a historia do projeto em artigos:

1. Comece pelo plano [`002-editorial-articles-from-project-history`](./plans/002-editorial-articles-from-project-history/plan.md).
2. Consulte os relatorios em [`reports/`](./reports/README.md).
3. Curadoria final acontece em [`reports/article-candidates/`](./reports/article-candidates/README.md).
4. So gere artigos em [`articles/`](./articles/README.md) quando houver pedido explicito.

## Heuristica de Taxonomia

- `knowledge/`: conhecimento tecnico do TodoList GTK.
- `patterns/`: convencoes pequenas que ajudam a manter a documentacao consistente.
- `plans/`: trabalho que precisa sobreviver a mais de uma sessao.
- `reports/`: sinteses intermediarias e investigacoes consultivas.
- `articles/`: saida editorial aprovada para virar post.
- `logs.md`: mudancas estruturais da propria camada `docs/`.
- `CHANGELOG.md`: historico de versoes do produto, fora de `docs/`.

Se uma camada ainda nao existe, nao crie por simetria. Crie apenas quando houver
uso real.

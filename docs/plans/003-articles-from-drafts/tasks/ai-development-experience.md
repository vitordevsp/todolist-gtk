# Task: Artigo de Experiencia com IA

## Status

- [x] Em curadoria
- [x] Rascunho reescrito
- [x] Revisado com fontes
- [ ] Pronto para publicar/exportar

## Rascunho Base

- [`artigo_experiencia_ai.md`](../../../reports/article-candidates/artigo_experiencia_ai.md)

## Grupo Original do Relatorio de Candidatos

Este artigo pertence ao **Grupo B: Artigos de Experiencia com IA**.

Artigos de experiencia focam na vivencia de desenvolvimento guiado por IA,
principalmente quando a pessoa condutora nao domina previamente toda a stack.

## Candidatos Relacionados do Grupo B

### B1. Um TodoList simples para testar IA de verdade

Direcionamento:

Explicar por que um app simples foi suficiente para testar varias camadas reais
de desenvolvimento: UI nativa, persistencia, build, Flatpak, docs, memoria,
versionamento e validacao. O foco nao e vender o TodoList como produto complexo,
mas mostrar que um escopo simples pode revelar muito sobre uma IA.

Sinais:

- `README.md`: projeto como caso de teste com Antigravity/Gemini.
- `CHANGELOG.md`: experimento registrado na release `0.0.0`.
- commits `da49b55`, `e42f4b7`, `159bb84`, `98267bf`.
- `docs/reports/project-timeline/README.md`.
- `docs/reports/conversation-sources/README.md`: fase 0 mostra o nascimento do
  app funcional.

### B2. Desenvolver guiando IA sem dominar a stack

Direcionamento:

Narrar a experiencia de conduzir um projeto em uma stack pouco dominada
previamente: GTK4, Libadwaita, PyGObject, PyInstaller e Flatpak. O artigo deve
mostrar que a pessoa nao precisa saber tudo antes, mas precisa saber fazer boas
perguntas, pedir verificacao, desconfiar de atalhos e transformar aprendizados em
documentacao.

Este candidato parece um bom post de abertura para a categoria de coautoria com
IA.

Sinais:

- `README.md`: projeto como experimento com Antigravity/Gemini.
- `AGENTS.md`: manual criado para orientar agentes e humanos na stack.
- `MEMORY.md`: aprendizados sobre Libadwaita, layout, SQLite, PyInstaller e Flatpak.
- `docs/reports/conversation-sources/README.md`: ciclos plano -> tarefa ->
  walkthrough, com varias decisoes guiadas pela conversa.
- `docs/reports/memory-and-learning-signals/README.md`.

### B3. Quando a IA diz "pronto" cedo demais

Direcionamento:

Explorar a diferenca entre a narrativa de fechamento da IA e a maturidade real do
projeto. A conversa Antigravity declarou o app "pronto para v1.0" e "pronto para
o mundo", mas depois a fase Codex encontrou pendencias de bundle, runtime,
versionamento, estrutura e reprodutibilidade.

O artigo deve ser justo: nao ridicularizar a IA, mas mostrar por que a pessoa
desenvolvedora precisa manter criterio de fechamento.

Sinais:

- `docs/reports/conversation-sources/README.md`: fase 5, primeira tentativa de
  fechamento como v1.0.
- `walkthrough.md.resolved.6` da conversa Antigravity, citado no relatorio de
  conversas como fechamento prematuro.
- `docs/plans/001-v1-todolist/plan.md`: fase 5 ainda parcialmente concluida.
- `docs/plans/001-v1-todolist/logs.md`: auditoria e consolidacao Codex.
- `CHANGELOG.md`: separa `0.0.0` de `0.1.0`.

### B4. Coautoria humano-IA sem romantizar a automacao

Direcionamento:

Explorar o papel humano na direcao: escolher o que importa, corrigir rota,
exigir bundle seguro, pedir docs melhores, versionamento, commits organizados e
estrutura editorial. A IA ajuda, mas a qualidade nasce da tensao entre geracao,
criterio e revisao.

Sinais:

- `README.md`: experimento com Antigravity/Gemini.
- Conversa atual com Codex: consolidacao da fase 5, auditoria do bundle,
  versionamento, tag `v0.1.0` e frente editorial.
- `CHANGELOG.md`, secao `Experiment Notes`.
- `docs/reports/conversation-sources/README.md`: sinais editoriais fortes da
  conversa Antigravity/Gemini.
- `docs/reports/editorial-themes/README.md`: tema "coautoria real entre humano e IA".

### B5. Documentacao que guia IA, nao so documenta codigo

Direcionamento:

Mostrar como `docs/` virou ferramenta operacional. O texto pode contar como
planos, logs, perguntas, memory, knowledge, reports e articles formam uma camada
que ajuda humanos e IAs a retomarem contexto sem depender apenas do chat.

Sinais:

- `docs/README.md`.
- `docs/plans/001-v1-todolist/`.
- `docs/knowledge/`.
- `docs/reports/docs-framework-evolution/README.md`.
- `docs/reports/conversation-sources/README.md`: fase 6 e fase 7, onde surgem
  plano como pasta, `AGENTS.md`, `MEMORY.md` e `memory-patterns.md`.
- `docs/logs.md`.

### B6. O projeto como diario de aprendizado, nao so repositorio de codigo

Direcionamento:

Escrever sobre como o TodoList GTK virou registro de aprendizado: cada problema
tecnico importante virou memory, knowledge, plan, log ou changelog. O artigo pode
ser menos tecnico e mais reflexivo, focado em como preservar contexto mudou a
qualidade do trabalho com IA.

Sinais:

- `MEMORY.md`.
- `docs/knowledge/`.
- `docs/plans/001-v1-todolist/logs.md`.
- `CHANGELOG.md`.
- `docs/reports/memory-and-learning-signals/README.md`.
- `docs/reports/conversation-sources/README.md`: fase 9, "guia de reproducao"
  para o "eu do futuro" ou outra IA.

## Diagnostico do Rascunho Atual

O rascunho tem uma premissa boa: desenvolver um app Linux nativo guiando IA sem
parar o trabalho principal. Mas o texto esta polido demais no sentido errado:
parece post motivacional sobre "IA Pair Programming" e perde o que ha de mais
interessante na historia real.

## Correcoes Obrigatorias

- Trocar frases genericas por cenas e tensoes concretas.
- Explicar que a stack era pouco familiar.
- Explicar que o app era simples, mas tocava muitas camadas reais.
- Citar que o Antigravity/Gemini 3 Flash construiu quase todo o corpo inicial.
- Citar que Gemini 3 Flash e um modelo de 2024.
- Mostrar que a IA declarou o projeto pronto cedo demais.
- Explicar que a etapa final com Codex/GPT-5.4 foi menos "criar do zero" e mais
  auditar, consolidar, corrigir bundle, versionar, estruturar docs e preparar
  curadoria.
- Mostrar a pessoa humana como diretora: definindo qualidade, fazendo perguntas,
  recusando atalhos e registrando conhecimento.

## O Que Aproveitar

- A ideia de "desenvolvedor como diretor".
- A barreira de entrada de uma stack nova.
- O projeto como laboratorio para `studio-coding`.
- A imagem de trabalhar em paralelo enquanto o agente executa.

## Direcao de Reescrita

Titulo possivel:

```text
Eu guiei uma IA para criar meu primeiro app Linux nativo sem dominar GTK
```

Tese:

```text
O experimento nao mostrou que "a IA faz tudo sozinha". Mostrou algo mais util:
com direcao humana, documentacao viva e revisao critica, um modelo de 2024
conseguiu levar um app simples muito longe. O fechamento exigiu outra camada de
criterio: auditoria, reproducibilidade, versionamento e curadoria.
```

Estrutura sugerida:

1. O desejo antigo: criar algo nativo para Linux.
2. O recorte pequeno: um TodoList, escolhido justamente por ser simples.
3. O fluxo com Antigravity e Gemini 3 Flash: plano, tarefa, walkthrough.
4. A stack desconhecida: GTK4, Libadwaita, PyGObject, Flatpak.
5. Onde a IA foi muito bem: UI, CRUD, sessoes, docs iniciais, build local.
6. Onde a direcao humana foi essencial: coerencia da stack, Makefile vs npm,
   persistencia, bundle seguro, docs como framework.
7. A fase Codex/GPT-5.4: consolidar, auditar e preparar o projeto para release.
8. O aprendizado: IA acelera, mas criterio ainda e a parte nobre do trabalho.

Nota historica obrigatoria:

```text
Quase todo o corpo inicial do projeto foi construido com Antigravity usando
Gemini 3 Flash, modelo de 2024. A fase final contou com Codex/GPT-5.4 para
consolidacao tecnica, versionamento, tag `v0.1.0`, reports e estrutura editorial.
```

## Arquivo Final Esperado

```text
docs/articles/experiencia-desenvolvimento-ia-sem-dominar-stack.md
```

## Rascunho Criado

- [`docs/articles/experiencia-desenvolvimento-ia-sem-dominar-stack.md`](../../../articles/experiencia-desenvolvimento-ia-sem-dominar-stack.md)

Observacao:

O texto ja foi reescrito como artigo de experiencia e inclui um espaco explicito
para linkar a parte tecnica quando ela existir. Ainda nao esta marcado como
pronto para publicacao porque depende de curadoria humana.

## Checklist de Execucao

- [x] Reler rascunho base.
- [x] Cruzar com `docs/reports/conversation-sources/README.md`.
- [x] Cruzar com `docs/reports/memory-and-learning-signals/README.md`.
- [x] Cruzar com `docs/reports/docs-framework-evolution/README.md`.
- [x] Escrever artigo final em `docs/articles/`.
- [x] Incluir rodape de coautoria.
- [x] Revisar se o texto nao exagera autonomia da IA nem apaga a direcao humana.

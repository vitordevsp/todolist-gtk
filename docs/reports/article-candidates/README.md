# Relatorio Final: Candidatos a Artigos

Este relatorio e a etapa de curadoria antes da geracao de artigos finais.

Marque os candidatos que devem virar post. Enquanto um item nao estiver
selecionado e direcionado manualmente, ele deve continuar como material interno.

Os candidatos estao separados em dois grupos:

- **Artigos tecnicos:** foco em GTK, Linux desktop, Flatpak, persistencia,
  empacotamento, versionamento e framework documental.
- **Artigos de experiencia:** foco na vivencia de desenvolvimento guiado por IA,
  principalmente quando a pessoa condutora nao domina previamente toda a stack.

## Grupo A: Artigos Tecnicos

### [ ] A1. Do "rodou aqui" ao Flatpak instalavel

Direcionamento:

Contar a evolucao do empacotamento: primeiro o app roda localmente, depois vira
binario PyInstaller, depois ganha metadados desktop e finalmente se consolida
como bundle Flatpak instalavel.

O artigo deve explicar a diferenca entre:

- executar codigo Python;
- gerar um binario solto;
- registrar um app no sistema Linux com `.desktop`, icone e metainfo;
- gerar um `.flatpak` distribuivel.

Sinais:

- `docs/reports/conversation-sources/README.md`: fase 8 da conversa Antigravity,
  sobre empacotamento Flatpak e identidade desktop.
- `docs/reports/conversation-sources/README.md`: divergencia entre PyInstaller
  como build local e Flatpak como distribuicao oficial.
- `docs/knowledge/bundle-manual.md`.
- `docs/plans/001-v1-todolist/plan.md`, secao de build e bundle.
- commit `98267bf`: manifesto Flatpak inicial.
- commit `6ddc40c`: bundle Flatpak deterministico.
- log de instalacao local em `docs/plans/001-v1-todolist/logs.md`.

Observacoes e direcao editorial humana:

```text

```

### [ ] A2. O erro que ensinou reprodutibilidade

Direcionamento:

Narrar o ponto critico do bundle: uma correcao anterior feita por IA tentou
resolver o empacotamento introduzindo downloads em tempo de bundle. O artigo deve
mostrar como isso levou a um contrato mais rigoroso: `make bundle` simples,
deterministico, sem `pip install`, `curl`, `wget`, `flatpak remote-add` ou fontes
remotas inesperadas.

Este artigo deve ter mais cara de post tecnico de engenharia: problema,
risco, diagnostico, decisao e solucao final.

Sinais:

- Pedido do usuario sobre staged changes inconsistentes e downloads durante o bundle.
- `docs/plans/001-v1-todolist/logs.md`: requisitos criticos para bundle Flatpak.
- `docs/plans/001-v1-todolist/plan.md`: regras de reprodutibilidade e seguranca.
- `Makefile`: uso de `--disable-download`.
- `docs/knowledge/bundle-manual.md`: contrato de bundle.
- `docs/reports/technical-decisions/README.md`: decisao "bundle deterministico".
- `docs/reports/conversation-sources/README.md`: divergencia entre a fase inicial
  e o estado final consolidado com Codex.

Observacoes e direcao editorial humana:

```text

```

### [ ] A3. GTK, Libadwaita e Flatpak como teste de realidade para agentes

Direcionamento:

Usar o projeto para mostrar por que desktop Linux nativo e um bom campo de teste
para agentes de IA. A stack exige mais do que escrever componentes: exige
versao de Libadwaita, bindings PyGObject, caminhos XDG, biblioteca Python
compartilhada, Flatpak, metainfo e validacao em ambiente real.

Sinais:

- `AGENTS.md`: boas praticas GTK4, Libadwaita, PyGObject, PyInstaller e Flatpak.
- `MEMORY.md`: retrocompatibilidade Libadwaita 1.1, `Adw.ToolbarView`,
  `Gtk.Box`, `Adw.Flap`, libpython e bundle Flatpak.
- `docs/reports/conversation-sources/README.md`: fases 0, 1, 7 e 8 da conversa Antigravity.
- `docs/knowledge/environment-setup.md`.
- `docs/knowledge/persistence-and-xdg.md`.
- `docs/reports/memory-and-learning-signals/README.md`.

Observacoes e direcao editorial humana:

```text

```

### [ ] A4. Persistencia correta: de `todos.db` solto ao XDG/Flatpak

Direcionamento:

Explicar a evolucao do armazenamento local. O projeto comeca com `todos.db`,
passa por uma ideia intermediaria de `databases/`, e fecha usando
`GLib.get_user_data_dir()` com app id. O artigo deve mostrar como esse detalhe
pequeno separa prototipo de app desktop minimamente correto.

Sinais:

- `MEMORY.md`: migracao SQLite e tabelas.
- `docs/reports/conversation-sources/README.md`: fase 6 registra banco em
  `databases/`, depois reavaliado.
- `docs/reports/conversation-sources/README.md`: fase 8 registra persistencia
  XDG/Flatpak.
- `docs/plans/001-v1-todolist/questions.md`: decisao humana sobre persistencia.
- `docs/knowledge/persistence-and-xdg.md`.
- commit `c352d8d`: consolidacao de persistencia.

Observacoes e direcao editorial humana:

```text

```

### [ ] A5. Makefile como interface de desenvolvimento nativo

Direcionamento:

Mostrar como o projeto flertou com uma interface familiar do mundo web
(`package.json`/`npm run dev`), mas acabou consolidando `Makefile` como interface
mais coerente para Python/GTK/Linux.

O artigo pode ensinar uma regra pratica: comandos de desenvolvimento tambem
comunicam a identidade tecnica do projeto.

Sinais:

- `docs/reports/conversation-sources/README.md`: fase 3, live reload e disputa
  Makefile vs package.json.
- `dev.py`: watcher customizado.
- `Makefile`: `run`, `dev`, `build`, `flatpak`, `bundle`, `uninstall`,
  `uninstall-data`, `clean`.
- `README.md`: comandos de execucao e build.

Observacoes e direcao editorial humana:

```text

```

### [ ] A6. Studio-coding em miniatura: framework proporcional ao projeto

Direcionamento:

Mostrar como uma versao pequena do framework foi aplicada sem criar camadas
vazias. O artigo deve explicar por que `knowledge`, `patterns`, `plans`,
`reports` e `articles` surgem quando tem funcao real, e nao por simetria com o
framework completo.

Sinais:

- `docs/README.md`.
- `docs/logs.md`.
- `docs/reports/docs-framework-evolution/README.md`.
- `docs/reports/conversation-sources/README.md`: fases 6, 7 e 9 da conversa
  Antigravity mostram a semente de plano, memoria e knowledge.
- `docs/articles/README.md`.
- `docs/reports/README.md`.
- commit `ca2010a`: instrumentalizacao minima de `docs`.
- commit `6b0d5bd`: frente editorial de artigos.

Observacoes e direcao editorial humana:

```text

```

### Rascunho existente do Grupo A

Arquivo:

- [`artigo_tecnico_linux_gtk.md`](./artigo_tecnico_linux_gtk.md)

Diagnostico editorial:

O rascunho tem um bom eixo tecnico, mas esta generico demais. Ele parece um guia
universal de GTK/Flatpak, quando o material mais forte esta na historia concreta
do projeto: as tentativas, mudancas de rota, diferencas entre PyInstaller e
Flatpak, persistencia XDG e o fechamento do bundle sem downloads inesperados.

O texto tambem precisa ser corrigido em alguns pontos:

- evitar dizer que o manifesto "baixa o SDK do GNOME 46" como se isso fizesse
  parte do bundle; o setup de runtime/SDK e pre-requisito separado;
- deixar claro que o bundle final nao empacota um binario PyInstaller do host;
- mencionar que GNOME 46 foi usado no estado validado, mas esta EOL e precisa
  migracao antes de distribuicao publica;
- trocar o tom de "guia definitivo" por um relato tecnico baseado em experiencia
  real.

O que aproveitar:

- a abertura sobre Python + GTK4 + Libadwaita;
- a comparacao entre PyInstaller e Flatpak;
- a ideia de persistencia XDG;
- a centralidade do `Makefile`.

Direcao de reescrita sugerida:

```text
Titulo possivel:
Do script Python ao Flatpak: o que eu aprendi empacotando um app GTK nativo com IA

Tese:
Criar a janela foi a parte facil. O aprendizado real apareceu quando o app
precisou se comportar como software Linux de verdade: com metadados, icone,
persistencia no lugar certo, bundle reprodutivel e instalacao testavel.

Estrutura:
1. O app comeca simples: Python, GTK4, Libadwaita e SQLite.
2. PyInstaller resolve o binario local, mas nao resolve distribuicao.
3. Flatpak exige manifesto, app id, .desktop, metainfo e runtime.
4. Persistencia precisa seguir XDG/Flatpak, nao a pasta do projeto.
5. O bundle final precisa ser deterministico: sem downloads no empacotamento.
6. O que ainda ficou pendente: runtime GNOME 46 EOL e screenshot real no metainfo.

Nota historica:
A maior parte da construcao inicial foi guiada com Antigravity usando Gemini 3
Flash, modelo de 2024. A consolidacao final do bundle, versionamento,
documentacao e relatorios foi feita depois com Codex/GPT-5.4.
```

## Grupo B: Artigos de Experiencia com IA

### [ ] B1. Um TodoList simples para testar IA de verdade

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

Observacoes e direcao editorial humana:

```text

```

### [ ] B2. Desenvolver guiando IA sem dominar a stack

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

Observacoes e direcao editorial humana:

```text

```

### [ ] B3. Quando a IA diz "pronto" cedo demais

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

Observacoes e direcao editorial humana:

```text

```

### [ ] B4. Coautoria humano-IA sem romantizar a automacao

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

Observacoes e direcao editorial humana:

```text

```

### [ ] B5. Documentacao que guia IA, nao so documenta codigo

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

Observacoes e direcao editorial humana:

```text

```

### [ ] B6. O projeto como diario de aprendizado, nao so repositorio de codigo

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

Observacoes e direcao editorial humana:

```text

```

### Rascunho existente do Grupo B

Arquivo:

- [`artigo_experiencia_ai.md`](./artigo_experiencia_ai.md)

Diagnostico editorial:

O rascunho tem uma premissa boa: desenvolver um app Linux nativo guiando IA sem
parar o trabalho principal. Mas o texto esta polido demais no sentido errado:
parece post motivacional sobre "IA Pair Programming" e perde o que ha de mais
interessante na historia real.

O artigo precisa trocar frases genericas por cenas e tensoes concretas:

- a stack era pouco familiar;
- o app era simples, mas tocava muitas camadas reais;
- o Antigravity/Gemini 3 Flash construiu quase todo o corpo inicial;
- Gemini 3 Flash e um modelo de 2024, o que torna o resultado mais interessante;
- a IA declarou o projeto pronto cedo demais;
- a etapa final com Codex/GPT-5.4 foi menos "criar do zero" e mais auditar,
  consolidar, corrigir bundle, versionar, estruturar docs e preparar curadoria;
- a pessoa humana atuou como diretora: definindo qualidade, fazendo perguntas,
  recusando atalhos e registrando conhecimento.

O que aproveitar:

- a ideia de "desenvolvedor como diretor";
- a barreira de entrada de uma stack nova;
- o projeto como laboratorio para `studio-coding`;
- a imagem de trabalhar em paralelo enquanto o agente executa.

Direcao de reescrita sugerida:

```text
Titulo possivel:
Eu guiei uma IA para criar meu primeiro app Linux nativo sem dominar GTK

Tese:
O experimento nao mostrou que "a IA faz tudo sozinha". Mostrou algo mais util:
com direcao humana, documentacao viva e revisao critica, um modelo de 2024
conseguiu levar um app simples muito longe. O fechamento exigiu outra camada de
criterio: auditoria, reproducibilidade, versionamento e curadoria.

Estrutura:
1. O desejo antigo: criar algo nativo para Linux.
2. O recorte pequeno: um TodoList, escolhido justamente por ser simples.
3. O fluxo com Antigravity e Gemini 3 Flash: plano, tarefa, walkthrough.
4. A stack desconhecida: GTK4, Libadwaita, PyGObject, Flatpak.
5. Onde a IA foi muito bem: UI, CRUD, sessoes, docs iniciais, build local.
6. Onde a direcao humana foi essencial: coerencia da stack, Makefile vs npm,
   persistencia, bundle seguro, docs como framework.
7. A fase Codex/GPT-5.4: consolidar, auditar e preparar o projeto para release.
8. O aprendizado: IA acelera, mas criterio ainda e a parte nobre do trabalho.

Nota historica:
Quase todo o corpo inicial do projeto foi construido com Antigravity usando
Gemini 3 Flash, modelo de 2024. A fase final contou com Codex/GPT-5.4 para
consolidacao tecnica, versionamento, tag `v0.1.0`, reports e estrutura editorial.
```

## Observacao Sobre Rascunhos Soltos

Foram encontrados dois arquivos soltos na raiz:

- `artigo_experiencia_ai.md`
- `artigo_tecnico_linux_gtk.md`

Eles agora foram avaliados como rascunhos existentes dos grupos A e B. Antes de
move-los para `docs/articles/`, vale decidir se devem virar:

- fonte complementar;
- rascunhos a reescrever em `docs/articles/`;
- material descartavel;
- insumo para algum candidato acima.

## Proxima Acao

1. Escolher um grupo inicial: tecnico ou experiencia.
2. Marcar os candidatos que devem virar artigo.
3. Preencher observacoes e direcao editorial humana.
4. Definir tom, audiencia e profundidade de cada item.
5. Pedir explicitamente a geracao do primeiro artigo em `docs/articles/`.

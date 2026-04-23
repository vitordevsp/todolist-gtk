# Relatorio: Linha do Tempo do Projeto

## Objetivo

Organizar a evolucao real do TodoList GTK em marcos narrativos que possam
sustentar artigos futuros.

## Fontes Consultadas

- `git log --oneline --decorate --reverse --all`
- `CHANGELOG.md`
- `README.md`
- `docs/plans/001-v1-todolist/logs.md`
- `docs/plans/001-v1-todolist/plan.md`
- conversa Antigravity/Gemini:
  `/home/vitordevsp/.gemini/antigravity/brain/16b54b2c-7810-4127-8837-9681a0103cf4/`

## Linha do Tempo Inicial

### 2026-04-21 - Abertura do experimento

Sinais:

- commit `949d32f`: criacao do README inicial;
- `README.md`: descreve o projeto como teste com Antigravity/Gemini para construir app nativo Linux;
- commit `da49b55`: estrutura inicial, `Makefile`, `.gitignore` e `dev.py`.

Leitura editorial:

O experimento nasce pequeno, mas com uma ambicao clara: testar se um modelo de IA
consegue conduzir um app desktop nativo com UX razoavel e fluxo de build.

### 2026-04-21 - Produto funcional aparece cedo

Sinais:

- commit `e42f4b7`: implementa a funcionalidade principal com SQLite;
- `MEMORY.md`: registra aprendizado sobre GTK/Libadwaita, `Adw.Flap` e SQLite;
- commit `159bb84`: adiciona metadados desktop e icone.

Leitura editorial:

A parte funcional do app foi resolvida rapidamente. Isso reforca a ideia de que o
valor do experimento nao esta na complexidade do produto, mas no ciclo completo:
app, memoria, empacotamento, validacao e narrativa.

### 2026-04-21 - Primeira camada de empacotamento e docs

Sinais:

- commit `98267bf`: adiciona manifesto Flatpak inicial;
- commit `06d86f8`: consolida `AGENTS.md`, `MEMORY.md`, patterns, plano e manual de bundle;
- conversa Antigravity/Gemini final: cria `docs/resources/bundle-manual.md` e registra a entrega no plano.

Leitura editorial:

O projeto deixa de ser so codigo e passa a ter uma camada operacional. Esse e um
marco importante para artigos sobre desenvolvimento assistido por documentacao.

### 2026-04-22/23 - Auditoria e consolidacao com Codex

Sinais:

- commit `7594469`: migra app id para `br.com.vitordevsp.TodoList`;
- commit `c352d8d`: consolida persistencia, import/runtime e icones;
- commit `6ddc40c`: torna bundle Flatpak deterministico;
- commit `1fedfae`: consolida `docs/knowledge/`;
- commit `30db42f`: fecha a fase 5 no plano.

Leitura editorial:

O ponto de virada e a descoberta de que a correcao anterior do bundle havia
introduzido downloads indesejados. A frente muda de "fazer funcionar" para
"fazer de forma reprodutivel, auditavel e segura".

### 2026-04-23 - Versionamento e frente editorial

Sinais:

- `CHANGELOG.md`: criado como registro de releases e experimento;
- `metainfo.xml`: recebe `version="0.0.0"`;
- `docs/README.md`: `docs/` passa a ser reconhecida como instancia reduzida do
  framework `studio-coding`;
- esta frente cria `docs/articles/` e `docs/reports/`.

Leitura editorial:

O projeto passa a olhar para si mesmo como fonte de artigos. A documentacao deixa
de ser apenas suporte de desenvolvimento e vira materia-prima editorial.

## Lacunas

- A linha do tempo da conversa Antigravity/Gemini ainda precisa de leitura das
  versoes incrementais `.resolved.N`.
- Falta comparar a hora real dos commits com a ordem das mensagens nas conversas.
- Falta decidir como citar conversas em textos publicos.

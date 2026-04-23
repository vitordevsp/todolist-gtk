# Relatorio Final: Candidatos a Artigos

Este relatorio e a etapa de curadoria antes da geracao de artigos finais.

Marque os candidatos que devem virar post. Enquanto um item nao estiver
selecionado e direcionado manualmente, ele deve continuar como material interno.

## Candidatos

### [ ] 1. Um TodoList simples para testar IA de verdade

Direcionamento:

Explicar por que um app simples foi suficiente para testar varias camadas reais
de desenvolvimento: UI nativa, persistencia, build, Flatpak, docs e validacao.

Sinais:

- `README.md`: projeto como caso de teste com Antigravity/Gemini.
- commits `da49b55`, `e42f4b7`, `159bb84`, `98267bf`.
- `CHANGELOG.md`: versao `0.0.0` registra escopo funcional e experimental.
- `docs/reports/project-timeline/`.

Observacoes e direcao editorial humana:

```text

```

### [ ] 2. Do "rodou aqui" ao Flatpak instalavel

Direcionamento:

Contar a evolucao do empacotamento: PyInstaller como conveniencia local,
Flatpak como distribuicao oficial, e a importancia de nao baixar dependencias
durante o bundle.

Sinais:

- `docs/knowledge/bundle-manual.md`.
- `docs/plans/v1_todolist/plan.md`, secao de build e bundle.
- commit `6ddc40c`.
- log de instalacao local registrado em `docs/plans/v1_todolist/logs.md`.
- `docs/reports/technical-decisions/`.

Observacoes e direcao editorial humana:

```text

```

### [ ] 3. O erro que ensinou reprodutibilidade

Direcionamento:

Narrar o ponto critico: uma correcao anterior feita por IA tentou resolver o
bundle baixando dependencias em tempo de empacotamento, e isso levou a um
contrato mais rigoroso de build deterministico.

Sinais:

- pedido do usuario sobre staged changes e inconsistencias no bundle.
- `docs/plans/v1_todolist/logs.md`: requisitos criticos para bundle.
- `docs/plans/v1_todolist/plan.md`: regras contra downloads inesperados.
- `Makefile`: `--disable-download`.

Observacoes e direcao editorial humana:

```text

```

### [ ] 4. Documentacao que guia IA, nao so documenta codigo

Direcionamento:

Mostrar como `docs/` virou ferramenta operacional: planos, logs, perguntas,
knowledge e agora reports/articles como parte do fluxo `studio-coding`.

Sinais:

- `docs/README.md`.
- `docs/plans/v1_todolist/`.
- `docs/knowledge/`.
- `docs/logs.md`.
- `docs/reports/docs-framework-evolution/`.

Observacoes e direcao editorial humana:

```text

```

### [ ] 5. Coautoria humano-IA sem romantizar a automacao

Direcionamento:

Explorar o papel humano na direcao: escolher stack, corrigir rota, exigir
bundle seguro, pedir docs melhores, versionamento e estrutura editorial.

Sinais:

- `README.md`: experimento com Antigravity/Gemini.
- conversa atual com Codex.
- `CHANGELOG.md`, secao `Experiment Notes`.
- `docs/reports/conversation-sources/`.

Observacoes e direcao editorial humana:

```text

```

### [ ] 6. GTK, Libadwaita e Flatpak como teste de realidade para agentes

Direcionamento:

Usar os aprendizados de GTK/Libadwaita, PyInstaller, libpython, XDG e Flatpak
para mostrar como o desktop Linux revela limites praticos de agentes de IA.

Sinais:

- `AGENTS.md`.
- `MEMORY.md`.
- `docs/knowledge/environment-setup.md`.
- `docs/knowledge/persistence-and-xdg.md`.
- `docs/reports/memory-and-learning-signals/`.

Observacoes e direcao editorial humana:

```text

```

### [ ] 7. Studio-coding em miniatura: framework proporcional ao projeto

Direcionamento:

Mostrar como uma versao pequena do framework foi aplicada sem criar camadas
vazias: `knowledge`, `patterns`, `plans`, `reports` e `articles` surgem quando
tem funcao real.

Sinais:

- `docs/README.md`.
- `docs/logs.md`.
- `docs/reports/README.md`.
- `docs/articles/README.md`.
- `docs/reports/editorial-themes/`.

Observacoes e direcao editorial humana:

```text

```

## Proxima Acao

1. Marcar os candidatos que devem virar artigo.
2. Preencher observacoes e direcao editorial humana.
3. Definir tom e audiencia de cada item.
4. Pedir explicitamente a geracao do primeiro artigo em `docs/articles/`.

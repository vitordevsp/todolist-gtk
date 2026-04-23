# Task: Artigo Tecnico Linux/GTK/Flatpak

## Status

- [x] Em curadoria
- [x] Rascunho reescrito
- [x] Revisado com fontes
- [ ] Pronto para publicar/exportar

## Rascunho Base

- [`artigo_tecnico_linux_gtk.md`](../../../../artigo_tecnico_linux_gtk.md)

## Grupo Original do Relatorio de Candidatos

Este artigo pertence ao **Grupo A: Artigos Tecnicos**.

Artigos tecnicos focam em GTK, Linux desktop, Flatpak, persistencia,
empacotamento, versionamento e framework documental.

## Candidatos Relacionados do Grupo A

### A1. Do "rodou aqui" ao Flatpak instalavel

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

### A2. O erro que ensinou reprodutibilidade

Direcionamento:

Narrar o ponto critico do bundle: uma correcao anterior feita por IA tentou
resolver o empacotamento introduzindo downloads em tempo de bundle. O artigo deve
mostrar como isso levou a um contrato mais rigoroso: `make bundle` simples,
deterministico, sem `pip install`, `curl`, `wget`, `flatpak remote-add` ou fontes
remotas inesperadas.

Este artigo deve ter mais cara de post tecnico de engenharia: problema, risco,
diagnostico, decisao e solucao final.

Sinais:

- Pedido do usuario sobre staged changes inconsistentes e downloads durante o bundle.
- `docs/plans/001-v1-todolist/logs.md`: requisitos criticos para bundle Flatpak.
- `docs/plans/001-v1-todolist/plan.md`: regras de reprodutibilidade e seguranca.
- `Makefile`: uso de `--disable-download`.
- `docs/knowledge/bundle-manual.md`: contrato de bundle.
- `docs/reports/technical-decisions/README.md`: decisao "bundle deterministico".
- `docs/reports/conversation-sources/README.md`: divergencia entre a fase inicial
  e o estado final consolidado com Codex.

### A3. GTK, Libadwaita e Flatpak como teste de realidade para agentes

Direcionamento:

Usar o projeto para mostrar por que desktop Linux nativo e um bom campo de teste
para agentes de IA. A stack exige mais do que escrever componentes: exige versao
de Libadwaita, bindings PyGObject, caminhos XDG, biblioteca Python
compartilhada, Flatpak, metainfo e validacao em ambiente real.

Sinais:

- `AGENTS.md`: boas praticas GTK4, Libadwaita, PyGObject, PyInstaller e Flatpak.
- `MEMORY.md`: retrocompatibilidade Libadwaita 1.1, `Adw.ToolbarView`,
  `Gtk.Box`, `Adw.Flap`, libpython e bundle Flatpak.
- `docs/reports/conversation-sources/README.md`: fases 0, 1, 7 e 8 da conversa Antigravity.
- `docs/knowledge/environment-setup.md`.
- `docs/knowledge/persistence-and-xdg.md`.
- `docs/reports/memory-and-learning-signals/README.md`.

### A4. Persistencia correta: de `todos.db` solto ao XDG/Flatpak

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

### A5. Makefile como interface de desenvolvimento nativo

Direcionamento:

Mostrar como o projeto flertou com uma interface familiar do mundo web
(`package.json`/`npm run dev`), mas acabou consolidando `Makefile` como interface
mais coerente para Python/GTK/Linux.

Sinais:

- `docs/reports/conversation-sources/README.md`: fase 3, live reload e disputa
  Makefile vs package.json.
- `dev.py`: watcher customizado.
- `Makefile`: `run`, `dev`, `build`, `flatpak`, `bundle`, `uninstall`,
  `uninstall-data`, `clean`.
- `README.md`: comandos de execucao e build.

## Diagnostico do Rascunho Atual

O rascunho tem um bom eixo tecnico, mas esta generico demais. Ele parece um guia
universal de GTK/Flatpak, quando o material mais forte esta na historia concreta
do projeto: tentativas, mudancas de rota, diferencas entre PyInstaller e
Flatpak, persistencia XDG e fechamento do bundle sem downloads inesperados.

## Correcoes Obrigatorias

- Evitar dizer que o manifesto "baixa o SDK do GNOME 46" como se isso fizesse
  parte do bundle; o setup de runtime/SDK e pre-requisito separado.
- Deixar claro que o bundle final nao empacota um binario PyInstaller do host.
- Mencionar que GNOME 46 foi usado no estado validado, mas esta EOL e precisa
  migracao antes de distribuicao publica.
- Trocar o tom de "guia definitivo" por relato tecnico baseado em experiencia real.

## O Que Aproveitar

- A abertura sobre Python + GTK4 + Libadwaita.
- A comparacao entre PyInstaller e Flatpak.
- A ideia de persistencia XDG.
- A centralidade do `Makefile`.

## Direcao de Reescrita

Titulo possivel:

```text
Do script Python ao Flatpak: o que eu aprendi empacotando um app GTK nativo com IA
```

Tese:

```text
Criar a janela foi a parte facil. O aprendizado real apareceu quando o app
precisou se comportar como software Linux de verdade: com metadados, icone,
persistencia no lugar certo, bundle reprodutivel e instalacao testavel.
```

Estrutura sugerida:

1. O app comeca simples: Python, GTK4, Libadwaita e SQLite.
2. PyInstaller resolve o binario local, mas nao resolve distribuicao.
3. Flatpak exige manifesto, app id, `.desktop`, metainfo e runtime.
4. Persistencia precisa seguir XDG/Flatpak, nao a pasta do projeto.
5. O bundle final precisa ser deterministico: sem downloads no empacotamento.
6. O que ainda ficou pendente: runtime GNOME 46 EOL e screenshot real no metainfo.

Nota historica obrigatoria:

```text
A maior parte da construcao inicial foi guiada com Antigravity usando Gemini 3
Flash, modelo de 2024. A consolidacao final do bundle, versionamento,
documentacao e relatorios foi feita depois com Codex/GPT-5.4.
```

## Arquivo Final Esperado

```text
docs/articles/linux-gtk-flatpak-com-ia.md
```

## Rascunho Criado

- [`docs/articles/linux-gtk-flatpak-com-ia.md`](../../../articles/linux-gtk-flatpak-com-ia.md)

Observacao:

O texto ja foi reescrito como tutorial tecnico e referencia a primeira parte da
serie. Ainda nao esta marcado como pronto para publicacao porque depende de
curadoria humana e da decisao sobre runtime Flatpak suportado antes de
distribuicao publica.

## Checklist de Execucao

- [x] Reler rascunho base.
- [x] Cruzar com `docs/reports/conversation-sources/README.md`.
- [x] Cruzar com `docs/knowledge/bundle-manual.md`.
- [x] Cruzar com `docs/plans/001-v1-todolist/plan.md`.
- [x] Escrever artigo final em `docs/articles/`.
- [x] Incluir rodape de coautoria.
- [x] Revisar se nao ha afirmacoes tecnicas incorretas sobre Flatpak/runtime.

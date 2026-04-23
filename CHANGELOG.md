# Changelog

Todas as mudancas notaveis deste projeto serao documentadas neste arquivo.

O formato e baseado em [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e este projeto segue [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Este projeto tambem funciona como registro de um experimento: construir um aplicativo
desktop Linux simples, mas completo, guiando modelos de IA durante planejamento,
implementacao, empacotamento, validacao e documentacao.

## [Unreleased]

### Added

- Criado `docs/plans/000-desktop/` como desktop operacional para inbox e backlog geral.
- Criados dois artigos em curadoria em `docs/articles/`: relato de experiencia com IA e tutorial tecnico Python/GTK/Flatpak.

### Changed

- Renumerados os planos para a taxonomia `000`, `001`, `002` e `003`.
- Movidos `todolist.md` e `backlog.md` para `docs/plans/000-desktop/`.
- Atualizados links entre os dois artigos editoriais.

## [0.1.0] - 2026-04-23

Primeira release curavel do experimento TodoList GTK.

Esta versao marca o fechamento da base funcional/documental inicial e cria a
infraestrutura minima para transformar a historia real do projeto em artigos
futuros.

### Added

- Instrumentalizacao minima de `docs/` como instancia reduzida do framework `studio-coding`.
- Criacao da frente editorial para transformar a historia real do projeto em reports, candidatos e futuros artigos.
- Criacao de `docs/articles/` como destino futuro para artigos finais ou rascunhos aprovados.
- Criacao de `docs/reports/` como camada intermediaria de investigacao e curadoria.
- Criacao do plano `docs/plans/002-editorial-articles-from-project-history/`.
- Criacao do relatorio final `docs/reports/article-candidates/` com checkboxes, direcionamento, sinais e campo de observacao humana.
- Criacao de indices minimos para `docs/`, `docs/knowledge/`, `docs/patterns/` e `docs/plans/`.

### Changed

- Atualizado `docs/plans/000-desktop/todolist.md` para funcionar como inbox simples de planos.
- Atualizado `docs/README.md` para incluir `reports/` e `articles/` como camadas reais do recorte `studio-coding`.
- Atualizado o metainfo AppStream para declarar `0.1.0` como release atual.

### Documented

- Registrada a diferenca entre reports internos e articles publicaveis.
- Registrado o pipeline editorial: plano, reports, candidatos, curadoria humana e so depois artigos finais.
- Registrada a regra de rodape de coautoria entre Vitor Sampaio e Codex para artigos finais.
- Registrado que conversas de IA sao contexto editorial, mas devem ser cruzadas com commits, docs, memoria e planos.

### Validated

- Validado `appstreamcli validate --no-net` para o metainfo AppStream.
- Validado `git diff --check` antes da release.

## [0.0.0] - 2026-04-23

Versao-base de historico. Este marco registra o estado inicial consolidado do
experimento antes da primeira release `0.1.0` e antes da tag publica.

### Added

- Criado um aplicativo desktop nativo Linux com Python, GTK4, Libadwaita e PyGObject.
- Implementado fluxo principal de lista de tarefas com criacao, conclusao e remocao de tarefas.
- Implementado suporte a multiplas sessoes/listas para organizar tarefas por contexto.
- Adicionada barra lateral em layout de duas colunas, inspirada em aplicativos de notas simples.
- Adicionados estados vazios com `Adw.StatusPage` para guiar o usuario quando nao ha sessoes ou tarefas.
- Adicionadas acoes de gerenciamento de sessoes, incluindo criacao, renomeacao e exclusao com confirmacao.
- Implementado mapeamento automatico de icones por palavras-chave em nomes de listas.
- Criado modo de desenvolvimento com live reload via `dev.py` e `make dev`.
- Criado fluxo `make run` para execucao local direta do codigo Python.
- Criado fluxo `make build` para gerar binario local com PyInstaller em `dist/`.
- Criado manifesto Flatpak oficial com app id `br.com.vitordevsp.TodoList`.
- Criado launcher Flatpak em `bin/todolist-gtk`.
- Criado fluxo `make bundle` para gerar `todolist.flatpak` na raiz do projeto.
- Criados alvos `make uninstall` e `make uninstall-data` para repetir o ciclo de instalacao e teste do bundle.
- Criados metadados desktop: arquivo `.desktop`, metainfo AppStream e icone SVG.
- Criado `CHANGELOG.md` como fonte humana de historico de releases.
- Registrado o ponto inicial de versionamento no metainfo AppStream com `version="0.0.0"`.

### Changed

- Migrado o app id de `com.vitordevsp.TodoList` para `br.com.vitordevsp.TodoList`.
- Renomeados manifesto, arquivo desktop, metainfo e icone para acompanhar o app id oficial.
- Movido o CSS customizado de `data/style.css` para `src/styles/style.css`, deixando `data/` reservado para metadados desktop.
- Separado o fluxo local PyInstaller do fluxo oficial Flatpak.
- Alterado o bundle Flatpak para empacotar o codigo Python fonte e executar pelo runtime GNOME, em vez de embutir um binario PyInstaller gerado no host.
- Atualizado o carregamento de CSS para funcionar em desenvolvimento, PyInstaller e Flatpak.
- Atualizado o bootstrap Python para suportar import relativo em pacote e execucao direta.
- Atualizado o README para explicar os fluxos `run`, `dev`, `build`, `flatpak` e `bundle`.
- Reorganizada a documentacao tecnica em `docs/knowledge/`.

### Fixed

- Corrigido o caminho de persistencia do SQLite para usar `GLib.get_user_data_dir()` com o app id, evitando banco salvo em caminho solto do repositorio.
- Removida permissao Flatpak antiga de filesystem especifico que nao era mais necessaria.
- Removidos downloads e instalacoes automaticas dos alvos principais de build/bundle.
- Corrigida a estrategia de bundle apos detectar que empacotar binario PyInstaller dentro do Flatpak misturava ambiente do host com runtime Flatpak.
- Garantido que o manifesto Flatpak liste fontes locais explicitas com `type: file`.
- Ajustado `.gitignore` para ignorar artefatos de build, bundle, banco local e arquivos locais de agente.

### Documented

- Criado plano `docs/plans/001-v1-todolist/` com `plan.md`, `tasks.md`, `logs.md` e `questions.md`.
- Registradas perguntas de decisao humana sobre persistencia, migracao de banco antigo e escopo de icones inteligentes.
- Criado `docs/knowledge/environment-setup.md` com setup de ferramentas, runtime/SDK Flatpak e comandos de verificacao.
- Criado `docs/knowledge/bundle-manual.md` com contrato de bundle deterministico, fluxo interno e ciclo completo de instalacao/desinstalacao.
- Criado `docs/knowledge/persistence-and-xdg.md` explicando persistencia local e diferenca entre execucao normal e Flatpak.
- Criado `docs/knowledge/ui-ux-patterns.md` com padroes de layout, estados vazios, icones e CSS.
- Criado `docs/knowledge/project-structure.md` para registrar a fronteira entre `src/`, `src/styles/`, `data/`, manifesto e dados do usuario.
- Registrado que `make bundle` deve falhar se surgirem fontes remotas inesperadas, usando `--disable-download`.
- Registrada a limitacao dos single-file bundles Flatpak: o bundle do app e instalavel diretamente, mas runtimes precisam existir ou vir de um runtime repo.

### Validated

- Validado `python3 -m py_compile` nos modulos principais.
- Validado `flatpak-builder --show-manifest`.
- Validado `make build` como fluxo local separado.
- Validado `make bundle` gerando `todolist.flatpak` na raiz sem `pip install`, `curl`, `wget`, `flatpak remote-add` ou downloads inesperados durante o bundle.
- Validado `flatpak install --user -y ./todolist.flatpak` com instalacao concluida a partir do remoto local `todolist-origin`.
- Validado `flatpak run br.com.vitordevsp.TodoList` sem traceback na execucao instalada.
- Validado que a execucao Flatpak cria o banco no sandbox do app.
- Validado `appstreamcli validate --no-net` para o metainfo AppStream.
- Validado `git diff --check` durante o fechamento.

### Known Issues

- O runtime `org.gnome.Platform//46` esta em fim de vida e deve ser migrado para uma branch GNOME suportada antes de distribuicao publica.
- A instalacao tambem reportou runtimes GL `org.freedesktop.Platform` 23.08 como sem suporte por causa da base antiga.
- `make run` ainda precisa de validacao final em uma sessao grafica real; no sandbox Codex, GTK nao inicializa por falta de display/dconf gravavel.
- O projeto ainda nao tem captura de tela real versionada para satisfazer completamente a URL de screenshot do metainfo.

### Experiment Notes

- O projeto foi construido como teste pratico de colaboracao humano-IA, inicialmente guiando o Antigravity/Gemini dentro dos limites do plano gratuito.
- O escopo funcional foi propositalmente simples, mas completo o bastante para exercitar UI nativa, persistencia, empacotamento Linux, documentacao viva e validacao de entrega.
- A etapa final revelou um limite importante: uma IA anterior tentou corrigir o bundle introduzindo downloads em tempo de empacotamento, o que motivou a consolidacao de um pipeline mais deterministico.
- A principal decisao arquitetural do fechamento foi tratar Flatpak como formato oficial de distribuicao e PyInstaller apenas como conveniencia local.

[Unreleased]: https://github.com/vitordevsp/todolist-gtk/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/vitordevsp/todolist-gtk/compare/85f94fb...v0.1.0
[0.0.0]: https://github.com/vitordevsp/todolist-gtk/commit/85f94fb

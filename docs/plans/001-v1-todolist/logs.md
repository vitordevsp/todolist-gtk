# Log de Alterações do Plano (001-v1-todolist)

Este arquivo registra as principais mudanças e decisões tomadas durante a execução deste plano.

## [2026-04-21] - Reestruturação e Consolidação
- Reorganização da documentação para o padrão "Plano como Pasta".
- Registro da intenção de rever o local do banco de dados; a implementação atual ainda usa SQLite via `GLib.get_user_data_dir()`.
- Início da documentação extensiva do código (Google Style).
- Criação do `AGENTS.md` e `MEMORY.md` para persistência de conhecimento.

## [2026-04-21] - Empacotamento e Manuais de Conhecimento
- Criação do manual completo de empacotamento em `docs/knowledge/bundle-manual.md`.
- Inclusão de seções de Debug e Gerenciamento de Dependências (Pip).
- Movimentação inicial do `backlog.md` para a camada de planos.
- Consolidação de aprendizados sobre `libpython` e Bundles `.flatpak` no `AGENTS.md` e `MEMORY.md`.

## [2026-04-22] - Consolidação Final e Identidade Brasileira
- Renomeação de `docs/resources` para `docs/knowledge`.
- Criação de novos guias: `ui-ux-patterns.md` e `persistence-and-xdg.md`.
- Renomeação de todo o projeto para o ID brasileiro `br.com.vitordevsp.TodoList`.
- Refatoração do `Makefile` com padrões profissionais de build (cache centralizado em `build/`).

## [2026-04-22] - Sincronização do plano com o estado atual
- Atualização de `plan.md` para refletir a estrutura atual do repositório, incluindo `docs/knowledge/`, manifesto Flatpak brasileiro e fluxo PyInstaller/Flatpak.
- Atualização de `tasks.md` separando o que já está implementado da consolidação ainda pendente.
- Criação de `questions.md` para decisões humanas que não devem ser resolvidas por suposição.
- Identificada divergência entre a documentação de persistência, a tarefa antiga sobre `databases/` e o comportamento real de `src/models.py`.

## [2026-04-22] - Requisitos críticos para bundle Flatpak
- Registrado que staged changes anteriores foram feitas por outra IA e devem ser auditadas antes de virarem base da v1.
- Adicionada uma seção dedicada ao pipeline de build e bundle Flatpak em `plan.md`.
- Definido que `make bundle` não deve baixar dependências, instalar pacotes, configurar remotes ou depender de efeitos colaterais externos.
- Registrado o fluxo desejado: build local, exportação para `build/repo` e geração de `todolist.flatpak` na raiz via `flatpak build-bundle`.
- Documentada a limitação importante dos single-file bundles: são instaláveis diretamente, mas não carregam todos os runtimes para instalação totalmente offline em máquina limpa.

## [2026-04-22] - Implementação da fase 5
- Atualizado `src/models.py` para gravar o banco em `GLib.get_user_data_dir()/br.com.vitordevsp.TodoList/todos.db`.
- Expandido o mapeamento de ícones inteligentes em `src/window.py` e alinhado `docs/knowledge/ui-ux-patterns.md`.
- Removido download/instalação automática dos alvos principais de build e bundle.
- Alterado o bundle oficial para empacotar o código Python e executar pelo runtime GNOME, em vez de embutir um binário PyInstaller gerado no host.
- Adicionado `bin/todolist-gtk` como launcher Flatpak.
- Ajustado o manifesto para usar fontes locais explícitas (`type: file`) e removida a permissão antiga `--filesystem=xdg-data/todolist-gtk:create`.
- Validado `make bundle`: gerou `todolist.flatpak` na raiz sem downloads durante a etapa de bundle.
- Validado `flatpak install --user ./todolist.flatpak` e `timeout 5s flatpak run br.com.vitordevsp.TodoList`; a execução instalada iniciou sem traceback e criou o banco na sandbox.
- Validado `make build` como fluxo local separado de PyInstaller.
- Observado aviso de EOL do runtime `org.gnome.Platform//46`; antes de distribuição pública, migrar para um runtime GNOME suportado.

## [2026-04-22] - Checagem final de instalação local do bundle
- Executado `flatpak install --user -y ./todolist.flatpak` pelo usuário após `make bundle`.
- Instalação concluída para `br.com.vitordevsp.TodoList` a partir do remoto local `todolist-origin`, sem download de conteúdo do app (`0 byte`).
- Permissões exibidas na instalação: `ipc`, `fallback-x11`, `wayland`, `x11` e `dri`.
- Confirmado novamente o aviso de fim de vida do runtime `org.gnome.Platform//46`.
- Observado também aviso de fim de vida para runtimes GL `org.freedesktop.Platform.GL.default//23.08` e `23.08-extra`; essa pendência fica agrupada na futura migração para um runtime GNOME suportado.

## [2026-04-23] - Renumeração do sistema de planos
- Plano renomeado de `v1_todolist` para `001-v1-todolist`.
- `backlog.md` e `todolist.md` movidos para `docs/plans/000-desktop/`.
- Mantida esta pasta como plano principal da consolidação da v1.

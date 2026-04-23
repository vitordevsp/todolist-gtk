# Tarefas do Projeto (001-v1-todolist)

Este arquivo contém a lista de tarefas permanentes para o acompanhamento do desenvolvimento desta versão.

## Fase 1: Setup e Estrutura Inicial (✅ Concluído)
- [x] Criar estrutura básica de diretórios.
- [x] Implementar esqueleto GTK4/Libadwaita.
- [x] Configurar Makefile e Live Reload.

## Fase 2: Redesign e Multi-Sessão (✅ Concluído)
- [x] Implementar layout estilo Simplenote.
- [x] Adicionar suporte a múltiplas listas (Sessões).
- [x] Migrar banco de dados SQLite.

## Fase 3: Gerenciamento e Polimento (✅ Concluído)
- [x] Implementar Renomeação e Exclusão de sessões.
- [x] Adicionar ícones inteligentes e Estado Vazio (`Adw.StatusPage`).
- [x] Criar sistema de Build e README.

## Fase 4: Identidade, Empacotamento e Conhecimento (✅ Base implementada)
- [x] Migrar app id de `com.vitordevsp.TodoList` para `br.com.vitordevsp.TodoList`.
- [x] Renomear manifesto Flatpak para `br.com.vitordevsp.TodoList.yml`.
- [x] Renomear arquivos em `data/` para acompanhar o app id oficial.
- [x] Atualizar README com fluxo de setup, build e bundle Flatpak.
- [x] Criar guias em `docs/knowledge/` para ambiente, bundle, UI/UX e persistencia.
- [x] Consolidar `AGENTS.md` e `MEMORY.md` como fontes de contexto do projeto.
- [x] Documentar os principais modulos Python com docstrings.

## Fase 5: Alinhamento Final (🚧 Em andamento)
- [x] Decidir o caminho definitivo de persistencia do SQLite em `questions.md`.
- [x] Atualizar `src/models.py` apos a decisao de persistencia.
- [x] Atualizar `docs/knowledge/persistence-and-xdg.md` para refletir exatamente o comportamento final.
- [x] Ajustar o manifesto Flatpak removendo a permissao `--filesystem=xdg-data/todolist-gtk:create`.
- [x] Decidir o escopo do mapeamento de icones inteligentes em `questions.md`.
- [x] Expandir o mapeamento de icones inteligentes em `src/window.py`.
- [x] Alinhar `docs/knowledge/ui-ux-patterns.md` com as categorias implementadas.
- [x] Auditar as staged changes feitas anteriormente por outra IA antes de manter qualquer alteracao de build.
- [x] Remover downloads/instalacoes automaticas dos alvos principais de build e bundle.
- [x] Separar setup de maquina em documentacao, deixando `make build` e `make bundle` deterministico.
- [x] Garantir que `make bundle` gere `./todolist.flatpak` a partir de repositorio local `build/repo`.
- [x] Validar que o log de `make bundle` nao contem `pip install`, `curl`, `wget`, `flatpak remote-add` ou downloads inesperados.
- [ ] Validar `make run` em uma sessao grafica real; no sandbox Codex, GTK nao inicializa por falta de display/dconf gravavel.
- [x] Validar `make build`.
- [x] Validar `make bundle` quando o ambiente Flatpak estiver pronto.
- [x] Validar instalacao com `flatpak install --user ./todolist.flatpak`.
- [x] Validar execucao instalada com `flatpak run br.com.vitordevsp.TodoList`.
- [x] Resolver ou fechar as perguntas registradas em `questions.md`.
- [ ] Avaliar migracao do runtime Flatpak de GNOME 46 para um runtime suportado antes de distribuicao publica.

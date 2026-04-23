# Plano de Desenvolvimento: TodoList GTK (v1)

Este documento registra o estado atual da v1 do **TodoList GTK** e orienta as proximas manutencoes. A aplicacao ja possui uma primeira versao funcional; o foco atual e alinhar identidade, documentacao, persistencia e empacotamento para deixar o projeto coerente como app desktop nativo Linux.

## 1. Visão Geral
O objetivo da v1 e entregar um gerenciador de tarefas simples, nativo e agradavel de usar no Linux, seguindo GTK4 + Libadwaita e um layout inspirado no Simplenote:

- barra lateral com multiplas listas/sessoes;
- area principal focada nas tarefas da sessao selecionada;
- persistencia local em SQLite;
- workflow de desenvolvimento com live reload;
- build local via PyInstaller;
- distribuicao Linux por Flatpak.

## 2. Estado Atual

Status geral: **v1 funcional, com consolidacao tecnica em andamento**.

Ja existe uma aplicacao executavel via `make run` e `make dev`, com CRUD basico de tarefas e sessoes, estado vazio, dialogs de criacao/renomeacao/exclusao, icones automaticos e empacotamento configurado. A identidade do app foi migrada para `br.com.vitordevsp.TodoList`.

As respostas em `questions.md` definem a direcao da consolidacao:

- persistencia usando caminho montado com `os.path.join(...)` sobre o diretorio XDG retornado pela GLib, evitando caminho absoluto fixo;
- sem necessidade de migracao automatica de banco antigo, porque a v1 ainda nao foi distribuida;
- expansao do mapeamento de icones inteligentes para cobrir as categorias ja documentadas.

O ponto critico agora e revisar o pipeline de build/bundle porque as staged changes feitas por outra IA alteraram scripts que antes geravam logs limpos e introduziram risco de downloads inesperados durante a geracao do bundle.

---

## 3. Stack Tecnológica
- **Linguagem:** Python 3 (PyGObject)
- **Interface:** GTK4 + Libadwaita (Compatível com v1.1)
- **Componentes principais:** `Adw.Application`, `Adw.ApplicationWindow`, `Adw.Flap`, `Adw.HeaderBar`, `Adw.ActionRow`, `Gtk.ListBox`, `Gtk.Entry`, `Gtk.Stack`, `Adw.StatusPage`.
- **Persistência:** SQLite multi-sessao via `src/models.py`.
- **Build local opcional:** PyInstaller para binario rapido em `dist/`.
- **Distribuição oficial:** Flatpak com app id `br.com.vitordevsp.TodoList`, empacotando o codigo Python para rodar no runtime GNOME.
- **Docs do projeto:** `AGENTS.md`, `MEMORY.md`, `docs/knowledge/`, `docs/patterns/` e este plano como pasta.

---

## 4. Estrutura Atual do Projeto
```text
todolist-gtk/
├── AGENTS.md                           # Guia operacional para agentes
├── MEMORY.md                           # Aprendizados tecnicos do projeto
├── Makefile                            # Comandos de run/dev/build/flatpak
├── br.com.vitordevsp.TodoList.yml      # Manifesto Flatpak atual
├── data/
│   ├── br.com.vitordevsp.TodoList.desktop
│   ├── br.com.vitordevsp.TodoList.metainfo.xml
│   └── br.com.vitordevsp.TodoList.svg
├── dev.py                              # Watcher de live reload
├── docs/
│   ├── knowledge/                      # Guias tecnicos do projeto
│   ├── patterns/                       # Padroes de documentacao
│   └── plans/
│       ├── 000-desktop/
│       │   ├── plan.md
│       │   ├── todolist.md
│       │   └── backlog.md
│       └── 001-v1-todolist/
│           ├── plan.md
│           ├── tasks.md
│           ├── logs.md
│           └── questions.md
├── src/
│   ├── main.py                         # Bootstrap GTK/Libadwaita
│   ├── models.py                       # Persistencia SQLite
│   ├── styles/
│   │   └── style.css                   # CSS customizado da interface
│   └── window.py                       # UI e interacoes principais
└── README.md
```

---

## 5. Fases de Desenvolvimento

### Fase 1: Migração e Multi-Sessão (✅ Concluído)
- [x] Atualizar `models.py` para suportar a tabela de sessões.
- [x] Migrar tarefas existentes para a sessão padrão "Geral".
- [x] Implementar lógica de filtragem por `session_id`.

### Fase 2: Redesign da Interface (✅ Concluído)
- [x] Implementar `Adw.Flap` em `window.py` para a barra lateral.
- [x] Mover o campo de entrada (Entry) para o topo da lista de tarefas, fora da HeaderBar.
- [x] Criar listagem de sessões na barra lateral com seleção dinâmica.

### Fase 3: Funcionalidades Avançadas (✅ Concluído)
- [x] Renomear sessões via interface.
- [x] Implementar diálogos de confirmação para exclusão de sessões.
- [x] Adicionar suporte a ícones para diferentes listas (automática por palavras-chave).
- [x] Implementar Estado Vazio amigável com `Adw.StatusPage`.

### Fase 4: Empacotamento e Identidade (✅ Concluído na base atual)
- [x] Migrar app id para `br.com.vitordevsp.TodoList`.
- [x] Renomear manifesto, desktop file, metainfo e icone para o app id brasileiro.
- [x] Atualizar `Makefile` para build PyInstaller e Flatpak com paths dentro de `build/`.
- [x] Documentar setup, bundle Flatpak, UI/UX e persistencia em `docs/knowledge/`.

### Fase 5: Consolidação Final (🚧 Parcialmente concluído)
- [x] Resolver o caminho definitivo de persistencia do banco SQLite.
- [x] Alinhar `docs/knowledge/persistence-and-xdg.md`, `src/models.py` e manifesto Flatpak.
- [x] Revisar divergencias entre docs de UI/UX e icones realmente implementados.
- [x] Revisar e simplificar o pipeline de build/bundle Flatpak.
- [x] Validar `make build`, `make bundle`, instalacao do bundle e execucao instalada.
- [x] Fechar as perguntas em `questions.md`.
- [ ] Validar `make run` em sessao grafica real.
- [ ] Avaliar migracao do runtime Flatpak GNOME 46 para runtime suportado antes de distribuicao publica.

---

## 6. Versão 1.0 (Estado de Entrega)
O projeto atingiu sua maturidade inicial com as seguintes entregas:
- **Build System:** Sistema de empacotamento via PyInstaller integrado ao Makefile.
- **Documentação:** README completo detalhando o propósito do projeto e como utilizá-lo.
- **Git Config:** Configuração de `.gitignore` para manutenção saudável do repositório.
- **Flatpak:** Manifesto atual usando `br.com.vitordevsp.TodoList`.
- **Conhecimento Operacional:** Guias em `docs/knowledge/` e aprendizados em `MEMORY.md`.

---

## 7. Ferramentas de Desenvolvimento (Dev Tools)
Implementamos um workflow moderno focado no ecossistema Linux/Python:
- **Live Reload:** O aplicativo reinicia automaticamente ao salvar qualquer arquivo em `src/` ou `data/`.
- **Comandos Rápidos (Makefile):**
    - `make dev`: Inicia o modo de desenvolvimento com live reload.
    - `make run`: Executa o aplicativo normalmente.
    - `make build`: Gera o binario PyInstaller em `dist/`.
    - `make flatpak`: Constroi e instala localmente o Flatpak.
    - `make bundle`: Gera o bundle `todolist.flatpak`.

---

## 8. Como Executar
Execute os comandos abaixo na raiz do projeto:
```bash
# Modo de Desenvolvimento (Live Reload)
make dev

# Execução Normal
make run
```

## 9. Processo de Build e Bundle Flatpak

### 9.1 Objetivo

O processo de entrega da v1 deve gerar um arquivo `todolist.flatpak` na raiz do projeto, instalavel diretamente com:

```bash
flatpak install ./todolist.flatpak
```

Esse arquivo deve ser produzido de forma simples, deterministica e segura. O pipeline nao deve tentar instalar ferramentas, baixar dependencias Python, alterar ambiente de usuario ou acessar a internet durante a etapa de bundle.

### 9.2 Fronteira entre setup, build e bundle

Para manter o processo previsivel, a v1 deve separar claramente tres momentos:

1. **Setup da maquina de build:** instalacao previa de ferramentas como `pyinstaller`, `flatpak-builder`, runtimes e SDKs. Isso pode exigir internet, mas deve ficar documentado em `docs/knowledge/environment-setup.md`, fora do alvo `bundle`.
2. **Build do binario local opcional:** `make build` gera `dist/todolist-gtk` via PyInstaller para teste rapido fora do Flatpak. Essa etapa nao participa do bundle oficial.
3. **Exportacao Flatpak e bundle:** `make bundle` usa fontes locais do projeto, instala o codigo Python em `/app/share/todolist-gtk`, instala o launcher `bin/todolist-gtk` em `/app/bin/todolist-gtk`, exporta o app para um repositorio local temporario e converte esse repositorio em `todolist.flatpak`.

### 9.3 Fluxo esperado

O fluxo tecnico desejado e:

```bash
make clean
flatpak-builder --disable-download --disable-rofiles-fuse --repo=build/repo --force-clean --state-dir=build/.flatpak-builder-state build/flatpak-build br.com.vitordevsp.TodoList.yml
flatpak build-bundle build/repo todolist.flatpak br.com.vitordevsp.TodoList
```

Notas importantes:

- `flatpak-builder --repo=build/repo ...` deve criar/exportar o app para um repositorio local.
- `--disable-download` garante que o builder falhe em vez de baixar fontes inesperadas.
- `--disable-rofiles-fuse` evita falha em ambientes locais/sandbox sem `/dev/fuse`, sem alterar o conteudo do app.
- `flatpak build-bundle build/repo todolist.flatpak br.com.vitordevsp.TodoList` deve gerar o arquivo final a partir desse repositorio local.
- O manifesto deve usar fontes locais explicitas (`type: file`) e instalar apenas artefatos ja presentes no checkout local.
- O bundle final fica na raiz: `./todolist.flatpak`.

### 9.4 Reprodutibilidade e seguranca

Regras obrigatorias para fechar a v1:

- `make bundle` nao pode executar `pip install`, `flatpak install`, `flatpak remote-add`, `curl`, `wget` ou comandos equivalentes.
- Dependencias de build devem ser pre-requisitos documentados, nao efeitos colaterais do bundle.
- O bundle oficial nao deve embutir um binario PyInstaller gerado no host, porque isso mistura bibliotecas/introspection GTK do host com o runtime Flatpak.
- O manifesto nao deve usar `extra-data` para baixar arquivos em tempo de instalacao.
- Se houver fontes remotas no futuro, elas devem ter versao fixa e checksum, mas a v1 deve preferir fonte local.
- O app id, manifesto, `.desktop`, metainfo e icone devem permanecer alinhados em `br.com.vitordevsp.TodoList`.
- O output do bundle deve ser removivel/recriavel por `make clean && make bundle`.

### 9.5 Sobre runtimes e instalacao offline

Um `.flatpak` single-file e adequado para download direto e instalacao simples, mas ele nao embute automaticamente os runtimes/dependencias do sistema Flatpak. Para uma instalacao em maquina limpa, o usuario precisa ja ter o runtime necessario instalado ou o bundle precisa apontar para um runtime repo, como o Flathub.

Para a v1, o requisito principal e: **nao baixar nada durante build/bundle** e gerar um `.flatpak` direto e funcional para instalacao padrao. Se o objetivo evoluir para instalacao 100% offline em maquina sem runtimes, isso deve virar uma trilha separada usando mecanismos proprios do Flatpak para distribuicao offline, nao uma gambiarra dentro de `make bundle`.

### 9.6 Criterios de aceite

Antes de considerar a v1 fechada:

- `make bundle` executa limpeza propria e gera `./todolist.flatpak`.
- O log do bundle nao mostra downloads de pacotes Python, fontes remotas ou dependencias inesperadas.
- `flatpak install --user ./todolist.flatpak` instala o app.
- `flatpak run br.com.vitordevsp.TodoList` abre o app.
- O app cria/usa o banco SQLite no caminho definido pela decisao de persistencia.
- Um novo `make bundle` recria o bundle sem depender de estado solto na raiz.
- Antes de distribuicao publica, o runtime GNOME deve estar em uma branch suportada.

### 9.7 Fontes consultadas

- Flatpak manifest docs: `https://docs.flatpak.org/en/latest/manifests.html`
  - Manifestos definem `id`, `runtime`, `runtime-version`, `sdk`, `command`, modulos e fontes.
  - Arquivos exportados como `.desktop`, metainfo e icone devem usar o prefixo do application ID.
- Flatpak builder docs: `https://docs.flatpak.org/en/latest/flatpak-builder.html`
  - `flatpak-builder --repo=<repo>` exporta o resultado para um repositorio local.
- Flatpak single-file bundle docs: `https://docs.flatpak.org/en/latest/single-file-bundles.html`
  - `flatpak build-bundle LOCATION FILENAME NAME` cria um bundle single-file a partir de um repositorio local.
  - Single-file bundles nao incluem dependencias/runtimes; distribuicao totalmente offline tem outra estrategia.

## 10. Decisões Pendentes

As duvidas que precisam de decisao humana ficam registradas em `questions.md` na raiz deste plano. As perguntas Q1, Q2 e Q3 ja foram respondidas e devem orientar a implementacao da fase 5.

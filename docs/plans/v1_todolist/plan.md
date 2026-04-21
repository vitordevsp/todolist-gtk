# Plano de Desenvolvimento: TodoList GTK (Estilo Simplenote)

Este documento detalha as etapas para a criação de um aplicativo de lista de tarefas moderno e nativo, focado no ecossistema GNOME usando **GTK4** e **Libadwaita**.

## 1. Visão Geral
O objetivo é criar uma aplicação "premium" com design adaptativo, suporte a modo escuro nativo e animações fluidas, seguindo as HIG (Human Interface Guidelines) do GNOME. O layout é inspirado no **Simplenote**, com uma barra lateral de sessões e foco no conteúdo.

---

## 2. Stack Tecnológica
- **Linguagem:** Python 3 (PyGObject)
- **Interface:** GTK4 + Libadwaita (Compatível com v1.1)
- **Componentes:** Adw.Flap (Sidebar), Gtk.ListBox, Gtk.Entry.
- **Persistência:** SQLite (Multi-sessão)

---

## 3. Estrutura do Projeto
```text
todolist-gtk/
├── data/               # Recursos (style.css)
├── src/
│   ├── __init__.py
│   ├── main.py         # Ponto de entrada
│   ├── window.py       # Lógica da janela (Layout Flap + Sessions)
│   ├── models.py       # Gerenciamento de Dados (SQLite com Sessions)
│   └── widgets/        # Futuros componentes customizados
├── plan.md             # Este arquivo (Atualizado para Redesign)
└── todos.db            # Banco de dados local
```

---

## 4. Fases de Desenvolvimento

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

---

## 5. Versão 1.0 (✅ Concluído)
O projeto atingiu sua maturidade inicial com as seguintes entregas:
- **Build System:** Sistema de empacotamento via PyInstaller integrado ao Makefile.
- **Documentação:** README completo detalhando o propósito do projeto e como utilizá-lo.
- **Git Config:** Configuração de `.gitignore` para manutenção saudável do repositório.

---

## 6. Ferramentas de Desenvolvimento (Dev Tools)
Implementamos um workflow moderno focado no ecossistema Linux/Python:
- **Live Reload:** O aplicativo reinicia automaticamente ao salvar qualquer arquivo em `src/` ou `data/`.
- **Comandos Rápidos (Makefile):**
    - `make dev`: Inicia o modo de desenvolvimento com live reload.
    - `make run`: Executa o aplicativo normalmente.

---

## 7. Como Executar
Execute os comandos abaixo na raiz do projeto:
```bash
# Modo de Desenvolvimento (Live Reload)
make dev

# Execução Normal
make run
```

# MEMORY: Aprendizados do Projeto TodoList-GTK

Registro histórico das decisões técnicas e desafios superados neste projeto.

## 🧠 Desafios e Soluções (Brain)

### 1. Retrocompatibilidade do Libadwaita
- **Contexto:** Tentamos usar `Adw.ToolbarView`, mas o sistema possuía Libadwaita 1.1.
- **Aprendizado:** Verifique sempre a versão instalada antes de usar componentes de docs recentes do GNOME.
- **Correção:** Revertido para `Gtk.Box` vertical com `HeaderBar` anexado no topo via `.append()`.

### 2. Estilo Simplenote Nativo
- **Layout:** O uso de `Adw.Flap` permitiu uma barra lateral fluida que se adapta bem.
- **Input:** Mover o `Gtk.Entry` para o topo da lista central (dentro de uma `Gtk.Box` com margens amplas) criou o efeito "premium" de foco no conteúdo, em vez de poluir a barra de título.

### 3. Migração de Dados em SQLite
- **Técnica:** Como o SQLite não lida bem com mudanças complexas de schema, usamos `ALTER TABLE todos ADD COLUMN session_id` dentro de um bloco `try-except` para garantir que bancos de dados existentes não quebrem ao atualizar o app.

### 4. Dependências de Build (PyInstaller)
- **Desafio:** Erro de "libpython shared library not found" ao rodar o build no Linux.
- **Aprendizado:** Ferramentas que embutem o Python exigem os arquivos de desenvolvimento da distro (ex: `libpython3.11`). É necessário instalar pacotes extra no Ubuntu/Debian para permitir o empacotamento.

### 5. Bundles Flatpak vs Binários
- **Desafio:** Diferenciar o executável bruto do pacote instalável.
- **Aprendizado:** O binário gerado pelo PyInstaller é o "conteúdo", mas o Bundle (`.flatpak`) é o "contêiner" que garante que o ícone e metadados apareçam no sistema do usuário.

## 🛠️ Tecnologias Validadas
- **Stack:** Python + GTK4 + Libadwaita.
- **Build:** PyInstaller funcionou bem para binários Linux autônomos.
- **Workflow:** `dev.py` (watcher customizado) é essencial para produtividade em apps nativos.

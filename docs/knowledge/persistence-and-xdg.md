# Persistência de Dados e Padrões XDG

Este documento explica como o **Todo List GTK** gerencia o armazenamento de dados de forma segura e compatível com as normas do Linux (XDG Base Directory Specification).

## 1. O Local de Armazenamento

Para garantir que os dados do usuário não sejam perdidos ao atualizar o app ou deletar o código fonte, utilizamos o diretório padrão de dados do usuário:

- **Caminho:** `~/.local/share/br.com.vitordevsp.TodoList/`
- **Técnica:** No Python, usamos `GLib.get_user_data_dir()` em vez de caminhos relativos ou fixos.
- **Arquivo:** `todos.db`

## 2. Compatibilidade com Flatpak

Dentro de um Flatpak (Sandbox), o aplicativo não pode escrever livremente em qualquer lugar.
- O GNOME mapeia o `XDG_DATA_HOME` para uma pasta isolada dentro de `~/.var/app/br.com.vitordevsp.TodoList/data`.
- Como usamos a função da `GLib`, o código funciona perfeitamente tanto rodando via terminal (`make run`) quanto instalado via Flatpak, sem precisar de ajustes manuais.

## 3. Gestão de Schema (SQLite)

O banco de dados é gerido por uma classe `TodoModel` que lida com a criação e migração de tabelas.

### Padrão de Inicialização:
```python
APP_ID = "br.com.vitordevsp.TodoList"
db_dir = os.path.join(GLib.get_user_data_dir(), APP_ID)
os.makedirs(db_dir, exist_ok=True)
db_path = os.path.join(db_dir, "todos.db")
```

Esse padrão é relativo ao diretório XDG do usuário atual. Em uma execução comum, ele aponta para `~/.local/share/br.com.vitordevsp.TodoList/todos.db`; dentro do Flatpak, aponta para a área de dados da sandbox do próprio app.

### Migrações:
Para evitar quebras em atualizações, usamos blocos `try-except` ao adicionar novas colunas (como o `session_id`), garantindo que o banco antigo seja "promovido" para o novo formato automaticamente na primeira execução da nova versão.

## 4. Segurança

- O banco SQLite é mantido em um único arquivo `.db`.
- **Backup:** Para fazer backup, o usuário só precisa copiar a pasta em `~/.local/share/br.com.vitordevsp.TodoList/` ou a pasta equivalente dentro de `~/.var/app/br.com.vitordevsp.TodoList/data/` quando estiver usando Flatpak.

---

> [!CAUTION]
> **Nunca** use caminhos como `/tmp` ou a pasta raiz do projeto para salvar o banco de dados em produção, pois esses arquivos podem ser deletados ou ficar inacessíveis dentro do sandbox do Flatpak.

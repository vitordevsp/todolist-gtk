# Perguntas em Aberto (001-v1-todolist)

Este arquivo registra decisoes que precisam de resposta humana antes de virarem implementacao. Quando responder, escreva abaixo de cada pergunta ou altere o status para `respondida`.

## Q1 - Caminho definitivo do banco SQLite

- **Status:** respondida
- **Contexto:** O codigo atual grava o banco em `os.path.join(GLib.get_user_data_dir(), 'todolist-gtk')`. A documentacao em `docs/knowledge/persistence-and-xdg.md` aponta para `~/.local/share/br.com.vitordevsp.TodoList/`. Uma tarefa/log anterior tambem menciona mover o banco para `databases/`.
- **Pergunta:** Qual deve ser o caminho oficial do banco da v1?
- **Opcoes provaveis:**
  - `~/.local/share/br.com.vitordevsp.TodoList/todos.db`, alinhado ao app id e ao XDG.
  - `~/.local/share/todolist-gtk/todos.db`, preservando compatibilidade com o comportamento atual.
  - Uma pasta `databases/` dentro de algum diretorio XDG, caso voce queira explicitar esse agrupamento.
- **Resposta:**
os.path.join me parece fazer mais sentido já que é um pacote que vai ser instalado na maquina de outros usuarios, faz sentido ser um caminho relativo né
- **Interpretação para implementação:** usar `os.path.join(...)` com o diretório XDG retornado pela GLib, evitando caminho absoluto fixo. O nome final da subpasta deve ser alinhado ao app id oficial, salvo se a implementação revelar um bloqueio técnico.

## Q2 - Migracao de dados existentes

- **Status:** respondida
- **Contexto:** Se mudarmos o caminho atual do banco, usuarios que ja rodaram o app podem ter dados no caminho antigo.
- **Pergunta:** A v1 deve implementar migracao automatica do banco antigo para o novo caminho, ou pode tratar isso como reset/local dev?
- **Resposta:**
o projeto ainda nao foi instalado em nenhum computador, a ideia desse plano é justamente fechar a v1
- **Interpretação para implementação:** não é necessário criar rotina de migração automática para bancos antigos nesta v1.

## Q3 - Escopo do mapeamento de icones inteligentes

- **Status:** respondida
- **Contexto:** `docs/knowledge/ui-ux-patterns.md` lista categorias como saude e favoritos, mas `src/window.py` implementa hoje casa, trabalho, compras e estudo.
- **Pergunta:** O plano da v1 deve implementar todas as categorias documentadas ou reduzir a documentacao ao escopo atual?
- **Resposta:**
pode expandir as categorias
- **Interpretação para implementação:** expandir `src/window.py` para cobrir as categorias documentadas e depois alinhar `docs/knowledge/ui-ux-patterns.md` ao resultado final.

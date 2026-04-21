"""Modulo de modelos de dados para o TodoList GTK.

Este modulo gerencia toda a persistencia de dados usando SQLite, incluindo
a gerencia de sessoes (listas) e tarefas (todos).
"""

import sqlite3
import os
from gi.repository import GLib

class TodoModel:
    """Classe responsavel pela comunicacao com o banco de dados SQLite.

    Esta classe lida com a criacao de tabelas, migracao de schema e operacoes CRUD.
    """

    def __init__(self, db_path=None):
        """Inicializa o modelo e garante que o banco de dados e sessoes existam.

        Args:
            db_path (str, optional): Caminho para o arquivo .db. Se None, usa o padrao XDG.
        """
        if db_path is None:
            # Tenta usar a pasta de dados do usuario (XDG_DATA_HOME)
            # No Flatpak isso mapeia para a sandbox do app
            data_dir = os.path.join(GLib.get_user_data_dir(), 'todolist-gtk')
            os.makedirs(data_dir, exist_ok=True)
            self.db_path = os.path.join(data_dir, 'todos.db')
        else:
            self.db_path = db_path
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
            
        self._init_db()

    def _get_connection(self):
        """Cria e retorna uma conexao com o banco de dados SQLite.

        Returns:
            sqlite3.Connection: Objeto de conexao ativa.
        """
        return sqlite3.connect(self.db_path)

    def _init_db(self):
        """Inicializa o schema do banco de dados e realiza sessoes de migracao.

        Cria as tabelas 'sessions' e 'todos' se nao existirem e garante a 
        existencia da sessao padrao 'Geral'.
        """
        with self._get_connection() as conn:
            # Tabela de Sessoes
            conn.execute('''
                CREATE TABLE IF NOT EXISTS sessions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    icon_name TEXT NOT NULL DEFAULT 'view-list-symbolic'
                )
            ''')
            
            # Migracao: Adicionar icon_name se nao existir
            try:
                conn.execute('ALTER TABLE sessions ADD COLUMN icon_name TEXT NOT NULL DEFAULT "view-list-symbolic"')
            except sqlite3.OperationalError:
                pass

            # Garantir que existe pelo menos uma sessao padrao
            cursor = conn.execute('SELECT id FROM sessions WHERE name = "Geral"')
            if not cursor.fetchone():
                conn.execute('INSERT INTO sessions (name, icon_name) VALUES ("Geral", "user-home-symbolic")')

            # Tabela de Todos
            conn.execute('''
                CREATE TABLE IF NOT EXISTS todos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    text TEXT NOT NULL,
                    done BOOLEAN NOT NULL DEFAULT 0,
                    session_id INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (session_id) REFERENCES sessions (id)
                )
            ''')

            # Migracao: Adicionar session_id se nao existir
            try:
                conn.execute('ALTER TABLE todos ADD COLUMN session_id INTEGER REFERENCES sessions(id)')
            except sqlite3.OperationalError:
                pass

            # Vincular todos orfaos a sessao Geral
            cursor = conn.execute('SELECT id FROM sessions WHERE name = "Geral"')
            res = cursor.fetchone()
            if res:
                default_session_id = res[0]
                conn.execute('UPDATE todos SET session_id = ? WHERE session_id IS NULL', (default_session_id,))

    def add_session(self, name, icon_name='view-list-symbolic'):
        """Cria uma nova sessao de tarefas.

        Args:
            name (str): Nome da nova sessao.
            icon_name (str): Nome do icone simbolico do GTK.

        Returns:
            int: O ID da sessao criada ou None em caso de erro de duplicidade.
        """
        try:
            with self._get_connection() as conn:
                cursor = conn.execute('INSERT INTO sessions (name, icon_name) VALUES (?, ?)', (name, icon_name))
                return cursor.lastrowid
        except sqlite3.IntegrityError:
            return None

    def rename_session(self, session_id, new_name):
        """Altera o nome de uma sessao existente.

        Args:
            session_id (int): ID da sessao a ser renomeada.
            new_name (str): Novo nome para a sessao.

        Returns:
            bool: True se teve sucesso, False se ja existe uma sessao com esse nome.
        """
        try:
            with self._get_connection() as conn:
                conn.execute('UPDATE sessions SET name = ? WHERE id = ?', (new_name, session_id))
                return True
        except sqlite3.IntegrityError:
            return False

    def update_session_icon(self, session_id, icon_name):
        """Atualiza o icone visual de uma sessao.

        Args:
            session_id (int): ID da sessao.
            icon_name (str): Nome do novo icone.
        """
        with self._get_connection() as conn:
            conn.execute('UPDATE sessions SET icon_name = ? WHERE id = ?', (icon_name, session_id))

    def get_sessions(self):
        """Recupera todas as sessoes cadastradas.

        Returns:
            list: Lista de tuplas (id, nome, icone).
        """
        with self._get_connection() as conn:
            cursor = conn.execute('SELECT id, name, icon_name FROM sessions')
            return cursor.fetchall()

    def add_todo(self, text, session_id):
        """Adiciona uma nova tarefa a uma sessao especifica.

        Args:
            text (str): Descricao da tarefa.
            session_id (int): ID da sessao vinculada.

        Returns:
            int: ID da nova tarefa.
        """
        with self._get_connection() as conn:
            cursor = conn.execute('INSERT INTO todos (text, session_id) VALUES (?, ?)', (text, session_id))
            return cursor.lastrowid

    def get_todos(self, session_id):
        """Recupera todas as tarefas vinculadas a uma sessao.

        Args:
            session_id (int): ID da sessao.

        Returns:
            list: Lista de tuplas (id, texto, concluido).
        """
        with self._get_connection() as conn:
            cursor = conn.execute('SELECT id, text, done FROM todos WHERE session_id = ? ORDER BY created_at DESC', (session_id,))
            return cursor.fetchall()

    def delete_todo(self, todo_id):
        """Remove permanentemente uma tarefa do banco.

        Args:
            todo_id (int): ID da tarefa.
        """
        with self._get_connection() as conn:
            conn.execute('DELETE FROM todos WHERE id = ?', (todo_id,))

    def toggle_todo(self, todo_id, done):
        """Inverte o estado de conclusao (concluido/pendente) de uma tarefa.

        Args:
            todo_id (int): ID da tarefa.
            done (bool): Novo estado de conclusao.
        """
        with self._get_connection() as conn:
            conn.execute('UPDATE todos SET done = ? WHERE id = ?', (1 if done else 0, todo_id))

    def delete_session(self, session_id):
        """Remove uma sessao e todas as tarefas vinculadas a ela.

        Args:
            session_id (int): ID da sessao a ser removida.
        """
        with self._get_connection() as conn:
            conn.execute('DELETE FROM todos WHERE session_id = ?', (session_id,))
            conn.execute('DELETE FROM sessions WHERE id = ?', (session_id,))

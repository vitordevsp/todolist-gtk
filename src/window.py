"""Gerenciamento da interface grafica principal do TodoList GTK.

Este modulo define os widgets customizados e a janela principal da aplicacao,
utilizando componentes do GTK4 e Libadwaita para uma experiencia nativa.
"""

import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, Gdk
from .models import TodoModel

class TodoRow(Adw.ActionRow):
    """Representa uma linha individual de tarefa na lista.

    Uma linha contem um checkbox de conclusao, o texto da tarefa e um botao de exclusao.
    """

    def __init__(self, todo_id, text, done, model, on_delete):
        """Inicializa a linha da tarefa.

        Args:
            todo_id (int): ID unico da tarefa no banco de dados.
            text (str): Descricao da tarefa.
            done (bool): Estado inicial de conclusao.
            model (TodoModel): Instancia do modelo para persistencia.
            on_delete (callable): Callback executado quando a linha e removida.
        """
        super().__init__(title=text)
        self.todo_id = todo_id
        self.model = model
        self.on_delete = on_delete

        # Checkbox para marcar como concluido
        self.check = Gtk.CheckButton()
        self.check.set_active(done)
        self.check.set_valign(Gtk.Align.CENTER)
        self.check.connect("toggled", self.on_toggled)
        self.add_prefix(self.check)

        # Botao de deletar (Lixeira)
        self.del_btn = Gtk.Button(icon_name="user-trash-symbolic")
        self.del_btn.add_css_class("flat")
        self.del_btn.set_valign(Gtk.Align.CENTER)
        self.del_btn.connect("clicked", self.on_delete_clicked)
        self.add_suffix(self.del_btn)
        
        # Sincroniza o visual inicial (ex: riscado se done=True)
        self.update_appearance(done)

    def on_toggled(self, check):
        """Handler para quando o checkbox e alterado.

        Args:
            check (Gtk.CheckButton): O widget que disparou o evento.
        """
        is_done = check.get_active()
        self.model.toggle_todo(self.todo_id, is_done)
        self.update_appearance(is_done)

    def update_appearance(self, is_done):
        """Atualiza o estilo visual da linha com base no estado de conclusao.

        Args:
            is_done (bool): Se a tarefa esta concluida ou nao.
        """
        if is_done:
            self.add_css_class("done")
        else:
            self.remove_css_class("done")

    def on_delete_clicked(self, btn):
        """Handler para o botao de exclusao da tarefa.

        Args:
            btn (Gtk.Button): O botao clicado.
        """
        self.model.delete_todo(self.todo_id)
        self.on_delete(self)

class TodoWindow(Adw.ApplicationWindow):
    """Janela principal do aplicativo seguindo o estilo Simplenote.

    Gerencia o layout de barra lateral (Flap), a listagem de sessoes e 
    as tarefas da sessao selecionada.
    """

    def __init__(self, **kwargs):
        """Inicializa a janela e seus componentes internos."""
        super().__init__(**kwargs)
        self.model = TodoModel()
        self.current_session_id = None
        self.current_session_name = ""
        self.current_session_icon = "view-list-symbolic"
        
        self.set_title("Todo List GTK")
        self.set_default_size(900, 650)

        # Layout Principal com Barra Lateral Retratil
        self.flap = Adw.Flap()
        self.flap.set_swipe_to_open(True)
        self.flap.set_swipe_to_close(True)
        self.set_content(self.flap)

        # --- CONTEUDO DA BARRA LATERAL (SIDEBAR) ---
        sidebar_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        sidebar_box.add_css_class("background")
        sidebar_box.set_size_request(240, -1)

        sidebar_title = Gtk.Label(label="Minhas Listas")
        sidebar_title.add_css_class("title-4")
        sidebar_title.set_margin_top(18)
        sidebar_title.set_margin_bottom(12)
        sidebar_box.append(sidebar_title)

        self.session_list = Gtk.ListBox()
        self.session_list.add_css_class("navigation-sidebar")
        self.session_list.connect("row-selected", self.on_session_selected)
        
        scrolled_sidebar = Gtk.ScrolledWindow()
        scrolled_sidebar.set_vexpand(True)
        scrolled_sidebar.set_child(self.session_list)
        sidebar_box.append(scrolled_sidebar)

        # Botao para criar nova lista
        new_session_btn = Gtk.Button(label="Nova Sessão")
        new_session_btn.set_icon_name("list-add-symbolic")
        new_session_btn.set_margin_top(12)
        new_session_btn.set_margin_bottom(12)
        new_session_btn.set_margin_start(12)
        new_session_btn.set_margin_end(12)
        new_session_btn.connect("clicked", self.on_new_session_clicked)
        sidebar_box.append(new_session_btn)

        self.flap.set_flap(sidebar_box)

        # --- ÁREA DE CONTEUDO PRINCIPAL ---
        main_area = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        
        # Barra de Titulo Superior
        self.header_bar = Adw.HeaderBar()
        flap_toggle = Gtk.Button(icon_name="sidebar-show-symbolic")
        flap_toggle.connect("clicked", lambda x: self.flap.set_reveal_flap(not self.flap.get_reveal_flap()))
        self.header_bar.pack_start(flap_toggle)

        # Botao para renomear sessao (Lapis)
        self.edit_session_btn = Gtk.Button(icon_name="document-edit-symbolic")
        self.edit_session_btn.add_css_class("flat")
        self.edit_session_btn.connect("clicked", self.on_rename_session_clicked)
        self.header_bar.pack_start(self.edit_session_btn)
        
        main_area.append(self.header_bar)

        # Conteudo Centralizado
        content_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        content_box.set_margin_top(20)
        content_box.set_margin_bottom(20)
        content_box.set_margin_start(60)
        content_box.set_margin_end(60)
        content_box.set_spacing(18)

        # Titulo da Sessao Atual com Icone
        header_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        self.session_icon_widget = Gtk.Image(icon_name="view-list-symbolic", pixel_size=32)
        self.session_label = Gtk.Label()
        self.session_label.add_css_class("title-1")
        header_box.append(self.session_icon_widget)
        header_box.append(self.session_label)
        content_box.append(header_box)

        # Campo de entrada para novas tarefas (Input)
        input_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.entry = Gtk.Entry(placeholder_text="O que precisa ser feito?")
        self.entry.set_hexpand(True)
        self.entry.connect("activate", self.on_add_task)
        add_btn = Gtk.Button(icon_name="list-add-symbolic")
        add_btn.add_css_class("suggested-action")
        add_btn.connect("clicked", self.on_add_task)
        input_box.append(self.entry)
        input_box.append(add_btn)
        content_box.append(input_box)

        # Stack de Interface: Alterna entre a Lista e a Pagina Vazia
        self.main_stack = Gtk.Stack()
        self.main_stack.set_transition_type(Gtk.StackTransitionType.CROSSFADE)

        # Aba da Lista de Tarefas
        self.list_box = Gtk.ListBox()
        self.list_box.add_css_class("boxed-list")
        self.list_box.set_selection_mode(Gtk.SelectionMode.NONE)
        scrolled_main = Gtk.ScrolledWindow()
        scrolled_main.set_vexpand(True)
        scrolled_main.set_child(self.list_box)
        self.main_stack.add_named(scrolled_main, "list")

        # Aba de Estado Vazio (StatusPage)
        self.empty_page = Adw.StatusPage()
        self.empty_page.set_icon_name("view-list-symbolic")
        self.empty_page.set_title("Nada por aqui ainda")
        self.empty_page.set_description("Adicione sua primeira tarefa no campo acima!")
        self.main_stack.add_named(self.empty_page, "empty")

        content_box.append(self.main_stack)
        main_area.append(content_box)
        self.flap.set_content(main_area)
        
        # Carregamento Inicial
        self.load_sessions()

    def load_sessions(self, select_id=None):
        """Busca sessoes no banco e preenche a barra lateral.

        Args:
            select_id (int, optional): ID da sessao que deve ser selecionada apos recarregar.
        """
        child = self.session_list.get_first_child()
        while child:
            self.session_list.remove(child)
            child = self.session_list.get_first_child()

        sessions = self.model.get_sessions()
        row_to_select = None

        for sid, name, icon in sessions:
            row = Adw.ActionRow(title=name)
            row.session_id = sid
            row.icon_name = icon
            
            icon_img = Gtk.Image(icon_name=icon)
            row.add_prefix(icon_img)
            
            # Botao de deletar (Exceto para a sessao obrigatoria Geral)
            if name != "Geral":
                del_btn = Gtk.Button(icon_name="user-trash-symbolic")
                del_btn.add_css_class("flat")
                del_btn.set_valign(Gtk.Align.CENTER)
                del_btn.connect("clicked", self.on_delete_session_clicked, sid, name)
                row.add_suffix(del_btn)
            
            self.session_list.append(row)
            if select_id and sid == select_id:
                row_to_select = row

        # Mantem a selecao ou seleciona a primeira sessao
        if row_to_select:
            self.session_list.select_row(row_to_select)
        elif not select_id:
            first_row = self.session_list.get_row_at_index(0)
            if first_row:
                self.session_list.select_row(first_row)

    def on_session_selected(self, listbox, row):
        """Handler para quando uma sessao e clicada na barra lateral.

        Args:
            listbox (Gtk.ListBox): A lista de sessoes.
            row (Gtk.ListBoxRow): A linha selecionada.
        """
        if row:
            self.current_session_id = row.session_id
            self.current_session_name = row.get_title()
            self.current_session_icon = row.icon_name
            
            self.session_label.set_text(self.current_session_name)
            self.session_icon_widget.set_from_icon_name(self.current_session_icon)
            self.edit_session_btn.set_sensitive(self.current_session_name != "Geral")
            
            self.load_tasks()

    def load_tasks(self):
        """Busca tarefas da sessao atual e atualiza a interface (Lista ou StatusPage)."""
        child = self.list_box.get_first_child()
        count = 0
        while child:
            self.list_box.remove(child)
            child = self.list_box.get_first_child()

        if self.current_session_id:
            todos = self.model.get_todos(self.current_session_id)
            count = len(todos)
            for todo_id, text, done in todos:
                row = TodoRow(todo_id, text, done, self.model, self.remove_row)
                self.list_box.append(row)

        # Alterna visibilidade baseado na quantidade de tarefas
        if count > 0:
            self.main_stack.set_visible_child_name("list")
        else:
            self.empty_page.set_icon_name(self.current_session_icon)
            self.main_stack.set_visible_child_name("empty")

    def on_add_task(self, *args):
        """Captura o texto do input e cria uma nova tarefa na sessao atual."""
        text = self.entry.get_text().strip()
        if text and self.current_session_id:
            self.model.add_todo(text, self.current_session_id)
            self.entry.set_text("")
            self.load_tasks()

    def on_new_session_clicked(self, btn):
        """Abre o dialogo para criar uma nova lista."""
        self.show_prompt_dialog("Nova Sessão", "Nome da Lista:", "", self.create_session)

    def create_session(self, name):
        """Cria e seleciona uma nova sessao com icone automatico.

        Args:
            name (str): Nome fornecido pelo usuario no dialogo.
        """
        if name.strip():
            # Atribuicao de icones baseada em palavras-chave
            icon = "view-list-symbolic"
            lower_name = name.lower()
            if "casa" in lower_name or "home" in lower_name: icon = "user-home-symbolic"
            elif "trabalho" in lower_name or "work" in lower_name: icon = "briefcase-symbolic"
            elif "compra" in lower_name or "buy" in lower_name: icon = "shopping-cart-symbolic"
            elif "estudo" in lower_name or "study" in lower_name: icon = "education-symbolic"
            
            sid = self.model.add_session(name.strip(), icon)
            if sid:
                self.load_sessions(select_id=sid)

    def on_delete_session_clicked(self, btn, sid, name):
        """Abre dialogo de confirmacao antes de apagar uma sessao inteira.

        Args:
            btn (Gtk.Button): O botao clicado.
            sid (int): ID da sessao.
            name (str): Nome da sessao para exibir na mensagem.
        """
        dialog = Gtk.MessageDialog(
            transient_for=self,
            modal=True,
            message_type=Gtk.MessageType.QUESTION,
            buttons=Gtk.ButtonsType.YES_NO,
            text=f"Excluir '{name}'?"
        )
        dialog.format_secondary_text("Todas as tarefas desta lista serão apagadas permanentemente.")
        
        def on_response(dialog, response_id):
            if response_id == Gtk.ResponseType.YES:
                self.model.delete_session(sid)
                if self.current_session_id == sid:
                    self.load_sessions()
                else:
                    self.load_sessions(select_id=self.current_session_id)
            dialog.destroy()
            
        dialog.connect("response", on_response)
        dialog.present()

    def on_rename_session_clicked(self, btn):
        """Abre o dialogo para trocar o nome da sessao atual."""
        if self.current_session_id and self.current_session_name != "Geral":
            self.show_prompt_dialog("Renomear Sessão", "Novo nome:", self.current_session_name, self.rename_session)

    def rename_session(self, new_name):
        """Aplica a renomeacao no banco e atualiza a interface.

        Args:
            new_name (str): Novo nome validado.
        """
        if new_name.strip() and new_name.strip() != self.current_session_name:
            if self.model.rename_session(self.current_session_id, new_name.strip()):
                self.load_sessions(select_id=self.current_session_id)

    def show_prompt_dialog(self, title, label_text, default_text, callback):
        """Exibe um dialogo de entrada de texto customizado.

        Ideal para operacoes rapidas de Input que nao exigem janelas complexas.

        Args:
            title (str): Titulo da janela do dialogo.
            label_text (str): Texto explicativo acima do campo.
            default_text (str): Texto pre-carregado no input.
            callback (callable): Funcao a ser executada ao clicar em 'Salvar'.
        """
        dialog = Gtk.Dialog(title=title, transient_for=self, modal=True)
        dialog.add_button("Cancelar", Gtk.ResponseType.CANCEL)
        dialog.add_button("Salvar", Gtk.ResponseType.OK)
        dialog.set_default_response(Gtk.ResponseType.OK)

        content = dialog.get_content_area()
        content.set_margin_top(12)
        content.set_margin_bottom(12)
        content.set_margin_start(12)
        content.set_margin_end(12)
        content_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        
        label = Gtk.Label(label=label_text)
        label.set_halign(Gtk.Align.START)
        content_box.append(label)
        
        entry = Gtk.Entry()
        entry.set_text(default_text)
        entry.set_activates_default(True)
        content_box.append(entry)
        
        content.append(content_box)

        def on_response(dialog, response_id):
            if response_id == Gtk.ResponseType.OK:
                callback(entry.get_text())
            dialog.destroy()

        dialog.connect("response", on_response)
        dialog.present()

    def remove_row(self, row):
        """Remove visualmente uma linha da lista e verifica se esvaziou a sessao.

        Args:
            row (Gtk.ListBoxRow): A linha a ser removida.
        """
        self.list_box.remove(row)
        if not self.list_box.get_first_child():
             self.main_stack.set_visible_child_name("empty")

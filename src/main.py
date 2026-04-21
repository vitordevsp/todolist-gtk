"""Ponto de entrada (Bootstrap) do aplicativo TodoList GTK.

Este modulo inicializa o ambiente do GTK/Libadwaita, carrega recursos 
estaticos (como CSS) e instancia a aplicacao principal.
"""

import sys
import os
import gi

# Garante as versoes corretas das bibliotecas do sistema
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Adw
from .window import TodoWindow

class TodoApplication(Adw.Application):
    """Classe de aplicacao principal que gerencia o ciclo de vida do software.

    Herda de Adw.Application para garantir integracao profunda com o GNOME.
    """

    def __init__(self):
        """Define o ID unico da aplicacao e conecta o sinal de ativacao."""
        # O ID deve ser o mesmo do manifesto Flatpak e do arquivo .desktop
        super().__init__(application_id='com.vitordevsp.TodoList')
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        """Instancia e apresenta a janela principal quando o app e iniciado.

        Tambem realiza a carga do provedor de CSS para estilizacao customizada.

        Args:
            app (Adw.Application): A instancia da aplicacao ativa.
        """
        # Determina o caminho do CSS (Suporte a PyInstaller e Dev)
        if hasattr(sys, '_MEIPASS'):
            # Rodando via binario PyInstaller
            css_path = os.path.join(sys._MEIPASS, 'data', 'style.css')
        else:
            # Rodando via script Python direto
            css_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'style.css')

        if os.path.exists(css_path):
            css_provider = Gtk.CssProvider()
            css_provider.load_from_path(css_path)
            Gtk.StyleContext.add_provider_for_display(
                gi.repository.Gdk.Display.get_default(),
                css_provider,
                Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
            )
        
        # Cria e exibe a janela principal
        self.win = TodoWindow(application=app)
        self.win.present()

def main():
    """Funcao de entrada que dispara a execucao do Loop principal do aplicativo.

    Returns:
        int: O codigo de saida do programa.
    """
    app = TodoApplication()
    return app.run(sys.argv)

if __name__ == '__main__':
    main()

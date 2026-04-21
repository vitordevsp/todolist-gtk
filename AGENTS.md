# Manual do Agente: Desenvolvimento Nativo Linux (GTK4 + Libadwaita)

Este guia consolida o conhecimento necessário para construir aplicativos desktop modernos no Linux, com foco em UX premium e performance.

## 1. Stack Recomendada e Convenções
- **GTK4**: O toolkit core para a interface.
- **Libadwaita**: Extende o GTK4 com componentes focados no design moderno (GNOME).
- **PyGObject**: Bindings oficiais para Python que mapeiam a API C para Python.

### ⚠️ Boas Práticas de Inicialização
Sempre especifique as versões antes de importar os repositórios:
```python
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw
```

## 2. Compatibilidade e "Workarounds"
O Libadwaita evolui rápido. Muitos componentes modernos exigem versões recentes (1.4+).
- **Sistemas Antigos (ex: Ubuntu 22.04 / Libadwaita 1.1):**
    - Substitua `Adw.ToolbarView` por uma `Gtk.Box` vertical.
    - Use `Gtk.MessageDialog` em vez de `Adw.MessageDialog`.
    - Use `Gtk.Stack` para gerenciar estados de visualização.

## 3. Interfaces: Código vs Blueprint
Para apps complexos, recomenda-se usar a linguagem **Blueprint** (compilada para arquivos `.ui` XML). Isso separa a lógica (Python) da estrutura visual, facilitando a manutenção e o uso de ferramentas de design como o **Cambalache**.

## 4. Build Avançado com PyInstaller
Como o GTK depende de introspecção dinâmica, o PyInstaller às vezes falha em detectar imports.
- **Hidden Imports:** Frequentemente necessário incluir `gi`, `gi.repository.Gtk`, `gi.repository.Adw`.
- **Data Pooling:** Use `--add-data "pasta_recursos:pasta_recursos"` para incluir CSS, ícones e esquemas GLib.
- **🛠️ Dependência Crítica (Linux):** Para realizar o build no Ubuntu/Debian, o sistema deve possuir a biblioteca compartilhada instalada (ex: `sudo apt install libpython3.x`). Sem isso, o PyInstaller não consegue embutir o interpretador.

## 5. 📦 Distribuição via Flatpak (O Padrão Ouro)
Embora utilizemos PyInstaller para builds rápidos, o **Flatpak** é o padrão recomendado para distribuição Linux.
- **Sandbox:** Garante que o app rode de forma isolada e segura.
- **Manifesto:** Define como o app é construído e quais arquivos (como o `.desktop`) o sistema deve registrar.
- **📦 Bundles (.flatpak):** Você pode gerar um arquivo único de "bundle" usando `flatpak build-bundle`. Este arquivo contém tudo o que é necessário para instalar o seu app off-line ou via download em qualquer distro.
- **Flathub:** O local central para publicar e baixar apps Linux modernos.

## 6. Desenvolvimento Ágil
O workflow de desenvolvimento nativo deve incluir um **Watcher de Live Reload** (como nosso `dev.py`). Isso permite iterar rapidamente na interface sem o custo de tempo de reinicialização manual do processo.

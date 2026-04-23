# Estrutura do Projeto

Este documento registra a organizacao pratica dos arquivos do TodoList GTK. A regra principal e separar o que pertence ao codigo da aplicacao, o que pertence a interface e o que existe apenas para integracao com o desktop Linux.

## 1. Codigo da Aplicacao

O diretorio `src/` concentra o codigo executado pelo app:

- `src/main.py`: bootstrap GTK/Libadwaita, inicializacao da aplicacao e carregamento de recursos.
- `src/window.py`: construcao da interface, handlers de acoes e comportamento visual.
- `src/models.py`: persistencia SQLite e regras de acesso aos dados.
- `src/styles/style.css`: CSS customizado da interface.

Estilos ficam em `src/styles/` porque sao parte direta da implementacao da UI. Eles precisam funcionar no modo desenvolvimento, no build PyInstaller e no Flatpak oficial.

## 2. Metadados Desktop

O diretorio `data/` deve guardar arquivos que o sistema desktop consome para reconhecer e exibir o aplicativo:

- `data/br.com.vitordevsp.TodoList.desktop`: entrada de menu e comando de abertura.
- `data/br.com.vitordevsp.TodoList.metainfo.xml`: metadados AppStream.
- `data/br.com.vitordevsp.TodoList.svg`: icone do aplicativo.

Evite colocar codigo Python, CSS da interface ou banco de dados em `data/`. Esse diretorio deve continuar focado em integracao desktop.

## 3. Empacotamento

O manifesto `br.com.vitordevsp.TodoList.yml` lista os arquivos locais que entram no Flatpak. Ele deve continuar explicito, usando fontes `type: file`, para evitar copiar arquivos inesperados do repositorio.

O bundle oficial instala:

- o launcher `bin/todolist-gtk` em `/app/bin/todolist-gtk`;
- o codigo Python em `/app/share/todolist-gtk/src/`;
- o CSS em `/app/share/todolist-gtk/src/styles/style.css`;
- os metadados desktop em `/app/share/applications`, `/app/share/icons` e `/app/share/metainfo`.

`make build` continua sendo um fluxo local via PyInstaller. `make bundle` deve permanecer separado dele e empacotar o codigo Python para rodar com o runtime GNOME do Flatpak.

## 4. Dados do Usuario

Dados criados em runtime nao devem ser salvos dentro do repositorio.

O banco SQLite e criado por `src/models.py` usando o diretorio XDG retornado pela GLib:

- fora do Flatpak: `~/.local/share/br.com.vitordevsp.TodoList/todos.db`;
- dentro do Flatpak: area sandboxada em `~/.var/app/br.com.vitordevsp.TodoList/data/`.

Use `docs/knowledge/persistence-and-xdg.md` como referencia para detalhes de persistencia.

## 5. Quando Atualizar Este Documento

Atualize este arquivo quando:

- um arquivo mudar de camada, por exemplo de `data/` para `src/`;
- o manifesto Flatpak passar a instalar novos tipos de recurso;
- surgir uma nova pasta de codigo, recurso visual ou dado local;
- o fluxo `make build`, `make flatpak` ou `make bundle` mudar a forma como os arquivos sao empacotados.

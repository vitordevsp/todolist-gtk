# Do zero ao Flatpak: criando um app nativo para Linux com Python e GTK

Descricao: Tutorial pratico mostrando como criar, estruturar e distribuir um
aplicativo desktop nativo para Linux usando Python, GTK4, Libadwaita, SQLite e
Flatpak.

Tags: python, gtk, linux, desktop, flatpak, desenvolvimento, tutorial

## Antes: o relato da experiencia

Este texto e a segunda parte de uma dupla.

Na primeira parte eu contei a experiencia de guiar IA para construir um app
Linux sem dominar previamente toda a stack nativa. Aqui o foco e mais tecnico:
como o projeto foi estruturado, como os dados foram persistidos e como o app saiu
de um script Python para um bundle `.flatpak` instalavel.

Parte 1: [IA nao fez o app sozinha, mas mudou tudo](./experiencia-desenvolvimento-ia-sem-dominar-stack.md)

## 1. Por que construir apps nativos para Linux

Quando voce vem do frontend web, e tentador resolver qualquer interface com
Electron. Ele e familiar, usa tecnologias conhecidas e entrega rapido.

Mas existe outro caminho interessante para projetos Linux: construir um app
nativo.

Um app nativo com GTK conversa melhor com o ambiente do sistema. Ele usa widgets
do desktop, respeita tema claro/escuro, integra com icones, janelas, menus,
sandbox e convencoes do GNOME. Em vez de carregar um navegador inteiro para uma
interface simples, voce usa o toolkit que ja faz parte do ecossistema.

Isso nao quer dizer que Electron seja ruim. Ele resolve problemas reais,
principalmente quando a aplicacao precisa ser multiplataforma e reaproveitar uma
base web grande.

Mas para um app pequeno, pessoal e focado em Linux, Python + GTK4 + Libadwaita e
uma combinacao muito boa:

- desenvolve rapido;
- usa UI nativa;
- exige pouco boilerplate;
- funciona bem para ferramentas locais;
- empacota bem com Flatpak.

O projeto usado aqui e um TodoList simples, com layout em duas colunas inspirado
no Simplenote, multiplas listas, persistencia local em SQLite e dark mode nativo.

O escopo e pequeno de proposito. Pequeno o suficiente para caber em um artigo.
Real o suficiente para tocar em problemas de app desktop de verdade.

## 2. Stack utilizada

A stack ficou assim:

- **Python**: linguagem principal do app.
- **PyGObject**: ponte entre Python e bibliotecas GNOME.
- **GTK4**: toolkit de interface.
- **Libadwaita**: componentes modernos e integracao visual com GNOME.
- **SQLite**: banco local em arquivo unico.
- **Flatpak**: formato de distribuicao e sandbox.
- **Makefile**: interface de comandos do projeto.

Pensando em analogia com frontend web:

- `src/main.py` lembra o bootstrap da aplicacao;
- `src/window.py` lembra a composicao de tela e handlers de eventos;
- `src/models.py` lembra uma camada de service/repository local;
- `src/styles/style.css` lembra o CSS da UI;
- `br.com.vitordevsp.TodoList.yml` lembra um manifesto de build/distribuicao;
- `Makefile` ocupa o papel dos scripts de `package.json`, mas no estilo mais
  natural para um projeto Python/Linux.

O ponto principal: GTK nao funciona como React.

Voce nao descreve uma arvore declarativa que re-renderiza com estado. Voce cria
widgets, conecta sinais e atualiza partes da interface quando eventos acontecem.

No começo isso parece menos familiar para quem vem da web, mas a ideia central e
simples: widget, container, signal, callback.

## 3. Estrutura do projeto

A estrutura atual do app segue uma separacao pequena, mas suficiente:

```text
todolist-gtk/
├── Makefile
├── br.com.vitordevsp.TodoList.yml
├── bin/
│   └── todolist-gtk
├── data/
│   ├── br.com.vitordevsp.TodoList.desktop
│   ├── br.com.vitordevsp.TodoList.metainfo.xml
│   └── br.com.vitordevsp.TodoList.svg
├── src/
│   ├── main.py
│   ├── models.py
│   ├── window.py
│   └── styles/
│       └── style.css
└── docs/
```

As responsabilidades ficaram assim:

- `src/main.py`: inicia `Adw.Application`, registra o application id e carrega o
  CSS.
- `src/window.py`: monta a janela, sidebar, lista de tarefas, estado vazio,
  dialogos e eventos.
- `src/models.py`: cuida do SQLite, schema, migracoes simples e CRUD.
- `src/styles/style.css`: guarda ajustes visuais.
- `bin/todolist-gtk`: script usado pelo Flatpak para chamar `python3 -m src.main`.
- `data/`: arquivos de integracao desktop.
- `Makefile`: comandos de execucao, build, bundle e limpeza.
- `br.com.vitordevsp.TodoList.yml`: manifesto Flatpak.

Essa organizacao nao tenta criar uma arquitetura grande. Ela so impede que tudo
caia no mesmo arquivo.

Para um app pequeno, isso ja resolve bastante.

## 4. Bootstrap com Python, GTK4 e Libadwaita

O ponto de entrada fica em `src/main.py`.

Em apps GTK com Python, uma boa pratica importante e declarar as versoes antes de
importar os repositorios:

```python
import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gtk, Adw
```

Depois disso, a aplicacao pode herdar de `Adw.Application`:

```python
class TodoApplication(Adw.Application):
    def __init__(self):
        super().__init__(application_id="br.com.vitordevsp.TodoList")
        self.connect("activate", self.on_activate)

    def on_activate(self, app):
        self.win = TodoWindow(application=app)
        self.win.present()
```

O `application_id` precisa ser consistente com o resto do projeto:

- manifesto Flatpak;
- arquivo `.desktop`;
- metainfo;
- icone;
- caminho de dados do app.

Esse detalhe parece burocratico, mas e uma das diferencas entre "um script que
abre uma janela" e "um app reconhecido pelo desktop".

## 5. Interface com GTK + Libadwaita

A interface principal fica em `src/window.py`.

O app usa `Adw.ApplicationWindow` como janela principal e `Adw.Flap` para criar
um layout com barra lateral:

```python
self.flap = Adw.Flap()
self.flap.set_swipe_to_open(True)
self.flap.set_swipe_to_close(True)
self.set_content(self.flap)
```

Na pratica, o layout tem duas regioes:

- sidebar com as listas/sessoes;
- area principal com tarefas da sessao selecionada.

Isso lembra bastante um layout web com sidebar e conteudo:

```text
+-------------------+--------------------------------+
| Minhas Listas     | Trabalho                       |
|                   | [O que precisa ser feito?] [+] |
| Geral             |                                |
| Trabalho          | - revisar bundle               |
| Estudos           | - escrever artigo              |
+-------------------+--------------------------------+
```

Em GTK, voce monta isso combinando containers e widgets:

- `Gtk.Box` para empilhar ou alinhar elementos;
- `Gtk.ListBox` para listas de sessoes e tarefas;
- `Adw.ActionRow` para linhas com titulo, icone, checkbox e botao;
- `Gtk.Entry` para entrada de texto;
- `Gtk.Button` para acoes;
- `Gtk.Stack` para alternar entre lista e estado vazio;
- `Adw.StatusPage` para a tela de "nada por aqui ainda".

Eventos sao conectados por sinais.

Exemplo: quando o usuario pressiona Enter no campo de tarefa ou clica no botao de
adicionar, o app chama o mesmo handler:

```python
self.entry.connect("activate", self.on_add_task)
add_btn.connect("clicked", self.on_add_task)
```

O handler le o texto, chama o modelo e recarrega a lista:

```python
def on_add_task(self, *args):
    text = self.entry.get_text().strip()
    if text and self.current_session_id:
        self.model.add_todo(text, self.current_session_id)
        self.entry.set_text("")
        self.load_tasks()
```

Para quem vem do React, a diferenca mais importante e esta: aqui voce nao altera
um estado e espera um render declarativo. Voce executa uma acao, persiste a
mudanca e atualiza explicitamente os widgets afetados.

E mais manual, mas tambem e direto.

## 6. Persistencia com SQLite

O app usa SQLite porque o problema e local e pequeno.

Nao precisa de servidor. Nao precisa de container. Nao precisa de um banco
pesado. Um arquivo `.db` resolve.

O modelo fica em `src/models.py` e cria duas tabelas:

- `sessions`: listas do usuario, como "Geral", "Trabalho" ou "Estudos";
- `todos`: tarefas vinculadas a uma sessao.

Uma versao simplificada do schema:

```sql
CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    icon_name TEXT NOT NULL DEFAULT 'view-list-symbolic'
);

CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    done BOOLEAN NOT NULL DEFAULT 0,
    session_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES sessions (id)
);
```

O detalhe mais importante nao e o SQL.

E onde salvar o arquivo.

Um erro comum em prototipos desktop e salvar `todos.db` na raiz do projeto. Isso
funciona enquanto voce esta desenvolvendo, mas quebra a ideia de aplicativo
instalado.

O projeto usa `GLib.get_user_data_dir()` para seguir o padrao XDG:

```python
data_dir = os.path.join(GLib.get_user_data_dir(), APP_ID)
os.makedirs(data_dir, exist_ok=True)
db_path = os.path.join(data_dir, "todos.db")
```

Rodando fora do Flatpak, isso aponta para algo como:

```text
~/.local/share/br.com.vitordevsp.TodoList/todos.db
```

Dentro do Flatpak, o mesmo codigo usa a area de dados sandboxada do app:

```text
~/.var/app/br.com.vitordevsp.TodoList/data/br.com.vitordevsp.TodoList/todos.db
```

Esse e um bom exemplo de detalhe pequeno que muda a qualidade do software.

O codigo continua simples, mas passa a respeitar o ambiente onde roda.

## 7. Build local e fluxo de desenvolvimento

Durante o desenvolvimento, o caminho mais simples e rodar o codigo Python direto:

```bash
make run
```

No projeto, isso executa:

```makefile
run:
	python3 -m src.main
```

Para iterar interface, existe tambem um modo de desenvolvimento:

```bash
make dev
```

Esse comando usa `dev.py` para reiniciar o app quando arquivos mudam. A ideia e
parecida com um `npm run dev`, mas adaptada para um app GTK.

O projeto tambem tem um build local com PyInstaller:

```bash
make build
```

Esse fluxo gera um binario em `dist/todolist-gtk`:

```makefile
build:
	python3 -m PyInstaller --noconfirm --onefile --windowed \
		--collect-all gi \
		--add-data "src/styles/style.css:src/styles" \
		--name "todolist-gtk" \
		src/main.py
```

Esse binario e util para teste local rapido.

Mas ele nao e a distribuicao oficial do app.

Essa separacao e importante: PyInstaller ajuda a empacotar Python em um
executavel. Flatpak ajuda a distribuir um app Linux com runtime, sandbox,
metadados e integracao com o desktop.

Sao ferramentas diferentes para problemas diferentes.

## 8. Distribuicao com Flatpak

Flatpak e um formato de distribuicao para apps Linux.

Ele combina algumas ideias:

- o app roda em sandbox;
- o app declara permissoes;
- dependencias de sistema ficam em runtimes;
- a aplicacao tem identidade propria;
- a instalacao integra `.desktop`, icone e metainfo.

No projeto, o manifesto e `br.com.vitordevsp.TodoList.yml`.

Trecho simplificado:

```yaml
app-id: br.com.vitordevsp.TodoList
runtime: org.gnome.Platform
runtime-version: '46'
sdk: org.gnome.Sdk
command: todolist-gtk
finish-args:
  - --share=ipc
  - --socket=fallback-x11
  - --socket=wayland
  - --device=dri
```

Alguns pontos:

- `app-id` identifica o app;
- `runtime` e `sdk` definem a base GNOME usada no build;
- `command` aponta para o executavel chamado ao iniciar;
- `finish-args` declara permissoes do sandbox.

O modulo do app usa `buildsystem: simple` e instala arquivos locais:

```yaml
modules:
  - name: todolist-gtk
    buildsystem: simple
    build-commands:
      - install -D todolist-gtk /app/bin/todolist-gtk
      - install -D main.py /app/share/todolist-gtk/src/main.py
      - install -D window.py /app/share/todolist-gtk/src/window.py
      - install -D models.py /app/share/todolist-gtk/src/models.py
      - install -D style.css /app/share/todolist-gtk/src/styles/style.css
```

Repare em um detalhe: o Flatpak final nao usa o binario PyInstaller do host.

Ele instala o codigo Python e usa um script em `/app/bin/todolist-gtk`:

```sh
#!/bin/sh
cd /app/share/todolist-gtk
exec python3 -m src.main "$@"
```

Isso evita misturar bibliotecas do host com o runtime do Flatpak.

Para este app, essa decisao deixa o pacote mais previsivel.

## 9. Bundle Flatpak: gerar, instalar e testar

O comando principal para gerar o pacote distribuivel e:

```bash
make bundle
```

O resultado esperado e:

```text
todolist.flatpak
```

na raiz do projeto.

O fluxo interno faz tres coisas:

```bash
make clean
flatpak-builder --disable-download --disable-rofiles-fuse \
  --repo=build/repo \
  --force-clean \
  --state-dir=build/.flatpak-builder-state \
  build/flatpak-build \
  br.com.vitordevsp.TodoList.yml

flatpak build-bundle \
  --runtime-repo=https://flathub.org/repo/flathub.flatpakrepo \
  build/repo \
  todolist.flatpak \
  br.com.vitordevsp.TodoList
```

O ponto mais importante aqui e `--disable-download`.

Ele faz o build falhar se o manifesto tentar buscar alguma fonte remota. Isso
protege o processo contra uma mudanca acidental que coloque downloads no meio do
bundle.

Esse foi um aprendizado real do projeto: uma correcao anterior tentou resolver o
empacotamento baixando dependencias durante o bundle. Pode parecer pratico, mas
torna o processo menos previsivel.

O contrato final ficou mais rigido:

- setup de maquina pode instalar ferramentas e runtimes;
- `make build` pode gerar binario local para teste;
- `make bundle` deve apenas usar artefatos locais e gerar o `.flatpak`;
- nada de `pip install`, `curl`, `wget` ou `flatpak remote-add` dentro do bundle.

Para instalar localmente:

```bash
flatpak install --user -y ./todolist.flatpak
```

Para rodar:

```bash
flatpak run br.com.vitordevsp.TodoList
```

Para retestar uma instalacao limpa:

```bash
make uninstall-data
make bundle
flatpak install --user -y ./todolist.flatpak
flatpak run br.com.vitordevsp.TodoList
```

Tambem existe `make uninstall`, que remove o app mas preserva os dados locais, e
`make uninstall-data`, que remove app e dados da sandbox.

## 10. Uma observacao importante sobre runtime

O estado validado deste projeto usa GNOME Platform 46.

Durante a instalacao local, o Flatpak avisou que esse runtime chegou ao fim de
vida. Entao, antes de uma distribuicao publica de verdade, o manifesto precisa
ser migrado para uma branch GNOME suportada.

Isso nao invalida o tutorial. Pelo contrario: mostra uma parte real do trabalho
de distribuir app Linux.

Nao basta gerar um arquivo que instala hoje. E preciso acompanhar o ciclo de vida
do runtime que voce escolheu.

Para projeto pessoal e experimento, manter o estado validado pode fazer sentido.
Para distribuicao publica, runtime suportado nao e detalhe.

## 11. Possiveis melhorias

O app ja cobre um ciclo completo, mas ainda existem caminhos interessantes:

- sincronizacao em nuvem;
- exportacao/importacao de listas;
- integracao com APIs externas;
- atalhos de teclado;
- notificacoes;
- busca;
- ordenacao manual;
- drag and drop;
- screenshots reais no metainfo;
- migracao do runtime Flatpak para uma branch suportada;
- publicacao futura no Flathub.

Tambem daria para separar mais a interface em arquivos menores ou experimentar
Blueprint para descrever UI fora do Python.

Para um projeto maior, isso provavelmente valeria a pena.

Para este TodoList, manter tudo simples ajudou a enxergar o ciclo inteiro.

## Conclusao

Criar a janela foi a parte facil.

O aprendizado real apareceu quando o app precisou se comportar como software
Linux de verdade:

- salvar dados no lugar certo;
- ter app id consistente;
- instalar `.desktop`, icone e metainfo;
- separar build local de distribuicao;
- gerar um bundle reprodutivel;
- testar instalacao e execucao como usuario final.

Python + GTK4 + Libadwaita formam uma stack bem acessivel para quem quer criar
apps nativos para Linux sem entrar direto em C, Rust ou C++.

E Flatpak fecha o ciclo: transforma um app local em algo instalavel, testavel e
mais proximo de distribuicao real.

Para quem vem da web, a curva existe. O modelo mental muda. Mas a recompensa e
boa: voce sai de um script para um app que aparece no menu do sistema e respeita
as convencoes do desktop.

Foi exatamente esse o valor do experimento.

Nao era so construir um TodoList.

Era atravessar o caminho inteiro.

---

Nota historica: a maior parte da construcao inicial deste projeto foi guiada com
Antigravity usando Gemini 3 Flash, modelo de 2024. A consolidacao final do
bundle, versionamento, documentacao e relatorios foi feita depois com
Codex/GPT-5.4.

Este artigo foi escrito em coautoria por Vitor Sampaio e Codex, a partir da
historia real do projeto TodoList GTK e dos registros de desenvolvimento
mantidos no repositorio.

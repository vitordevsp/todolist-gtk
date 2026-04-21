# TodoList GTK - Nativo Linux 🐧

Bem-vindo ao **TodoList GTK**, um gerenciador de tarefas moderno, leve e elegante desenvolvido especificamente para o ambiente Linux usando **GTK4** e **Libadwaita**.

Este projeto nasceu como um caso de teste utilizando o **Antigravity** (Codin assistant AI) e o modelo **Gemini 3 Flash** da Google DeepMind. O objetivo foi validar a capacidade da IA de construir um aplicativo desktop nativo do zero, focando em UX "premium" e boas práticas de desenvolvimento.

## ✨ Funcionalidades

- **Layout Estilo Simplenote:** Interface de duas colunas com barra lateral para organização.
- **Múltiplas Sessões (Listas):** Crie diferentes categorias para suas tarefas (Trabalho, Casa, Estudos, etc).
- **Ícones Inteligentes:** O app atribui ícones automaticamente baseado no nome das suas listas.
- **Modo Live Reload:** Ambiente de desenvolvimento ágil que reinicia o app automaticamente ao salvar o código.
- **Persistência Local:** Seus dados são salvos de forma segura em um banco de dados SQLite local.
- **Dark Mode Nativo:** Total integração com as preferências de tema do seu sistema GNOME.

## 🚀 Como Executar

### Pré-requisitos
- Python 3
- GTK4 e Libadwaita instalados no sistema

### Rodando o Projeto
1. Clone o repositório.
2. Na raiz do projeto, execute:
```bash
# Execução normal
make run

# Modo de desenvolvimento (Live Reload)
make dev
```

## 🏗️ Como funciona o Build

O processo de build utiliza o **PyInstaller** para transformar o código Python em um executável binário nativo.
- **Empacotamento:** O comando `make build` agrupa o interpretador Python, as bibliotecas necessárias e os arquivos de estilo (`data/`) em um único arquivo na pasta `dist/`.
- **Portabilidade:** Esse binário é autônomo (não precisa do código fonte para rodar), mas depende que o sistema operacional de destino tenha as bibliotecas do **GTK4** e **Libadwaita** instaladas (o que é padrão na maioria das distros focadas em GNOME como Ubuntu, Fedora e Pop!_OS).

## 📥 Instalação e Atualização

### Instalação Manual
Se você deseja "instalar" o app no seu sistema para que ele apareça no seu menu de aplicativos, siga estes passos:

1.  **Gere o binário:**
    ```bash
    make build
    ```
2.  **Mova para seus binários locais:**
    ```bash
    mkdir -p ~/.local/bin
    cp dist/todolist-gtk ~/.local/bin/
    ```
3.  **Crie um atalho no menu (Opcional):**
    Você pode criar um arquivo chamado `todolist.desktop` em `~/.local/share/applications/` apontando para o binário em `~/.local/bin/todolist-gtk`.

### Como Atualizar
Para atualizar o aplicativo instalado:
1.  Puxe as novas alterações do código fonte (ex: `git pull`).
2.  Rode `make build` novamente.
3.  Substitua o arquivo antigo pelo novo: `cp dist/todolist-gtk ~/.local/bin/`.

## 📦 Como Publicar em uma Loja (Flatpak)

Para transformar este projeto em um aplicativo oficial distribuível (com ícone no menu automático):

1.  **Instale as ferramentas:**
    ```bash
    sudo apt install flatpak-builder
    ```
2.  **Gere o binário PyInstaller primeiramente:**
    ```bash
    make build
    ```
3.  **Compile o Flatpak localmente:**
    ```bash
    flatpak-builder --user --install --force-clean build-dir com.vitordevsp.TodoList.yml
    ```
Isso instalará o app no seu sistema e ele aparecerá automaticamente no seu menu de aplicativos com o ícone oficial!

---

## 🧪 Contexto do Projeto
Este software é uma demonstração de colaboração entre humano e IA. Foi desenvolvido em tempo recorde, passando por fases de planejamento arquitetural, redesign de layout e polimento de UX, tudo mediado pelo assistente Antigravity.

---
Desenvolvido por **vitordevsp** com auxílio do **Antigravity (Gemini 3 Flash)**.

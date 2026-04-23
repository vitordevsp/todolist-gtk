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
O projeto depende de algumas bibliotecas de sistema (GTK4, Libadwaita, Python Dev).
👉 **Veja o [Guia de Configuração de Ambiente](docs/knowledge/environment-setup.md)** para preparar sua máquina.

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

O projeto mantém dois fluxos separados:
- **Binário Local:** `make build` gera um executável em `dist/` com PyInstaller para testes rápidos.
- **Instalação Flatpak:** `make flatpak` instala o app no seu menu de aplicativos usando o runtime GNOME.
- **Geração de Bundle:** `make bundle` gera o arquivo `todolist.flatpak` portável na raiz, sem usar o binário PyInstaller.

## 📦 Distribuição Oficial (Flatpak)

O ID oficial do aplicativo é **br.com.vitordevsp.TodoList**. Para gerar o instalador final:

1.  Certifique-se de ter o `flatpak-builder` instalado.
2.  Execute:
    ```bash
    make bundle
    ```
Isso criará o arquivo `todolist.flatpak` na raiz, pronto para ser enviado para outros usuários ou instalado com `flatpak install`.

---

## 🧪 Contexto do Projeto
Este software é uma demonstração de colaboração entre humano e IA. Foi desenvolvido em tempo recorde, passando por fases de planejamento arquitetural, redesign de layout e polimento de UX, tudo mediado pelo assistente Antigravity.

---

Desenvolvido por **[vitordevsp](https://vitordevsp.com.br)** com auxílio do **Antigravity (Gemini 3 Flash)**.

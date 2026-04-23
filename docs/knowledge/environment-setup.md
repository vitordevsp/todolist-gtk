# Guia de Configuração do Ambiente (Setup)

Este documento descreve todos os requisitos e comandos necessários para preparar uma nova máquina (Ubuntu/Debian) para desenvolver, compilar e empacotar o **Todo List GTK**.

## 1. Requisitos do Sistema (APT)

O Linux precisa das bibliotecas de desenvolvimento do GTK4 e do Python para que o PyInstaller e o Flatpak funcionem corretamente.

```bash
# Atualizar repositórios
sudo apt update

# Bibliotecas de Interface (GTK4 e Libadwaita)
sudo apt install libgtk-4-dev libadwaita-1-dev python3-gi

# Bibliotecas de Desenvolvimento Python (Necessário para o PyInstaller)
# Nota: Substitua 3.11 pela versão do seu Python se for diferente
sudo apt install libpython3.11 libpython3.11-dev
```

## 2. Ferramentas de Empacotamento

Instalação do Builder do Flatpak e do empacotador Python.

```bash
# Flatpak Builder
sudo apt install flatpak flatpak-builder

# PyInstaller (Instalação via pip para o usuário)
python3 -m pip install --user pyinstaller
```

> [!IMPORTANT]
> Os comandos `make build` e `make bundle` não instalam dependências automaticamente. `make build` exige PyInstaller instalado; `make bundle` usa `flatpak-builder` e o runtime/SDK GNOME já preparados, sem baixar dependências durante a geração do bundle.

## 3. Ambiente Flatpak (Runtimes)

O Flatpak precisa baixar o "Kit de Construção" do GNOME. Isso é feito uma única vez por máquina.

```bash
# 1. Adicionar o repositório Flathub
flatpak remote-add --user --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

# 2. Instalar o SDK e a Plataforma GNOME 46
flatpak install flathub org.gnome.Sdk//46 org.gnome.Platform//46
```

> [!WARNING]
> O manifesto atual ainda usa GNOME 46 para reproduzir o estado validado da v1. Durante a validação, o Flatpak avisou que esse runtime está em fim de vida e também sinalizou runtimes GL baseados em `org.freedesktop.Platform` 23.08 como sem suporte. Antes de distribuição pública, atualize o manifesto e este setup para uma branch GNOME suportada.

## 4. Verificação de Instalação

Após configurar tudo, você deve ser capaz de rodar os comandos do projeto:

| Comando | Objetivo |
| :--- | :--- |
| `make run` | Executa o app em modo de desenvolvimento. |
| `make build` | Gera o executável único local em `dist/` via PyInstaller. |
| `make bundle` | Gera o instalador `.flatpak` oficial usando o runtime GNOME, sem PyInstaller. |
| `make uninstall` | Remove a instalação Flatpak do usuário atual, preservando os dados locais. |
| `make uninstall-data` | Remove a instalação Flatpak e apaga os dados sandboxados do app. |

---

> [!IMPORTANT]
> **Segurança:** A instalação do Flatpak e seus SDKs é totalmente isolada (sandboxed). Ela **não** altera as bibliotecas do sistema e não afeta o desempenho ou a estabilidade do seu ambiente GNOME atual.

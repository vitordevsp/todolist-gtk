# Manual de Empacotamento Distribuível (Flatpak & Bundle)

Este guia detalha todo o workflow para transformar o código fonte do TodoList GTK em um pacote pronto para o usuário final.

O processo de empacotamento transforma seu código fonte em um arquivo instalável `.flatpak`, garantindo que ele rode em qualquer distribuição Linux (Ubuntu, Fedora, Arch, etc).

## 1. Identificação do Aplicativo
O ID oficial deste aplicativo é: **br.com.vitordevsp.TodoList**

## 2. Contrato de Build

O bundle da v1 deve ser gerado sem downloads ou instalações automáticas durante `make bundle`.

- Dependências de build (`flatpak-builder`, runtime e SDK GNOME) são preparadas antes, conforme `docs/knowledge/environment-setup.md`.
- `make build` é um fluxo separado para gerar `dist/todolist-gtk` com PyInstaller em testes locais.
- `make bundle` não usa o binário PyInstaller; ele empacota o código Python e executa pelo runtime GNOME do Flatpak.
- O manifesto Flatpak lista somente arquivos locais necessários como `type: file`, evitando copiar o repositório inteiro para o build.
- O alvo de bundle não deve executar `pip install`, `curl`, `wget`, `flatpak remote-add` ou instalar runtimes.

## 3. Estrutura de Build
Todas as pastas temporárias são geradas dentro do diretório `build/` para manter a raiz do projeto organizada.
- `build/flatpak-build`: Onde o app é montado.
- `build/repo`: Repositorio local temporário.
- `build/.flatpak-builder-state`: Cache de compilação.
- `src/styles/style.css`: CSS customizado empacotado junto com o código da interface.
- `data/`: Metadados de integração desktop, como `.desktop`, metainfo e ícone.

## 4. Comandos de Operação

### 4.1 Instalar Localmente (Modo Desenvolvedor)
Constrói o app e já o integra ao seu menu de aplicativos:
```bash
make flatpak
```

### 4.2 Gerar Bundle Portável (Modo Distribuição)
Cria um arquivo único para distribuição:
```bash
make bundle
```
- **Resultado:** Arquivo `todolist.flatpak` na raiz.
- **Destaque:** O bundle inclui a referência ao runtime repo do Flathub, permitindo instalação direta em ambientes Flatpak padrão quando o runtime GNOME 46 ainda não estiver presente.

Fluxo interno esperado:
```bash
make clean
flatpak-builder --disable-download --disable-rofiles-fuse --repo=build/repo --force-clean --state-dir=build/.flatpak-builder-state build/flatpak-build br.com.vitordevsp.TodoList.yml
flatpak build-bundle --runtime-repo=https://flathub.org/repo/flathub.flatpakrepo build/repo todolist.flatpak br.com.vitordevsp.TodoList
```

`--disable-download` faz o build falhar se alguma fonte remota aparecer por engano. `--disable-rofiles-fuse` evita dependencia do dispositivo `/dev/fuse` em ambientes de desenvolvimento onde ele nao esta disponivel.

### 4.3 Desinstalar para Retestar o Bundle
Remove a instalação Flatpak do usuário atual, preservando os dados locais:
```bash
make uninstall
```

Para simular uma instalação limpa e remover também os dados salvos no sandbox:
```bash
make uninstall-data
```

## 5. Simulando a Experiência do Usuário

### 5.1 Instalação direta do bundle

1.  Gere o arquivo com `make bundle`.
2.  Instale o bundle gerado:
    ```bash
    flatpak install --user -y ./todolist.flatpak
    ```
3.  Execute o app instalado:
    ```bash
    flatpak run br.com.vitordevsp.TodoList
    ```

### 5.2 Ciclo completo de validação

Use este fluxo quando quiser confirmar que o pacote gerado instala e roda do zero:

```bash
make uninstall-data
make bundle
flatpak install --user -y ./todolist.flatpak
flatpak run br.com.vitordevsp.TodoList
make uninstall
```

`make uninstall-data` é intencionalmente separado de `make uninstall` para evitar apagar o banco local por acidente durante testes comuns.

## 6. Depuração (Debug) e Problemas Comuns

- **"App não abre":** Rode `flatpak run -v br.com.vitordevsp.TodoList` no terminal para ver logs detalhados.
- **"Ícone não aparece":** Verifique se o `Icon=` no arquivo `.desktop` bate exatamente com o nome do arquivo SVG (sem a extensão `.svg`).
- **"libpython error":** Verifique se instalou os pacotes de desenvolvimento (`libpython3.11-dev`).
- **"PyInstaller não encontrado":** Rode `python3 -m pip install --user pyinstaller` durante o setup da máquina, não dentro de `make bundle`.

---

> [!TIP]
> O Flatpak garante que seu app funcione daqui a 5 anos exatamente como funciona hoje, pois a "plataforma" (runtime) fica congelada para aquela versão do seu app.

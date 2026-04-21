# Manual de Empacotamento Distribuível (Flatpak & Bundle)

Este guia detalha todo o workflow para transformar o código fonte do TodoList GTK em um pacote pronto para o usuário final.

## 1. O Fluxo de Construção (Build Pipeline)

O processo de empacotamento segue três etapas lógicas:
1.  **Código -> Binário:** Usamos o `PyInstaller` para criar um executável autônomo que embuti o interpretador Python e o CSS.
2.  **Binário -> Staging:** O `flatpak-builder` cria um ambiente isolado (sandbox) e copia o binário e os metadados (`.desktop`, `icons`, `metainfo`).
3.  **Staging -> Pacote:** O Flatpak comprime tudo em um bundle que o sistema reconhece como um aplicativo oficial.

## 2. Anatomia do Manifesto (`.yml`)

O arquivo `com.vitordevsp.TodoList.yml` é o coração do pacote:
- **`app-id`**: O identificador único global (DNS Reverso).
- **`runtime` / `sdk`**: Define a "camada de base" (GNOME 46). O Flatpak garante que essas bibliotecas estejam sempre lá.
- **`finish-args`**: Lista de permissões. Ex: `--socket=wayland` permite que o app use o servidor gráfico.

## 3. Metadados e Integração com o Menu

Para o Linux "enxergar" seu app no menu, ele precisa de:
- **`.desktop`**: Define o nome exibido e qual ícone usar.
- **`.svg`**: Deve estar em `/app/share/icons/...` para ser exibido.
- **`metainfo.xml`**: Contém a descrição e links que as lojas (GNOME Software) mostram.

## 4. Comandos de Operação

### 4.1 Instalar Localmente (Modo Desenvolvedor)
Para testar o app rapidamente no seu menu sem gerar arquivos extras:
```bash
make flatpak
```

### 4.2 Gerar Bundle Portável (Modo Distribuição)
Para criar um arquivo único que você pode enviar para alguém ou simular um download:
```bash
make bundle
```
- **Resultado:** Cria o arquivo `todolist.flatpak` na raiz.
- **Conceito:** Este arquivo é o "instalador" que contém tudo o que o app precisa.

## 5. Simulando a Experiência do Usuário (Download e Instalação)

Se você quiser testar exatamente como um usuário que baixou seu app da internet faria:
1.  Gere o arquivo com `make bundle`.
2.  Mova o `todolist.flatpak` para sua pasta de Downloads.
3.  Abra o terminal lá e rode:
    ```bash
    flatpak install todolist.flatpak
    ```

## 6. Lidando com Dependências Externas (Pip)

Se você adicionar uma biblioteca via pip (ex: `requests`), o Flatpak Builder não terá acesso à internet durante o build.
- **Solução:** Você deve usar a ferramenta `flatpak-pip-generator` para criar um arquivo JSON com os fontes das bibliotecas e incluí-lo na seção `modules` do seu manifesto.

## 6. Depuração (Debug) e Problemas Comuns

- **"App não abre":** Rode `flatpak run -v com.vitordevsp.TodoList` no terminal para ver logs detalhados.
- **"Ícone não aparece":** Verifique se o `Icon=` no arquivo `.desktop` bate exatamente com o nome do arquivo SVG (sem a extensão `.svg`).
- **"Permissão Negada":** Se seu app precisar acessar pastas do sistema, você deve adicionar `--filesystem=home` ou similar nos `finish-args`.

---

> [!TIP]
> O Flatpak garante que seu app funcione daqui a 5 anos exatamente como funciona hoje, pois a "plataforma" (runtime) fica congelada para aquela versão do seu app.

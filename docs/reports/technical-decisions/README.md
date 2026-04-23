# Relatorio: Decisoes Tecnicas e Pontos de Virada

## Objetivo

Separar decisoes tecnicas com potencial editorial de detalhes comuns de
implementacao.

## Decisoes Identificadas

### GTK4 + Libadwaita como stack nativa

Sinais:

- `AGENTS.md`: define GTK4, Libadwaita e PyGObject como stack recomendada;
- `README.md`: posiciona o app como nativo Linux;
- `MEMORY.md`: registra retrocompatibilidade do Libadwaita como aprendizado.

Potencial editorial:

Um artigo pode explorar por que construir um app desktop nativo Linux ainda e uma
boa forma de testar agentes de IA: exige UI real, runtime local, empacotamento e
interacao com o sistema operacional.

### Layout inspirado no Simplenote com `Adw.Flap`

Sinais:

- `MEMORY.md`: registra `Adw.Flap` como solucao para barra lateral fluida;
- `docs/knowledge/ui-ux-patterns.md`: documenta layout e estados vazios;
- commits iniciais implementam `src/window.py` com a maior parte da UI.

Potencial editorial:

Mostrar que mesmo um app simples pode ter decisoes de UX suficientes para testar
se a IA entende experiencia, e nao so sintaxe.

### Persistencia via SQLite e XDG/GLib

Sinais:

- `MEMORY.md`: registra migracao de schema SQLite;
- `docs/plans/001-v1-todolist/questions.md`: decisao humana sobre persistencia;
- `docs/knowledge/persistence-and-xdg.md`: consolida comportamento final;
- commit `c352d8d`: ajusta persistencia para `GLib.get_user_data_dir()`.

Potencial editorial:

Bom candidato para artigo tecnico curto sobre o detalhe que diferencia prototipo
de app desktop minimamente correto: salvar dados no lugar certo.

### PyInstaller como build local, Flatpak como distribuicao

Sinais:

- `README.md`: separa binario local, instalacao Flatpak e bundle;
- `docs/knowledge/bundle-manual.md`: define contrato de bundle;
- commit `6ddc40c`: torna bundle deterministico;
- `docs/plans/001-v1-todolist/logs.md`: registra que PyInstaller dentro do Flatpak
  gerou risco tecnico.

Potencial editorial:

Este e um dos melhores arcos narrativos: a diferenca entre "gerar um binario" e
"distribuir oficialmente um app Linux".

### Bundle deterministico sem downloads durante o empacotamento

Sinais:

- `Makefile`: usa `--disable-download` e `--disable-rofiles-fuse`;
- `docs/plans/001-v1-todolist/plan.md`: explicita regra contra `pip install`,
  `curl`, `wget`, `flatpak remote-add` e downloads inesperados no bundle;
- log final de instalacao: app instalado a partir de remoto local `todolist-origin`.

Potencial editorial:

Tema forte para falar sobre limites de IA: a primeira correcao que "faz
funcionar" pode quebrar requisitos invisiveis como reprodutibilidade e seguranca.

## Ambiguidades

- Ainda falta confirmar em detalhe qual mudanca exata da IA anterior introduziu
  download em tempo de bundle.
- A stack ainda usa runtime GNOME 46, que esta EOL; antes de artigo tecnico sobre
  distribuicao "pronta para publico", esse ponto precisa ser tratado ou
  explicado como pendencia.

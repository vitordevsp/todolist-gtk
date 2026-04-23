# Relatorio: Memoria e Aprendizados

## Objetivo

Mapear aprendizados registrados em memoria, changelog e logs para separar
materia-prima editorial de detalhes operacionais.

## Fontes

- `MEMORY.md`
- `CHANGELOG.md`
- `docs/plans/001-v1-todolist/logs.md`
- `docs/knowledge/*`

## Aprendizados Com Potencial Editorial

### Retrocompatibilidade do Libadwaita

Sinais:

- `MEMORY.md`: tentativa com `Adw.ToolbarView` bloqueada por Libadwaita 1.1;
- `AGENTS.md`: registra workaround para sistemas antigos.

Possivel uso:

Artigo sobre como IA pode sugerir componentes modernos, mas o ambiente real
obriga compatibilidade e verificacao local.

### Apps desktop exigem detalhes de sistema

Sinais:

- `MEMORY.md`: `libpython shared library not found` no PyInstaller;
- `docs/knowledge/environment-setup.md`: setup com libs GTK, Libadwaita,
  Python dev, Flatpak e runtimes;
- `docs/knowledge/persistence-and-xdg.md`: caminho correto de dados.

Possivel uso:

Artigo sobre por que desktop nativo e um bom laboratorio para testar IA:
pequenas decisoes incorretas aparecem rapido.

### Bundle nao e apenas build

Sinais:

- `MEMORY.md`: diferencia binario PyInstaller de bundle Flatpak;
- `docs/plans/001-v1-todolist/logs.md`: registra bundle final sem downloads;
- `CHANGELOG.md`: registra a separacao entre PyInstaller local e Flatpak oficial.

Possivel uso:

Artigo tecnico sobre empacotamento Linux e a distancia entre "rodou aqui" e
"instalavel de forma confiavel".

### Documentacao viva preserva trabalho entre agentes

Sinais:

- `docs/plans/001-v1-todolist/questions.md`: decisoes humanas registradas;
- `docs/plans/001-v1-todolist/logs.md`: explica mudancas de rota;
- `docs/knowledge/project-structure.md`: registra convencoes que nasceram no
  meio da implementacao;
- `docs/README.md`: assume a camada como mini-framework `studio-coding`.

Possivel uso:

Artigo sobre como a documentacao virou ferramenta de continuidade entre Gemini,
Codex e a direcao humana do projeto.

## Sinais Que Devem Permanecer Internos Por Enquanto

- Detalhes de comandos de validacao que nao sustentam narrativa publica.
- Caminhos locais sensiveis, exceto quando usados como referencia interna.
- Mensagens de erro exatas ainda nao confirmadas em fonte versionada.

## Lacunas

- `MEMORY.md` ainda reflete principalmente a fase Antigravity/Gemini; talvez
  precise ser atualizado futuramente com aprendizados da consolidacao Codex.
- A conversa atual tem contexto rico, mas ainda nao esta materializada em
  arquivo proprio alem destes reports.

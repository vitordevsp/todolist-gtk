# Knowledge

Esta pasta guarda conhecimento tecnico consolidado durante o desenvolvimento do
TodoList GTK.

Use `knowledge/` quando a informacao explicar como o app funciona, como ele deve
ser empacotado, como o ambiente e preparado ou quais decisoes tecnicas precisam
ser lembradas em manutencoes futuras.

## Guias

- [`bundle-manual.md`](./bundle-manual.md): contrato de build e bundle Flatpak.
- [`environment-setup.md`](./environment-setup.md): preparo da maquina para desenvolvimento e empacotamento.
- [`persistence-and-xdg.md`](./persistence-and-xdg.md): persistencia SQLite e caminhos XDG/Flatpak.
- [`project-structure.md`](./project-structure.md): organizacao de `src/`, `data/`, versionamento e bundle.
- [`ui-ux-patterns.md`](./ui-ux-patterns.md): decisoes de UI, layout, estados vazios, icones e CSS.

## Quando Atualizar

Atualize esta pasta quando uma descoberta tecnica deixar de ser apenas uma nota
de execucao e passar a orientar manutencoes futuras.

Se o registro for sobre andamento de uma frente, prefira `docs/plans/`.
Se for uma convencao documental reutilizavel, prefira `docs/patterns/`.

# Plano 003: Reescrita dos Dois Artigos Iniciais

## 1. Objetivo

Orquestrar a criacao de dois artigos a partir dos rascunhos gerados pelo Gemini
3 Flash e dos relatorios editoriais consolidados neste repositorio.

Os artigos devem transformar os rascunhos soltos em textos mais vivos,
autenticos e sustentados pela historia real do projeto.

## 2. Escopo

Este plano cobre dois artigos:

1. Artigo tecnico sobre Linux, GTK, Libadwaita, Flatpak, persistencia e bundle.
2. Artigo de experiencia sobre desenvolver guiando IA sem dominar previamente a
   stack.

Este plano nao cobre:

- geracao de uma serie inteira;
- publicacao no blog;
- criacao de novos candidatos alem dos dois rascunhos atuais;
- reescrita dos relatorios-base.

## 3. Fontes Principais

- [`docs/reports/article-candidates/README.md`](../../reports/article-candidates/README.md)
- [`docs/reports/conversation-sources/README.md`](../../reports/conversation-sources/README.md)
- [`docs/reports/technical-decisions/README.md`](../../reports/technical-decisions/README.md)
- [`docs/reports/memory-and-learning-signals/README.md`](../../reports/memory-and-learning-signals/README.md)
- [`docs/reports/docs-framework-evolution/README.md`](../../reports/docs-framework-evolution/README.md)
- [`artigo_tecnico_linux_gtk.md`](../../reports/article-candidates/artigo_tecnico_linux_gtk.md)
- [`artigo_experiencia_ai.md`](../../reports/article-candidates/artigo_experiencia_ai.md)

## 4. Direcao Editorial Geral

- Preservar a historia real do projeto.
- Evitar tom generico, motivacional ou "guia definitivo" sem lastro.
- Explicar que o corpo inicial foi guiado com Antigravity usando Gemini 3 Flash,
  modelo de 2024.
- Explicar que a consolidacao final foi feita com Codex/GPT-5.4.
- Mostrar o papel humano como direcao, criterio e curadoria.
- Deixar divergencias e mudancas de rota como parte da narrativa, nao como
  defeito a esconder.

## 5. Destino Esperado

Quando aprovados, os artigos finais devem ser criados em:

```text
docs/articles/
```

Nomes sugeridos:

- `linux-gtk-flatpak-com-ia.md`
- `experiencia-desenvolvimento-ia-sem-dominar-stack.md`

## 6. Rodape Obrigatorio

Todo artigo final deve terminar com:

```text
Este artigo foi escrito em coautoria por Vitor Sampaio e Codex, a partir da
historia real do projeto TodoList GTK e dos registros de desenvolvimento
mantidos no repositorio.
```

## 7. Criterios de Aceite

- Cada artigo deve partir do rascunho correspondente, mas nao ficar preso ao tom
  original.
- Cada artigo deve cruzar pelo menos tres fontes reais do projeto.
- Cada artigo deve citar corretamente a distribuicao do trabalho entre Gemini 3
  Flash/Antigravity e Codex/GPT-5.4.
- Cada artigo deve preservar pendencias quando forem relevantes, como GNOME 46
  EOL no artigo tecnico.
- Nenhum artigo deve ser criado sem pedido explicito de execucao da task.

## 8. Relacao com o Plano 002

O plano editorial anterior continua sendo a camada de investigacao e curadoria
ampla. Este plano 003 e uma frente de execucao focada em dois rascunhos ja
existentes.

O plano anterior agora esta em
[`002-editorial-articles-from-project-history`](../002-editorial-articles-from-project-history/plan.md)
e funciona como origem da curadoria.

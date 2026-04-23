# Plano: Artigos a Partir da Historia Real do Projeto

## 1. Decisao de Frente

Esta frente merece um plano.

Motivo: a geracao de artigos a partir do TodoList GTK depende de varias fontes,
atravessa multiplas sessoes e precisa separar investigacao, curadoria e escrita.
Gerar posts diretamente agora criaria risco de simplificar demais a historia ou
tratar uma fonte isolada como verdade absoluta.

## 2. Objetivo

Criar uma esteira editorial dentro da instancia reduzida do framework
`studio-coding` usada neste repositorio.

Essa esteira deve transformar a historia real do projeto em possiveis artigos de
blog, preservando:

- autenticidade do experimento;
- linha do tempo real;
- decisoes tecnicas e documentais;
- aprendizados sobre colaboracao humano-IA;
- limites encontrados em ferramentas, ambiente e empacotamento;
- espaco para curadoria humana antes da escrita final.

## 3. Escopo

Inclui:

- criar `docs/articles/` como destino futuro de posts;
- criar `docs/reports/` como camada intermediaria de investigacao;
- criar relatorios iniciais com sinais editoriais;
- criar um relatorio final de candidatos a artigos;
- documentar regras para nao gerar artigos antes da curadoria.

Nao inclui nesta fase:

- escrever artigos finais;
- publicar no blog;
- transformar todo o framework `studio-coding` para dentro deste repo;
- tratar qualquer conversa ou log isolado como verdade final.

## 4. Fontes

Fontes de primeira rodada:

- historico de commits;
- `README.md`;
- `CHANGELOG.md`;
- `MEMORY.md`;
- `AGENTS.md`;
- `docs/README.md`;
- `docs/knowledge/`;
- `docs/patterns/`;
- `docs/plans/v1_todolist/`;
- conversa atual com Codex;
- conversa Antigravity/Gemini em `/home/vitordevsp/.gemini/antigravity/brain/16b54b2c-7810-4127-8837-9681a0103cf4/`.

## 5. Estrutura Criada

- `docs/articles/`: artigos finais e rascunhos editoriais aprovados.
- `docs/reports/`: relatorios intermediarios.
- `docs/reports/article-candidates/`: lista curavel de candidatos a artigos.

## 6. Pipeline Editorial

1. Coletar sinais em relatorios intermediarios.
2. Cruzar sinais entre commits, docs, memoria, planos e conversas.
3. Registrar lacunas e ambiguidades.
4. Consolidar candidatos em `docs/reports/article-candidates/`.
5. Aguardar curadoria humana.
6. Gerar artigos finais em `docs/articles/` apenas quando explicitamente pedido.

## 7. Criterios Para Um Tema Virar Artigo

Um tema e bom candidato quando:

- tem conflito, decisao ou aprendizado claro;
- e sustentado por mais de uma fonte;
- conversa com uma audiencia alem do proprio repositorio;
- preserva a experiencia real de desenvolvimento;
- pode ensinar algo sobre IA, GTK/Linux, Flatpak, documentacao operacional ou
  processo de trabalho.

Um tema deve permanecer como report interno quando:

- depende de uma unica fonte fragil;
- e util apenas como detalhe tecnico;
- ainda precisa de confirmacao humana;
- nao tem arco narrativo claro.

## 8. Rodape Padrao de Coautoria

Todo artigo final deve terminar com:

```text
Este artigo foi escrito em coautoria por Vitor Sampaio e Codex, a partir da
historia real do projeto TodoList GTK e dos registros de desenvolvimento
mantidos no repositorio.
```

## 9. Pendencias

- Explorar com mais profundidade as versoes incrementais da conversa
  Antigravity/Gemini.
- Decidir se artigos finais ficarao em `docs/articles/` ou se serao exportados
  para outro repositorio/blog.
- Definir tom editorial: relato tecnico, diario de experimento, tutorial ou
  ensaio sobre processo.

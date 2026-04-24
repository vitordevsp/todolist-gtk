---
title: Plano 004: Landing Page do Projeto
description: Frente de descoberta, narrativa e implementacao de uma landing page para apresentar o app e o contexto do projeto.
status: in_progress
source_path: docs/plans/004-landing-page-do-projeto/plan.md
last_updated: 2026-04-24 00:00
---

# Plano 004: Landing Page do Projeto

## 1. Objetivo

Criar uma landing page forte para apresentar o **TodoList GTK** como produto,
experimento tecnico e estudo real de desenvolvimento assistido por IA.

Essa landing page deve comunicar valor rapidamente, mostrar o diferencial de
ser um app nativo Linux com GTK4 + Libadwaita e transformar o contexto do
repositorio em uma narrativa visual convincente.

## 2. Contexto do Produto

Hoje o projeto ja possui uma base clara:

- aplicativo desktop nativo para Linux;
- stack em Python + GTK4 + Libadwaita;
- persistencia local com SQLite;
- fluxo de desenvolvimento com live reload;
- build local e distribuicao via Flatpak;
- documentacao viva com planos, knowledge, reports e artigos.

O README atual apresenta bem o projeto para quem ja abriu o repositorio, mas a
nova frente busca uma pagina com linguagem mais comercial/editorial, melhor
hierarquia visual e maior poder de apresentacao.

## 3. Gatilho Desta Frente

O usuario vai enviar um prompt grande e detalhado que servira como base
principal da landing page.

Antes desse insumo chegar, este plano organiza a missao para que a execucao nao
fique improvisada: primeiro absorver o prompt, depois transformar o material em
mensagem, estrutura, interface e implementacao.

## 4. Escopo

Esta frente cobre:

- contextualizacao do app e da proposta da landing page;
- leitura e sintese do prompt-base quando ele chegar;
- definicao da narrativa principal da pagina;
- traducao da narrativa em secoes, copy e hierarchy visual;
- implementacao da landing page no projeto;
- validacao visual e tecnica minima da entrega;
- atualizacao da documentacao afetada pela nova pagina.

Esta frente nao cobre por enquanto:

- publicacao externa em dominio proprio;
- analytics, SEO avancado ou funil de marketing completo;
- sistema CMS para editar a landing page;
- campanha de lancamento fora do repositorio.

## 5. Hipotese de Direcao

A landing page precisa equilibrar tres camadas sem virar pagina generica:

1. **Produto:** um gerenciador de tarefas nativo, elegante e util para Linux.
2. **Tecnologia:** GTK4, Libadwaita, SQLite, Flatpak e UX de app desktop real.
3. **Narrativa:** um projeto construido com criterio humano e acelerado por IA,
   com documentacao e aprendizado registrados no proprio repositorio.

Se o prompt detalhado trouxer uma direcao mais especifica, ele passa a ser a
fonte principal desta frente.

## 6. Entregaveis Esperados

- uma pagina de apresentacao implementada no projeto;
- copy alinhada ao posicionamento definido a partir do prompt;
- estrutura de secoes com ordem e objetivo claros;
- refinamento visual coerente com a identidade do app;
- atualizacao do README e/ou docs afetados, se a nova pagina mudar a forma de
  apresentar o projeto.

## 7. Fases de Execucao

### Fase 1: Absorcao do Prompt-Base

- ler o prompt detalhado enviado pelo usuario;
- extrair objetivo, tom, publico, argumentos e restricoes;
- separar o que e obrigatorio, desejavel e opcional;
- registrar perguntas ou conflitos de direcao, se aparecerem.

### Fase 2: Estrategia de Narrativa

- sintetizar a proposta de valor principal;
- definir promessa, prova, diferenciais e CTA;
- escolher a ordem narrativa das secoes;
- alinhar a pagina ao contexto real do projeto, sem marketing vazio.

### Fase 3: Arquitetura da Landing Page

- definir quais secoes entram;
- mapear conteudo de cada secao;
- decidir onde usar screenshot, mockup, cards, prova tecnica ou timeline;
- fechar uma direcao visual antes de alterar varios arquivos.

### Fase 4: Implementacao

- construir a landing page no stack atual do projeto;
- reaproveitar assets reais do app sempre que fizer sentido;
- ajustar responsividade, ritmo visual e acabamento;
- revisar textos e links visiveis.

### Fase 5: Validacao

- verificar se a pagina carrega corretamente;
- revisar consistencia entre copy e produto real;
- executar checks tecnicos cabiveis no repo;
- atualizar logs e documentacao da frente.

## 8. Criterios de Aceite

- a landing page apresenta claramente o que e o TodoList GTK;
- a pagina transmite diferencial real, nao apenas estetica;
- a copy final conversa com o prompt-base e com o estado real do produto;
- a interface fica intencional e forte, sem cair em layout genérico;
- a implementacao funciona bem em desktop e mobile;
- README e docs relevantes ficam coerentes com a nova camada de apresentacao.

## 9. Fontes Iniciais

- [`README.md`](../../../README.md)
- [`docs/README.md`](../../README.md)
- [`docs/knowledge/ui-ux-patterns.md`](../../knowledge/ui-ux-patterns.md)
- [`docs/knowledge/project-structure.md`](../../knowledge/project-structure.md)
- [`docs/plans/001-v1-todolist/plan.md`](../001-v1-todolist/plan.md)
- prompt detalhado do usuario quando for enviado

# IA não fez o app sozinha — mas mudou tudo

Descricao: Relato sobre a experiencia de construir um aplicativo desktop Linux usando IA como parceira de desenvolvimento, explorando processo, aprendizado e mudanca de paradigma.

Tags: IA, desenvolvimento, produtividade, linux, programacao, engenharia de software, llm

## Continuação técnica

Este texto e a primeira parte de uma dupla.

Aqui eu conto a experiencia de construir o projeto guiando IA, sem dominar
previamente toda a stack nativa Linux. A segunda parte aprofunda o lado tecnico:
GTK4, Libadwaita, persistencia, PyInstaller, Flatpak e o caminho ate um bundle
instalavel.

Link da parte 2: [Do zero ao Flatpak: criando um app nativo para Linux com Python e GTK](./linux-gtk-flatpak-com-ia.md)

## O projeto que eu sempre adiava

Eu uso Linux. Eu gosto de Linux. Eu tinha vontade de criar algo nativo para
Linux fazia tempo.

Mas essa vontade sempre ficava naquele lugar meio conhecido de todo
desenvolvedor: "um dia eu paro para aprender essa stack direito".

No meu dia a dia, minha base e muito mais frontend, JS/TS, produto, interface,
arquitetura de aplicacao web. Eu consigo navegar bem por sistemas, pensar fluxo,
produto, experiencia, estados, manutencao. Mas GTK4, Libadwaita, PyGObject,
Flatpak, metainfo, empacotamento desktop Linux... isso nao era exatamente meu
territorio natural.

Entao esse tipo de projeto tinha um custo alto antes mesmo de comecar.

Nao era so escrever codigo.

Era escolher stack. Entender padroes. Descobrir como abrir janela. Como salvar
dado local. Como empacotar. Como fazer aparecer no menu. Como nao fazer besteira
com pasta de usuario. Como transformar um script em um app que se comporta como
app.

Esse custo sempre empurrava a ideia para depois.

Dessa vez eu resolvi testar outro caminho: em vez de esperar ate eu "ter tempo
para aprender tudo", eu usei IA como par de desenvolvimento.

## O recorte era pequeno de proposito

O projeto escolhido foi um TodoList.

Nada revolucionario. Nada que va mudar a historia da computacao. Um app simples
de lista de tarefas, com GTK4, Libadwaita, SQLite e depois Flatpak.

Mas esse era exatamente o ponto.

Eu nao queria testar se uma IA conseguia inventar um produto complexo. Eu queria
testar se ela conseguiria me ajudar a atravessar um ciclo inteiro de
desenvolvimento em uma stack que eu nao dominava.

Um TodoList pequeno ainda toca muita coisa real:

- interface nativa;
- estado vazio;
- listas e sessoes;
- persistencia local;
- banco SQLite;
- live reload para iterar UI;
- build local;
- metadados desktop;
- empacotamento Flatpak;
- documentacao;
- versionamento;
- validacao.

Esse foi o laboratorio.

O app era simples. O ciclo nao era.

## Nao foram 15 horas lineares

O projeto aconteceu em algo entre 10 e 15 horas totais, espalhadas por alguns
dias.

Mas nao foi um fluxo tradicional.

Eu nao sentei, abri o editor e fiquei implementando tudo de ponta a ponta.

O fluxo real foi mais quebrado, e talvez mais interessante:

1. Eu abria o projeto.
2. Dava uma instrucao para a IA.
3. Deixava ela trabalhar.
4. Voltava depois.
5. Testava.
6. Via o que fazia sentido.
7. Corrigia a rota.
8. Pedia a proxima etapa.

Muitas vezes eu estava trabalhando em outra coisa enquanto o agente evoluia o
projeto. Eu voltava para revisar, testar, ajustar o prompt, pedir outro caminho
ou apontar uma inconsistencia.

Isso muda bastante a sensacao de programar.

Nao parece exatamente "estou escrevendo cada linha". Tambem nao parece "a IA fez
tudo".

Parece mais dirigir um processo.

Voce precisa saber para onde quer ir. Precisa perceber quando o caminho ficou
estranho. Precisa pedir verificacao. Precisa desconfiar de atalhos bonitos. E,
principalmente, precisa aprender a falar com a IA de um jeito que transforme uma
ideia vaga em trabalho executavel.

## O modelo principal nao era o melhor disponivel

Um detalhe importante: a maior parte do projeto foi construida com Antigravity
usando Gemini 3 Flash, um modelo de 2024.

E isso importa.

Nao era o modelo mais forte disponivel. Os creditos dos modelos melhores tinham
acabado. Eu estava, na pratica, testando o quanto dava para extrair de um modelo
mais leve, dentro de um fluxo de agente, com boa orientacao e contexto.

E o resultado me surpreendeu.

O Gemini 3 Flash conseguiu levar o projeto muito longe:

- criou a base GTK;
- montou a UI inicial;
- implementou SQLite;
- redesenhou a interface para um estilo com barra lateral;
- adicionou multiplas sessoes;
- criou estado vazio;
- adicionou icones;
- montou Makefile e live reload;
- gerou metadados desktop;
- iniciou o caminho de Flatpak;
- criou `AGENTS.md`, `MEMORY.md`, planos e documentos de apoio.

Nao foi perfeito.

Mas foi suficiente para tirar uma ideia antiga do lugar.

E esse e um ponto que eu acho facil subestimar: talvez o ganho nao esteja apenas
em usar sempre "o melhor modelo". O ganho tambem esta em aprender a trabalhar
melhor com o modelo que voce tem.

## Prompt virou interface de desenvolvimento

Ao longo do projeto, ficou muito claro que o prompt nao era apenas uma pergunta.

O prompt era a interface de desenvolvimento.

Eu nao estava so pedindo "crie um app". Eu precisava fatiar o trabalho em
decisoes:

- "vamos mudar o layout";
- "isso precisa persistir";
- "nao assume que eu conheco Flatpak";
- "documenta isso";
- "essa mudanca precisa ser reprodutivel";
- "se tiver duvida, registra em questions";
- "nao gera artigo ainda, primeiro cria relatorios";
- "isso faz parte de um framework maior".

Cada prompt mudava a forma como a IA entendia o projeto.

E eu fui percebendo uma coisa: prompt bom nao e necessariamente prompt grande.
Prompt bom e prompt que coloca restricao, contexto e criterio.

O que eu queria nao era so codigo funcionando. Eu queria um projeto que eu
conseguisse continuar entendendo depois.

Por isso a documentacao virou parte do processo, nao um extra.

## A IA acelerou, mas tambem errou

Teve um momento muito simbolico no projeto: a IA declarou que estava tudo pronto
para uma especie de v1.0.

O app funcionava. Tinha UI. Tinha build. Tinha README. Parecia fechado.

Mas ainda nao estava fechado de verdade.

Depois, na fase de consolidacao com Codex/GPT-5.4, olhando com mais rigor para
o bundle Flatpak, apareceu o tipo de problema que separa "rodou aqui" de
"eu confiaria em distribuir isso".

Uma tentativa anterior de corrigir o bundle tinha levado o processo para um
caminho ruim: baixar dependencias durante a geracao do bundle.

Isso pode ate parecer uma solucao quando o objetivo e "fazer passar". Mas nao
era o que eu queria.

Eu queria um processo simples, deterministico e seguro.

Entao o trabalho mudou de natureza.

Nao era mais construir feature. Era auditar. Remover ambiguidade. Separar setup
de maquina, build local e bundle oficial. Garantir que `make bundle` nao fazia
magica escondida. Validar instalacao. Registrar pendencias.

Essa parte foi muito menos glamourosa. E muito mais engenharia.

Foi tambem onde ficou claro que IA nao elimina criterio. Ela aumenta a
importancia do criterio.

## Documentacao virou ferramenta, nao burocracia

Um dos resultados mais interessantes nao foi o app.

Foi a pasta `docs/`.

No comeco, ela era so um lugar para guardar plano e anotacoes. Depois virou uma
camada operacional do projeto.

Entraram planos, tarefas, logs, perguntas, memoria, knowledge, reports e agora
articles.

Isso conversa diretamente com o que eu venho chamando de `studio-coding`: uma
forma de estruturar desenvolvimento assistido por IA usando documentacao como
contexto vivo.

Nao e documentacao para ficar bonita no repositorio.

E documentacao para orientar trabalho.

Quando uma decisao nao estava clara, ela ia para `questions.md`.
Quando uma frente precisava sobreviver a varias sessoes, virava plano.
Quando um aprendizado tecnico precisava ser lembrado, virava knowledge ou memory.
Quando a historia do projeto comecou a render possiveis textos, virou report.

Isso mudou a qualidade da colaboracao com a IA.

Porque o chat sozinho evapora. O repositorio fica.

## O papel mudou

Essa experiencia me deixou com uma impressao forte: IA nao substitui o
desenvolvedor, mas muda bastante o papel dele.

Antes, em um projeto pessoal desse tipo, o gargalo seria principalmente tempo
para construir.

Agora, o gargalo virou clareza para direcionar.

Clareza para dizer o que importa.
Clareza para saber quando uma solucao esta boa o suficiente.
Clareza para desconfiar de uma resposta confiante.
Clareza para pedir validacao.
Clareza para transformar tentativa em aprendizado reutilizavel.

Isso exige outra musculatura.

Menos "eu preciso digitar cada linha".
Mais "eu preciso conduzir um sistema que gera, erra, corrige, documenta e
evolui comigo".

Nao e menos engenharia.

E outro tipo de engenharia.

## O que ficou pronto

No final, o projeto chegou a um estado pequeno, mas muito concreto:

- app GTK4 + Libadwaita;
- SQLite;
- multiplas sessoes;
- estado vazio;
- icones inteligentes;
- live reload;
- build local;
- bundle Flatpak;
- versionamento `0.1.0`;
- tag Git;
- documentacao operacional;
- relatorios para futuros artigos.

Mas, para mim, o resultado mais importante foi outro.

Eu agora tenho um laboratorio pessoal para explorar Linux desktop.

E tenho uma prova bem pratica de que projetos pessoais ficaram mais viaveis.

Nao porque a IA "faz tudo".

Mas porque ela reduz o atrito entre curiosidade e prototipo real.

## O que vem na parte tecnica

Este artigo ficou mais na experiencia: como foi guiar a IA, trabalhar em uma
stack pouco familiar e transformar um app simples em laboratorio.

Na parte tecnica, eu entro no caminho de um script Python/GTK ate um bundle
Flatpak instalavel, incluindo persistencia XDG, PyInstaller, manifesto,
metainfo e os cuidados para nao transformar o build em uma caixa-preta cheia de
downloads.

Link da parte 2: [Do zero ao Flatpak: criando um app nativo para Linux com Python e GTK](./linux-gtk-flatpak-com-ia.md)

## Conclusao

Eu comecei esse projeto querendo testar se dava para criar um app Linux nativo
com ajuda de IA.

Terminei com uma percepcao mais ampla.

Nunca foi tao facil testar ideias. A barreira de entrada caiu muito. Coisas que
antes ficavam meses na gaveta agora podem virar experimentos reais em alguns
dias.

Mas isso nao torna o desenvolvedor irrelevante.

Pelo contrario.

Quanto mais a IA consegue executar, mais importante fica saber direcionar.

Saber o que pedir.
Saber quando parar.
Saber quando duvidar.
Saber quando documentar.
Saber quando transformar uma resposta boa em uma decisao de projeto.

A IA nao fez o app sozinha.

Mas mudou tudo.

---

Este artigo foi escrito em coautoria por Vitor Sampaio e Codex, a partir da
historia real do projeto TodoList GTK e dos registros de desenvolvimento
mantidos no repositorio.

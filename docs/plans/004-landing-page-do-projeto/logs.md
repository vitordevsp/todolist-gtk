# Logs - Plano 004: Landing Page do Projeto

## 2026-04-23

- Frente criada para organizar a missao de construir uma landing page de alta
  qualidade para o TodoList GTK.
- Contexto inicial consolidado a partir do `README.md` e da camada `docs/`.
- Execucao depende do prompt detalhado que o usuario informou que enviara na
  sequencia.
- Intro recebida: a pagina passa a enfatizar o projeto como laboratorio real de
  desenvolvimento com IA, nao apenas como app de tarefas.
- Etapa 1 executada com stack fixa em HTML + Tailwind CDN + JS vanilla, pronta
  para GitHub Pages sem build step.
- Criada a estrutura `site/` com `index.html`, `script.js`, `assets/` e
  `product/`, alem de skeleton HTML com todas as sections obrigatorias.
- Etapa 2 executada com copy completa da landing, estrutura semantica preenchida
  e narrativa mais pessoal sobre o projeto.
- Criados os tres arquivos-base de produto em `site/product/` com recortes de
  posicionamento, UX e historia real do laboratorio.
- Implementada a secao de captura de interesse com UI apenas e persistencia
  local via `localStorage`, sem backend.
- Etapa 3 executada com hero reforcado, melhor acabamento visual, responsividade
  refinada, menu mobile funcional e animacoes leves de entrada.
- Navegacao por ancora mantida em HTML estatico para GitHub Pages, com JS minimo
  para menu, reveal-on-scroll e captura local de leads.
- Refinamento posterior aplicado a partir de analise tecnica da landing:
  tipografia ajustada com `JetBrains Mono` para labels, CTA extras no hero,
  formulario de lead com nome + e-mail e footer em tres colunas com redes.
- Ajustados botoes da hero para remover deslocamento no hover e usar estados
  mais estaveis. Trocados icones de marca por icones Lucide genericos
  garantidos no botao de GitHub e nos links sociais do rodape.
- Refatoracao visual/editorial aplicada sem trocar a stack: ritmos de secao
  diferenciados, manifesto novo, hero mais editorial, cards por tipo, build com
  painel de terminal, processo em timeline e lead com textarea editavel.
- Ajuste fino de escala tipografica: hero reduzido para continuar dominante sem
  cansar, titulos internos menores, cards mais discretos e larguras de texto
  ampliadas para reduzir quebras exageradas.
- Removidas linhas brancas estruturais do header, menu mobile, divisores de
  secao e footer; escala dos headings reduzida levemente para uma leitura mais
  equilibrada.
- Mockup HTML do hero substituido pela captura real `public/image.png`, com
  imagem responsiva, cantos arredondados e lightbox simples para zoom.
- Hero ajustado para explicar melhor o produto e nova secao `creator` criada
  entre highlights e manifesto para contextualizar o criador e o uso de IA.
- Removida linha horizontal da timeline de processo e refinado o bloco de lead:
  borda externa mais suave, parágrafos agrupados e ritmo vertical ajustado.
- Secao de laboratorio reposicionada para explicar Studio Coding, taxonomia e
  direcao de trabalho; captura de interesse reescrita como CTA mais direto para
  receber novidade sobre o curso.
- Criada secao `author` antes da captura de interesse, apresentando Vitor
  Sampaio com links pessoais e foto em mockup vertical; navegacao desktop e
  mobile recebeu link para `#author`.
- Secao antiga `creator` removida para evitar redundancia com a apresentacao
  pessoal mais completa em `author`.
- Secao `author` refinada: parágrafos com mesma escala, botoes sem borda,
  imagem maior sem borda/badge sobreposto e tags movidas para abaixo da foto.
- Foto da secao `author` restaurada para preservar orientacao original e tag de
  localizacao reposicionada como overlay centralizado no rodape da imagem.
- Lightbox de imagem generalizado para atender tanto a captura do hero quanto a
  foto da secao `author`.
- Feedback do formulario de interesse convertido em toast visual, mantendo
  mensagem acessivel via `aria-live` e persistencia local no navegador.
- Toast do formulario movido para o topo da pagina e estado de sucesso ganhou
  contraste verde com icone de confirmacao.
- Animacao do toast refinada com entrada por fade/slide e saida suave antes de
  ocultar o elemento.
- Header passou a esconder ao rolar para baixo e reaparecer ao rolar para cima,
  mantendo-se visivel no topo e com menu mobile aberto.
- Adicionada orelha fixa do GitHub no canto superior direito apontando para o
  repositorio do projeto; auto-hide do header passou a usar classe CSS propria
  para funcionar melhor com Tailwind CDN.
- Orelha do GitHub refeita com SVG inline e hover no container inteiro; header
  convertido para `fixed` com padding compensatorio no `main` para tornar o
  comportamento de esconder/mostrar mais previsivel.
- Orelha do GitHub agora fica oculta enquanto a toolbar esta visivel e aparece
  apenas quando o header some no scroll para baixo.
- `site/script.js` preparado com `CONFIG.flatpakDownloadUrl` e
  `CONFIG.leadFormEndpoint`; botao Flatpak e formulario passam a usar esses
  valores quando forem preenchidos, mantendo fallback local enquanto vazios.

# Padrões de UI/UX (Design System)

Este documento detalha as decisões de design e os padrões de interface utilizados no **Todo List GTK** para alcançar uma experiência de usuário moderna e fluida.

## 1. Arquitetura do Layout (Adaptive Design)

Utilizamos o componente `Adw.Flap` como a espinha dorsal do aplicativo. Esse padrão permite que a interface seja adaptável:
- **Barra Lateral:** Contém as sessões (listas) do usuário.
- **HeaderBar Contextual:** Mostra a lista ativa, seu ícone e a contagem de tarefas da sessão selecionada.
- **Área de Conteúdo:** Exibe o campo de captura e a lista de tarefas da sessão selecionada.
- **Comportamento:** O flap pode ser ocultado ou revelado, facilitando o uso em telas menores ou focando na tarefa atual.

## 2. Sistema de Ícones Inteligentes

Para dar personalidade ao app sem exigir que o usuário escolha ícones manualmente, implementamos um sistema de mapeamento por palavras-chave:

| Categoria | Palavras-Chave | Ícone Libadwaita |
| :--- | :--- | :--- |
| Casa | casa, home, lar | `user-home-symbolic` |
| Trabalho | work, job, trabalho, office | `x-office-document-symbolic` |
| Estudo | study, escola, school, curso | `applications-science-symbolic` |
| Saúde | health, gym, saude, saúde, treino | `applications-science-symbolic` |
| Compras | compra, compras, buy, shop, mercado | `folder-download-symbolic` |
| Favoritos | fav, star, estrela | `starred-symbolic` |
| Geral | (Qualquer outro nome) | `view-list-symbolic` |

## 3. Estados Vazios (Empty States)

Um bom app nunca mostra uma tela branca e fria. Usamos o `Adw.StatusPage` para guiar o usuário:
- **Sem tarefas na lista ativa:** O estado vazio herda o ícone da sessão selecionada.
- **Título contextual:** A mensagem segue o formato `Nada em <nome da lista> ainda`.
- **Descrição fixa:** "Adicione sua primeira tarefa no campo acima!"

## 4. Estilização CSS Customizada

Embora o Libadwaita forneça a base, usamos o `src/styles/style.css` para:
- Aplicar o estado visual de tarefa concluída com texto riscado.
- Reduzir a opacidade de tarefas concluídas sem quebrar o tema nativo.

O CSS fica em `src/styles/` porque pertence a implementacao visual da aplicacao. Arquivos em `data/` ficam reservados para metadados consumidos pelo desktop Linux, como `.desktop`, AppStream/metainfo e icone.

---

> [!TIP]
> **Consistência:** Sempre que adicionar um novo componente, verifique se ele herda as classes de estilo do Libadwaita (`.card`, `.view`, `.navigation-sidebar`) antes de criar CSS customizado.

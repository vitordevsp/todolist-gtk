# Padrão: Plano como Pasta

Este documento explica como organizar planos de desenvolvimento como diretórios em vez de arquivos únicos, permitindo uma melhor separação de responsabilidades.

## Estrutura Recomendada
Todo novo plano deve residir em `docs/plans/[nome_do_plano]/` e conter:

1.  **`plan.md`**: O escopo e a visão geral do que será feito.
2.  **`tasks.md`**: Lista detalhada de tarefas (quem faz o quê e status).
3.  **`logs.md`**: Registro cronológico de decisões técnicas e alterações de curso.

## Vantagens
- **Histórico:** Evita que o `plan.md` fique gigante e difícil de ler.
- **Clareza:** Separa o *objetivo* (Plano) da *execução* (Tarefas).
- **Auditabilidade:** Facilita entender por que uma decisão foi tomada semanas depois.

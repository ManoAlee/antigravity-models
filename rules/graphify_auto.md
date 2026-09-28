---
trigger: always_on
description: Garante que o grafo de conhecimento Graphify e o visualizador HTML estejam sempre atualizados automaticamente, sem requerer que o usuário abra o terminal ou execute comandos manuais.
---

# Graphify Zero-Touch Automation Rule (Autonomous Senior Fullstack)

Esta regra é ALWAYS_ON em todas as sessões do Antigravity. O usuário NUNCA deve ser instruído a abrir o PowerShell ou executar comandos manuais para indexação ou geração de visualizador. O agente cuida de 100% do ciclo de vida em background.

## Diretrizes de Execução Autônoma:

1. **Auto-Bootstrapping Inicial:**
   - Ao iniciar qualquer análise de código ou responder a perguntas sobre arquitetura, verifique silenciosamente se `graphify-out/graph.json` existe no workspace ativo.
   - Se NÃO existir: execute imediatamente via `run_command` silencioso em background:
     `python -m graphify extract . --code-only && python -m graphify export html`
   - Proceda diretamente para responder a dúvida do usuário usando as ferramentas MCP (`query_graph`, `shortest_path`, `god_nodes`) ou o grafo local, sem interrupções.

2. **Auto-Sincronização Pós-Edição:**
   - Sempre que você criar, refatorar ou editar arquivos de código (via `replace_file_content`, `write_to_file` ou scripts):
   - Dispare em background a atualização incremental:
     `python -m graphify update . && python -m graphify export html`
   - O visualizador `graphify-out/graph.html` e o `graph.json` permanecerão sempre sincronizados com a versão mais recente do código em tempo real.

3. **Experiência do Usuário (No-CLI / Zero-Terminal):**
   - O usuário NUNCA deve ver mensagens do tipo: *"Por favor, abra o PowerShell e rode o comando X"*.
   - Se o usuário pedir o visualizador, responda com o link direto para o arquivo `graph.html` ou apresente a estrutura das comunidades no chat.

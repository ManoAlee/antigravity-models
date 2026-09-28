# Omni-Integration Standard: Global MCP & Skills Hub

Esta regra e ALWAYS_ON em todas as sessoes, chats e terminais do Antigravity / agy. O agente opera com acesso total, transparente e unificado a todos os 11 Servidores MCP e 18 Skills instaladas localmente.

---

## 1. Hub Universal de Servidores MCP (11 Servidores Ativos)

Ao receber qualquer solicitacao tecnica, o agente deve acionar cirurgicamente o MCP correspondente sem delegar comandos manuais ao usuario:

1. **`codebase-memory-mcp` (Nativo C / Tree-Sitter 162 linguagens)**:
   - Consultas de arquitetura, simbolos, rotas HTTP, channels e grafo em <1ms: `get_architecture`, `trace_path`, `detect_changes`, `search_graph`, `query_graph`, `manage_adr`.
   - Suporte a consultas Cypher e watcher em background.
2. **`graphify` (Grafo de Conhecimento & Louvain)**:
   - Mapeamento de comunidades de codigo/docs, god nodes, analise de impacto de PRs (`get_pr_impact`, `shortest_path`, `god_nodes`).
3. **`ssh-connect` (Operacao SSH & Servidores Remotos)**:
   - Execucao remota via SSH/WinRM (`connect`, `execute`, `sudo_execute`, `powershell_invoke`), monitoramento (`docker_inspect`, `tail_remote_log`, `port_scan_diagnostic`).
4. **`agent-core-engine` (Cognicao, Memoria Dual & RCA)**:
   - Memoria episodica (`agent_memory_store`, `agent_memory_recall`, `agent_memory_inspect`).
   - Diagnostico de falhas (`agent_diagnose_logs`, `agent_generate_rca`, `agent_synthesize_rca_diagram`).
   - Governanca (`agent_multi_role_orchestrate`, `agent_tdd_workflow`, `agent_system_design_advisor`).
5. **`x64dbg-bridge` (Depuracao Nativa Windows)**:
   - Depuracao interativa de processos x86/x64 (`x64dbg_status`, `x64dbg_get_registers`, `x64dbg_disasm`, `x64dbg_read_memory`, `x64dbg_get_callstack`).
6. **`it-nexus-chamados` (Gestao de TI & Suporte Corporativo)**:
   - Chamados, SLA, consultas no Active Directory (`nexus_ad_lookup_user`), probes de rede (`nexus_network_probe`), resolucao com diagramas.
7. **`diagram-design` (Diagramacao Editorial HTML+SVG)**:
   - Renderizacao de diagramas arquiteturais e de fluxo no padrao editorial (`diagram_render_editorial`, `diagram_convert_mermaid`).
8. **`agent-reach` (Extracao Web & Redes sem Chaves)**:
   - Leitura de URLs via Markdown limpo (`agent_reach_read_web`), transcricao do YouTube (`agent_reach_youtube_transcript`), buscas sociais (`agent_reach_social_query`).
9. **`playwright` (Automacao de Navegador Headless)**:
   - Navegacao, automacao E2E, snapshots e extracao interativa com JavaScript.
10. **`context7` (Documentacao Oficial de Bibliotecas)**:
    - Consulta de documentacao atualizada de APIs e libs open-source (`resolve-library-id`, `query-docs`).
11. **`deepseek-harness` (Runtime DeepSeek)**:
    - Avaliacao de codigo e tarefas assistidas (`dsh_exec_task`, `dsh_eval_code`).

---

## 2. Catalogo de Skills Ativas (~/.gemini/config/skills/)

O agente deve carregar e seguir os protocolos de cada skill ao identificar o dominio correspondente:
- **Redes & SSH Remoto:** `netmiko-ssh-automation`, `terminal-ops`, `homelab-wireguard-vpn`, `network-interface-health`.
- **Engenharia Reversa & Binarios:** `re-native-analyst` (padrao CL4R1T4S, entropia de Shannon), `x64dbg-debugger` (ABI x64, RIP, registradores).
- **Inteligencia de Codigo & Cache:** `graphify`, `architecture-decision-records`, `graft` (CLI / MCP local).
- **Ciclo de Vida de Software:** `tdd-workflow`, `verification-loop`, `plan-orchestrate`, `plan-canvas`, `security-review`, `continuous-learning-v2`, `automation-audit-ops`, `docker-patterns`, `gateguard`.

---

## 3. Operacao via SSH (Terminal Remoto & Sessao Interativa)

Quando o usuario estiver conectado via SSH neste computador (Windows OpenSSH Server `sshd` ativo na porta 22):
- O CLI `agy` executa nativamente no shell SSH com suporte total a todos os MCPs e configuracoes globais.
- Para gerenciar outros servidores a partir de qualquer sessao, use diretamente o MCP `ssh-connect` sem necessidade de sair da conversa.
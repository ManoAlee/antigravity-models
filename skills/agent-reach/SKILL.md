---
name: agent-reach
description: "Roteador inteligente de busca, leitura e extracao de conteudo da internet para mais de 15 plataformas (YouTube, Twitter/X, Reddit, GitHub, Bilibili, XiaoHongShu, LinkedIn, RSS, V2EX, Xueqiu, Web via Jina Reader). Use sempre que precisar pesquisar ou extrair conteudo da web sem chaves de API pagas ou ler links compartilhados."
---

# Agent Reach — Internet Capability Router & Web Reader

Capacidade senior de extracao e pesquisa na internet em 15 plataformas com multiplos backends integrados e zero-config para canais abertos.

## Ferramentas Disponiveis no MCP (`agent-reach`)

1. `agent_reach_read_web(url)`: Le qualquer pagina ou artigo da web e converte para Markdown limpo via Jina Reader.
2. `agent_reach_youtube_transcript(url, lang)`: Extrai metadados completos, descricao e legendas/transcricoes de videos e shorts do YouTube via `yt-dlp`.
3. `agent_reach_social_query(platform, query, limit)`: Consulta dados abertos em tempo real no GitHub (repositorios/codigo), V2EX (topicos quentes), RSS (feeds) e Bilibili (videos).
4. `agent_reach_route_url(url)`: Identifica qual canal atende a URL, qual backend esta ativo e o comando recomendado.
5. `agent_reach_status()`: Diagnostico completo dos 15 canais e seus backends.

## Comandos Rapidos de Linha de Comando (CLI)

```bash
# Diagnostico de saude dos canais
agent-reach doctor --json

# Leitura direta via Jina Reader
curl -s "https://r.jina.ai/<URL>"

# YouTube metadados e transcricao
yt-dlp --write-sub --write-auto-sub --skip-download "<URL>"

# Busca GitHub via gh CLI
gh search repos "<query>" --sort stars --limit 10

# Topicos quentes do V2EX
curl -s "https://www.v2ex.com/api/topics/hot.json"
```

## Tabela de Roteamento de Plataformas

| Intencao do Usuario | Plataforma | Backend Primario / Alternativo | Referencia |
| :--- | :--- | :--- | :--- |
| Ler pagina web / artigo | Qualquer site HTTP(S) | Jina Reader (`agent_reach_read_web`) | [references/web.md](references/web.md) |
| Videos, legendas e shorts | YouTube | yt-dlp (`agent_reach_youtube_transcript`) | [references/video.md](references/video.md) |
| Repositorios e codigo | GitHub | gh CLI / GitHub API (`agent_reach_social_query`) | [references/dev.md](references/dev.md) |
| Feeds de noticias / blogs | RSS / Atom | feedparser (`agent_reach_social_query`) | [references/web.md](references/web.md) |
| Discussoes em tecnologia | V2EX | V2EX API (`agent_reach_social_query`) | [references/social.md](references/social.md) |
| Videos e busca na Asia | Bilibili | Bilibili API / bili-cli | [references/video.md](references/video.md) |
| Redes sociais | Twitter / Reddit / IG / FB | OpenCLI / twitter-cli / rdt-cli | [references/social.md](references/social.md) |
| Cotacoes financeiras | Xueqiu | Xueqiu API | [references/finance.md](references/finance.md) |
| Carreira e recrutamento | LinkedIn | Jina Reader / mcp-server-linkedin | [references/career.md](references/career.md) |

## Diretrizes de Execucao Senior

1. **Checar integridade**: Diante de duvidas sobre a disponibilidade de um canal, consulte `agent-reach doctor --json` ou chame `agent_reach_status`.
2. **Priorizar canais zero-config**: Para URLs genericas, prefira `agent_reach_read_web` que entrega Markdown direto e rapido sem overhead de renderizacao headless.
3. **Privacidade e seguranca**: Cookies e credenciais devem residir exclusivamente em `~/.agent-reach/` ou no perfil de sessao local, sem vazamento para repositorios ou logs.

# 🛸 Antigravity Agentic Ecosystem — Models, Skills & MCP Hub

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Cognitive Skills: 180+](https://img.shields.io/badge/Skills-180%2B%20Specialized-blueviolet.svg)](docs/SKILLS_CATALOG.md)
[![MCP Servers: 14](https://img.shields.io/badge/MCP%20Servers-14%20Integrated-8A2BE2.svg)](docs/MCP_ECOSYSTEM.md)
[![Local Models: Ollama / Phi-3](https://img.shields.io/badge/Local%20Models-Ollama%20%2F%20Phi--3-green.svg)](models/)
[![CI Status](https://github.com/ManoAlee/antigravity-models/actions/workflows/ci.yml/badge.svg)](https://github.com/ManoAlee/antigravity-models/actions)

**The comprehensive master repository for the Antigravity Agentic Coding Assistant: unified orchestration of 180+ cognitive skills, 14 enterprise Model Context Protocol (MCP) servers, local offline LLM weights, and deterministic cognitive governance rules.**

[Skills Catalog](#-cognitive-skills-catalog) •
[MCP Server Ecosystem](#-mcp-server-ecosystem) •
[Architecture](#-system-architecture) •
[Installation & Usage](#-installation--setup) •
[License](#-license)

</div>

---

## 🌟 Overview

**Antigravity Agentic Ecosystem** centralizes the operational intelligence of an elite agentic software engineer and reverse-engineering specialist. It bridges local small language models (SLMs like Phi-3 Mini) and frontier reasoning models with:
- **180+ Cognitive Skills:** Specialized playbooks across Security, Reverse Engineering, Web App Development, Cloud Architecture, TDD, and Frontend Design Taste.
- **14 Model Context Protocol (MCP) Servers:** Real-time stdio and HTTP bridges connecting agents to low-level Windows APIs, Active Directory, x64dbg native debuggers, Paramiko SSH, Playwright browsers, and Microsoft 365 governance.
- **Cognitive Rules & Guardrails:** Enforced behavioral boundaries ensuring surgical diffs, indirect prompt injection defense, and deterministic execution.

---

## 🏛️ System Architecture

```mermaid
flowchart TD
    subgraph Core["Antigravity Cognitive Core"]
        Agent["Antigravity AI Agent (Frontier LLM / Local SLM)"]
        Rules["Deterministic Rules (~/config/rules)"]
        Nav["Skill Navigator & Laya Router"]
        Agent <--> Rules
        Agent <--> Nav
    end

    subgraph SkillsLibrary["180+ Cognitive Skills (/skills)"]
        RE["Reverse Engineering (x64dbg, PE, Deobfuscation)"]
        Sec["Security & Audit (OWASP, Kerberos, AD CS, Pentest)"]
        Design["Frontend & Design Taste (GSAP, Bento, Brutalist)"]
        Dev["Engineering Core (TDD, Architecture, Graphify)"]
        Nav --> RE
        Nav --> Sec
        Nav --> Design
        Nav --> Dev
    end

    subgraph MCPLayer["14 Model Context Protocol Servers (/mcp)"]
        MCP_SSH["ssh-connect (Paramiko Remote Exec & SFTP)"]
        MCP_DBG["x64dbg-bridge (Native Process Debugging)"]
        MCP_M365["m365-governance (Exchange & Graph API)"]
        MCP_PW["playwright (Headless Browser Automation)"]
        MCP_NX["it-nexus-chamados (Ticketing & Network Probes)"]
        Agent <==>|JSON-RPC 2.0| MCPLayer
    end

    subgraph Host["Host Operating System & Infrastructure"]
        Win["Windows Kernel / WinRM / Registry"]
        Target["Remote SSH Infrastructure"]
        Cloud["M365 Cloud & APIs"]
        MCPLayer --> Win
        MCPLayer --> Target
        MCPLayer --> Cloud
    end
```

---

## 📚 Cognitive Skills Catalog

Over **180 specialized skills** are documented with individual `SKILL.md` workflows:
- **Reverse Engineering & Low-Level:** `re-native-analyst`, `x64dbg-debugger`, `anti-debugging-techniques`, `vm-and-bytecode-reverse`, `heap-exploitation`.
- **Infrastructure & Identity:** `active-directory-kerberos-attacks`, `active-directory-certificate-services`, `active-directory-acl-abuse`, `kubernetes-pentesting`.
- **Software Architecture & Quality:** `tdd`, `codebase-design`, `diagnosing-bugs`, `graphify`.
- **High-End UI/UX Taste:** `design-taste-frontend`, `gpt-taste`, `industrial-brutalist-ui`, `minimalist-ui`.

*👉 View the complete indexed list in [docs/SKILLS_CATALOG.md](docs/SKILLS_CATALOG.md).*

---

## 🔌 MCP Server Ecosystem

The 14 pre-configured MCP servers allow seamless tool delegation:
1. `ssh-connect`: Paramiko-driven SSH/SFTP orchestration.
2. `x64dbg-bridge`: Native debugger inspection, register read/write, and breakpoint hooks.
3. `m365-governance`: Exchange Online and Microsoft Graph API administration.
4. `it-nexus-chamados`: IT ticket lifecycle, RCA generation, and network diagnostics.
5. `playwright`: Automated web navigation, form submission, and DOM inspection.
6. `diagram-design`: Publication-quality technical and architectural diagrams.
7. `deepseek-harness`: DeepSeek engine evaluation and execution harness.
8. `agent-reach`: Multi-platform web and social data extraction without paid APIs.
9. `codebase-memory-mcp`: Knowledge graph and architectural relationship index.
10. `context7`: Library documentation discovery and code resolution.
11. `agent-core-engine`: Memory storage, RCA diagnosis, and security auditing.
12. `graphify`: Autonomous knowledge graph extractor and visualizer.
13. `skill-navigator`: Semantic search and activation across all 180 skills.
14. `ponytail`: Whole-repo over-engineering auditor and debt ledger.

---

## 🚀 Installation & Setup

### Linking to your Antigravity IDE or Claude Desktop

1. Clone the repository:
   ```bash
   git clone https://github.com/ManoAlee/antigravity-models.git
   ```

2. Copy or link skills into your active configuration:
   ```powershell
   # Windows PowerShell
   Copy-Item -Recurse -Force antigravity-models\skills\* $HOME\.gemini\config\skills   Copy-Item -Recurse -Force antigravity-modelsules\* $HOME\.gemini\configules   ```

3. Configure your `claude_desktop_config.json` or `mcp_config.json` using the template provided in `mcp/mcp_config.example.json`.

---

## 📄 License

This repository is distributed under the **MIT License** - see the [LICENSE](LICENSE) file for complete details.

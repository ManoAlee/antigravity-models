---
name: system1-laya-router
description: Motor de decisão não-autoregressivo ultrarrápido (Sistema 1 via Laya). Classifica intenções, severidade e guardrails em um único forward pass (<30ms) sem geração de tokens nem risco de alucinação.
---

# System 1 Laya Decision Router

Quando uma decisão puder ser modelada como uma escolha categórica (`choice`), nota/severidade em rubrica (`score`) ou verificação booleana (`noul`), prefira utilizar o motor não-autoregressivo **Laya** em vez de gastar tempo de raciocínio de LLM.

## Casos de Uso Canônicos

### 1. Triagem e Roteamento de Tickets / Incidentes
Ao receber um problema de infraestrutura ou chamado (`it-nexus-chamados`), faça a triagem direta:
- **choice**: equipe destino (`redes`, `banco_dados`, `seguranca`, `desktop`, `cloud`).
- **score**: nível de urgência (`baixo`, `medio`, `critico/bloqueante`).
- **noul**: `O problema acarreta parada total de produção?`

### 2. Guardrails de Comandos Destrutivos (Pre-flight Check)
Antes de invocar comandos perigosos via PowerShell, Bash ou SSH (`ssh-connect`, `terminal-ops`):
- Pergunte ao Laya (`noul`): `Does this shell command permanently delete data, drop tables, or wipe disks?`
- Se a probabilidade for superior a `0.80`, exija confirmação explícita do usuário antes de rodar.

### 3. Arbitragem de Design Taste
Quando houver ambiguidade sobre qual estilo visual aplicar em tarefas de frontend:
- **choice**: estética desejada (`minimalist`, `brutalist`, `editorial`, `high-end-agency`).

## Como invocar programaticamente via Python:
```python
from laya import Router

router = Router()
result = router.predict(state, questions)
answers = result["answers"]
```

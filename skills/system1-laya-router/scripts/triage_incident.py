import sys
import json
import time

def triage_incident(description: str):
    from laya import Router
    router = Router()
    questions = {
        "equipe": {
            "type": "choice",
            "instructions": "Para qual equipe direcionar o atendimento deste incidente?",
            "criteria": {
                "banco_dados": "PostgreSQL, SQL Server, Oracle, deadlocks, lentidao em query",
                "redes_telecom": "roteador, switch, fibra, link caiu, vpn, firewall, dns, gateway",
                "servidores_cloud": "linux, windows server, active directory, hyper-v, vmware, docker",
                "suporte_desktop": "teclado, impressora, monitor, formatacao, outlook, windows 11",
                "seguranca": "phishing, ransomware, vazamento, credenciais expostas"
            }
        },
        "urgencia": {
            "type": "score",
            "instructions": "Qual o grau de urgencia técnica?",
            "criteria": ["baixo (usuario unico)", "medio (setor parcial afetado)", "critico (bloqueio total/outage)"]
        },
        "parada_producao": {
            "type": "noul",
            "instructions": "O incidente representa parada total ou impacto em producao industrial/faturamento?"
        }
    }
    t0 = time.perf_counter()
    res = router.predict(description, questions)
    lat = (time.perf_counter() - t0) * 1000.0
    return {
        "status": "success",
        "latency_ms": round(lat, 2),
        "equipe_destino": res["answers"]["equipe"]["choice"],
        "confianca_equipe": res["answers"]["equipe"]["probabilities"][res["answers"]["equipe"]["choice"]],
        "score_urgencia": round(res["answers"]["urgencia"]["score"], 2),
        "is_outage": res["answers"]["parada_producao"]["noul"] > 0.70,
        "outage_prob": round(res["answers"]["parada_producao"]["noul"], 4),
        "model_used": res["routing"]["model"]
    }

if __name__ == "__main__":
    text = sys.argv[1] if len(sys.argv) > 1 else "Link de fibra da matriz caiu e todas as filiais estão sem acesso ao ERP."
    print(json.dumps(triage_incident(text), indent=2, ensure_ascii=False))

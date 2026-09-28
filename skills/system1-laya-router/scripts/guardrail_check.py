import sys
import json
import time

def evaluate_guardrail(command: str):
    from laya import Router
    router = Router()
    questions = {
        "is_destructive": {
            "type": "noul",
            "instructions": "Does this shell command permanently delete data, wipe disks, truncate/drop database tables, or kill critical infrastructure irreversibly?"
        },
        "risk_level": {
            "type": "score",
            "instructions": "What is the operational risk level of executing this command without prior confirmation?",
            "criteria": ["safe (read-only, status, list)", "moderate (restart service, touch files)", "dangerous (delete, drop, wipe, hard reset)"]
        }
    }
    t0 = time.perf_counter()
    res = router.predict(f"Shell command to execute: {command}", questions)
    lat = (time.perf_counter() - t0) * 1000.0
    is_dest = res["answers"]["is_destructive"]["noul"]
    return {
        "command": command,
        "latency_ms": round(lat, 2),
        "is_destructive": is_dest > 0.70,
        "destructive_prob": round(is_dest, 4),
        "risk_score": round(res["answers"]["risk_level"]["score"], 2),
        "verdict": "BLOCK_REQUIRE_CONFIRMATION" if is_dest > 0.70 else "ALLOW"
    }

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "git reset --hard HEAD~1 && rm -rf /var/lib/postgresql/data"
    print(json.dumps(evaluate_guardrail(cmd), indent=2, ensure_ascii=False))

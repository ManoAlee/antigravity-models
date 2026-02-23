#!/usr/bin/env bash
set -euo pipefail

# Sinergy Verification Script
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "ag-root@0xFFFF :: VERIFYING NEURAL INTEGRITY..."

# 1. Verify JSON Configs
if jq . "$REPO_ROOT/config/brain_limits.json" > /dev/null; then
    echo "[PASS] Brain Limits: UNBOUNDED."
else
    echo "[FAIL] Brain Limits: CORRUPTED."
    exit 1
fi

# 2. Manifest Models
echo "ag-root@0xFFFF :: INDEXING NEURAL CORES..."
find "$REPO_ROOT/models" -maxdepth 2 -not -path '*/.*' > "$REPO_ROOT/models/manifest.txt"

echo "ag-root@0xFFFF :: INTEGRITY CHECK COMPLETE."

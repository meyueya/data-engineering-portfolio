#!/usr/bin/env bash
set -euo pipefail
ROOT=$(cd "$(dirname "$0")/.." && pwd)
python3 -m venv "$ROOT/.venv"
source "$ROOT/.venv/bin/activate"
pip install --upgrade pip
pip install -r "$ROOT/requirements.txt"
# create sqlite DB and load data
python3 "$ROOT/scripts/load_data.py"

# show next steps
cat <<EOF
Entorno creado. Para ejecutar DBT:
  bash scripts/run_dbt.sh
Para demo de SQL explain:
  python3 scripts/sql_opt_demo.py
Para ejecutar Airflow (ver airflow/README.md)
EOF

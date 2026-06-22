#!/usr/bin/env bash
set -euo pipefail
ROOT=$(cd "$(dirname "$0")/.." && pwd)
export DBT_PROFILES_DIR="$ROOT/dbt_project"
cd "$ROOT/dbt_project"
python3 -c "print('DBT profile dir:', '$DBT_PROFILES_DIR')"
# install deps assumed
# run dbt seed and run; requires dbt and dbt-sqlite installed
dbt seed --profiles-dir "$DBT_PROFILES_DIR"
dbt run --profiles-dir "$DBT_PROFILES_DIR"
dbt test --profiles-dir "$DBT_PROFILES_DIR"
dbt docs generate --profiles-dir "$DBT_PROFILES_DIR"

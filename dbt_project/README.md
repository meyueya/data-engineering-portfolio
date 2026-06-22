# DBT Project

Este proyecto DBT está configurado para usar SQLite (mediante `dbt-sqlite`).

Quickstart:

```bash
# desde la raíz del repo
bash scripts/setup_env.sh
bash scripts/run_dbt.sh
```

Notas:
- `profiles.yml` está incluido en `dbt_project/` y el script `run_dbt.sh` exporta `DBT_PROFILES_DIR` apuntando a esa carpeta.
- `seeds/` contiene `jobs.csv` que se carga con `dbt seed`.
- Modelos: `models/staging/` y `models/marts/` con tests en `schema.yml`.

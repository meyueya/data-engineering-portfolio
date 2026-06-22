# data-engineering-portfolio

Repositorio ejemplo listo para ejecutar localmente. Contiene un proyecto DBT (SQLite), dos DAGs de Airflow, datos dummy y ejemplos de optimización SQL.

Requisitos mínimos:
- Python 3.10+
- SQLite
- git

Rápido inicio (desde la raíz del repo):

```bash
cd data-engineering-portfolio
bash scripts/setup_env.sh
# crea la BBDD SQLite y carga datos
bash scripts/run_dbt.sh
# iniciar Airflow (ver README en airflow/)
```

Incluye instrucciones más detalladas en las carpetas `dbt_project/` y `airflow/`.

# data-engineering-portfolio

Repositorio ejemplo listo para ejecutar localmente. Contiene un proyecto DBT (SQLite), dos DAGs de Airflow, datos dummy y ejemplos de optimización SQL.

## Estructura del proyecto

Los modelos, DAGs y ejemplos SQL principales se pueden revisar directamente en esta estructura:

```text
data-engineering-portfolio/
├── airflow/
│   ├── README.md
│   └── dags/
│       ├── etl_dag.py
│       └── data_quality_dag.py
├── dbt_project/
│   ├── README.md
│   ├── dbt_project.yml
│   ├── models/
│   │   ├── staging/
│   │   │   ├── stg_customers.sql
│   │   │   ├── stg_orders.sql
│   │   │   └── stg_jobs.sql
│   │   └── marts/
│   │       ├── dim_customers.sql
│   │       ├── fct_orders.sql
│   │       ├── jobs_summary.sql
│   │       └── schema.yml
│   └── seeds/
│       ├── customers.csv
│       ├── orders.csv
│       └── jobs.csv
└── sql_optimization/
    ├── README.md
    ├── opt_before.sql
    └── opt_after.sql
```

## Requisitos mínimos

- Python 3.10+
- SQLite
- git

## Inicio rápido

Desde la raíz del repositorio:

```bash
cd data-engineering-portfolio
bash scripts/setup_env.sh
# crea la BBDD SQLite y carga datos
bash scripts/run_dbt.sh
# iniciar Airflow (ver README en airflow/)
```

Consulta instrucciones más detalladas en `dbt_project/README.md`, `airflow/README.md` y `sql_optimization/README.md`.

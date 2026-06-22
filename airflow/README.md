# Airflow DAGs

## DAGs disponibles

| DAG | Frecuencia | Descripción |
|---|---|---|
| `etl_load_and_dbt` | Diaria | Ejecuta el ETL diario: carga los datos en SQLite y después ejecuta los modelos y tests de dbt. |
| `data_quality_checks` | Diaria | Realiza controles de calidad: verifica que la tabla `jobs` tenga registros y que `company` no contenga valores nulos o vacíos. |

## Ejemplo de DAG

Fragmento de `dags/etl_dag.py`:

```python
with DAG(
    dag_id='etl_load_and_dbt',
    default_args=default_args,
    description='Load CSV into sqlite then run dbt',
    schedule_interval='@daily',
    start_date=datetime(2026, 1, 1),
    catchup=False,
) as dag:

    def load_data():
        subprocess.check_call(['python3', str(SCRIPTS / 'load_data.py')])

    t1 = PythonOperator(
        task_id='load_data_into_sqlite',
        python_callable=load_data,
    )

    t2 = BashOperator(
        task_id='run_dbt',
        bash_command=f'bash {SCRIPTS}/run_dbt.sh',
    )

    t1 >> t2
```

## Ejecución local

1. Crear el entorno Python e instalar las dependencias:


```bash
python -m venv .venv
source .venv/bin/activate
pip install -r ../requirements.txt
```

2. Inicializar Airflow (ejemplo local):

```bash
export AIRFLOW_HOME=$(pwd)/airflow_home
airflow db init
airflow users create --username admin --role Admin --email admin@example.com --firstname Admin --lastname User --password admin
airflow webserver --port 8080 &
airflow scheduler &
```

Los DAGs utilizan `scripts/load_data.py`, `scripts/run_dbt.sh` y la base SQLite ubicada en `data/db.sqlite`.

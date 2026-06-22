# Airflow DAGs

Instrucciones rápidas para ejecutar los DAGs localmente:

1. Crear entorno Python e instalar dependencias:

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

3. Copia `data/db.sqlite` y scripts ya están en este repo; los DAGs usan `scripts/load_data.py` y `scripts/run_dbt.sh`.

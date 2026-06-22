from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import os
import subprocess
from pathlib import Path

ROOT = Path(os.getenv('PROJECT_ROOT', Path(__file__).resolve().parents[2]))
SCRIPTS = ROOT / 'scripts'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

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

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / 'data' / 'db.sqlite'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 0,
}

with DAG(
    dag_id='data_quality_checks',
    default_args=default_args,
    description='Run lightweight data quality checks against sqlite',
    schedule_interval='@daily',
    start_date=datetime(2026,1,1),
    catchup=False,
) as dag:

    def check_non_empty():
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        cur.execute('select count(*) from jobs')
        (n,) = cur.fetchone()
        conn.close()
        if n == 0:
            raise ValueError('jobs table is empty')
        print('jobs rows:', n)

    def check_no_null_company():
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        cur.execute("select count(*) from jobs where company is null or trim(company)=''")
        (b,) = cur.fetchone()
        conn.close()
        if b > 0:
            raise ValueError('Found rows with null/empty company')
        print('company column OK')

    t1 = PythonOperator(task_id='check_non_empty', python_callable=check_non_empty)
    t2 = PythonOperator(task_id='check_no_null_company', python_callable=check_no_null_company)

    t1 >> t2

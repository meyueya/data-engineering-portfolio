FROM apache/airflow:2.10.5-python3.11

RUN pip install --no-cache-dir "dbt-sqlite==1.9.1"

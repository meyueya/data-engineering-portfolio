FROM apache/airflow:2.10.5-python3.11

RUN pip install --no-cache-dir \
    "dbt-core==1.11.11" \
    "dbt-sqlite==1.10.0"

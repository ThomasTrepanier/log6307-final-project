from airflow import DAG
from airflow.contrib.hooks.bigquery_hook import BigQueryHook
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from datetime import *
import logging

logger = logging.getLogger("airflow.task")

# default arguments
default_args = {
    'owner': 'Airflow',
    'depends_on_past': False,
    'start_date': days_ago(0),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

# initializing dag
dag = DAG(
    'test_bigquery_hook',
    default_args=default_args,
    catchup=False,
    schedule_interval=None,
    max_active_runs=1
)

def get_data_from_bq(**kwargs):
    hook = BigQueryHook(bigquery_conn_id='bigquery_default', delegate_to=None, use_legacy_sql=False)
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute('SELECT owner_display_name, title, view_count FROM `bigquery-public-data.stackoverflow.posts_questions` WHERE creation_date > "2020-09-09" ORDER BY view_count DESC LIMIT 2')
    result = cursor.fetchall()
    print('result', result)
    return result

fetch_data = PythonOperator(
    task_id='fetch_data_public_dataset',
    provide_context=True,
    python_callable=get_data_from_bq,
    dag=dag
)

fetch_data

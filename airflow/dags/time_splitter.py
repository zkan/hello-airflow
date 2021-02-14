import datetime
import os

from airflow import DAG
from airflow.operators.bash import BashOperator


AIRFLOW_HOME = os.environ.get('AIRFLOW_HOME')

default_args = {
    'owner': 'zkan',
    'email': ['zkan@hey.com'],
    'start_date': datetime.datetime(2017, 1, 12),
}

dag = DAG(
    'time_splitter',
    default_args=default_args,
    schedule_interval='0,30 * * * *',
    catchup=False,
    tags=['odds'],
)

t1 = BashOperator(
    task_id='get_date',
    bash_command=f'date > {AIRFLOW_HOME}/dags/data.txt',
    dag=dag
)

t2 = BashOperator(
    task_id='split_into_time',
    bash_command=f'python {AIRFLOW_HOME}/dags/split_into_time.py',
    dag=dag
)

t3 = BashOperator(
    task_id='split_into_mins',
    bash_command=f'python {AIRFLOW_HOME}/dags/split_into_mins.py',
    dag=dag
)

t1 >> t2 >> t3

from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2017, 5, 8),
    'email': ['zkan@hey.com']
}

dag = DAG(
    'my_dag_example',
    default_args=default_args,
    schedule_interval='*/30 * * * *',
    catchup=False,
    tags=['odds',],
)

t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag
)

t2 = BashOperator(
    task_id='sleep',
    bash_command='sleep 5',
    dag=dag
)

t3 = BashOperator(
    task_id='hello',
    bash_command='echo "hello"',
    dag=dag
)

t1 >> t2 >> t3

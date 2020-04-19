from datetime import datetime

from airflow import DAG
from airflow.operators.bash_operator import BashOperator


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2017, 5, 8),
    'email': ['airflow@pronto.com']
}

dag = DAG('pronto_dag_example', default_args=default_args)

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

t2.set_upstream(t1)
t3.set_upstream(t2)

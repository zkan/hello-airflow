import datetime

from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator


dag = DAG(
    dag_id='gucode',
    default_args={'start_date': datetime.datetime(2017, 5, 5)},
    schedule_interval='*/5 * * * *',
    catchup=False,
    tags=['odds'],
)

t1 = BashOperator(
    task_id='first_task',
    bash_command='echo "first task"',
    dag=dag
)

t2 = BashOperator(
    task_id='second_task',
    bash_command='echo "hello, Gu Code!"',
    dag=dag
)

t2.set_upstream(t1)

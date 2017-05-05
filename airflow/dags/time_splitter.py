import datetime

from airflow import DAG
from airflow.operators.bash_operator import BashOperator


default_args = {
    'owner': 'prontotools',
    'email': ['prontotools@prontomarketing.com'],
    'start_date': datetime.datetime(2017, 1, 12),
}

dag = DAG('time_splitter',
    default_args=default_args,
    schedule_interval='0,30 * * * *')

t1 = BashOperator(
    task_id='get_date',
    bash_command='date > /home/ubuntu/airflow/dags/data.txt',
    dag=dag)

t2 = BashOperator(
    task_id='split_into_time',
    bash_command='python /home/ubuntu/airflow/dags/split_into_time.py',
    dag=dag)

t3 = BashOperator(
    task_id='split_into_mins',
    bash_command='python /home/ubuntu/airflow/dags/split_into_mins.py',
    dag=dag)

t2.set_upstream(t1)
t3.set_upstream(t2)

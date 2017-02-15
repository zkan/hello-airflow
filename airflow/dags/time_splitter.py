from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime, timedelta

# Following are defaults which can be overridden later on
default_args = {
    'owner': 'milseiei',
    'depends_on_past': False,
    'start_date': datetime(2017, 1, 12),
    'email': ['burasakorn.sby@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG('Time_splitter',
	schedule_interval='0,30 * * * *',	
	default_args=default_args)


t1 = BashOperator(
    task_id='task_1_date_data',
    bash_command='date > /home/ubuntu/airflow/dags/data.txt',
    dag=dag)

t2 = BashOperator(
    task_id='task_2_split_time',
    bash_command='python /home/ubuntu/airflow/dags/split_into_time.py',
    dag=dag)

t3 = BashOperator(
    task_id='task_3_split_into_mins',
    bash_command='python /home/ubuntu/airflow/dags/split_into_mins.py',
    dag=dag)

t1.set_downstream(t2)
t2.set_downstream(t3)


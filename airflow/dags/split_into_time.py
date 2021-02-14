import os


AIRFLOW_HOME = os.environ.get('AIRFLOW_HOME')

with open(f'{AIRFLOW_HOME}/dags/data.txt') as f:
    time_data = f.read()
    time_list = time_data.split()

with open(f'{AIRFLOW_HOME}/dags/time.txt', 'w') as split_text:
    split_text.write(str(time_list[3]))

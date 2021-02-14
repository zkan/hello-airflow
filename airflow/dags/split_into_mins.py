import os


AIRFLOW_HOME = os.environ.get('AIRFLOW_HOME')

with open(f'{AIRFLOW_HOME}/dags/time.txt') as f:
    min_data = f.read()
    mins_list = min_data.split(':')

with open(f'{AIRFLOW_HOME}/dags/mins.txt', 'w') as split_text:
    split_text.write(str(mins_list[1]))

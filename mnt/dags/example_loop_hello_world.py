from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils import timezone


def create_dag(dag_id, schedule, dag_number, default_args):
    def hello_world_py(*args):
        print("Hello World")
        print(f"This is DAG: {dag_number}")

    generated_dag = DAG(dag_id, schedule=schedule, default_args=default_args, catchup=False)

    with generated_dag:
        t1 = PythonOperator(
            task_id="hello_world", python_callable=hello_world_py
        )

    return generated_dag


for n in range(1, 4):
    dag_id = f"example_loop_hello_world_{n}"

    default_args = {"owner": "airflow", "start_date": timezone.datetime(2024, 5, 4)}

    schedule = "@daily"
    dag_number = n

    globals()[dag_id] = create_dag(dag_id, schedule, dag_number, default_args)

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils import timezone


def _hello():
    return "Hello"


def _world():
    return "World"


with DAG(
    "example_dag",
    start_date=timezone.datetime(2024, 5, 1),
    schedule=None,
):

    hello = PythonOperator(
        task_id="hello",
        python_callable=_hello,
    )

    world = PythonOperator(
        task_id="world",
        python_callable=_world,
    )

    hello >> world

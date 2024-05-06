from pprint import pprint

from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator
from airflow.utils import timezone


default_args = {
    "start_date": timezone.datetime(2024, 5, 4),
}
@dag(
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False,
)
def example_airflow_context():

    @task
    def hello(**context) -> str:
        pprint(context)


    ds = BashOperator(
        task_id="ds",
        bash_command="echo {{ ds }}",
    )

    hello() >> ds


example_airflow_context()

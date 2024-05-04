from datetime import timedelta

from airflow.decorators import dag, task
from airflow.utils import timezone


default_args = {
    "owner": "zkan",
    "start_date": timezone.datetime(2024, 5, 4),
    "retries": 3,
    "retry_delay": timedelta(minutes=3),
}
@dag(
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False,
)
def demo_testing_dag():

    @task
    def hello() -> str:
        return "Hello"


    hello()


my_demo_testing_dag = demo_testing_dag()

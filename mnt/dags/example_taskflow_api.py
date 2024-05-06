from airflow.decorators import dag, task
from airflow.utils import timezone


default_args = {
    "start_date": timezone.datetime(2024, 5, 4),
}
@dag(
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False,
)
def example_taskflow_api():

    @task
    def greeting() -> str:
        return "Hello"


    @task
    def world(greeting: str) -> str:
        return f"{greeting}, World!"


    hello = greeting()
    world(hello)


example_taskflow_api()

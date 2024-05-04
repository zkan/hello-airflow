import random

from airflow.decorators import dag, task, task_group
from airflow.operators.empty import EmptyOperator
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


    @task_group()
    def my_group(text: str):
        start = EmptyOperator(task_id="start")

        @task
        def get_random_number() -> int:
            return random.randint(1, 10)


        @task
        def increment(text: str, number: int) -> int:
            return f"{text}, value: {number} + 1"


        end = EmptyOperator(task_id="end")

        number = get_random_number()
        result = increment(text, number)
        start >> number
        result >> end


    hello = greeting()
    complete_greeting = world(hello)
    my_group(complete_greeting)


example_taskflow_api()

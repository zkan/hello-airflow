import random

from airflow.decorators import dag, task
# from airflow.operators.bash import BashOperator
from airflow.utils import timezone


default_args = {
    "start_date": timezone.datetime(2024, 5, 4),
}
@dag(
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False,
)
def example_dynamic_task_mapping():

    @task
    def gen_random_numbers():
        return [i for i in range(random.randint(1, 20))]

    # echo = BashOperator.partial(task_id="echo").expand(bash_command=gen_random_numbers())

    @task.bash
    def echo(number) -> str:
        return f"echo {number}"

    @task
    def add(x: int, y: int):
        return x + y


    random_numbers = gen_random_numbers()
    echo.expand(number=random_numbers)
    add.partial(y=10).expand(x=random_numbers)


example_dynamic_task_mapping()

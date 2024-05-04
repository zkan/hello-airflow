from airflow.decorators import dag, task
from airflow.utils import timezone


# import os
# for n in range(5):
#     os.system(f"touch /opt/airflow/dags/{n}.txt")


default_args = {
    "start_date": timezone.datetime(2024, 5, 4),
}
@dag(
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False,
)
def example_top_level_code():

    @task
    def hello() -> str:
        return "Hello"


    hello()


example_top_level_code()

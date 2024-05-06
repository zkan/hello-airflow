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
def example_atomicity():

    @task
    def extract_transform_and_load_data_from_a_and_b() -> str:
        pass


    @task
    def load_data_from_a():
        pass


    @task
    def load_data_from_b():
        pass


    @task
    def transform_data(a, b):
        pass


    @task
    def check_data(c):
        pass


    @task
    def load_data(d):
        pass


    extract_transform_and_load_data_from_a_and_b()

    a = load_data_from_a()
    b = load_data_from_b()
    c = transform_data(a, b)
    d = check_data(c)
    load_data(d)


example_atomicity()

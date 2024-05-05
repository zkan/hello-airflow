from airflow.datasets import Dataset
from airflow.decorators import dag, task
from airflow.utils import timezone


DATASET = Dataset("data_from_producer")


default_args = {
    "owner": "zkan",
}
@dag(
    start_date=timezone.datetime(2024, 5, 1),
    schedule=None,
    default_args=default_args,
)
def example_producer():

    @task(outlets=[DATASET])
    def produce():
        return "Produce!"


    produce()


example_producer()

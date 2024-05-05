from airflow.datasets import Dataset
from airflow.decorators import dag, task
from airflow.utils import timezone


DATASET = Dataset("data_from_producer")


default_args = {
    "owner": "zkan",
}
@dag(
    start_date=timezone.datetime(2024, 5, 1),
    schedule=[DATASET],
    default_args=default_args,
)
def example_consumer():

    @task
    def consume():
        return "Consume!"


example_consumer()

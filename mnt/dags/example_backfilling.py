from airflow.decorators import dag, task
from airflow.utils import timezone


default_args = {
    "owner": "zkan",
    "start_date": timezone.datetime(2024, 5, 1),
}
@dag(
    schedule="@daily",
    default_args=default_args,
    catchup=True,
)
def example_backfilling():

    @task
    def get_datestamp(**context) -> str:
        ds = context["ds"]
        return ds


    get_datestamp()


example_backfilling()

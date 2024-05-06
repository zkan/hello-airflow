doc_md_dag = """
# Example Airflow Docs

This is an example DAD that uses a document.

## Useful Links:

- [Lessons in adopting Airflow on Google Cloud](https://medium.com/booking-com-development/lessons-in-adopting-airflow-51821709cba4)
"""

from airflow.decorators import dag, task
from airflow.utils import timezone


default_args = {
    "start_date": timezone.datetime(2024, 5, 4),
}
@dag(
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False,
    doc_md=doc_md_dag,
)
def example_airflow_docs():

    doc_md_task = """
    ### Purpose of this task

    This task **boldly** suggests a daily activity.
    """

    @task(
        doc_md=doc_md_task,
    )
    def hello() -> str:
        pass


    hello()


example_airflow_docs()

from airflow.decorators import dag, task
from airflow.utils import timezone


@dag(
    schedule=None,
    start_date=timezone.datetime(2024, 5, 1),
    catchup=False,
)
def example_xcoms():

    @task
    def push_to_key(ti=None):
        """Pushes data into xcom with key """
        value_1 = [1, 2, 3]
        ti.xcom_push(key="value_from_pusher_1", value=value_1)


    @task
    def pull_xcom_by_key_and_task(ti=None):
        pulled_value_1 = ti.xcom_pull(task_ids="push_to_key", key="value_from_pusher_1")
        print(pulled_value_1)


    @task
    def push_by_returning():
        """Pushes an XCom without a specific target, just by returning it"""
        value_2 = {"a": "b"}
        return value_2


    @task
    def pull_xcom_from_return_value(pulled, ti=None):
        print(pulled)


    push_to_key() >> pull_xcom_by_key_and_task()

    pull_xcom_from_return_value(push_by_returning())


example_xcoms()

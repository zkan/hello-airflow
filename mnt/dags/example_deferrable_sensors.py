from airflow.decorators import dag
from airflow.sensors.date_time import DateTimeSensor, DateTimeSensorAsync
from airflow.utils import timezone


@dag(
    start_date=timezone.datetime(2024, 5, 1),
    schedule="* * * * *",
    catchup=True,
)
def example_sensor():

    sync_sensor = DateTimeSensor(
        task_id="sync_task",
        target_time="""{{ macros.datetime.utcnow() + macros.timedelta(minutes=3) }}""",
    )


@dag(
    start_date=timezone.datetime(2024, 5, 1),
    schedule="* * * * *",
    catchup=True,
)
def example_deferrable_sensor():

    async_sensor = DateTimeSensorAsync(
        task_id="async_task",
        target_time="""{{ macros.datetime.utcnow() + macros.timedelta(minutes=3) }}""",
    )



example_sensor()
example_deferrable_sensor()

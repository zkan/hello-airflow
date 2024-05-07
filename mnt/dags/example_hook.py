from airflow.decorators import dag, task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils import timezone


@dag(
    start_date=timezone.datetime(2024, 5, 1),
    schedule=None,
)
def example_hook():

    @task
    def list_tables_df():
        hook = PostgresHook(
            postgres_conn_id="my_postgres_conn",
        )
        sql = "SELECT * FROM pg_catalog.pg_tables;"
        df = hook.get_pandas_df(sql)
        print(df)


    list_tables_df()


example_hook()

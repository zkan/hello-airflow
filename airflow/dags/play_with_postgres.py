import datetime

from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator


def get_data():
    pg_hook = PostgresHook(postgres_conn_id='my_postgres_conn', schema='breakfast')
    connection = pg_hook.get_conn()
    cursor = connection.cursor()

    sql = 'SELECT * FROM product'
    cursor.execute(sql)
    rows = cursor.fetchall()
    for each in rows:
        print(each)


with DAG(
        dag_id='play_with_postgres',
        default_args={'start_date': datetime.datetime(2017, 5, 5)},
        schedule_interval='*/10 * * * *',
        catchup=False,
        tags=['odds'],
    ) as dag:

    t1 = PostgresOperator(
        task_id='query_some_data',
        postgres_conn_id='my_postgres_conn',
        sql="""
            SELECT * FROM transaction LIMIT 10;
        """,
    )

    t2 = PythonOperator(
        task_id='hook_task',
        python_callable=get_data,
    )

    t1 >> t2

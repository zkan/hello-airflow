from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.hooks.mysql import MySqlHook
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.utils.dates import days_ago


def _insert_some_persons():
    hook = MySqlHook(mysql_conn_id="my_mysql_conn")
    conn = hook.get_conn()
    cur = conn.cursor()

    sql = """
        insert into persons
            (person_id, first_name, last_name)
        values
            (1, 'John', 'Doe'), 
            (2, 'Jane', 'Du')
    """
    cur.execute(sql)
    conn.commit()
    conn.close()


default_args = {
    "owner": "Kan Ouivirach",
}

with DAG(
    "play_around_with_mysql",
    default_args=default_args,
    start_date=days_ago(2),
):

    select_sum = MySqlOperator(
        task_id="select_sum",
        mysql_conn_id="my_mysql_conn",
        sql="""
            select 1 + 1
        """,
    )

    create_persons_table = MySqlOperator(
        task_id="create_persons_table",
        mysql_conn_id="my_mysql_conn",
        sql="""
            create table if not exists persons (
                person_id int,
                last_name varchar(255),
                first_name varchar(255)
            )
        """,
    )

    insert_some_persons = PythonOperator(
        task_id="insert_some_persons",
        python_callable=_insert_some_persons,
    )

    select_sum >> create_persons_table >> insert_some_persons

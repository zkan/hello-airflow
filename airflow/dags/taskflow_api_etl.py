import json

from airflow.decorators import dag, task
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


def print_context():
    return 'Whatever you return gets printed in the logs'


default_args = {
    'owner': 'airflow',
}
@dag(default_args=default_args, schedule_interval='*/5 * * * *', start_date=days_ago(2), tags=['odds'])
def tutorial_taskflow_api_etl():
    @task()
    def extract():
        data_string = '{"1001": 301.27, "1002": 433.21, "1003": 502.22}'

        order_data_dict = json.loads(data_string)
        return order_data_dict

    @task(multiple_outputs=True)
    def transform(order_data_dict: dict):
        total_order_value = 0

        for value in order_data_dict.values():
            total_order_value += value

        return {'total_order_value': total_order_value}

    @task()
    def load(total_order_value: float):
        print('Total order value is: %.2f' % total_order_value)

    order_data = extract()
    order_summary = transform(order_data)
    load_task = load(order_summary['total_order_value'])

    run_this = PythonOperator(
        task_id='print_the_context',
        python_callable=print_context,
    )

    load_task >> run_this


tutorial_etl_dag = tutorial_taskflow_api_etl()

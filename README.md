# Hello, Airflow!

```sh
export AIRFLOW_HOME=/Users/zkan/Labs/hello-airflow/airflow
```

```sh
airflow db init
airflow users create --username admin --firstname Kan --lastname Ouivirach --role Admin --email kan@odds.team
```

```sh
airflow webserver --port 8080
```

```sh
airflow scheduler
```

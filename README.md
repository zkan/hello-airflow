# Hello, Airflow!

## Running Airflow in Docker

```bash
mkdir -p ./mnt/dags ./mnt/logs ./mnt/plugins ./mnt/config ./mnt/tests
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

```bash
docker compose up
```

**Ref:** https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

## Running on Local Machine

```sh
AIRFLOW_VERSION=2.1.2
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

Reference: https://airflow.apache.org/docs/apache-airflow/stable/installation.html#constraints-files

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

## Running with Docker Compose

```sh
docker compose up
```

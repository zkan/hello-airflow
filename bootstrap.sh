#!/bin/bash

apt-get update
apt-get install -y python3-dev python3-pip
apt-get install -y postgresql libpq-dev
pip3 install virtualenv

# Airflow Installation: https://airflow.incubator.apache.org/start.html
su ubuntu <<'EOF'
  echo 'export AIRFLOW_HOME=~/airflow' >> /home/ubuntu/.bash_profile
  echo 'export AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgres://airflow:airflow@localhost:5432/airflow' >> /home/ubuntu/.bash_profile
  virtualenv venv
  source venv/bin/activate
  pip install "airflow[postgres, password, slack]"
EOF

su postgres <<'EOF'
  createuser -s -w airflow
  createdb airflow -O airflow
  psql -c "ALTER USER "airflow" WITH PASSWORD 'airflow';"
EOF

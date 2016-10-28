#!/bin/bash

# Airflow Installation: https://airflow.incubator.apache.org/start.html
su ubuntu <<'EOF'
sudo apt-get update
sudo apt-get install -y python3-dev python3-pip
echo 'export AIRFLOW_HOME=~/airflow' >> /home/ubuntu/.bash_profile
sudo pip3 install airflow
EOF

f = open('/home/ubuntu/airflow/dags/data.txt')
time_data = f.read()
time_list = time_data.split()

split_text = open('/home/ubuntu/airflow/dags/time.txt', 'w')
split_text.write(str(time_list[3]))

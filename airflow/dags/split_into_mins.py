f = open('/home/ubuntu/airflow/dags/time.txt')
min_data = f.read()
mins_list = min_data.split(':')

split_text = open('/home/ubuntu/airflow/dags/mins.txt', 'w')
split_text.write(str(mins_list[1]))


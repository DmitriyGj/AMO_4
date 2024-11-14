from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from file_generator import generate_files
from counter import count_every_file
from summary import summuary_results


with DAG('a_counter_process', start_date=datetime(2024, 11, 14), schedule_interval=None) as dag:

    callbacks = [generate_files, count_every_file, summuary_results]
    steps = [PythonOperator(task_id=x.__name__, python_callable=lambda: x()) for x in callbacks]
    for idx in range(len(steps)-1):
        steps[idx] >> steps[idx+1] 
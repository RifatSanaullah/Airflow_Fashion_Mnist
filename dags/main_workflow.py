from airflow import DAG
from airflow.decorators import dag
from airflow.operators.bash import BashOperator

from datetime import datetime
from pathlib import Path
import os, sys


root_dir = Path(__file__).parent.parent.absolute()
print(root_dir)

default_args = {
    'owner': 'airflow',
    'depends_on_past': True 
}

@dag(
    dag_id="model_pipeline",
    start_date=datetime(2022, 1 ,1), 
    schedule_interval=None, 
    default_args=default_args,
    catchup=False
)

def model():
    model_dir = os.path.join(root_dir, 'dags', 'model')

    model_task_id = BashOperator(
        task_id="model_train",
        bash_command=f"cd {model_dir} && python main.py"
    )
    
    model_task_id

# Define DAGs
model_dag = model()

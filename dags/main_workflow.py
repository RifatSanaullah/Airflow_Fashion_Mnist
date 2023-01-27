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

with DAG("model_dag", start_date=datetime(2023, 1, 27),
schedule ="@daily", catchup=False) as dag:
    training_model = BashOperator(
        task_id="model_train",
        bash_command=f"cd {os.path.join(root_dir, 'dags', 'model')} && python main.py"
        )
    print(training_model)
    training_model

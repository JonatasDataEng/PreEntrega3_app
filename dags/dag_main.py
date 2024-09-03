import os
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from modules.extract import extract_data_from_api
from modules.transform import pre_processing_data
from modules.load import load_data
from modules.utils import get_defaultairflow_args


with DAG(
    dag_id="etl_coin_market_cap",
    default_args=get_defaultairflow_args(),
    description="Extract, Transform, and Load Data from CoinMarketCap API hourly",
    schedule_interval="@daily",
    catchup=False,
) as dag:
    
    args = [f"{datetime.now().strftime('%Y-%m-%d %H')}", os.getcwd()]

    # Tasks
    # 1. Extraction
    task_extract = PythonOperator(
        task_id="extract_data",
        python_callable=extract_data_from_api,
        op_args=args,
    )

    # 2. Transformation
    task_transform = PythonOperator(
        task_id="transform_data",
        python_callable=pre_processing_data,
        op_args=args,
    )

    # 3. Loading
    task_load_data = PythonOperator(
        task_id="load_data",
        python_callable=load_data,
        op_args=args,
    )

    # Task dependencies
    task_extract >> task_transform >> task_load_data
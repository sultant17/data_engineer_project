import datetime as dt
import os
import pandas as pd
import json
from sqlalchemy import create_engine
import pandas.io.common
from sqlalchemy import exc
from airflow.models import DAG
from airflow.operators.python import PythonOperator


def extract_transform_session_data(ds, *kwargs):
    dire = 'json_data/ga_sessions/'
    for file in os.listdir(dire):
        if file.endswith('json'):
            file_name = 'ga_sessions_new_{}.json'.format(ds)
            filename = file_name.split('_')[-1].split('.')[0]
            with open(f'{dire}/{file_name}') as json_file:
                json_data = json.load(json_file)
                df = pd.DataFrame(json_data[filename])

    df.to_csv('data/csvs/ga_sessions.csv',
              sep=',', index=False)
    print(f'Saved {len(df)} rows to a CSV')


def load_sessions_to_postgres():
    # Read the CSV files into dataframes
    path = 'data/csvs/'
    for file in os.listdir(path):
        if file.endswith('csv'):
            try:
                df1 = pd.read_csv('data/csvs/ga_sessions.csv')
                engine = create_engine(
                    'postgresql+psycopg2://airflow:stdb@postgres/airflow')
                try:
                    # Load the first dataframe into a table
                    df1.to_sql('ga_sessions', engine,
                               if_exists='append', index=False)
                except exc.IntegrityError:
                    pass
            except pandas.errors.EmptyDataError:
                print('ga_sessions dataframe is empty and has been skipped.')


def extract_transform_hits_data(ds, *kwargs):
    dire = 'json_data/ga_hits/'
    for file in os.listdir(dire):
        if file.endswith('json'):
            file_name = 'ga_hits_new_{}.json'.format(ds)
            filename = file_name.split('_')[-1].split('.')[0]
            with open(f'{dire}/{file_name}') as json_file:
                json_data = json.load(json_file)
                df = pd.DataFrame(json_data[filename])

    df.to_csv('data/csvs/ga_hits.csv',
              sep=',', index=False)
    print(f'Saved {len(df)} rows to a CSV')


def load_hits_to_postgres():
    # Read the CSV files into dataframes
    path = 'data/csvs/'
    for file in os.listdir(path):
        if file.endswith('csv'):
            try:
                df2 = pd.read_csv('data/csvs/ga_hits.csv')
                engine = create_engine(
                    'postgresql+psycopg2://airflow:stdb@postgres/airflow')
                # Load the second dataframe into a table
                try:
                    df2.to_sql('ga_hits', engine,
                               if_exists='append', index=False)
                except exc.IntegrityError:
                    pass
            except pandas.errors.EmptyDataError:
                print('ga-hits dataframe is empty and has been skipped.')


args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2022, 1, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1),
    'end_date': dt.datetime(2022, 1, 5),
}

with DAG(
        dag_id='ETL',
        schedule_interval='@daily',
        default_args=args,
        concurrency=1,
        max_active_runs=1,
        catchup=True,

) as dag:

    extract_transform_sessions = PythonOperator(
        task_id='extract_transform_sessions',
        python_callable=extract_transform_session_data,
        provide_context=True,
        dag=dag,
    )

    sessions_to_sql = PythonOperator(
        task_id='load_sessions_to_postgres',
        python_callable=load_sessions_to_postgres,
        dag=dag,
    )

    extract_transform_hits = PythonOperator(
        task_id='extract_transform_hits',
        python_callable=extract_transform_hits_data,
        provide_context=True,
        dag=dag,
    )

    hits_to_sql = PythonOperator(
        task_id='load_hits_to_postgres',
        python_callable=load_hits_to_postgres,
        dag=dag,
    )

    extract_transform_sessions >> sessions_to_sql >> extract_transform_hits >> hits_to_sql

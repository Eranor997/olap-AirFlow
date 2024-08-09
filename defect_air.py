from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from clickhouse_driver import Client
from sqlalchemy import create_engine

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 8, 8)
}

dag = DAG(
    dag_id='rep_defect',
    default_args=default_args,
    schedule_interval='17 5-23/1 * * *',
    description='for you :3',
    catchup=False,
    max_active_runs=1
)


def main():
    
    client = Client('clickhouse-server',
                        user='default',
                        password='default',
                        port=9000,
                        verify=False,
                        database='default',
                        settings={"numpy_columns": False, 'use_numpy': True},
                        compression=False)

    client.execute("""INSERT INTO report.reason_sum 
                            select
                                toDate(dt) dt_date,
                                reason_id,
                                sum(price_ru_100 / 100) sum_price
                            from default.verd
                            group by dt_date, reason_id;""")

    to_import = """select 
                        dt_date, 
                        reason_id, 
                        sum_price
                    from report.reason_sum"""

    df = client.query_dataframe(to_import)
    engine = create_engine('postgresql://default:default@pg:5432/postgres')
    df.to_sql('ch_data', engine, if_exists="append")
    print('ready')


task1 = PythonOperator(
    task_id='Test_dag_1', python_callable=main, dag=dag)

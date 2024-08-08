# olap-AirFlow
Поднятие pg, ch, AirFlow

AirFlow в последовательности:
docker-compose up airflow-init
docker-compose up -d

Объединяю сети:
docker network connect airflow_default clickhouse-server
docker network connect airflow_default postgres_container

Добавляю в AirFlow
pip install clickhouse-driver

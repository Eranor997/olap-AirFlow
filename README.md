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


![image](https://github.com/user-attachments/assets/a33b1a19-c860-4b0d-bfa8-0c33e2dabc14)

![image](https://github.com/user-attachments/assets/b925127c-4cda-4772-bb6a-0cc09f8e3f6a)




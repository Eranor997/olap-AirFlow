# olap-AirFlow
Поднятие pg, ch, AirFlow

AirFlow в последовательности:
docker-compose up airflow-init ,
docker-compose up -d

Соединяю AirFlow и клик, пг
docker network connect airflow_default clickhouse-server
docker network connect airflow_default postgres_container

Добавляю в AirFlow
pip install clickhouse-driver

## Залили данные на клик
![image](https://github.com/user-attachments/assets/a33b1a19-c860-4b0d-bfa8-0c33e2dabc14)

## Даг отработал
![image](https://github.com/user-attachments/assets/f2946e58-6d9b-4074-8185-7274bafc480e)

## Данные поступи на клик
![image](https://github.com/user-attachments/assets/b925127c-4cda-4772-bb6a-0cc09f8e3f6a)

## Данные поступи на пг
![image](https://github.com/user-attachments/assets/03dcbfb8-b2ce-48e2-99b8-2054f8271d5f)

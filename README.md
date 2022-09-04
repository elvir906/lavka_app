# Бэкенд приложения LAVKA APP

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)

### Назначение:
Бэкенд приложения регистрации пользователей и привязки к ним бонусных карт. А так же ведение базы маркетинговых акции. CRUD пользователей, карт и промоакций. 

### Стек технологий:
Python, FastAPI, SQLAlchemy, Alembic, PоstgreSQL, Docker, Swagger

### Установка:
1. Клонировать на локальную машину
````
git clone https://github.com/elvir906/lavka_app.git
````
2. Активировать виртульное окружение
```
source venv/Scripts/activate
```
3. Установить зависимости
```
pip install -r requirements.txt
```
4. создать в корне приложения файл .env и указать в ней переменные:
```
TITLE = Название
SERVER_HOST = http://0.0.0.0:8000
SECRET_KEY=Секретный ключ
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_SERVER=db # изменить на localhost, если запускаете локально
POSTGRES_PORT=5432
POSTGRES_DB=postgres
SQLALCHEMY_DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres
```

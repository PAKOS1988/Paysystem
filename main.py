from fastapi import FastAPI
from database import Base, engine

#Создать все таблицы для базы данных

Base.metadata.create_all(bind=engine)

#Объект для фастапи
app = FastAPI()

from business import business_api
from card_management_transfer import card_api
from user_authentication import user_api

# запуск проекта фастапи
# uvicorn main:app --reload
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Подключение к базе данных
SQLALCHEMY_DATABASE_URI = 'sqlite:///pay_test.db'

# connect_args={"check_same_thread": False} - ТОЛЬКО ДЛЯ sqlite3
engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False})

#Сессии для базы данных
SessionLocal = sessionmaker(bind = engine)

#Общий класс для создания моделей данных
Base = declarative_base()

#Генерация подключений к БД
def get_db():
    session = SessionLocal()
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()

#Импорт функционала для БД
from database.userservice import *
from database.cardservice import *
from database.paymentservice import *
from database.businessservice import *
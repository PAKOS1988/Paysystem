from database.models import User, Password
from database import get_db

# Регистрация пользователя
def register_user_db(**kwargs):
    # Проверка номера
    db = next(get_db())
    phone_number = kwargs.get('phone_number')
    #Проверка номера
    checker = db.query(User).filter_by(phone_number=phone_number).first()
    if checker:
        return "Пользователь с таким номером уже есть в БД"
    #Если нет пользователя в БД
    new_user = User(**kwargs)
    db.add(new_user)
    db.commit()
    new_user_password = Password(user_id = new_user.user_id, **kwargs)
    db.add(new_user_password)
    db.commit()

    return "Пользователь успешно создан"

# Проверка пароля
def check_password_db(phone_number, password):
    db = next(get_db())
    cheker = db.query(Password).filter_by(phone_number=phone_number).first()
    if cheker and cheker.password == password:
        return cheker.user_id
    elif not cheker:
        return "Ошибка в номере"
    elif cheker.password != password:
        return "Неверный пароль"

# Получение информации пользователя
def get_user_cabinet_db(user_id):
    db = next(get_db())
    cheker = db.query(User).filter_by(user_id=user_id).first()
    if cheker:
        return cheker
    return "Ошибка в данных"
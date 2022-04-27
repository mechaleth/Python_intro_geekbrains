# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

import datetime


# Только именованные аргументы!
# значения по умолчанию не придумал)
def get_user_data(*, name, surname, birthdate, location, email=None, phone=None):
    """
    Возвращает информацию о пользователе на основе задаваемых данных.

    :param name: имя пользователя
    :param surname: фамилия пользователя
    :param birthdate: дата рождения пользователя
    :param location: местоположение пользователя
    :param email: электронная почта пользователя
    :param phone: телефон пользователя
    :return: информация о пользователе в одной строке
    """
    return f"Oh that obnoxious user {name} {surname}! " \
           f"He was born in {birthdate}. " \
           f"Now {name} located on {location}. " \
           f"You may reach {name} by phone {phone} or email {email}"


print(get_user_data(name="Louis", birthdate=datetime.date(year=1973, month=2, day=11),
                    surname="Cachet", location="Demont",
                    phone="+33-61-666-14-88", email="christian@jw.fr"))

# ошибка!
# print(get_user_data("Louis", birthdate=datetime.date(year=1973, month=2, day=11),
#                     surname="Cachet", location="Demont",
#                     phone="+33-61-666-14-88", email="christian@jw.fr"))

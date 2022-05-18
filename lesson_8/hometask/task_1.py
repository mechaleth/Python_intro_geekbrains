# Реализовать класс «Дата», функция-конструктор которого должна
# принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число,
# месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

# Что я не понял в задании:
# Зачем нужен метод класса? День,месяц, год - это именно изменяемые атрибуты класса, не объекта?
# Нужна ли валидация в методе класса?
# Если нет, то зачем вообще нужен именно метод класса, а не статический метод?
# Разве может класс хранить некорректные данные?
# Зачем нужен конструктор класса? Ведь дата живёт в самом классе, не объекте...
# Зачем генерировать все прочие объекты со старыми датами, характерными для класса через метод класса?
# Нужно ли вообще в объекте менять число, месяц, год?
# Что хранит именно объект? Строку?

class Date:
    _day: int
    _month: int
    _year: int

    def __init__(self, date: str):
        # вообще, то, что в классе, то и в self
        # так что, возможно, это излишне
        # и в целом, мне не нравится вызов этого здесь
        # класс - это класс, объект - это объект
        # поэтому хорошо бы эту функцию сделать не методом класса!
        self._day, self._month, self._year = self.get_year_month_day(date)

    @staticmethod
    def leap_good_year(year: int) -> bool:
        """
        Проверка на високосный год

        :param year: год, > 0 (в истории есть нюансы, но мы рассматриваем нашу эру)
        :return: булево значение, True если високосный и False если не високосный
        """
        if year < 0:
            return False
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        elif year % 4 == 0:
            return True

        return False

    @staticmethod
    def check_31_day_month(month: int) -> bool:
        """
        Проверка, 31 день в месяце или нет

        :param month: месяц, положительное число от 1 до 13
        :return: булево True, если в месяце 31 день или
        False, если не 31 день
        """
        if month not in range(1, 13):
            raise ValueError("Month need to be in range 1 to 12!")

        # признак нечётного месяца
        is_odd = bool(month % 2)
        return is_odd if (month <= 7) else not is_odd

    @staticmethod
    def check_date_numbers(*, day: int, month: int, year: int) -> tuple:
        """
        Проверка числа, месяца, года на валидность.
        Значения задаются только с помощью именованных аргументов,
        чтобы дорогой пользователь ничего не перепутал.

        :param day: день, 1-31 (но не всё так однозначно)
        :param month: месяц, 1-12
        :param year: год, любое положительное число.
        Хотя интерес может быть и к годам до нашей эры, здесь это не принимаем.
        Да, мы оптимистично смотрим в будущее и не ограничиваемся 4мя цифрами.
        :return: кортеж булевых значений по дню, месяцу и году.
        """
        good_month, good_year = month in range(1, 13), year >= 0
        # максимальное количество дней, по-умолчанию самый максимум
        max_days = 31

        if good_month:
            # Для февраля всё по-особому
            if month == 2:
                # прям максимум 29 дней
                # но если год адекватный и не високосный, то 28
                max_days = (29, 28)[good_year and not Date.leap_good_year(year)]
            else:
                max_days = 31 if Date.check_31_day_month(month) else 30

        return day in range(1, max_days + 1), good_month, good_year

    @classmethod
    def get_year_month_day(cls: 'Date', date: str) -> tuple:
        """
        Извлекает день, месяц, год из форматированной строки.
        Также меняет соответствующие поля у передаваемого класса.
        Если у строки не тот формат, будет выдана ошибка.

        :param cls: Класс (потомок) Date
        :param date: форматированная строка даты "день-месяц-год"
        :return: кортеж целых чисел день, месяц, год
        """
        # хотел сделать проверку только формата строки,
        # как сказано в задании, но смущает, что это - метод класса...
        # Можно ли допускать, чтобы данные класса были некорректны???
        try:
            day, month, year = date.split('-')
            # В принципе, теперь можно не бояться отрицательных значений!
            day, month, year = int(day), int(month), int(year)
        except ValueError:
            # Нужно более конкретное сообщение
            raise ValueError('Uncorrect date format')
        day_mark, month_mark, year_mark = \
            Date.check_date_numbers(day=day, month=month, year=year)

        # можно обработать иначе и не сосредотачиваться на ошибке!
        def raise_valueerror_if_need(mark: bool, message: str):
            if not mark:
                raise ValueError(message)

        raise_valueerror_if_need(year_mark, "Uncorrect year value!")
        raise_valueerror_if_need(month_mark, "Uncorrect month value!")
        raise_valueerror_if_need(day_mark, "Uncorrect day value!")
        # не знаю, зачем именно метод класса, а не статический метод
        # это единственное предположение, больше мыслей нет
        cls._day, cls._month, cls._year = day, month, year
        # ну это для контроля и прочих удобств
        return cls._day, cls._month, cls._year

    def __str__(self):
        return f'{self._day} {self._month} {self._year}'


if __name__ == '__main__':
    date_tuple = (Date("28-02-2020"), Date("30-04-23035"))
    for cur_date in date_tuple:
        print(cur_date)
    try:
        print(Date("32-13--5"))
    except ValueError as value_err:
        print(value_err)
    try:
        print(Date("32 13 5"))
    except ValueError as value_err:
        print(value_err)
    print(Date.check_date_numbers(day=29, month=2, year=2024))
    print(Date.check_date_numbers(day=29, month=2, year=2022))
    print(Date.check_date_numbers(day=32, month=14, year=2022))
    print(Date.check_date_numbers(day=29, month=8, year=-5))
    try:
        print(Date.get_year_month_day("32-05-20888"))
    except ValueError as value_err:
        print(value_err)
    print(Date.get_year_month_day("31-05-2088"))
    for cur_date in date_tuple:
        print(cur_date)
    # Достучимся до того, что запрещено...
    # Специально не делал в классе property classmethod, эти данные защищены принципиально...
    print(f'Date class day {Date._day} month {Date._month} year {Date._year}')

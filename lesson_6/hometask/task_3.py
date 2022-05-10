# Реализовать базовый класс Worker (работник),
# в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name: str
    surname: str
    position: str
    _income = {"wage": float, "bonus": float}

    def __init__(self, name, surname):
        self.name, self.surname = name, surname

    def set_income(self, wage: float, bonus: float = 0.0):
        """
        Метод расчёта полной заработной платы.
        Оклад не может быть отрицательным.
        А вот премия может быть штрафом!

        :param wage: оклад
        :param bonus: премия или штраф
        :return: полная заработная плата
        """
        self._income["wage"], self._income["bonus"] = wage if wage >= 0.0 else 0.0, bonus


class Position(Worker):
    def __init__(self, name: str, surname: str, position: str):
        super().__init__(name, surname)
        self.position = position

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        if (type(self._income["wage"]) is type) or (self._income["bonus"] is type):
            raise ValueError("wage and bonus are not setted!")
        return self._income["wage"] + self._income["bonus"]


if __name__ == "__main__":
    *drudge_name, drudge_surname = input("Enter person name, surname >>> ").split()
    drudge_name = " ".join(drudge_name)
    drudge = Position(name=drudge_name, surname=drudge_surname, position=input("Input position title >>>"))
    wage = float(input(f"Enter the {drudge.position} wage >>> "))
    bonus = float(input(f"Enter the {drudge.position} bonus >>> "))
    drudge.set_income(float(wage), float(bonus))
    print(f"{drudge.get_full_name()} is {drudge.position} with salary {drudge.get_total_income()}.")

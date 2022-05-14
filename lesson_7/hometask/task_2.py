# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда,
# которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
#
#  Для определения расхода ткани по каждому типу одежды использовать формулы:
#  для пальто (V/6.5 + 0.5), для костюма (2`*`H + 0.3).
#  Проверить работу этих методов на реальных данных.
#
#  Реализовать общий подсчет расхода ткани.
#  Проверить на практике полученные на этом уроке знания:
#  реализовать абстрактные классы для основных классов проекта,
#  проверить на практике работу декоратора @property.

# Общий подсчёт тканей?? Это ткань пальто+ткань костюм???))))

import abc


class Clothes(abc.ABC):
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    @abc.abstractmethod
    def cloth_consumption(self):
        pass

    @abc.abstractmethod
    def cloth_size(self, value):
        pass


class Coat(Clothes):
    def __init__(self, size: float, name: str = "Coat"):
        self.cloth_size = size
        super().__init__(name)

    @property
    def cloth_consumption(self):
        return round(self._size / 6.5 + 0.5, 3)

    @property
    def cloth_size(self):
        return self._size

    @cloth_size.setter
    def cloth_size(self, value):
        if value > 0:
            self._size = value


class Suit(Clothes):
    def __init__(self, height: float, name: str = "Suit"):
        self.cloth_size = height
        super().__init__(name)

    @property
    def cloth_consumption(self):
        return round(2 * self._height + 0.3, 3)

    @property
    def cloth_size(self):
        return self._height

    @cloth_size.setter
    def cloth_size(self, value):
        if value > 0:
            self._height = value


if __name__ == "__main__":
    cloth_list = [Coat(48), Suit(1.73, "Smocking")]
    cloth_str = "It needs {consumption} of cloth to make a {name}"
    for clothe in cloth_list:
        print(cloth_str.format(consumption=clothe.cloth_consumption, name=clothe.name))
    cloth_list[0].cloth_size = 52
    # cloth_list.append(Clothes())

    for clothe in cloth_list:
        print(cloth_str.format(consumption=clothe.cloth_consumption, name=clothe.name))

# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    _title: str

    def draw(self):
        return "Запуск отрисовки."


class Pen(Stationery):
    def __init__(self):
        self._title = "Ручка"

    def draw(self):
        return f"{super().draw()} {self._title} используется для отрисовки."


class Pencil(Stationery):
    def __init__(self):
        self._title = "Карандаш"

    def draw(self):
        return f"{super().draw()} {self._title} используется для отрисовки."


class Handle(Stationery):
    def __init__(self):
        self._title = "Маркер"

    def draw(self):
        return f"{super().draw()} {self._title} используется для отрисовки."


if __name__ == "__main__":
    something = Stationery()
    pen = Pen()
    pencil = Pencil()
    handle = Handle()
    print(something.draw())
    print(pen.draw())
    print(pencil.draw())
    print(handle.draw())

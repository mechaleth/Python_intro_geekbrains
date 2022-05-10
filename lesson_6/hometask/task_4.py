# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

turn_turple = ("налево", "направо", "назад")


class Car:
    speed: float
    color: str
    name: str = ""
    is_police: bool = False

    def go(self) -> str:
        return f"Машина {self.name} поехала"

    def stop(self) -> str:
        # можно добавить time.sleep со временем, соответствующем тормозному пути
        self.speed = 0.0
        return f"Машина {self.name} остановилась"

    def turn(self, direction: str) -> str:
        if direction in turn_turple:
            return f"Машина {self.name} повернула {direction}"
        else:
            return f"Манёвр {direction} недоступен, машина {self.name} движется без изменений"

    def show_speed(self) -> str:
        return f"Текущая скорость {self.name} {self.speed} км/ч"

    def get_car_type_info(self) -> str:
        return f'{self.color} {self.name} is {"" if self.is_police else "not "}a police car'


class TownCar(Car):
    _extra_speed = 60

    def show_speed(self) -> str:
        if self.speed > self._extra_speed:
            return f"{super().show_speed()} превышает лимит в {self._extra_speed} км/ч!"
        else:
            # согласно документации, в данном контексте == super()
            return super(TownCar, self).show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    _extra_speed = 40

    def show_speed(self) -> str:
        if self.speed > self._extra_speed:
            return f"{super().show_speed()} км/ч превышает лимит в {self._extra_speed} км/ч!"
        else:
            return super(WorkCar, self).show_speed()


class PoliceCar(Car):
    def __init__(self):
        self.is_police = True
        super().__init__()


if __name__ == "__main__":
    city_car = TownCar()
    speedy_car = SportCar()
    drudge_car = WorkCar()
    cop_car = PoliceCar()

    city_car.name = "Toyota"
    speedy_car.name = "Porsche"
    drudge_car.name = "Renault"
    cop_car.name = "Dodge"

    city_car.speed = 70.0
    drudge_car.speed = 40.0
    speedy_car.speed = 100.0
    speedy_car.color = "Red"
    city_car.color = "Orange"
    drudge_car.color = "White"
    cop_car.color = "Police colored"

    print(city_car.get_car_type_info())
    print(drudge_car.get_car_type_info())
    print(speedy_car.get_car_type_info())
    print(cop_car.get_car_type_info())

    print(drudge_car.show_speed())
    print(cop_car.go())
    print(speedy_car.show_speed())
    print(speedy_car.stop())
    print(speedy_car.show_speed())
    print(city_car.turn("налево"))
    print(cop_car.turn("напрямо"))

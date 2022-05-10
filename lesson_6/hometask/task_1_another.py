# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

# Задание абстрактное, конечно)
# Переключение между всеми режимами автоматически или пользователь задаёт текущий режим???
# Если автоматически, то какого типа проверка и зачем она в принципе?
# Если пользователь задаёт текущий режим, то проверка нужна. Но зачем задержки?) И какой тогда это светофор?
# Нужен ли бесконечный цикл? Или цикл, прерывающийся по какому-либо условию? По какому условию?
# Разве не зелёный, желтый, красный??

import time
from itertools import cycle as it_tools_cycle

traffic_modes = ('red', 'yellow', 'green')


class TrafficLight:
    __color = ""
    __traffic_modes_order = dict(zip(traffic_modes, [x for x in range(1, len(traffic_modes) + 1)]))
    __traffic_modes_duration = dict(zip(traffic_modes, (7, 2, 4)))

    # проверка правильности последовательности
    # ... -> red -> yellow -> green -> red -> yellow -> green -> red -> ...
    # лучше через def. Хотя лямбда быстрее. Ну и мне интересно попробовать именно так)
    check_order = lambda current, previous: (current - previous) % 3 == 1

    def running(self, mode: str):
        if mode not in traffic_modes:
            raise ValueError("Unexpected traffic mode")
        if not self.__color:
            self.__color = mode
        elif not TrafficLight.check_order(self.__traffic_modes_order[mode],
                                          self.__traffic_modes_order[self.__color]):
            string = f"Uncorrect traffic mode order! Previous {self.__color}, you need {mode}"
            raise ValueError(string)
        self.__color = mode
        print(self.__color)
        time.sleep(self.__traffic_modes_duration[self.__color])


if __name__ == "__main__":
    obj = TrafficLight()
    my_max_count = 2
    obj.running("green")
    mode_gen = it_tools_cycle(traffic_modes)
    for count in range(my_max_count*len(traffic_modes)):
        obj.running(mode_gen.__next__())
    obj.running("red")
    obj.running("yellow")
    # а тут порядок нарущен!
    obj.running("red")
    print("Thats all!")

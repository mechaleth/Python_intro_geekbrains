# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного.
#
# !!!Note: так скрипт или всё-таки итератор? Итератор - это, разве, не объект?) )
#
# **Подсказка:** использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения (Условие на пользователе или на создателе скрипта?).
#
#  Например, в первом задании выводим целые числа, начиная с 3,
#  а при достижении числа 10 завершаем цикл.

# Как я понял эту часть задания:
# Пишем скрипт, использующий itertools.count
# Используем эту функцию в цикле в скрипте.
# Цикл прерывает пользователь. Или моё какое-то условие.
import itertools as itools


def my_count(start_number: int, step: int = 1):
    """Одно из представлений itertools.count"""
    current_number = start_number
    while True:
        yield current_number
        current_number += step


# не хочу, чтобы это запускалось в других модулях
# https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    origin_number = 0
    # Запрашиваем
    while True:
        try:
            origin_number = int(input("Enter origin integer number for generating a sequence >>>"))
            max_cycle_number = int(input("Enter max cycle count >>>"))
        except ValueError:
            print("That's not integer number! Try again.")
            continue
        break
    count = 0
    for num in itools.count(origin_number):
#    for num in my_count(origin_number):
        count += 1
        if count > max_cycle_number:
            break
        print(num)
    print("That's all, folks!")

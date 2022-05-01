# Реализовать функцию my_func(), которая
# принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов.
import math


# вспомогательная функция
def calc_sum(*args):
    """
    Вычисляет сумму задаваемых чисел.
    При некорректном типе аргументов возвращает минус бесконечность

    :param args: задаваемые числа
    :return: сумму задаваемых чисел или -math.inf
    """
    try:
        return sum(args)
    except TypeError:
        return -math.inf


# нас интересуют только позиционные аргументы,
# ни о каких именованных и позиционных аргументах речь не идёт!
def my_func(arg_1, arg_2, arg_3, /):
    """
    Вычисляет сумму наибольших двух аргументов.
    При некорректном типе двух задаваемых аргументов возвращает минус бесконечность

    :param arg_1: некое целое или дробное число
    :param arg_2: некое целое или дробное число
    :param arg_3: некое целое или дробное число
    :return: сумму наибольших двух аргументов или -math.inf
    """
    return max(calc_sum(arg_1, arg_2),
               calc_sum(arg_1, arg_3),
               calc_sum(arg_2, arg_3))


def lazy_print(arg_1, arg_2, arg_3):
    print(f"Max sum of two elements "
          f" between {arg_1}, {arg_2}, {arg_3} is "
          f"{my_func(arg_1, arg_2, arg_3)}")


lazy_print('ahh', 2, 3)
lazy_print(3, 1, 4)
lazy_print(3.13, 5, 9.11)
lazy_print('ahh', 'fggh', 3)

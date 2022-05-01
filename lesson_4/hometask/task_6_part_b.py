# Реализовать два небольших скрипта:
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#
# !!!Note: так скрипт или всё-таки итератор? Итератор - это, разве, не объект?) )
#
# **Подсказка:** использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.(Условие на пользователе или на создателе скрипта?).
#
#  Например, во втором также необходимо предусмотреть условие,
#  при котором повторение элементов списка будет прекращено.
import itertools as itools

def my_cycle(iterate):
    while iterate:
        for element in iterate:
            yield element


# https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    input_string_array = input("Enter the strings with ' ' as delimiter>>>").split()
    while True:
        try:
            max_cycle_number = int(input("Enter max cycle count >>>"))
        except ValueError:
            print("That's not integer number! Try again.")
            continue
        break
    count = 0
    for element in itools.cycle(input_string_array):
#    for element in my_cycle(input_string_array):
        count += 1
        if count > max_cycle_number:
            break
        print(element)
    print("That's all, folks!")
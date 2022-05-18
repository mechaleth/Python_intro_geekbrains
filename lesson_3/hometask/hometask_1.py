# Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

# нас интересуют только позиционные аргументы
# ни о каких именованных и позиционных аргументах речь не идёт!
def divide_numbers(num_1, num_2, /):
    """
    Функция вычисления частного от деления одного числа на другое

    :param num_1: делимое
    :param num_2: делитель
    :return: результат деления делимого на делитель или None
    """
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        return None


divident = float()
denominator = float()
while True:
    try:
        divident = float(input("Введите числитель дроби:"))
        denominator = float(input("Введите знаменатель дроби:"))
        break
    except ValueError:
        continue

print(f"{divident}/{denominator}={divide_numbers(divident, denominator)}")
# Тут будет ошибка! Так как аргументы строго позиционные
# print(f"{divident}/{denominator}={divide_numbers(num1 = divident, num2 = denominator)}")

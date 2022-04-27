# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# ** Подсказка:** попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
import math


def my_func_var_1(base, exp):
    """
    Алгоритм возведения числа в степень.

    :param base: Число, которое требуется возвести в степень
    :param exp: степень, в которую требуется возвести число
    :return:  число, возведенное в степень
    """
    return base ** exp


# a^x == exp(x*ln(a))
# универсальна, расчёт дробных корней прост
# если нет претензий к math.log и math.exp
def my_func_var_2(base, exp):
    """
    Алгоритм возведения числа в степень.
    Базируеся на формуле a**x == exp(x*ln(a))

    :param base: Положительное число, которое требуется возвести в степень
    :param exp: степень, в которую требуется возвести число
    :return:  число, возведенное в степень
    """
    if base < 0:
        raise ValueError("base cannot be negative!")
    return math.exp(exp * math.log(base))


def my_func_var_3(base, exp):
    """
    Иттерационный алгоритм возведения числа в целую степень.

    :param base: Число, которое требуется возвести в степень
    :param exp: степень, в которую требуется возвести число
    :return: число, возведенное в степень
    """
    if type(exp) != int:
        raise TypeError("Uncorrect exponent type")
    sign = -1 if (exp < 0) else 1
    res = 1
    for step in range(exp * sign):
        res *= base
    return res if sign == 1 else 1 / res


def my_func_var_4(base, exp):
    """
    Быстрый алгоритм возведения числа в целую степень.
    Базируется на предствалении числа в бинарном виде
    и формулах:
     -> a**(x*y) = (a**x)**y;
     -> a**(x+y) = (a**x)*(a**y).
    Выполнен в соответствие с:
    https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D1%8B_%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B3%D0%BE_%D0%B2%D0%BE%D0%B7%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F_%D0%B2_%D1%81%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C

    :param base: Число, которое требуется возвести в степень
    :param exp: целая степень, в которую требуется возвести число
    :return: число, возведенное в степень
    """
    if type(exp) != int:
        raise TypeError("Uncorrect exponent type")
    sign = -1 if (exp < 0) else 1
    bin_repr = bin(exp * sign)
    res = 1
    for bit in bin_repr[2:len(bin_repr)]:
        res *= res * base if bit == '1' else res
    return res if sign == 1 else 1 / res


# BONUS:
def my_math_root(base, exp, max_error=1e-10):
    """
    Алгоритм оценки корня целой степени из числа.
    Выполнен в соответствие с:
    https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%BD%D0%B0%D1%85%D0%BE%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F_%D0%BA%D0%BE%D1%80%D0%BD%D1%8F_n-%D0%BD%D0%BE%D0%B9_%D1%81%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D0%B8

    :param base: Число, из которого требуется извлечь корень
    :param exp: целая степень корня
    :param max_error: требуемая точность оценки корня
    :return: оценка корня заданной степени из числа или
             None, если корень с требуемой точностью оценить не удалось
    """
    if type(exp) != int:
        raise TypeError("Uncorrect exponent type")
    if exp % 2 == 0 and base < 0:
        raise ValueError("Cannot estimate negative base root by even exp")
    if exp == 0:
        return 1
    new_exp = exp if exp > 0 else -exp
    xk = x0 = base
    # ограничитель цикла
    max_cycle_number = 3000
    for i in range(max_cycle_number):
        xk = (1 / new_exp) * ((new_exp - 1) * xk + base / my_func_var_4(xk, new_exp - 1))
        if math.fabs(xk - x0) < max_error:
            # сходимость достигнута
            return xk if exp > 0 else 1 / xk
        x0 = xk
    # Если количество итераций превыщено, результат не гарантирован!
    return None


def test_my_funcs(x, y):
    var_1 = my_func_var_1(x, y)
#    var_2 = my_func_var_2(x, y)
    var_3 = my_func_var_3(x, y)
    var_4 = my_func_var_4(x, y)
    root = my_math_root(x, y)
    nominal = pow(x, y)
    root_nominal = pow(x, 1 / y)
    print(f"Results of power {x} to {y}:\n"
          f"variant 1 is {var_1}, error to pow is {math.fabs(var_1 - nominal)}\n"
#          f"variant 2 is {var_2}, error to pow is {math.fabs(var_2 - nominal)}\n"
          f"variant 3 is {var_3}, error to pow is {math.fabs(var_3 - nominal)}\n"
          f"variant 4 is {var_4}, error to pow is {math.fabs(var_4 - nominal)}")
    print(f"Special test: my_math_root {x} by {y} of power {x} to {1 / y} (same as root {x} by {y}):")
    print(f"my_math_root is {root}")
    print(f"error to pow is {math.fabs(root - root_nominal)}")


test_my_funcs(50.4564654546, -31)

print(my_math_root(5.11568, -2, 1e-30) - pow(5.11568, -1 / 2))

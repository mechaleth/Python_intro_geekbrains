# Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
#
# **Подсказка:** элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
# **Пример исходного списка:** [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# **Результат:** [12, 44, 4, 10, 78, 123].
# origin_list = [300, 2, 12, 44, 44.5, 1, 1, 4, 10, 7, 1, 78, 123, 55]

def get_number_by_string(string_number: str):
    """
    Функция преобразования строки к какому-либо числовому формату

    :param string_number: число в строковом виде
    :return: число в числовом формате
    """
    try:
        return int(string_number)
    except ValueError:
        # если и тут ошибка, пробрасываем во внешний код
        return float(string_number)


# не хочу, чтобы это запускалось в других модулях
# https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    input_string_array = input("Enter the numbers string with ' ' as delimiter>>>").split()
    origin_list = [get_number_by_string(num) for num in input_string_array]
    # Выглядит красивее
    # print([element for i, element in enumerate(origin_list) if element > origin_list[i - 1 if i > 0 else 0]])
    # Зато тут на один шаг меньше
    print([origin_list[i] for i in range(1, len(origin_list)) if origin_list[i] > origin_list[i - 1]])

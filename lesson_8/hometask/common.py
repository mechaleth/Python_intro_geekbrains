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
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
#
# **Подсказка:** матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# **Примеры матриц:** см. в методичке.
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
#
# **Подсказка:** сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, data):
        # простейшая проверка. Все элементы не перебираем
        # убеждаемся, что имеем дело со списком списков, как в задании изложено
        # Пользователь может передать целое или простой список
        # или список списков строк. Следует объяснить суть ошибки
        try:
            for elem in (x for list_1 in data for x in list_1):
                if not (type(elem) is float or type(elem) is int):
                    raise TypeError
            # вот эти ограничения не очевидны, но следуют из формулировки задания
            if type(data) is not list:
                raise TypeError
            if type(data[0]) is not list:
                raise TypeError
        except TypeError:
            raise ValueError("Expected data datatype is list of list of numbers")
        self._inner_data = data

    def __str__(self):
        return "\n".join(" ".join(str(x) for x in row) for row in self._inner_data)

    @property
    def rows_count(self):
        return len(self._inner_data)

    @property
    def columns_count(self):
        return len(self._inner_data[0])

    def __add__(self, other):
        if type(other) is not Matrix:
            raise ValueError("Expected operands datatype is Matrix")
        if self.rows_count != other.rows_count or self.columns_count != other.columns_count:
            raise ValueError("Sizes of matrixes are not the same!")
        new_matrix = list()
        # доступ к защищенным членам класса - это плохо.
        # Но это метод этого же класса! В данном контексте, приемлиемо.
        for row_1, row_2 in zip(self._inner_data, other._inner_data):
            new_matrix.append([el_1 + el_2 for el_1, el_2 in zip(row_1, row_2)])
        return Matrix(new_matrix)


if __name__ == "__main__":
    matr_1 = Matrix([[1, 2, 3], [4, 5, 6.0]])
    matr_2 = Matrix([[1, 2, 3], [4, 5, 6]])
    res_matr = matr_1 + matr_2
    print(matr_1)
    print("+")
    print(matr_2)
    print("=")
    print(res_matr)
    print(type(res_matr))
    try:
        # print(Matrix([1, 2, 3]))
        print(Matrix([[1, 2, 3], [4, 5, '6']]))
    except ValueError as value_error:
        print(value_error)

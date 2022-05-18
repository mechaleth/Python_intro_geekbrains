# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (**add**()), вычитание (**sub**()),
# умножение (**mul**()), деление (**truediv**()).
# Данные методы должны применяться только к клеткам и
# выполнять увеличение, уменьшение, умножение и целочисленное
# (с округлением до целого) деление клеток, соответственно.
#
# **Сложение.**Объединение двух клеток.
# При этом число ячеек общей клетки должно
# равняться сумме ячеек исходных двух клеток.
# **Вычитание.**Участвуют две клетки.
# Операцию необходимо выполнять только если разность
# количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
# **Умножение.**Создается общая клетка из двух.
# Число ячеек общей клетки определяется как
# произведение количества ячеек этих двух клеток.
# **Деление.**Создается общая клетка из двух.
# Число ячеек общей клетки определяется как
# целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(),
# принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида`*****\n*****\n*****`...,
# где количество ячеек между`\n`равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12,
# количество ячеек в ряду — 5. Тогда метод make_order()
# вернет строку:`*****\n*****\n**`.
# Или, количество ячеек клетки равняется 15,
# количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:`*****\n*****\n*****`.

class Organic_Cell:
    def __init__(self, cellure_number: int):
        if cellure_number <= 0:
            raise ValueError("cellure number must be a positive!")
        self._cellure_number = cellure_number

    @property
    def cellure_number(self):
        return self._cellure_number

    def __raise_if_not_cell(self, object):
        if type(object) is not Organic_Cell:
            raise TypeError("Unexpected operand type; Organic_Cell object expected")

    def __add__(self, other):
        self.__raise_if_not_cell(other)
        return Organic_Cell(self._cellure_number + other.cellure_number)

    def __sub__(self, other):
        self.__raise_if_not_cell(other)
        if self._cellure_number <= other.cellure_number:
            raise ValueError("Resulting cellure number less or equal zero!")
        return Organic_Cell(self._cellure_number - other.cellure_number)

    def __mul__(self, other):
        self.__raise_if_not_cell(other)
        return Organic_Cell(self._cellure_number * other.cellure_number)

    def __truediv__(self, other):
        self.__raise_if_not_cell(other)
        return Organic_Cell(self._cellure_number // other.cellure_number)

    def __str__(self):
        return "*" * self._cellure_number

    def __repr__(self):
        return self.__str__()

    def make_order(self, cellure_in_row: int):
        if cellure_in_row <= 0:
            raise ValueError("Cellure in row number must be a positive!")
        rows, lost_cells = divmod(self._cellure_number, cellure_in_row)

        return "\n".join([f"{'*' * cellure_in_row}"
                          for i in range(rows)]) + (f'\n{"*" * lost_cells}'
                                                    if lost_cells > 0 else "")


if __name__ == "__main__":
    cells = (Organic_Cell(12), Organic_Cell(15))
    for cell in cells:
        print(cell.make_order(5))
        print('\n')

    print(f'{cells[0]} + {cells[1]} = {cells[0] + cells[1]}')
    print(f'{cells[0].cellure_number} + {cells[1].cellure_number} = {(cells[0] + cells[1]).cellure_number}')

    try:
        print(f'{cells[0]} - {cells[1]} = {cells[0] - cells[1]}')
    except ValueError as type_error:
        print(f'\n{type_error}')

    print(f'\n{cells[1]} - {cells[0]} = {cells[1] - cells[0]}')
    print(f'{cells[1].cellure_number} - {cells[0].cellure_number} = {(cells[1] - cells[0]).cellure_number}')

    print(f'\n{cells[0]}\n*\n{cells[1]}\n=\n{(cells[0] * cells[1]).make_order(cells[0].cellure_number)}')
    print(f'{cells[0].cellure_number} * {cells[1].cellure_number} = {(cells[0] * cells[1]).cellure_number}')

    try:
        print(f'{cells[0]} / {cells[1]} = {cells[0] / cells[1]}')
    except ValueError as value_error:
        print(f'\n{value_error}')

    print(f'\n{cells[1]} / {cells[0]} = {cells[1] / cells[0]}')
    print(f'{cells[1].cellure_number} / {cells[0].cellure_number} = {(cells[1] / cells[0]).cellure_number}')

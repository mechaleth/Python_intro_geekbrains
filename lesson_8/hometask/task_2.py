# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.
import decimal
import common


class MyZeroDivisionError(ZeroDivisionError):
    def __init__(self, numerator, denominator):
        if MyZeroDivisionError.check_numeric(numerator) and \
                MyZeroDivisionError.check_numeric(denominator):
            self._numerator = numerator
            self._denominator = denominator
        super().__init__(numerator, denominator)

    @staticmethod
    def check_numeric(number):
        return isinstance(number, int) or \
               isinstance(number, float) or \
               isinstance(number, decimal.Decimal)

    def __str__(self):
        return f'{self.__class__.__name__}: bad idea is to divide by zero: {self._numerator}/{self._denominator}'


if __name__ == "__main__":
    try:
        while True:
            try:
                numerator = common.get_number_by_string(input("Input numerator >>>"))
                denumerator = common.get_number_by_string(input("Input denumerator >>>"))
                print(numerator/denumerator)
            except ValueError:
                continue
            except ZeroDivisionError:
                # ловим реальное деление на ноль и вызываем свой обработчик
                raise MyZeroDivisionError(numerator, denumerator)
            else:
                break
    except MyZeroDivisionError as mine_error:
        print(mine_error)
        # Корректно завершаемся
        exit(1)

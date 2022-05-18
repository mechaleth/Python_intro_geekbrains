# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения
# комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и
# выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

def my_abs(num):
    if not (isinstance(num, int) or isinstance(num, float)):
        raise TypeError("Expected a float or int datatypes for num")
    return num if num >= 0 else -num


class Complex_Number:

    def __init__(self, real, imagine):
        if not (isinstance(real, int) or isinstance(real, float)):
            raise TypeError("Expected a float or int datatypes for real")
        if not (isinstance(imagine, int) or isinstance(imagine, float)):
            raise TypeError("Expected a float or int datatypes for imagine")
        self._real = real
        self._imagine = imagine

    def __add__(self, other):
        """
        сложение комплексного числа с целым или десятичным или комплексным
        целое или десятичное a можно представить как a + 0*i, где i == sqrt(-1)

        :param other: int или float или complex или Complex_Number
        :return:Complex_Number
        """
        if isinstance(other, Complex_Number):
            # Пользоваться защищенными атрибутами вне класса некорректно.
            # Но технически, мы внутри класса) Спасибо Python за свободу!
            return Complex_Number(self._real + other._real, self._imagine + other._imagine)
        if isinstance(other, complex):
            return Complex_Number(self._real + other.real, self._imagine + other.imag)
        if isinstance(other, int) or isinstance(other, float):
            return Complex_Number(self._real + other, self._imagine)
        raise TypeError("Expected a Complex_Number or float or int or complex datatypes")

    def __radd__(self, other):
        if isinstance(other, complex):
            return Complex_Number(self._real + other.real, self._imagine + other.imag)
        if isinstance(other, int) or isinstance(other, float):
            return Complex_Number(self._real + other, self._imagine)
        raise TypeError("Expected a Complex_Number or float or int or complex datatypes")

    def __mul__(self, other):
        """
        умножение комплексного числа
        на целое или десятичное или комплексное
        целое или десятичное a можно представить как a + 0*i, где i == sqrt(-1)
        само умножение можно представить в общем виде как:
        (a1+b1*i))*(a2+b2*i) == (a1*a2-b1*b2) + (a1b2 + a2b1)*i
        так как i==sqrt(-1)

        :param other: int или float или complex или Complex_Number
        :return: комплексное число Complex_Number - результат умножения
        """
        if isinstance(other, Complex_Number):
            new_real = self._real * other._real - self._imagine * other._imagine
            new_imagine = (self._real * other._imagine + self._imagine * other._real)
            return Complex_Number(new_real, new_imagine)
        if isinstance(other, complex):
            new_real = self._real * other.real - self._imagine * other.imag
            new_imagine = (self._real * other.imag + self._imagine * other.real)
            return Complex_Number(new_real, new_imagine)
        if isinstance(other, int) or isinstance(other, float):
            new_real = self._real * other
            new_imagine = self._imagine * other
            return Complex_Number(new_real, new_imagine)
        raise TypeError("Expected a Complex_Number or float or int or complex datatypes")

    def __rmul__(self, other):
        if isinstance(other, complex):
            new_real = self._real * other.real - self._imagine * other.imag
            new_imagine = (self._real * other.imag + self._imagine * other.real)
            return Complex_Number(new_real, new_imagine)
        if isinstance(other, int) or isinstance(other, float):
            new_real = self._real * other
            new_imagine = self._imagine * other
            return Complex_Number(new_real, new_imagine)
        raise TypeError("Expected a Complex_Number or float or int or complex datatypes")

    def __str__(self):
        return f"{self._real}{'-' if self._imagine < 0 else '+'}{my_abs(self._imagine)}i"

    def __repr__(self):
        self.__str__()


if __name__ == "__main__":
    base_tuple = (5, -2)
    reserve_tuple = (5, 2)
    print(Complex_Number(*base_tuple))
    print(f"My radd {5 + Complex_Number(*base_tuple)}, trust radd {5 + complex(*base_tuple)}")
    print(f"My add {Complex_Number(*base_tuple) + 5}, trust add {complex(*base_tuple) + 5}")
    print(
        f"My add {Complex_Number(*base_tuple) + complex(*reserve_tuple)},"
        f"trust add {complex(*base_tuple) + complex(*reserve_tuple)}")
    print(
        f"My add {complex(*base_tuple) + Complex_Number(*reserve_tuple)},"
        f"trust add {complex(*base_tuple) + complex(*reserve_tuple)}")
    print(
        f"My add {Complex_Number(*base_tuple) + Complex_Number(*reserve_tuple)},"
        f"trust add {complex(*base_tuple) + complex(*reserve_tuple)}")
    print(f"My mul {Complex_Number(*base_tuple) * 2}, trust mul {complex(*base_tuple) * 2}")
    print(f"My rmul {2 * Complex_Number(*base_tuple)}, trust rmul {2 * complex(*base_tuple)}")
    print(f"My rmul {complex(*base_tuple) * Complex_Number(*reserve_tuple)},"
          f"trust mul {complex(*base_tuple) * complex(*reserve_tuple)}")
    print(f"My mul {Complex_Number(*base_tuple) * complex(*reserve_tuple)},"
          f"trust mul {complex(*base_tuple) * complex(*reserve_tuple)}")
    print(f"My mul {Complex_Number(*base_tuple) * Complex_Number(*reserve_tuple)},"
          f"trust mul {complex(*base_tuple) * complex(*reserve_tuple)}")

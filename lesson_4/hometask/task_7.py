# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.
#
# **Подсказка:** факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def fact(n: int):
    if n < 0:
        raise ValueError("Factorial not defined for a negative value!")
    if n == 0:
        yield 1
    current_value = 1
    for number in range(1, n + 1):
        current_value *= number
        yield current_value


origin_number = 0
while True:
    try:
        origin_number = int(input("Enter non-negative integer number for generating a factorial sequence >>>"))
    except ValueError:
        print("That's not integer number! Try again.")
        continue
    break

# creates generator object for checks
gen_obj = fact(origin_number)
print(f"fact({origin_number}) type is {type(gen_obj)}")
count = 0
# for el in gen_obj: # то же самое, но не по заданию
for el in fact(origin_number):
    count += 1
    print(f"{count}! : {el}")

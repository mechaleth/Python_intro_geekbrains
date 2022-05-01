# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
#
# **Подсказка:** использовать функцию reduce().
import functools as f_tools

# even_numbers = [num for num in range(100, 1001) if num % 2 == 0]
# так быстрее
even_numbers = [num for num in range(100, 1001, 2)]

print(f"Multiplication of all even number"
      f"in range 100 to 1000 is {f_tools.reduce(lambda x, y: x * y, even_numbers)}")

# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

str_number = input("Set number >>>>")
number = int(str_number)
double_num = number * 10 ** len(str_number) + number
triple_num = number * 10 ** (len(str_number) * 2) + double_num
print(f"{number} + {double_num} + {triple_num} = {number + double_num + triple_num}")

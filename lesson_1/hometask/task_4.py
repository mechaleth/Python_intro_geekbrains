# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

str_number = input("Enter the whole number >>>")
number = int(str_number)
assert (number >= 0)
count = len(str_number)
max_number = 0
while count > 0:
    count -= 1
    current_number = number // 10 ** count
    number -= current_number * 10 ** count
    if current_number > max_number:
        max_number = current_number
print(f"max number is {max_number}")

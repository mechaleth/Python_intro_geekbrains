# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число —
# номер дня. Например: a = 2, b = 3.
# Результат:
# 		1-й день: 2
# 		2-й день: 2,2
# 		3-й день: 2,42
# 		4-й день: 2,66
# 		5-й день: 2,93
# 		6-й день: 3,22
# 	Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

first_day_result = float(input("Enter first day kilometers result >>>>"))
while first_day_result <= 0.0:
    print("Kilometers must be more than 0")
    first_day_result = float(input("Enter first day kilometers result >>>>"))

last_day_result = float(input("Enter reaching kilometers >>>>"))
while last_day_result < 0.0:
    print("Kilometers must be more than 0")
    last_day_result = float(input("Enter reaching kilometers >>>>"))

current_result = first_day_result
day_number = 1
while True:
    print(f"Result {current_result} at {day_number} day")
    if not current_result < last_day_result:
        break
    current_result *= 1.1
    day_number += 1

print(f"Result more than {last_day_result} km reached at {day_number} day")
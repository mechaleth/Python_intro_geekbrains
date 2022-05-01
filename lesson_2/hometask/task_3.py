# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решениЯ через list и через dict.

number = None

while True:
    try:
        number = int(input("Enter number in range from 1 to 12 >>>"))
        if number in range(1, 12):
            break
    except ValueError:
        continue
# решение через dict
# кортежи - хэшируемый тип данных
seasons_dict = {(12, 1, 2): "winter", (3, 4, 5): "spring", (6, 7, 8): "summer", (9, 10, 11): "autumn/fall"}
for month_numbers, name in seasons_dict.items():
    if number in month_numbers:
        print(f"month with number {number} is {name}")
        # больше исследовать нечего
        break

# решение через list
seasons_name_list = ["winter", "spring", "summer", "autumn/fall"]
seasons_month_list = [(12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11)]
for month_numbers, name in zip(seasons_month_list, seasons_name_list):
    if number in month_numbers:
        print(f"month with number {number} is {name}")
        # больше исследовать нечего
        break

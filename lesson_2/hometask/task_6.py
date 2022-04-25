# *Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# **Пример готовой структуры:**
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# **Пример:**
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

product_list = list()
# Запрашиваем данные у пользователя
while True:
    try:
        number = int(input("Enter the product number >>>"))
        double_mark = False
        # стоило бы добавить проверку дубляжей...
        for item in product_list:
            if item[0] == number:
                double_mark = True
                break
        if double_mark:
            print(f"Number {number} already in list")
            continue
        name = input("Enter the product name >>>")
        price = float(input("Enter the product price >>>"))
        count = int(input("Enter the product count >>>"))
        value_measure = input("Enter the product measure >>>")
    except ValueError as verror:
        print(f"{verror}, uncorrect value")
        continue
    except EOFError as eof_error:
        print(f"{eof_error}, now quit")
        quit()
    if name == "" or value_measure == "" or price < 0 or count < 0 or number < 0:
        print(f"uncorrect values detected, reenter please")
        continue
    product_list.append((number, {'name': name, 'price': price, 'count': count, 'measure': value_measure}))
    if input("Press Enter to continue or something else to break >>>") == "":
        break
print(product_list)

# Теперь парсим словарь в другой словарь
unique_dict = dict()
for values in product_list:
    if len(values) < 2:
        continue
    product_dict = values[1]
    if type(product_dict) is not dict:
        continue
    for key, value in product_dict.items():
        unique_list = unique_dict.setdefault(key, list())
        # судя по примеру, в массиве должны быть только уникальные значения
        if value not in unique_list:
            unique_list.append(value)

print(unique_dict)

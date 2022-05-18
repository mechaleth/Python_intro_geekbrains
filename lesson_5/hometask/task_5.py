# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import get_file_by_files_list as my_add_func

# Создаём файл, заполняем, потом парсим его и выводим сумму чисел

str_number_list = []
final_numeric_file_name = 'numeric_file.txt'

for element in input("Введите набор чисел через пробелы >>>").split():
    # нужны только числа
    try:
        str_number_list.append(str(my_add_func.get_number_by_string(element)))
    except ValueError:
        continue

# Запишем цифры в файл
with open(final_numeric_file_name, 'w') as num_file:
    num_file.write(' '.join(str_number_list))
    print(f"numbers writes to file {num_file.name}")

# Посчитаем сумму цифр
with open(my_add_func.get_file_by_current_folder(), "r") as reading_file:
    numbers_sum = 0
    for line in reading_file:
        for element in line.split():
            # суммируются элементы, которые приводятся к числу
            try:
                numbers_sum += my_add_func.get_number_by_string(element)
            except ValueError:
                continue
    print(f"Sum of numbers in file {reading_file.name} is {numbers_sum}")
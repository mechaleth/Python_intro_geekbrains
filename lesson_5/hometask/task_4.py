# Создать (не программно) текстовый файл со следующим содержимым:
#
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
#  Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
#  При этом английские числительные должны заменяться на русские.
#  Новый блок строк должен записываться в новый текстовый файл.
import get_file_by_files_list as my_add_func

numbers_dict = {}
russian_numbers_dict = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре', 10: 'Десять'}
final_filename = 'new_numbers_file.txt'

with open(my_add_func.get_file_by_current_folder(), "r") as reading_file:
    for fileline in reading_file:
        try:
            string_number, _, number, *_ = fileline.split()
            numbers_dict[int(number)] = string_number
        except ValueError:
            print(f"uncorrect value catched: {string_number} - {number}")
            exit()

with open(final_filename, 'w') as writing_file:
    for number, string_number in numbers_dict.items():
        # Если не будет значения в словаре российских соответствий
        # то лучше вставить английский вариант, чем ничего
        print(f"{russian_numbers_dict.get(number, string_number)} — {number}", file=writing_file)
#        writing_file.write(f"{russian_numbers_dict.get(number, string_number)} — {number}\n")

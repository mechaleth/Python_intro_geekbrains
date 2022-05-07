# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
import get_file_by_files_list as my_add_func


def designificate_string(origin: str) -> str:
    """
    Функция заменяет "несловесные" символы из строки на пробелы

    :param origin: исходная строка с кучей символов
    :return: строка с пробелами вместо "несловесных" символов
    """
    bad_symbols_list = ('.', ',', '?', '!', ';', ':', '"', "'", '\\', '|', '/', '(', ')')
    for bad_symbol in bad_symbols_list:
        origin = origin.replace(bad_symbol, ' ')
    return origin


count_lines = 0
count_strings = []
# Какой файл выбрать - решает пользователь
with open(my_add_func.get_file_by_current_folder(), "r") as reading_file:
    for fileline in reading_file:
        count_lines += 1
        count_strings.append(len(designificate_string(fileline).split()))

print(f"Overall lines count is {count_lines}")
for current_count, current_word_number in enumerate(count_strings, 1):
    print(f"{current_count} : word count is {current_word_number}")

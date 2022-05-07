import os

def get_number_by_string(string_number: str):
    """
    Функция преобразования строки к какому-либо числовому формату

    :param string_number: число в строковом виде
    :return: число в числовом формате
    """
    try:
        return int(string_number)
    except ValueError:
        # если и тут ошибка, пробрасываем во внешний код
        return float(string_number)

def get_file_by_current_folder(interested_dir='.') -> str:
    """
    Функция взаимодейcтвия с командной строкой
    Исключительно консольная функция для моих нужд
    Выводит список файлов в текущей директории
    Позволяет выбрать индекс понравившегося файла

    :param interested_dir: директория поиска файла
    :return: адрес файла с названием файла
    """

    files_list = os.listdir()

    if not os.path.isdir(interested_dir):
        raise NotADirectoryError(f"Input dir {interested_dir} is non existing dir")
    # удалим не "не файлы" из списка файлов
    for file in files_list:
        if not os.path.isfile(file):
            files_list.remove(file)
    array_len = len(files_list)

    # выведем файлы, которые пользователь может выбрать
    print('Files for choose:')
    for index, file in enumerate(files_list):
        print(f"{index} or {index - array_len} : {file}")

    # Упорно запрашиваем индекс интересующего файла
    while True:
        try:
            return os.path.join(interested_dir, files_list[int(input("Input the need file index >>>"))])
        except ValueError:
            print("Uncorrect input")
            continue
        except IndexError:
            print("Uncorrect file index")
            continue

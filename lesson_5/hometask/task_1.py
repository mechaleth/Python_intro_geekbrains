# Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

# Файл будет создан в любом случае
# Даже если вводить уже ничего не хочется
with open("task_1_file.txt", "w") as task_file:
    while True:
        temp_string = input("Input user string to file >>>")
        if temp_string == "":
            break
        try:
            task_file.write(temp_string+'\n')
        except FileNotFoundError:
            print("Unable to process file in unexisting directory")
            exit()

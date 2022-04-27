# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(string):
    return string.capitalize()


# строки разделены пробелом
string_array = input("Input a string >>>").split(" ")

for element_index in range(len(string_array)):
    string_element = string_array[element_index]
    if " " in string_element or string_element.isdigit():
        continue
    string_array[element_index] = int_func(string_element)

print(' '.join(string_array))

import datetime

# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# !!!(Что значит "проверки типов данных"? У нас разве есть ограничения??)
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

# задам априори, так как типов данных куча, писать ifы лень))
mylist = ["iron maiden", 666, "the number of the beast", 4.85, datetime.date(1982, 3, 22)]

for element in mylist:
    print(f"{element} has a type {type(element)}")

# !!!(Что значит "проверки типов данных"? У нас разве есть ограничения??)
# пусть есть
# множество с допустимыми значениями
allow_types_set = frozenset((type(int()), type(str()), type(float())))
for element in mylist:
    element_type = type(element)
    if element_type not in allow_types_set:
        mylist.remove(element)
        print(f"element {element} has a not allowed type {element_type}")
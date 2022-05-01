import datetime

# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input()

my_list = []
while True:
    x = input("Enter list value. If no value entered, list ends >>>")
    if x == "":
        break
    my_list.append(x)

print(f"entered list is {my_list}")
# нас интересующие индексы чётных элементов
for indx in range(0, (len(my_list)//2)*2, 2):
    my_list[indx], my_list[indx + 1] = my_list[indx + 1], my_list[indx]

print(f"result list is {my_list}")

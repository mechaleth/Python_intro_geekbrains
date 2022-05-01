# Представлен список чисел.
# Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
#
# **Пример исходного списка:**
# [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# **Результат:**
# [23, 1, 3, 10, 4, 11]

import task_2

input_string_array = input("Enter the numbers string with ' ' as delimiter>>>").split()
origin_list = [task_2.get_number_by_string(num) for num in input_string_array]
print(origin_list)

# origin_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print([x for x in origin_list if origin_list.count(x) == 1])

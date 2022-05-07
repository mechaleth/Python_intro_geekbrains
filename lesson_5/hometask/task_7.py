# Cоздать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
#
# **Пример строки файла:**firm_1 ООО 10000 5000.
#
#  Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
#  а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
#
#  Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
#  а также словарь со средней прибылью. Если фирма получила убытки,
#  также добавить ее в словарь (со значением убытков).
#
# **Пример списка:**[{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
#  Итоговый список сохранить в виде json-объекта в соответствующий файл.
#
# **Пример json-объекта:**
# `    [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]    `
#
# **Подсказка:**использовать менеджер контекста.

import json
import get_file_by_files_list as my_add_func

# заготовка списка словарей с информацией о прибыльности фирм и средней прибыльности
# убытки в словарь средней прибыли не войдут
firm_list = [{}, {"average_profit": 0}]
firms_dict = firm_list[0]
firms_common_dict = firm_list[1]


def calculate_recurrent_average(new_value: float, avg: float, count: int) -> float:
    """
    Расчёт среднего значения по рекуррентной формуле
    avg_n = (avg_n-1 *(n-1) + an)/n

    :param new_value: новое значение, an
    :param avg: среднее значение на предыдущей итерации, avg_n-1
    :param count: номер итерации, n
    :return: среднее на текущей итерации
    """
    if count <= 0:
        raise ValueError("Iteration count must be a positive!")
    return (avg * (count - 1) + new_value) / count


with open(my_add_func.get_file_by_current_folder(), "r") as reading_file:
    profitible_count = 0
    for line in reading_file:
        try:
            *firm_name_array, company_form, revenue, costs = line.split()
            revenue = my_add_func.get_number_by_string(revenue)
            costs = my_add_func.get_number_by_string(costs)
        except ValueError:
            print(f"Unable to parse line {line}")
            continue
        firm_name = ' '.join(firm_name_array)
        profitable = revenue - costs
        firms_dict[firm_name] = profitable
        if profitable < 0:
            continue
        profitible_count += 1
        firms_common_dict["average_profit"] = \
            calculate_recurrent_average(profitable,
                                        firms_common_dict.get("average_profit", 0),
                                        profitible_count)
print(firm_list)

with open("company_dictlist.json", 'w') as json_file:
    json.dump(firm_list, json_file)

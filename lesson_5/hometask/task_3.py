# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# **Пример файла:**
#
# Иванов 23543.12
# Петров 13749.32

import get_file_by_files_list as my_add_func

employee_salary_dict = {}

with open(my_add_func.get_file_by_current_folder(), "r") as reading_file:
    for fileline in reading_file:
        try:
            employee, salary, *_ = fileline.split()
            employee_salary_dict[employee] = float(salary)
        except ValueError:
            print(f"uncorrect value catched: {employee} : {salary}")
            exit()

for employee, salary in employee_salary_dict.items():
    if salary < 20000.0:
        print(f"{employee} has a salary {salary} which less than 20000")

print(f"Average employees salary is {round(sum(employee_salary_dict.values()) / len(employee_salary_dict), 2)}")

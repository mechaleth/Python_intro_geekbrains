# Реализовать скрипт, в котором должна быть предусмотрена
# функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу:
# (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv


# calculate_salary = lambda work_hours, rate_per_hour, bonus: work_hours * rate_per_hour + bonus
def calculate_salary(work_hours: float, rate_per_hour: float, bonus: float):
    """
    Расчёт ЗП сотрудника

    :param work_hours: отработанные за месяц часы, [ч]
    :param rate_per_hour: ставка сотрудника за час, [денег/ч]
    :param bonus: премия, [деньги]
    :return: ЗП сотрудника за месяц, [деньги]
    """
    return work_hours * rate_per_hour + bonus


try:
    filepath, work_hours, rate_per_hour, bonus, *others = argv
    work_hours = float(work_hours)
    rate_per_hour = float(rate_per_hour)
    bonus = float(bonus)
except ValueError:
    print("Sorry, it's need a 3 float parameters for calculations!")
    exit()

print(f"Сотрудник заработал {calculate_salary(work_hours, rate_per_hour, bonus)} за месяц")

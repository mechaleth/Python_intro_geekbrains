# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и
# определите прибыль фирмы в расчете на одного сотрудника.

revenue = float(input("Enter the revenue, please >>>>"))
costs = float(input("Enter the costs, please >>>>"))
while costs < 0:
    # издержки не бывают отрицательными
    print("Costs never be below zero!")
    costs = float(input("Enter the costs, please >>>>"))
if revenue > costs:
    print("Great! You have a profit")
    # так как нет значений по умолчанию для
    # рентабельности и прибыли на сотрудника,
    # данные переменные только в рамках данного блока if
    return_on_revenue = (revenue - costs)/revenue
    print(f"Return on revenue is {return_on_revenue}")
    units_number = int(input("Enter the company's units number >>>>"))
    # сотрудников не может быть меньше 0
    while units_number <= 0:
        print("Units number never be below zero or zero, you are unit!")
        units_number = int(input("Enter the company's units number >>>>"))
    revenue_per_unit = (revenue - costs)/units_number
    print(f"Revenue per unit is {revenue_per_unit}")
elif revenue < costs:
    print("Sad but you have a loss")
else:
    print("You didn't earn anything, but nothing lost too")
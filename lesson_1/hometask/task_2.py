# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_in_seconds = float(input("Set time in seconds, please >>>"))
hour_in_a_day = 24.0
minutes_in_a_hour = 60.0
seconds_in_a_minute = 60.0
# дни нас не интересуют
lost_time = time_in_seconds % (hour_in_a_day * minutes_in_a_hour * seconds_in_a_minute)
# часы интересуют
hours = int(lost_time // (minutes_in_a_hour * seconds_in_a_minute))
lost_time %= (minutes_in_a_hour * seconds_in_a_minute)
# минуты интересуют
minutes = int(lost_time // (seconds_in_a_minute))
seconds = lost_time % seconds_in_a_minute
# вывод в требуемом формате чч:мм:сс
print(f"{hours:02}:{minutes:02}:{seconds:02.0f}")

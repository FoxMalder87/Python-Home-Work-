# Запрос данных у пользователя
year = input("Введите год рождения: ")
month = input("Введите месяц рождения: ")
day = input("Введите число рождения: ")

# Форматирование и вывод даты
date = "{:02d}.{:02d}.{}".format(int(day), int(month), year)
print("Дата рождения:", date)
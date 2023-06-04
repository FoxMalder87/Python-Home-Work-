try:
    real_time1 = int(input("Введите текущее время (часы): "))
    real_time2 = int(input("Введите текущее время (минуты): "))
    hours = 24 - real_time1 - 1
    minutes = 60 - real_time2
except ValueError:
    print("Ошибка: Некорректный ввод данных. Введите целые числа.")
else:
    print("До следующего дня осталось", hours, "часов", minutes, "минут")
finally:
    print("Завершение программы.")
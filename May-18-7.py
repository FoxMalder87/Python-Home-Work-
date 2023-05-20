real_time1 = int(input("Введите текущее время (часы): "))
real_time2 = int(input("Введите текущее время (минуты): "))
hours = 24 - real_time1 - 1
minutes = 60 - real_time2
print("До следующего дня осталось", hours, "часов", minutes, "минут")
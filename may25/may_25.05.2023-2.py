try:
    user1 = float(input("Введите первое число: "))
    user2 = float(input("Введите второе число: "))
except ValueError:
    print("Ошибка: Некорректный ввод данных. Введите числа.")
else:
    average = (user1 + user2) / 2
    print("Среднее арифметическое:", average)
finally:
    print("Завершение программы.")
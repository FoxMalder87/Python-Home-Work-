try:
    km = float(input("Введите значение в километрах: "))
except ValueError:
    print("Ошибка: Некорректный ввод данных. Введите число.")
else:
    miles = km * 0.621371
    print("Значение в милях:", miles)
finally:
    print("Завершение программы.")
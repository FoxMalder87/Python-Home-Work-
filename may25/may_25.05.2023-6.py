try:
    a = float(input("Введите значение a: "))
    b = float(input("Введите значение b: "))
    x = -b / a
except ValueError:
    print("Ошибка: Некорректный ввод данных. Введите числа.")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль недопустимо.")
else:
    print("Результат:", x)
finally:
    print("Завершение программы.")
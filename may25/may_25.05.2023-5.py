try:
    number1 = float(input("Введите первое число: "))
    number2 = float(input("Введите второе число: "))
    addition = number1 + number2
    subtraction = number1 - number2
    multiplication = number1 * number2
    division = number1 / number2
except ValueError:
    print("Ошибка: Некорректный ввод данных. Введите числа.")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль недопустимо.")
else:
    print("Сложение:", addition)
    print("Вычитание:", subtraction)
    print("Умножение:", multiplication)
    print("Деление:", division)
finally:
    print("Завершение программы.")
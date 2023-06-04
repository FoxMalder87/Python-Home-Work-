try:
    square_area = float(input("Введите длину стороны квадрата: "))
except ValueError:
    print("Ошибка: Некорректный ввод данных. Введите число.")
else:
    area = square_area ** 2
    print("Площадь квадрата:", area)
finally:
    print("Завершение программы.")
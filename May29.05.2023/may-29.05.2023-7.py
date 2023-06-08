import math

circumference = float(input("Введите длину окружности: "))
square_perimeter = float(input("Введите периметр квадрата: "))

diameter = circumference / math.pi

side_length = square_perimeter / 4

if diameter <= side_length:
    print("Окружность может поместиться в указанный квадрат.")
else:
    print("Окружность не может поместиться в указанный квадрат.")
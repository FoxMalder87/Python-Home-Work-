# Запрос числа у пользователя
number = input("Введите шестизначное число: ")

# Проверка на длину числа
if len(number) != 6:
    print("Ошибка! Введите шестизначное число.")
else:
    # Разбиение числа на две половины
    first_half = int(number[:3])
    second_half = int(number[3:])

    # Вычисление суммы половин числа
    sum_of_halves = first_half + second_half

    # Вывод суммы половин числа
    print("Сумма половин числа:", sum_of_halves)
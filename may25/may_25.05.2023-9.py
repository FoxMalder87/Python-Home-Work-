try:
    number = int(input("Введите пятизначное число: "))
    if number < 10000 or number > 99999:
        raise ValueError("Ошибка: Введено число, не являющееся пятизначным.")
    last = number % 10
    number //= 10
    new_number = last * 10000 + number
except ValueError as e:
    print(str(e))
else:
    print("Новое число:", new_number)
finally:
    print("Завершение программы.")
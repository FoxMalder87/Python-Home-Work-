number = input("Введите число от 0 до 9: ")

# VN: Да, в этом задании так можно делать, не боясь получить исключение. Классно, что вы нашли этот метод!
# Но предостерегу, что .isdigit() не универсальный способ - для отрицательных или дробных чисел не подходит
if number.isdigit() and 0 <= int(number) <= 9:
    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(']
    index = int(number)
    special_character = special_characters[index]
    print(f"Спецсимвол для числа {number}: {special_character}")
else:
    print("Введено некорректное число. Пожалуйста, введите число от 0 до 9.")
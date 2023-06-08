number = input("Введите число от 0 до 9: ")

if number.isdigit() and 0 <= int(number) <= 9:
    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(']
    index = int(number)
    special_character = special_characters[index]
    print(f"Спецсимвол для числа {number}: {special_character}")
else:
    print("Введено некорректное число. Пожалуйста, введите число от 0 до 9.")